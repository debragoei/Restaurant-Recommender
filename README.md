# GTA Restaurant Recommender

by Debra Goei

---
Data Source: The data used for this project was part of a Kaggle competition by [*Yelp*](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset).

---
1. Problem Statement
2. Background
3. Methodology
4. Data Dictionary
5. Conclusion and Takeaways
---
### Problem Statement

[*"Yelp connects people with great local businesses"*](https://www.yelp.com/about) - Yelp is a business directory service which allows users to leave ratings and create reviews on businesses, as well as a reservation system. For the purpose of this project, we will be looking closely at restaurant reviews in some parts of the Greater Toronto Area in Canada. 

This project applies Natural Language Processing on Yelp reviews in order to create a new insight into the driving force behind business reviews created by users. As both a self-declared 'foodie' as well as a contractor for the GTA BIA (Business Improvement Area), this project will provide a user-driven recommender system that the BIA can use to provide feedback to businesses for improvement and upkeep. For everyday users, it provides more than just a number rank for restaurants, which would encourage more honest reviews and for users to be introduced to small local businesses.

---
### Background

Recommender Systems are algorithms that aim to suggest to users the most relevant and accurate information from an information [*base*](https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada) and are used very frequently in machine learning. They recognize trends in the data through learning user patterns, thus producing reliable outcomes. This dataset is an extracted subset of Yelp’s user data for restaurant business reviews, which was originally made available for the Yelp Dataset Challenge as yelp does not allow the scraping of data from its [*website*](https://www.yelp-support.com/article/Can-I-copy-or-scrape-data-from-the-Yelp-site?l=en_US).

---
### Methodology

#### Data Cleaning and Preprocessing
The Yelp dataset is extremely large with roughly 6 million rows and 14 features for across various states. As such the data had to be constantly transformed in order for the notebooks to be able to process it. Some features were created to enhance our exploratory data analysis in the next section.

#### EDA and Sentiment Analysis
Using EDA to identify and explore unique features, visualizing any relationships and creating a plot on Mapbox. For sentiment analysis, using additional packages like textprocessing in Textblob and evaluation in VADER to analyze text reviews to derive further understanding of a user's overall sentiment and reasoning behind reviews (both positive and negative).

#### Recommender System
This project will build a Content-Based Recommendation System with cosine similarity, which is is a useful metric to measure the text-similarity between two variables irrespective of their sizes. That is important as the two variables in this case are the restaurant name and the engineered text. Additionally, using the latitude and longitude points of restaurants to build a Location-Based Recommendation System and using K-Means clustering. Clustering can address several known issues in recommendation systems but was unable to be used successfully on this project.

---
### Data Dictionary

##### This data dictionary has been created based on the original data (Yelp) and is repeated throughout the datasets
|Feature|Type|Dataset|Description|
|---|---|---|---|
|business_id|int|Yelp|Unique business IDs assigned to each business by Yelp| 
|name|obj|Yelp|Business names| 
|address|obj|Yelp|Business addresses| 
|city|obj|Yelp|City businesses are located in|
|state|obj|Yelp|State businesses are located in|
|postal_code|int|Yelp|Business postal code|
|latitude|float|Yelp|Geographical North-South position|
|longitude|float|Yelp|Geographical East-West position|
|stars|float|Yelp|Overall star rating of the business|
|attributes|obj|Yelp|Features or facilities available for customers|
|categories|obj|Yelp|Various categories for which the business can be included in|
|user_id|float|Yelp|User ID of the users giving reviews|
|review_stars|float|Yelp|User-given star rating of the business|
|text|obj|Yelp|Original text body of the user reviews|
|date|float|Yelp|Original date including year, month and day|
|---|---|---|---|
|year|int|GTA|Feature created to drop month and day| 
|text_word_count|int|GTA|The word count from the original 'text' feature|
|pos_neg|int|GTA|Feature created to differentitae between negative (0) and positive (1) reviews|
|text_clean|obj|GTA|Cleaned feature originating from 'text' feature|
|---|---|---|---|
|rev|obj|cbf|Originating from 'text_clean' transformed feature|
|bag_of_words|obj|cbf|Originating from 'text_clean' transformed feature|

---
### Conclusion and Takeaways

This project managed to successfully create an alternative food recommendation system based on user reviews through content-based filtering. With additional data made available, this project can be applied to other cities as long as similar text (user review) information is available and can provide valuable alternative feedback. Stakeholders at the GTA BIA are able to use the recommender to identify target words in order to assist business owners in improving their businesses, as well as ensure the upkeep of public use areas. For the general public, the recommender can also increase awareness of local restaurants which are considered small businesses that need more revenue to stay afloat. 

Next steps following this project would be to improve on the recommender and ensure the location-based recommender is working, and to deploy both on Streamlit for general use. 




