import pickle
import ast
import pandas as pd
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
import openai
from getpass import getpass
import re

# Load the DataFrame from the pickle file
with open('Data/x.pickle', 'rb') as f:
    embedded_quraan = pickle.load(f)

with open('Data/embedded_bible.pickle', 'rb') as f:
    embedded_bible = pickle.load(f)


# Open AI API connection
openai.api_key = "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"


# Removing verse numbers from verse
embedded_bible['Verses'] = embedded_bible['Verses'].apply(
    lambda x: re.sub(r'^\d+:\d+\s+', '', x))


def find_similar_vectors(search, embedded_quraan):

    search_vector = get_embedding(search, engine="text-embedding-ada-002")
    embedded_quraan = embedded_quraan.dropna(subset=['Embeddings'])
    embedded_quraan["similarities"] = embedded_quraan['Embeddings'].apply(
        lambda x: cosine_similarity(x, search_vector))
    embedded_quraan = embedded_quraan.sort_values(
        'similarities', ascending=False)

    return embedded_quraan['Verse'].unique()[0:5]

# Function 2 (quraan to bible mapping)


def find_similar_vectors2(search, embedded_bible):

    search_vector = get_embedding(search, engine="text-embedding-ada-002")
    embedded_bible = embedded_bible.dropna(subset=['Embeddings'])
    embedded_bible["similarities"] = embedded_bible['Embeddings'].apply(
        lambda x: cosine_similarity(x, search_vector))
    embedded_bible = embedded_bible.sort_values(
        'similarities', ascending=False)

    return embedded_bible['Verses'].unique()[0:5]
