import streamlit as st
import pickle
import pandas as pd
import joblib
import numpy as np
import nltk
import sklearn


st.title(" Movie Recommendation System")
with open("model.pkl", "rb") as f:
    movies = pickle.load(f)
    
    
similarity_matrix= joblib.load('similarity_matrix.joblib')

movie_names=movies['title'].values
name_movie= st.selectbox("Select a movie", movie_names)

# build recommendation function
def recommend(name_movie,top_n=5):
    item_name = name_movie.lower()
    # get the index of the movie
    movie_index = movies[movies['title']== item_name].index[0]
    
    # get the similarity scores for the movie
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))
    
    # sort the movies based on similarity scores
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    # get the top 5 similar movies (excluding the first one which is the movie itself)
    top_movies = sorted_movies[1:6]
    
    # get the titles of the top 5 similar movies with similarity scores 
    recommended_movies = [(movies.iloc[i[0]]['title'], i[1]) for i in top_movies]
    return recommended_movies

if st.button("Recommend"):
    recommended = recommend(name_movie)
    st.write("Recommended movies are:")
    for i in recommended:
        st.write(f"{i[0]} ")