import pandas as pd
import numpy as np
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""
# GTA Restaurant Recommender

This is a subset of the Yelp Kaggle Challenge, focusing on the
top 5 cities in the province of Ontario, Canada
with the most restaurant reviews on the Yelp dataset.

This is a Content Based Recommender System using cosine similarity.

Checkout my [Github](https://github.com/debragoei) for the full project!
"""

@st.cache(allow_output_mutation=True)
def load_data(nrows):
    data = pd.read_csv("./data/GTATop5_final.csv", nrows=nrows)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

st.subheader('Raw data')
st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]


count = CountVectorizer()
count_matrix = count.fit_transform(data['bag_of_words'])

def content_based_recommendations(name, cosine_sim):

    recommended_restaurants = []
    indices = pd.Series(data.index)
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    idx = indices[indices == name].index[0]

    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

    top_10_indexes = list(score_series.iloc[1:11].index)

    for i in top_10_indexes:
        recommended_restaurants.append(list(data.index)[i])

    return recommended_restaurants

with st.container():
    col1, col2, col3 = st.columns([2,1,2])
    if st.button("Recommend Restaurants"):
        if st.session_state['start_track_i'] < len(tracks):
            st.session_state['start_track_i'] += tracks_per_page
