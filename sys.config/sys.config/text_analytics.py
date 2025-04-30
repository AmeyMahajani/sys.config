import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
# Download the 'wordnet' resource
nltk.download('wordnet') # This line was added to download the missing resource

import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

doc = """Natural Language Processing (NLP) is a subfield of artificial intelligence that gives machines the ability to read, understand and derive meaning from human languages. NLP combines computational linguistics with machine learning and deep learning models."""
doc2 = """Machine learning is a branch of artificial intelligence (AI) that focuses on building systems that learn from data. It involves algorithms that can recognize patterns and make decisions with minimal human intervention."""
doc3 = """Deep learning is a class of machine learning techniques based on artificial neural networks. These networks are designed to simulate the workings of the human brain, allowing systems to learn from large amounts of data."""
doc4 = """Artificial intelligence (AI) is the simulation of human intelligence processes by machines, particularly computer systems. It includes learning, reasoning, problem-solving, perception, and language understanding."""
doc5 = """Data science is an interdisciplinary field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data."""
doc

tokens = word_tokenize(doc)
print(tokens)

tags = pos_tag(tokens)
print(tags)

stop_words = set(stopwords.words('english'))
print(stop_words)

filtered_words = [word for word in tokens if word.lower() not in stop_words and word.isalpha()]
print(filtered_words)

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]
print(stemmed_words)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
print(lemmatized_words)

vectorizer = TfidfVectorizer()
tf_idf = vectorizer.fit_transform([doc, doc2, doc3, doc4, doc5])
tf_idf

import pandas as pd
df_tfidf = pd.DataFrame(tf_idf.toarray(), columns=vectorizer.get_feature_names_out())
df_tfidf