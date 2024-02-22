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

if page == pages[9] : 
    st.write('## Testes Statistiques')
    st.write('### ANOVA : Test de Kruskal-Wallis (Végétation régionale & Taille des feux)')
    st.write('H0 : Il n'y a pas d'effet significatif de la végétation sur la Taille des feux')
    col1, col2 = st.columns(2)
    col1.metric("KruskalResult(statistic)", "97811.02482749475")
    col2.metric("pvalue", "0.0")
    st.write('On rejette H0 : Il y a un effet statistique significatif de la végétation sur la taille des feux')

    st.write('### ANOVA : Test de Kruskal-Wallis (Cause & Taille des feux')
    st.write('H0 : Il n'y a pas d'effet significatif de la cause sur la Taille des feux')
    col1, col2 = st.columns(2)
    col1.metric("KruskalResult(statistic)", "29011.246268456314")
    col2.metric("pvalue", "0.0")
    st.write('On rejette H0 : la cause des feux semble bien avoir un impact significatif sur la taille des feux : cas des causes naturelles en majorité dans le Sud Ouest et Nord Ouest')

    st.write('### Corrélation : Test de Pearson (Précipitation moy. mens. & Taille des feux)')
    st.write('H0 : Il n'y a pas de corrélation entre la précipitation et la Taille des feux')
    col1, col2 = st.columns(2)
    col1.metric("Corrélation de Pearson(précipitation moy.mens.)", "-0.02047855970785961")
    col2.metric("pvalue", "3.49452e-207")
    st.write("On rejette H0 : corrélation statistiquement significative entre Précipitation moy. mens. et Taille des feux, mais une corrélation négative très faible et proche de 0 (-0,02)")

    st.write('### Corrélation : Test de Spearman (Précipitation moy. mens. & Taille des feux)')
    st.write('H0 : Il n'existe pas de relation linéaire entre la précipitation et la Taille des feux')
    col1, col2 = st.columns(2)
    col1.metric("Corrélation de Spearman", "0.15550443118114127")
    col2.metric("pvalue", "0.0")
    st.write("On rejette H0 : Le test de Spearman confirme qu’il existe bien une relation statistique significative entre ces 2 variables")
    st.image("Relation_Precip&TailleFeux.png")

    st.write('### Corrélation : Test de Pearson (Température moy. mens. & Taille des feux')
    st.write('H0 : Il n'y a pas de corrélation entre la Température moy.mens. et la Taille des feux')
    col1, col2 = st.columns(2)
    col1.metric("Corrélation de Pearson(température moy.mens.)", "0.011750792216244654")
    col2.metric("pvalue", "1.61714208e-69")
    st.write("On rejette H0 : Il existe une faible relation monotone entre la taille des feux et la température moyenne mensuelle. Même si la corrélation est statistiquement significative (p-value = 0), la variation de la température moyenne mensuelle ne semble pas expliquer d’une manière significative la taille des feux")
    

    st.write('### Corrélation : Test de Spearman (Température moy. mens. & Taille des feux)')
    st.write('H0 : Il n'existe pas de relation linéaire entre la Température et la Taille des feux')
    col1, col2 = st.columns(2)
    col1.metric("Corrélation de Spearman", "-0.04421683488823663")
    col2.metric("pvalue", "0.0")
    st.write("On rejette H0 : Le test de Spearman confirme le rejet de notre hypothèse nulle selon laquelle il n’y a pas de corrélation entre ces 2 variables")
    st.image("Relation_Temp&TailleFeu.png")

    st.write("Plusieurs facteurs peuvent expliquer la taille des incendies (végétation, cause, précipitation moyenne, température")





st.sidebar.divider()


st.sidebar.header("L'équipe")


