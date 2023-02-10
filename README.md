# Recommender System

## About Dataset
### Background
What can we say about the success of a movie before it is released? Are there certain companies (Pixar?) that have found a consistent formula? Given that major films costing over $100 million to produce can still flop, this question is more important than ever to the industry. Film aficionados might have different interests. Can we predict which films will be highly rated, whether or not they are a commercial success?

This is a great place to start digging in to those questions, with data on the plot, cast, crew, budget, and revenues of several thousand films.

### Data Source Transfer Summary
Several of the new columns contain json. You can save a bit of time by porting the load data functions [from this kernel]().

Even in simple fields like runtime may not be consistent across versions. For example, previous dataset shows the duration for Avatar's extended cut while TMDB shows the time for the original version.

There's now a separate file containing the full credits for both the cast and crew.

All fields are filled out by users so don't expect them to agree on keywords, genres, ratings, or the like.

Your existing kernels will continue to render normally until they are re-run.

If you are curious about how this dataset was prepared, the code to access TMDb's API is posted here.

New columns:

homepage

id

original_title

overview

popularity

production_companies

production_countries

release_date

spoken_languages

status

tagline

vote_average
# app link: 
https://sandy252-recommender-system-app-i5kz1a.streamlit.app/
