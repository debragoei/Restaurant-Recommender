import pickle
import streamlit as st
import requests

def recommend(restaurant):
    index = toronto_final[toronto_final['name'] == restaurant].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_restaurant_names = []
    for i in distances[1:6]:
        movie_id = restaurant.iloc[i[0]].movie_id
        recommended_restaurant_names.append(restaurant.iloc[i[0]].title)
    return recommended_restaurant_names


st.header('Toronto Restaurant Recommender System')
restaurants = pickle.load(open('..Code/restaurant_list.pkl','rb'))
similarity = pickle.load(open('..Code/similarity.pkl','rb'))

restuarant_list = toronto_final['name'].values
selected_restaurant = st.selectbox(
    "Type or select a restaurant from the dropdown",
    restaurant_list
)

if st.button('Show Recommendation'):
    recommended_restaurant_names = recommend(selected_restaurant)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_restaurant_names[0])
    with col2:
        st.text(recommended_restaurant_names[1])
    with col3:
        st.text(recommended_restaurant_names[2])
    with col4:
        st.text(recommended_restaurant_names[3])
    with col5:
        st.text(recommended_restaurant_names[4])
