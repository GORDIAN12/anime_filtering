import requests
import streamlit as st
import json
import pandas as pd
import time

headers = {
    'x-rapidapi-key': "c6fe4a1625msh85a232902b3f65ap19965cjsn47c3f07001ac",
    'x-rapidapi-host': "anime-db.p.rapidapi.com"
}


def search_anime(anime):
    search_url = f"https://anime-db.p.rapidapi.com/anime?page=1&size=10&search={anime}"
    response = requests.get(search_url, headers=headers)
    anime_data = response.json()
    data_list=anime_data["data"]
    title=[item['title'] for item in data_list]
    print(title[0])
    get_url=[item['image'] for item in data_list]
    print(get_url[0])
    return get_url[0]

def recommend_anime(anime_name):
    index=animes[animes['title']==anime_name].index[0]

    distances=sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    recmmended_name=[]
    recmmended_img=[]

    for i in distances[1:6]:
        anime_title=animes.iloc[i[0]].index
        print(anime_title)
        anime_search=animes.iloc[i[0]].title
        recmmended_img.append(search_anime(anime_search))
        recmmended_name.append(animes.iloc[i[0]].title)

    return recmmended_name,recmmended_img


def recommend_gen(movie_title):
    anime_idx = anime_gen[anime_gen['title'] == movie_title].index[0]
    similarity_scores = sorted(list(enumerate(similarity_gen[anime_idx])), reverse=True, key=lambda x:x[1])
    recmmended_name_gen = []
    recmmended_img_gen = []

    movie_indices = [i[0] for i in similarity_scores[1:]]  # Excluir la película en sí misma

    for i in movie_indices[:5]:
        anime_gen_name=anime_gen.iloc[i]['title']

        recmmended_img_gen.append(search_anime(anime_gen_name))
        recmmended_name_gen.append(anime_gen_name)

    return recmmended_name_gen,recmmended_img_gen

st.header('Movie Recommendations')
animes=pd.read_pickle('animes_list.pkl')
similarity=pd.read_pickle('similarity.pkl')
anime_gen=pd.read_pickle('genres_filter.pkl')
similarity_gen=pd.read_pickle('similarity_genres.pkl')

anime_list=animes['title'].values
selected_movies=st.selectbox(
    "Selecciona el anime de la lista",
    anime_list
)


import streamlit as st

if st.button('Recomendar la pelicula'):
    recommend_movie_names,recommend_movie_posters=recommend_anime(selected_movies)
    recommend_name_gen,recommend_img_gen=recommend_gen(selected_movies)
    cols1=st.columns(5)
    cols2=st.columns(5)

    for i, col in enumerate(cols1):
        col.text(recommend_movie_names[i])
        col.image(recommend_movie_posters[i])

    for i, col in enumerate(cols2):
        col.text(recommend_name_gen[i])
        col.image(recommend_img_gen[i])
