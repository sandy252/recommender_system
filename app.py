import streamlit as st
import pickle
import requests


similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8011943be1f4d77ee493a14da30f7406&language=en-US'.format(movie_id))
    # print(response)
    movie_data = response.json()
    # st.text(movie_data)
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key=8011943be1f4d77ee493a14da30f7406&language=en-US'.format(movie_id))
    return 'https://image.tmdb.org/t/p/w500/' + movie_data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    # st.text(movies_list)

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        # st.text(movie_id)

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


# movies = pickle.load(open('data.pkl', 'rb'))
movies = pd.read_pickle('data.pkl')
# movies_list = movies_list['title'].values
st.title("Movie Recommender System")
# print(movies)

selected_movie = st.selectbox('Search for the movie', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
