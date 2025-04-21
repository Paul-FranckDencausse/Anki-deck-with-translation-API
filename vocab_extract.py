# vocab_extract.py

import nltk
from googletrans import Translator
import csv

# Télécharger les données nécessaires pour tokenizer
nltk.download('punkt')

# --- Étape 1 : lecture du texte portugais ---
texte_portugais = """
O cachorro está correndo no parque. Ele gosta de brincar com seus amigos.
"""

# --- Étape 2 : découpage du texte en mots uniques ---
def decouper_texte(texte):
    mots = nltk.word_tokenize(texte, language='portuguese')
    mots_uniques = sorted(set([mot.lower() for mot in mots if mot.isalpha()]))
    return mots_uniques

# --- Étape 3 : traduction des mots en français ---
def traduire_mots(mots, src='pt', dest='fr'):
    translator = Translator()
    traductions = {}
    for mot in mots:
        try:
            traduction = translator.translate(mot, src=src, dest=dest).text
            traductions[mot] = traduction
        except Exception as e:
            traductions[mot] = "Erreur"
            print(f"Erreur de traduction pour '{mot}' : {e}")
    return traductions

# --- Étape 4 : sauvegarde dans un fichier CSV ---
def sauvegarder_csv(traductions, filename="vocabulaire.csv"):
    with open(filename, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Mot Portugais", "Traduction Française"])
        for mot, trad in traductions.items():
            writer.writerow([mot, trad])

# --- Exécution ---
mots = decouper_texte(texte_portugais)
trads = traduire_mots(mots)
sauvegarder_csv(trads)

print("✅ Deck Anki généré : vocabulaire.csv")
