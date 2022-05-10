# Capstone Project - Restaurant-Recommender
by Debra Goei
---
Background
Recommender Systems are algorithms that aim to suggest to users the most relevant and accurate information from an information [*base*](https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada). They recognize trends in the data through learning user patterns, thus producing reliable outcomes. This dataset is an extracted subset of Yelp’s user data for restaurant business reviews, which was originally made available for the Yelp Dataset Challenge as yelp does not allow the scraping of data from its [*website](https://www.yelp-support.com/article/Can-I-copy-or-scrape-data-from-the-Yelp-site?l=en_US).

Problem Statement
[*"Yelp connects people with great local businesses"*](https://www.yelp.com/about) - Yelp is a business directory service which allows users to leave ratings and create reviews on businesses, as well as a reservation system. For the purpose of this porject, we will be looking closely at restaurant reviews in the city of Toronto in Canada.

In particular, we will focus on the following in order to build a restaurant recommender in [*StreamLit:*](https://share.streamlit.io/debragoei/RestaurantRecommender/main/[app path])

Reviews of the restaurant
Word cloud and top most common words in reviews 
Sentiment Analysis
Using models (logistic regression and random forests), count and tfid vectorizer, gridsearch to evaluate performance
StreamLit