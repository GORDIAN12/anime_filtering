# System recommendation with sos_similrarity
# Anime Filtering Recommendation System

A **Streamlit-based anime recommendation web app** that suggests similar anime titles using two filtering approaches:

- **title similarity filtering**
- **genre-based filtering**

The application also integrates the **Anime DB API** through RapidAPI to fetch anime cover images dynamically.

---

## Overview

This project recommends anime titles based on precomputed similarity matrices stored in `.pkl` files.  
When a user selects an anime from the dropdown menu, the app generates recommendations using:

1. **Similarity filtering** → recommends anime with similar overall features
2. **Genre filtering** → recommends anime based on genre similarity

Additionally, the app calls an external API to retrieve anime poster images and display them in the interface.

---

## Features

- Interactive web app built with **Streamlit**
- Anime selection from a dropdown list
- Recommendation generation using:
  - similarity matrix filtering
  - genre-based filtering
- Dynamic anime image retrieval using **RapidAPI**
- Clean multi-column recommendation display
- Uses preprocessed and serialized datasets with `pickle`

---

## Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **Requests**
- **Pickle**
- **RapidAPI (Anime DB API)**

---

## Project Structure

Example project structure:

```bash
anime_filtering/
│
├── app.py
├── animes_list.pkl
├── similarity.pkl
├── genres_filter.pkl
├── similarity_genres.pkl
├── requirements.txt
└── README.md


![image](https://github.com/user-attachments/assets/2b061286-aba7-4593-a9d7-2ac443def972)
