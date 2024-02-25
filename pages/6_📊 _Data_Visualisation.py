import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import gdown

# Replace 'FILE_ID' with the actual ID of your Google Drive file
file_id = '1m73Ot3M2O2YPPH1urzuTejOaOEQuDi2P'
# Google Drive API endpoint to download the file
url = f'https://drive.google.com/uc?id={file_id}'
file = gdown.download(url,output="wildfire_base_clean.zip")
# Convert the downloaded file bytes to a BytesIO object
# file_in_memory = BytesIO(file_bytes)

df=pd.read_csv(file,compression='zip')
st.set_page_config(page_title="Data Visualisation", page_icon="Fire_logo.png",)
pages=["Data Viz' générale","Data Viz' régionale","Data Viz' temporelle"]

page = st.sidebar.radio("Cliquez sur la partie à afficher", pages)
if page == pages[0] :
    tab1, tab2, tab3 = st.tabs(["Taille des feux","Dichotomie des feux", "Focus sur les Mégafeux"])
    with tab1:
        st.header("Focus sur la variable Taille des feux")
        st.dataframe(df.taille_feu.describe())
     
    with tab2:
        col1, col2, col3 = st.columns([1,3,1])
        col1.write("")
        col2.write("## La dichotomie des feux")
        col3.write("")
        st.write("Nous pouvons observer dans le jeu de données, 2 « tendances », illustrées par une série de 2 graphiques sur la même variable")
        col1, col2 = st.columns(2)
        col1.write("Les feux nombreux, de petite taille,  de cause humaine")
        col2.write("Les feux plus rares, de taille importante, de cause naturelle")
        st.divider()
        st.image("Variable_Cause.png",width=1100)
        st.divider()
        st.image("Variable_Classe.png",width=1100)
        st.divider()
        st.image("Variable_mois.png", width=1100)
        st.divider()
        st.image("Variable_année.png", width=1100)
        st.divider()
        st.image("Variable_region.png", width=1100)
        st.divider()
        st.image("Variable_vegetation.png", width=1100)

    with tab3:
        st.header("Focus sur les mégafeux")

if page == pages[1] :
    st.write("###Relation entre nombre de feux et données géographiques")
    st.write("##Les régions Southeast et Southwest représentent le plus grand nombres de feux entre 1992 et 2020.") 
    st.divider()
    st.image("Nombre_de_Feux_par_Régions.gif")
    st.divider()
    st.write('Cette carte affiche les mégafeux principalement situés à l’ouest du continent. ils sont liés a des cause Naturelles')
    st.divider()
    st.image("Carto_Megafeux.png")
    st.divider()
    st.write("#Relation entre température, précipitation et taille des feux")
    st.divider()
    st.image("TempMoy_classG_feu.png")
    st.write("Elles sont significatives entre 2005 et 2015 mais c’est surtout dans la région de SouthEast ou la température a un impact sur le nombre des Mégafeux.")
    st.image("Evol_tempMoyenn_sur_Megafeu_southeast.png")
    st.divider()
    st.write("#Relation entre végétation et taille des feux")
    st.write("Les végétations Boreal Evergreen (feuillage persistant de la forêt boréale) et shrubland (arbustes) sont les végétations du continent les plus touchées.")
    st.image("Moy_Taille_Feu_par_Veget.png")
    st.divider()
    st.write("#Relation entre cause et taille des feux")
    st.write("La taille des feux augmente significativement jusqu’en 2006 et reste stable jusqu’en 2020. La cause Natural est la plus importante depuis 2006.")
    st.divider()
    st.image("Relation_cause_taille_feux_par_année.png")
    st.divider()

if page == pages[2] :
    st.write("## Temporelle")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()

