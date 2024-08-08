import requests
import streamlit as st
import json
import pandas as pd
headers = {
    'x-rapidapi-key': "YOUR_RAPIDAPI_KEY",
    'x-rapidapi-host': "YOUR_RAPIDAPI_HOST"
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

st.header('Movie Recommendations')
animes=pd.read_pickle('animes_list.pkl')
similarity=pd.read_pickle('similarity.pkl')

anime_list=animes['title'].values
selected_movies=st.selectbox(
    "Selecciona el anime de la lista",
    anime_list
)


import streamlit as st

if st.button('Recomendar la pelicula'):
    recommend_movie_names,recommend_movie_posters=recommend_anime(selected_movies)
    cols=st.columns(5)

    for i, col in enumerate(cols):
        col.text(recommend_movie_names[i])
        col.image(recommend_movie_posters[i])

