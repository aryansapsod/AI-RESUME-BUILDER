from flask import Flask, request, render_template, redirect, url_for, send_file, flash
import os
from werkzeug.utils import secure_filename
from extractor import extract_text_from_file
from preprocess import clean_text
from utils import compute_similarity_scores
from utils import zip_top_n, allowed_file
import uuid
import csv

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}
RESULTS_FOLDER = 'results'

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULTS_FOLDER'] = RESULTS_FOLDER

# ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get job description text
        jd_text = request.form.get('job_description', '')
        if not jd_text.strip():
            flash('Please provide a job description.')
            return redirect(request.url)

        # process upload resumes
        uploaded_files = request.files.getlist('resumes')
        if not uploaded_files or uploaded_files[0].filename == '':
            flash('Please upload one or more resume files.')
            return redirect(request.url)
        
        resume_texts = {}
        resume_filenames = []
        for f in uploaded_files:
            if f and allowed_file(f.filename, ALLOWED_EXTENSIONS):
                filename = secure_filename(f.filename)
                unique_name = str(uuid.uuid4()) + '_' + filename
                save_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
                f.save(save_path)
                # extract text
                text = extract_text_from_file(save_path)
                cleaned = clean_text(text)
                resume_texts[unique_name] = {
                    'filename': filename,
                    'text': cleaned
                }
                resume_filenames.append(unique_name)
            else:
                flash(f"File {f.filename} is not allowed.")
        # preprocess job description
        cleaned_jd = clean_text(jd_text)
        # compute similarities
        scores = compute_similarity_scores(cleaned_jd, resume_texts)
        # scores is a list of dicts: [{'resume_id': ..., 'filename': ..., 'score': ...}, ...] sorted descending
        
        # save result CSV
        result_csv_path = os.path.join(app.config['RESULTS_FOLDER'], f"results_{uuid.uuid4().hex}.csv")
        with open(result_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Resume Filename', 'Match Score (%)'])
            for item in scores:
                writer.writerow([item['filename'], f"{item['score']*100:.2f}"])
        
        # optionally zip top N resumes
        top_n = int(request.form.get('top_n', 3))
        top_resume_ids = [item['resume_id'] for item in scores[:top_n]]
        zip_path = zip_top_n(app.config['UPLOAD_FOLDER'], resume_texts, top_resume_ids, app.config['RESULTS_FOLDER'])
        
        # pass to template
        return render_template('results.html', scores=scores, result_csv=os.path.basename(result_csv_path), zip_file=os.path.basename(zip_path))
    else:
        return render_template('index.html')

@app.route('/download_csv/<filename>')
def download_csv(filename):
    path = os.path.join(app.config['RESULTS_FOLDER'], filename)
    return send_file(path, as_attachment=True)

@app.route('/download_zip/<filename>')
def download_zip(filename):
    path = os.path.join(app.config['RESULTS_FOLDER'], filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
