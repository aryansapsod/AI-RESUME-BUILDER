import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ensure required NLTK data downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text: str) -> str:
    # lower
    text = text.lower()
    # remove punctuation & special chars
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    # tokenize
    tokens = nltk.word_tokenize(text)
    # remove stopwords & short tokens
    tokens = [t for t in tokens if t not in stop_words and len(t) > 1]
    # lemmatize
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)
