from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity_scores(job_desc_text: str, resume_texts: dict):
    """
    resume_texts: dict mapping resume_id -> {'filename': <original filename>, 'text': cleaned resume text}
    Returns list of items sorted by descending similarity, each item: {'resume_id', 'filename', 'score'}
    """
    # prepare corpus: first item is job description, then all resume texts
    corpus = [job_desc_text] + [info['text'] for _id, info in resume_texts.items()]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    jd_vec = tfidf_matrix[0]
    resume_vecs = tfidf_matrix[1:]
    sims = cosine_similarity(jd_vec, resume_vecs)[0]  # vector of length = # resumes
    results = []
    for idx, (resume_id) in enumerate(resume_texts.keys()):
        results.append({
            'resume_id': resume_id,
            'filename': resume_texts[resume_id]['filename'],
            'score': round(float[idx]*100,2)
        })
    # sort descending
    results.sort(key=lambda x: x['score'], reverse=True)
    return results
