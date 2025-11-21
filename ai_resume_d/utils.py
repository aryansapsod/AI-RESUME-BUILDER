import os
import zipfile

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def zip_top_n(upload_folder, resume_texts, top_resume_ids, results_folder):
    zip_filename = f"top_{len(top_resume_ids)}_resumes_{os.urandom(4).hex()}.zip"
    zip_path = os.path.join(results_folder, zip_filename)
    with zipfile.ZipFile(zip_path, 'w') as zf:
        for rid in top_resume_ids:
            # the saved file is in upload_folder with name rid
            # need to map rid to actual filepath
            # resume filenames saved with rid as key
            # but path is upload_folder / rid
            src_path = os.path.join(upload_folder, rid)
            if os.path.exists(src_path):
                zf.write(src_path, os.path.basename(resume_texts[rid]['filename']))
    return zip_path
