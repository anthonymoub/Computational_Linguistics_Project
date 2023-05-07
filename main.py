from flask import Flask, render_template
from flask import Flask, render_template, request
import pickle
import ast
import pandas as pd
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
import openai
from getpass import getpass
from Openai_model import find_similar_vectors, find_similar_vectors2
from flask_caching import Cache
import re


app = Flask(__name__)


cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@cache.cached(timeout=3600, key_prefix='embedded_quraan')
def get_embedded_quraan():
    with open('Data/x.pickle', 'rb') as f:
        embedded_quraan = pickle.load(f)
    return embedded_quraan


@cache.cached(timeout=3600, key_prefix='embedded_bible')
def get_embedded_bible():
    with open('Data/embedded_bible.pickle', 'rb') as f:
        embedded_bible = pickle.load(f)
    return embedded_bible


all_bible_verses = pd.read_csv('Data/total_verses.csv')


embedded_quraan = get_embedded_quraan()
embedded_bible = get_embedded_bible()

# Removing verse numbers from verse
embedded_bible['Verses'] = embedded_bible['Verses'].apply(
    lambda x: re.sub(r'^\d+:\d+\s+', '', x))

# Removing verse numbers from verse
all_bible_verses['Verses'] = all_bible_verses['Verses'].apply(
    lambda x: re.sub(r'^\d+:\d+\s+', '', x))

# Open AI API connection
openai.api_key = "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"

# Define a list of example sentences
sentences = list(all_bible_verses['Verses'].unique())

sentences_q = list(embedded_quraan['Verse'].unique())


@app.route("/", methods=["GET", "POST"])
def hello():

    if request.method == "POST":

        if "message" in request.form:
            search = request.form["message"]
            message = [request.form["message"], embedded_quraan['Verse']
                       [0], embedded_quraan['Verse'][1]]
            # Run the find_similar_vector function
            results = list(find_similar_vectors(search, embedded_quraan))
            # Add the input so we can show case it
            results.append(search)
            return render_template('index.html', message=results, sentences=sentences, sentences_q=sentences_q)

        elif "message2" in request.form:
            search = request.form["message2"]
            message = [request.form["message2"], embedded_bible['Verses']
                       [0], embedded_bible['Verses'][1]]
            # Run the find_similar_vector function
            results = list(find_similar_vectors2(search, embedded_bible))
            # Add the input so we can show case it
            results.append(search)
            return render_template('index.html', message2=results, sentences=sentences, sentences_q=sentences_q)

    else:
        message = ""
        search = ""
        results = [" "]
        return render_template('index.html', message='', sentences=sentences, sentences_q=sentences_q)


if __name__ == '__main__':
    app.run(debug=True)
