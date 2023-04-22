from flask import Flask, render_template
from flask import Flask, render_template, request
import pickle
import ast
import pandas as pd
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
import openai
from getpass import getpass
from Openai_model import find_similar_vectors

# Load the DataFrame from the pickle file
with open('Data/x.pickle', 'rb') as f:
    embedded_quraan = pickle.load(f)

 
# Open AI API connection 
openai.api_key = "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"
 

app = Flask(__name__)

# Define a list of example sentences
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "She sells seashells by the seashore",
    "Peter Piper picked a peck of pickled peppers",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "The rain in Spain stays mainly in the plain"
]

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        search = request.form["message"]
        message = [request.form["message"], embedded_quraan['Verse'][0], embedded_quraan['Verse'][1]]
        # Run the find_similar_vector function
        results = list(find_similar_vectors(search, embedded_quraan))
        # Add the input so we can show case it
        results.append(search)
        return render_template('index.html', message=results, sentences=sentences)
    
    else:
        message = ""
        search = ""
        results = [" "]
        return render_template('index.html', message='', sentences=sentences)


if __name__ == '__main__':
    app.run(debug=True)

