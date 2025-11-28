import streamlit as st
import pickle

# Charger le modèle et le vecteur TF-IDF
with open("models/spam_detector_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

st.title(" Anti-Spam Intelligent")
st.write("Analyse d’un email à partir de son **objet** et son **contenu**.")

# Champs séparés
objet = st.text_input(" Objet de l'email :")
message = st.text_area(" Contenu de l'email :")

if st.button("Analyser"):
    if objet.strip() == "" and message.strip() == "":
        st.warning("Veuillez remplir l'objet ou le contenu.")
    else:
        # Fusion : objet + contenu
        email_text = objet + " " + message

        # Vectorisation
        vec = vectorizer.transform([email_text])
        prediction = model.predict(vec)[0]

        # Résultat
        if prediction == 1:
            st.error(" Ce message est  SPAM")
        else:
            st.success(" Ce message semble légitime (HAM)")
