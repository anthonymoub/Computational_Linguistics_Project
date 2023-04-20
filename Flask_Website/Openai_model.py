import pickle
import ast
import pandas as pd
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
import openai
from getpass import getpass

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

 



