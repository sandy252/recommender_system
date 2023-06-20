# Recommender System

## About Dataset
### Background
What can we say about the success of a movie before it is released? Are there certain companies (Pixar?) that have found a consistent formula? Given that major films costing over $100 million to produce can still flop, this question is more important than ever to the industry. Film aficionados might have different interests. Can we predict which films will be highly rated, whether or not they are a commercial success?

This is a great place to start digging in to those questions, with data on the plot, cast, crew, budget, and revenues of several thousand films.

### Data Source Transfer Summary
Several of the new columns contain json. You can save a bit of time by porting the load data functions from [this]() kernel. Even in simple fields like runtime may not be consistent across versions. For example, previous dataset shows the duration for Avatar's extended cut while TMDB shows the time for the originalversion. There's now a separate file containing the full credits for both the cast and crew.All fields are filled out by users so don't expect them to agree on keywords, genres, ratings, or the like.Your existing kernels will continue to render normally until they are re-run.
If you are curious about how this dataset was prepared, the code to access TMDb's API is posted here.

## Similarity Score 
How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

## How Cosine Similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
![2b4a7a82-ad4c-4b2a-b808-e423a334de6f](https://github.com/sandy252/recommender_system/assets/66490787/bfed0fa4-dae4-4840-9298-32883e83e062)


# app link: 
https://sandy252-recommender-system-app-i5kz1a.streamlit.app/
