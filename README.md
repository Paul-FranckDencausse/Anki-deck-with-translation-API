# 🧠 Anki - Extraction de vocabulaire Portugais ⇨ Français

Ce petit script te permet de :
1. Prendre un texte écrit en portugais (européen)
2. Extraire automatiquement les mots de vocabulaire (mots uniques uniquement)
3. Les traduire en français
4. Générer un fichier `.csv` compatible avec **Anki**

## 🚀 Installation

### 1. Cloner ou télécharger le projet
      https://github.com/Paul-FranckDencausse/Anki-deck-with-translation-API
### 2. Imposter les dépendances
  pip install nltk googletrans==4.0.0-rc1

## Utilisation

  Tu peux modifier la variable texte_portugais dans le fichier vocab_extract.py avec n'importe quel texte en portugais.Puis, lance le script :
    python vocab_extract.py
  Tu obtiendras un fichier vocabulaire.csv que tu peux importer dans Anki :
    Recto : mot portugais
    Verso : traduction en français

## Exemple (avec le fichier test.txt)

  Mot Portugais   |   Traduction Française
    amigos        |     amis
    brincar       |     jouer
    cachorro      |     chien
    correndo      |     courir
    ele           |     il
    gosta         |     aime
    no            |     dans le
    o             |     le
    parque        |     parc
    seus          |     ses
    está          |     est

## Limites

  - Traduction mot-à-mot : pas de contexte, donc parfois approximatif.

  - Mots très fréquents (articles, prépositions) ne sont pas filtrés (tu peux le faire si tu veux affiner).

  - L'API gratuite de Google Translate peut parfois échouer ou ralentir.

## Axes d'amélioration

  - Ajouter une interface graphique

  - Filtrer les "stop words" portugais

  - Ajouter des exemples d’usage en contexte

  - Support de texte HTML ou PDF
