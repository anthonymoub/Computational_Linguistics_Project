from flask import Flask, request, jsonify
import pickle
from openai.embeddings_utils import get_embedding, cosine_similarity
import pandas as pd
import openai
from flask import render_template 

# Load the DataFrame from the pickle file
with open('../Data/x.pickle', 'rb') as f:
    embedded_quraan = pickle.load(f)

# Open AI API connection 
openai.api_key = "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"


# Load the DataFrame from the pickle file
with open('../Data/x.pickle', 'rb') as f:
    embedded_quraan = pickle.load(f)


 
# Open AI API connection 
openai.api_key = "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"
 
# Define function  
def find_similar_vectors(search , embedded_quraan):

    search_vector = get_embedding(search , engine="text-embedding-ada-002")
    embedded_quraan = embedded_quraan.dropna(subset=['Embeddings'])
    embedded_quraan["similarities"] = embedded_quraan['Embeddings'].apply(lambda x: cosine_similarity(x, search_vector))
    embedded_quraan = embedded_quraan.sort_values('similarities', ascending=False)
    return embedded_quraan['Verse'][0:5]


# Define the Flask app
app = Flask(__name__)

# Define a route that accepts a search query and returns the most similar verses
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/find_similar', methods=['POST'])
def find_similar():
	search = request.form['quote']
	result = find_similar_vectors(search, embedded_quraan)
	return render_template('index.html', result=result)

if __name__ == '__main__':
	app.run()
