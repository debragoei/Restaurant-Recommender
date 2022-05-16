# GTA Restaurant Recommender
by Debra Goei
---
Data Source: The data used for this project was part of a Kaggle competition by [*Yelp*](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset).

Link to [*Streamlit App*](http://192.168.1.76:8501).
---
Problem Statement

[*"Yelp connects people with great local businesses"*](https://www.yelp.com/about) - Yelp is a business directory service which allows users to leave ratings and create reviews on businesses, as well as a reservation system. For the purpose of this project, we will be looking closely at restaurant reviews in some parts of the Greater Toronto Area in Canada. 

This project applies Natural Language Processing on Yelp reviews in order to create a new insight into the driving force behind business reviews created by users. As both a self-declared 'foodie' as well as a contractor for the GTA BIA (Business Improvement Area), this project will provide a user-driven recommender system that the BIA can use to provide feedback to businesses for improvement and upkeep. For everyday users, it provides more than just a number rank for restaurants, which would encourage more honest reviews and for users to be introduced to small local businesses.

---

Background

Recommender Systems are algorithms that aim to suggest to users the most relevant and accurate information from an information [*base*](https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada) and are used very frequently in machine learning. They recognize trends in the data through learning user patterns, thus producing reliable outcomes. This dataset is an extracted subset of Yelp’s user data for restaurant business reviews, which was originally made available for the Yelp Dataset Challenge as yelp does not allow the scraping of data from its [*website](https://www.yelp-support.com/article/Can-I-copy-or-scrape-data-from-the-Yelp-site?l=en_US).

Using clustering can address several known issues in recommendation systems, including increasing the diversity, consistency, and reliability of recommendations; the data sparsity of user-preference matrices; and changes in user preferences over time. This work will be useful for both beginners in the field of recommender systems and specialists in related fields that are interested in examining the applicability of recommender systems. This review is focused on the analysis of the scientific literature on the topics of recommender systems and clustering models that have appeared in recent years and contains a representative list of the literature for the further exploration of this topic. In the first part, a brief introduction to the so-called classic or traditional recommendation algorithms is given, along with an overview of the clustering problem.

---

In particular, we will focus on the following in order to build a restaurant recommender in [*StreamLit:*](https://share.streamlit.io/debragoei/RestaurantRecommender/main/[app path])





---
Methodology

Using Sentiment Analysis Packages like Textblob and VADER, we can analyze text reviews to derive further quantitative metrics on a user's overall sentiment and review of a restaurant visit. 

Lastly, this project will use the longitude and latitude points of restaurants to build a Location Based Recommendation System and cluster restaurants together using the K-Means Clustering Algorithm.


---
Conclusion and Remarks
this Capstone Project aims to create is an alternative food recommendation system based on user reviews and sentiment analysis. As more and more people are starting to frequent restaurants again in Phase 2, this Capstone Project aims to help people become more aware of local Restaurants through this Recommendation System and help keep their businesses alive.

The Recommendation System Models will be built based on the Yelp Reviews Dataset on Kaggle, particularly focusing on Restaurant Reviews in the city of Toronto. With the models built out, this project can be applied to other cities as long as we can get similar datasets for such cities.

