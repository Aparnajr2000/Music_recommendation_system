import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load data from CSV file
@st.cache
def load_data():
    df = pd.read_csv('D:\College\Sem 1\Step presentation\Spotify-2000.csv')
    return df

df = load_data()

# Music Recommendation Model
def recommend_songs(song_name, n_recommendations=3):
    song_index = df[df['Song'] == song_name].index[0]
    features = df[['Feature1', 'Feature2']]
    model = NearestNeighbors(n_neighbors=n_recommendations+1, algorithm='auto').fit(features)
    distances, indices = model.kneighbors(features)
    recommendations = indices[song_index][1:]  # Exclude the song itself
    recommended_songs = df.iloc[recommendations]['Song'].values
    return recommended_songs

# Streamlit Front End
st.title('Music Recommendation System')

# User Input
selected_song = st.selectbox('Select a song you like:', df['Song'].values)

if st.button('Recommend'):
    recommendations = recommend_songs(selected_song)
    st.write(f"Because you like **{selected_song}**, you might also like:")
    for song in recommendations:
        st.write(song)

# To run this script, use the terminal and navigate to the directory containing this file
# Then run: streamlit run music_recommender.py
