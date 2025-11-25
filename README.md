**Anti-Spam Intelligent — Détecteur d'emails malveillants**

Contexte

En tant que développeur IA , ce projet a pour objectif de concevoir un système intelligent capable de détecter automatiquement les emails malveillants (spam) afin de renforcer la sécurité des communications. Le pipeline combine l'exploration des données, le prétraitement textuel NLP, la vectorisation et l'entraînement de modèles supervisés, avec une intégration via une interface Streamlit.

**Structure du projet**
- `app/` : application Streamlit (interface utilisateur pour tester et déployer le modèle)
- `Data/raw/` : jeu de données original (`DataSet_Emails.csv`)
- `Data/processed/` : jeux de données prétraités
- `models/` : modèles entraînés et pipelines sauvegardés
- `notebooks/` : notebooks pour EDA, prétraitement, entraînement et évaluation
- `requirements.txt` : dépendances Python

**Prérequis**
- Python 3.8+ (recommandé)
- Environnement virtuel recommandé (`venv`, `conda`)

**Installation**
- Créer et activer un environnement virtuel (ex. `venv`) puis installer les dépendances :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Exécution (développement / test)**
- Lancer l'application Streamlit locale :

```powershell
streamlit run app/streamlit_app.py
```

**Jeu de données**
- Emplacement : `Data/raw/DataSet_Emails.csv`.
- Colonnes attendues (exemples) : `id`, `text` (corps du message), `label` (`spam` / `ham`) et éventuellement d'autres métadonnées (expéditeur, date, sujet).

**Pipeline résumé**
- **Analyse des données** : vérifier taille, types de colonnes, valeurs manquantes, doublons et distribution de la cible (spam vs ham). Générer des WordClouds pour visualiser les mots fréquents séparément pour `spam` et `ham`.
- **Nettoyage** : suppression des doublons, suppression des lignes où la colonne texte est vide ou manquante.
- **Normalisation** : passage en minuscules, suppression de la ponctuation et des caractères spéciaux (via regex).
- **Tokenisation** : découpage en tokens (mots).
- **Suppression des stopwords** : éliminer les mots à faible valeur informative.
- **Stemming** : appliquer `PorterStemmer` pour réduire les mots à leur racine.
- **Vectorisation** : `TfidfVectorizer` ou `CountVectorizer` pour convertir le texte en vecteurs numériques.

**Entraînement et évaluation**
- Notebooks présents :
  - `01_EDA.ipynb` — exploration et visualisations (WordClouds, distributions)
  - `02_Preprocessing.ipynb` — pipeline de nettoyage et transformation
  - `03_Model_Training.ipynb` — entraînement de plusieurs classifieurs
  - `04_Evaluation.ipynb` — métriques et comparaisons (accuracy, precision, recall, F1, AUC)
- Modèles recommandés pour essais : Logistic Regression, Random Forest, SVM, Gradient Boosting, XGBoost. Utiliser une séparation train/test stratifiée et validation croisée.

**Sauvegarde du meilleur modèle**
- Sauvegarder le pipeline complet (prétraitement + vectorizer + modèle) dans `models/` (ex. `models/best_model.pkl`) pour un chargement direct par l'application Streamlit.

**Intégration Streamlit**
- L'app `app/streamlit_app.py` doit charger le modèle sauvegardé et proposer :
  - Zone de saisie pour coller ou écrire un email
  - Prédiction `spam` / `ham` et probabilité associée
  - Optionnel : affichage des mots-clés influents ou interprétabilité (ex. coefficients de LR, SHAP pour modèles plus complexes)

**Bonnes pratiques**
- Gérer le déséquilibre des classes : stratified split, pondération de classes, sur-échantillonnage (SMOTE) ou réglage des seuils de décision.
- Reproductibilité : encapsuler le flux dans un `sklearn.pipeline.Pipeline` et versionner les modèles.
- Validation robuste : cross-validation, courbes ROC, matrices de confusion et analyse des faux positifs/négatifs.
- Logging et métriques : enregistrer les scores d'entraînement et d'évaluation (ex. fichier `models/metrics.json`).

**Étapes recommandées (prochaines actions)**
- Exécuter les notebooks `01` → `04` dans l'ordre pour reproduire EDA → prétraitement → entraînement → évaluation.
- Sauvegarder le pipeline final dans `models/` et vérifier que `app/streamlit_app.py` peut le charger.
- Ajouter des tests unitaires pour les fonctions de prétraitement textuel.
- Mettre en place une intégration continue (lint/tests) et versionner les modèles si nécessaire.



----

