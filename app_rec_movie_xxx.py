import streamlit as st
from myfunction_6xxx import get_movie_recommendations
import pickle
 
# Load data back from the file
with open('recommendation_data.pkl', 'rb') as file:
    user_similarity_df, user_movie_ratings = pickle.load(file)
 
st.title('Movie Recommendation System')
 
# Get recommendations for a user
user_id = st.number_input('Enter User ID', min_value=1, max_value=610, value=1)
n_recommendations = st.slider('Number of recommendations', min_value=1, max_value=20, value=10)
 
if st.button('Get Recommendations'):
    recommendations = get_movie_recommendations(user_id, user_similarity_df, user_movie_ratings, n_recommendations)
 
    st.write(f"Top {n_recommendations} movie recommendations for User {user_id}:")
    for movie_title in recommendations:
        st.write(movie_title)

