# Religious Text Recommendation System




# Motivation

This project was created with the intention of creating a product that would portray that the central teaching of religions are more similar than they are different. Within the three Abrahamic Religions, Judaism , Christianity and Islam, the main teachings of each religion can be primarily found in their respective books: Torah, Bible and Quran. To limit the scope of the project, we decided to focus on comparing the Bible and the Quran.



# Project Description

Our attempt to accomplish the above resulted in a user interactive HTML file that enables users to chose or type a verse from either book and receive the top 5 verses from the other book in terms of similarity. To accomplish this, the following steps were completed:
1) data gathering and processing: 
The most reliable and soundest translations we were able to find from each book were gathered from online sources. The Quran came in the form of individuals Aye's (Verse's). The Bible however was found on Project Gutenberg. Each book was processed as such into a list of verses. 

2) Embedding:
In order to determine which verse from each book can be more similar to another verse from a different book, a measure of similarity must be defined. In order to compute these similarity measures, each verse from each book as well as the individual verse of interest must be turned into there numeric vector representation. As such , different Embedding techniques such as TF-IDF, BERT, and OpenAI's embedder were used. Since there was no numeric metric to determine the relative performance of these models, we perfomed some QA on the result of some verses we had chosen to see which model subjectively performs better. The OpenAI model outperformed all other embedding techniques and we decided to move forward with that. 

3) Cosine Similarity:
Moving forward, the task was simple. After creating numeric vector representaitons for each book, given an input verse from a user, the input verse would also be changed to represent a numeric vector and the cosine similarity of that would be calculated against every verse from the other text. The top 5 most similar verses would be returned as a result. 




4) These numeric representations of each book were saved as pickle files in order for us to be able to preserve and use them easier during run time. 



5) A Flask App was developed for the front end that enables users to chose a verse from each book. This app takes the users input, runs the model through the python files and returns the most similar verses from the other book. 


# Usage:

All files necessary for recreating the project are available in the Repo. 
As for Usage, While in the projects directory, the website can be rendered by doing the following:

1) Unzip the embedded_bible.pickle.zip and embedded_quraan.pickle.zip

2) Download requirements from requirements.txt 

3) Run python main.py


A demo of the project can be found below:

[![Demo](data/demo.png)](https://www.youtube.com/watch?v=dsTI9qa58wY)










