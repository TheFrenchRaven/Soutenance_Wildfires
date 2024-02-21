import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

# Les titres 
st.title("Analyse des feux de forêts aux USA")
st.sidebar.title("**Feux de forêts aux USA**")
st.sidebar.divider()
st.sidebar.header("Un projet en 4 étapes :")
st.sidebar.subheader("1) Présentation du jeu de données")
st.sidebar.subheader("2) Préparation des données")
st.sidebar.subheader("3) Data Visualisation")
st.sidebar.subheader("4) Modélisation")
st.sidebar.divider()

#Les pages
pages=["1a.Compréhension du jeu de données", "1b.Volumétrie du jeu de données",
       "2a. Nettoyage et sélection","2b.Web Scrapping",
       "3a. Statistique","3b. Régionale","3c. Temporelle",
       "4a. Classification","4b. Time Series"]

page = st.sidebar.radio("                 Cochez la page à afficher", pages)

if page == pages[0] :
    st.write("## Compréhension du jeu de données : première exploration")
    st.divider()
    st.write("https://www.fs.usda.gov/rds/archive/catalog/RDS-2013-0009.6")
    st.divider()
    st.image("https://www.fs.usda.gov/sites/default/files/users/user3824/Photos/CWDG/SweetCrk-Milepost2Fire-Marcus-Kauffman.jpg")

if page == pages[1] :
    st.write("## Préparation des données : complétude des données")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()
if page == pages[2] :
    st.write("## Nettoyage et sélection")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()
if page == pages[3] :
    st.write("## Webscraping")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()
if page == pages[4] :
    st.write("## Statistique")
    st.write('Nous pouvons observer dans le jeu de données, 2 « tendances », avec d’un côté les feux nombreux, de petite taille  avec une cause humaine, et de l’autre les feux plus rares, de taille importante avec une cause naturelle.')
    st.write("Cette dichotomie peut s'observer avec une série de double graphiques sur une même variable :")
    st.write('le premier représente la variable en % du nombre de feux, le second en % de la surface')
    st.divider()
    st.image("Variable_Cause.png")
    st.divider()
    st.image("Variable_Classe.png")
    st.divider()
    st.image("Variable_mois.png")
    st.divider()
    st.image("Variable_année.png")
    st.divider()
    st.image("Variable_region.png")
    st.divider()
    st.image("Variable_vegetation.png")

if page == pages[5] :
    st.write("## Régionale")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()

if page == pages[6] :
    st.write("## Temporelle")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()

if page == pages[7] : 
    st.write('## Modèle de classification')
    st.write('### LogisticRegression')
    st.write('score sur le jeu de test : 0.6471896781847842')
    st.write('score sur le jeu de train: 0.6525264009985726')
    st.write('### RandomForestClassifier')
    st.write('score sur le jeu de test : ')
    st.write('score sur le jeu de train: ')
    st.write('### DecisionTreeClassifier')
    st.write('score sur le jeu de test : 0.5963221118196649')
    st.write('score sur le jeu de train: 0.9997713664254686')
    st.divider()

if page == pages[8] :
    st.header('Time Series avec Prophet')


st.write('Notre base de données comportant plusieurs variables temporelles, il était logique de s’intéresser aux séries temporelles ou Time Series. Nous nous sommes tournés vers la librairie Prophet de Meta (ou Facebook Prophet), librairie open source et facile d’utilisation, pour mettre en œuvre cette Time Series. Nous avons testé le modèle multiplicatif et le modèle additif de Facebook Prophet et nous avons vu que le premier correspond mieux à nos données. Notre objectif est d’essayer de prédire la décennie suivante (2021-2030) par rapport à la dernière décennie (2011-2020) du jeu de données.')
st.write('Premières tendances sur le jeu de données filtré :')

st.image("Tendances.png")


st.write('On crée alors un dataset qui contient la décennie retenue et la décennie à prédire. Puis Prophet calcule la prédiction sur les feux pour la décennie suivante.')

st.image('Première prédiction.png')

st.write('La prédiction, qui commence en 2021 sur ce graphique, montre des feux en croissance régulière, mais constante.')

st.write('On peut vérifier les tendances et la saisonnalité en affichant les composantes de la prédiction.')

st.image('Composantes de la prédiction.png')

st.write('Le premier graphique montre que la tendance est croissante. Le deuxième graphique indique que les feux sont constants et plus fréquents en avril et en juillet, ce qui confirme nos premières observations.')

st.write('Les change points (points de changements) sont les points dans le temps où les séries temporelles présentent des changements abrupts dans la trajectoire.')


st.image('Première prédiction avec change points.png', caption = 'Première prédiction avec change points' )

st.write('Premières métriques')
col1, col2, col3, col4 = st.columns(4)
col1.metric("Horizon", "37 jours",  "365 jours")
col2.metric("RMSE", "106.38", "-51.93")
col3.metric("MAE", "77.48", "-36.85")
col4.metric("MAPE", "54%", "57%")

st.write('Prédiction avec ajustement des hyperparamètres')

st.image('Prédiction avec hyperparamètres ajustés.png')

col1, col2, col3, col4 = st.columns(4)
col1.metric("Horizon", "37 jours",  "365 jours")
col2.metric("RMSE", "104.8", "-52.86")
col3.metric("MAE", "76.42", "-37.22")
col4.metric("MAPE", "82%", "-58%")


st.write('L’ajustement des hyperparamètres n’a pas permis d’obtenir de meilleurs résultats sur les métriques. Bien au contraire, les pourcentages d’erreurs dans la prédiction sont plus élevés.')

st.write('Si Prophet est adapté à la prévision de données contenant des outliers, les métriques telles que la RMSE et la MAE ne le sont pas. Elles y sont, au contraire, très sensibles, ce qui peut expliquer que notre modèle échoue à prédire la prochaine décennie. Le même problème s’est présenté sur le modèle de classification qui a échoué à prédire les classes D, E, F et G.')

st.write('Pour aller plus loin : nous pourrions envisager de travailler sur une autre Time Series, mais en supprimant certaines classes de feux.')




st.sidebar.divider()

st.sidebar.header("L'équipe")


