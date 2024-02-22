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
    col1, col2 = st.columns(2)
    col1.metric("Score X_test", "0.6471896781847842")
    col2.metric("Score X_train", "0.6525264009985726")

    st.write('### RandomForestClassifier')
    col1, col2 = st.columns(2)
    col1.metric("Score X_test", "0.6554204360077117")
    col2.metric("Score X_train", "0.9997342907106797")

    st.write('### DecisionTreeClassifier')
    col1, col2 = st.columns(2)
    col1.metric("Score X_test", "0.5963221118196649")
    col2.metric("Score X_train", "0.9997713664254686")

    st.write('Classification Report & Matrice de Confusion du RandomForestClassifier')
    st.image("MatConf_ClassReport-RF_1.png")

    st.write('Features Importances du RandomForestClassifier (20 premières fonctionnalités)')
    st.image("Feat_Importance_RF_1.png")

    st.write('#### Ajustement des hyperparamètres du RandomForestClassifier')   
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("max_depth", "None")
    col2.metric("min_samples_leaf", "1")
    col3.metric("min_samples_split", "10")
    col4.metric("n_estimators", "200")
       
    st.metric("Score X_test", "0.6778140293637847")
    st.write("Le modèle RandomForest performe mieux sans limitation de la profondeur des arbres.")
    st.write("L'optimisation des hyperparamètres a contribué à améliorer la performance du RandomForest par rapport à ses paramètres par défaut. Il semble mieux généraliser aux données non vues dans l'ensemble de test.")
       
    st.write('Classification Report & Matrice de Confusion du RandomForestClassifier aprés ajustement des hyperparaètres')
    st.image("MatConf_ClassReport-RF_2(optimisation).png")
    st.write('Le modèle semble bien performant pour les classes A et B, mais a des difficultés avec les autres classes')
    st.write('Défis potentiels dans la classification des classes moins fréquentes ou moins bien représentées.')
    st.image("DistributionClasse_avant_prediction.png")  
    st.image("DistributiClassePrédites_RF.png") 
    st.write('Les classes moins fréquentes (F et G) présentent des difficultés plus importantes pour le modèle.')
    st.image("Valeurs_Predites_RF.png")

    st.write('## Autres modèles testés')
    col1, col2, col3 = st.columns(3)
    col1.metric("SVM : Score X_test", "0.6731054426812991")
    col2.metric("Gradient Boosting : Score X_test", "0.6499147263829156")
    col3.metric("knn : Score X_test", "0.6440753373869198")

    
       
       
       
    st.divider()

if page == pages[8] :
    st.write("## Modélisation temporelle avec Prophet")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()
st.sidebar.divider()

st.sidebar.header("L'équipe")


