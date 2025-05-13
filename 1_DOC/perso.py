
# fonction
import sys
sys.path.append(r"C:\Users\franc\Desktop\DATA_SCIENCE\ML_PRO\DOC")
from perso import *
import warnings


# libriairies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import sklearn
from sklearn.model_selection import train_test_split




## MES FONCTION 

def explore_col(data,max_value=15):
    """Affiche les valeurs uniques des colonnes de type texte ou catégoriel vec un message pour celles
       qui dépassent max_values (15 par default valeurs uniques."""
   # Sélectionner les colonnes de type texte ou catégoriel
    cat_columns = data.select_dtypes(include=['object', 'category']).columns.tolist()
    # Liste pour les colonnes ayant 15 valeurs uniques ou moins  
    for column in cat_columns:
        unique_count = data[column].nunique()
        if unique_count > max_value:
            print(f"La colonne '{column}' prend plus de {max_value} valeurs ({unique_count}).")
        else:
            liste_column=data[column].unique().tolist() 
            print(f"Les {len(liste_column)} valeurs prises par '{column}' sont : {liste_column}")


def liste_vd(data,max_value=15):
    """Retourne la liste des colonnes de type texte ou catégoriel"""
    # Sélectionner les colonnes de type texte ou catégoriel
    cat_columns = data.select_dtypes(include=['object', 'category']).columns.tolist()
    
    return cat_columns


def affichage_hb(data, col):  
    """Affiche un boxplot et un histogramme pour une variable continue"""
    fig, ax = plt.subplots(2, 1, sharex=True)
    sns.boxplot(data=data, x=col, ax=ax[1])
    sns.histplot(data=data, x=col, ax=ax[0])
    plt.suptitle(f"Visualisation de la variable {col}")
    plt.show()
    return fig , ax


def split(data, test_size=0.2 ):
    train_set ,test_set = train_test_split(data, test_size=0.2 , random_state=0)
    print("train_set : ",train_set.shape )
    print("test_set : ",test_set.shape )

    if isinstance(data, pd.DataFrame):
        return pd.DataFrame(train_set, columns=data.columns),pd.DataFrame(test_set, columns=data.columns)
    else :    
        return pd.DataFrame(train_set),pd.DataFrame(test_set)


def ignore_warnings():   
    """Ignore les FutureWarnings"""
    warnings.filterwarnings("ignore", category=FutureWarning)









def plot_bar_with_values(series, normalize=False, sort=True, rotation=0, decimals=2, color='black' ):
    """
    Affiche un bar plot annoté à partir d'une Series pandas.

    Paramètres :
    - series : pd.Series — la série de données catégorielles
    - normalize : bool — True pour afficher les proportions, False pour les comptes
    - sort : bool — True pour trier les valeurs
    - rotation : int — angle de rotation des étiquettes (x-ticks)
    - decimals : int — nombre de décimales à afficher sur les barres
    - color : str — couleur des bords des barres (edgecolor)

    Retour :
    - ax : objet matplotlib Axes
    """

    # Création du graphique
    counts = series.value_counts(normalize=normalize, sort=sort)
    ax = counts.plot(kind="bar", edgecolor=color)

    # Orientation des labels en x
    plt.xticks(rotation=rotation)

    # Ajout des annotations sur chaque barre
    for p in ax.patches:
        height = p.get_height()
        ax.annotate(f"{height:.{decimals}f}",               # Texte formaté
                    (p.get_x() + p.get_width() / 2, height), # Coordonnées texte
                    ha='center', va='bottom')                # Centré au-dessus

    plt.show()
    return ax
