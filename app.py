import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

chatbot = pipeline("text-generation", model="distilgpt2")

disease_treatment = {
    "cold": "Take rest, drink warm fluids, and consider paracetamol for fever.",
    "fever": "Stay hydrated, rest well, and take prescribed antipyretics.",
    "diabetes": "Maintain a balanced diet, exercise regularly, and monitor blood sugar levels.",
    "hypertension": "Reduce salt intake, exercise regularly, and take prescribed medications.",
    "headache": "Stay hydrated, get enough sleep, and avoid excessive screen time.",
    "cough": "Drink warm fluids, use honey and ginger, and avoid cold air.",
    "asthma": "Use prescribed inhalers, avoid allergens, and practice breathing exercises.",
    "allergy": "Identify allergens, take antihistamines if needed, and consult a doctor.",
    "stomach pain": "Eat light food, stay hydrated, and consider antacids if necessary.",
    "migraine": "Rest in a dark room, stay hydrated, and avoid loud noises."
}

def healthcare_chatbot(user_input):
    for disease, treatment in disease_treatment.items():
        if disease in user_input.lower():
            return f"Treatment for {disease}: {treatment}"
    
    if "symptom" in user_input:
        return "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like me to schedule an appointment with a doctor?"
    elif "medication" in user_input:
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    else:
        response = chatbot(user_input, max_length=300, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?", "")
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()
