import streamlit as st
import pandas as pd
import random
from model import SmartTutorModel

# Load dataset
df = pd.read_csv("vocab_dataset.csv")

# Train ML model
tutor_model = SmartTutorModel()
tutor_model.train("learner_history.csv")

# Initialize session state
defaults = {
    "score": 0,
    "attempts": 0,
    "asked_words": [],
    "current_question": None,
    "shuffled_options": [],
    "show_feedback": False
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# Function to pick next word adaptively
def get_next_word():
    # Choose difficulty based on ML prediction
    prob_easy = tutor_model.predict_success("easy")
    prob_medium = tutor_model.predict_success("medium")
    prob_hard = tutor_model.predict_success("hard")

    if prob_easy < 0.5:
        difficulty = "easy"
    elif prob_medium < 0.7:
        difficulty = "medium"
    else:
        difficulty = "hard"

    available = df[(df["difficulty"] == difficulty) & (~df["word"].isin(st.session_state.asked_words))]

    if available.empty:
        available = df[~df["word"].isin(st.session_state.asked_words)]  # fallback

    if available.empty:
        return None
    return available.sample(1).iloc[0]

# UI
st.title("SmartVocabTutor 🧠")
st.write("An AI-powered personalized vocabulary tutor")

# Load first question if none
if st.session_state.current_question is None:
    q = get_next_word()
    if q is not None:
        st.session_state.current_question = q
        st.session_state.shuffled_options = [
            q["correct_meaning"], q["option1"], q["option2"], q["option3"]
        ]
        random.shuffle(st.session_state.shuffled_options)

# Show current question
if st.session_state.current_question is not None:
    q = st.session_state.current_question
    st.write(f"**Word:** {q['word']} ({q['part_of_speech']})")

    st.session_state.user_choice = st.radio(
        "Select the correct meaning:",
        st.session_state.shuffled_options,
        index=None
    )

    if st.button("Submit Answer"):
        if st.session_state.user_choice:
            st.session_state.attempts += 1
            st.session_state.asked_words.append(q["word"])
            st.session_state.show_feedback = True

            if st.session_state.user_choice == q["correct_meaning"]:
                st.session_state.score += 1
                st.success(f"✅ Correct! Meaning: {q['correct_meaning']}")
            else:
                st.error(f"❌ Incorrect! Correct meaning: {q['correct_meaning']}")
        else:
            st.warning("Please select an option before submitting.")

# Next Question or Finish
if st.session_state.show_feedback:
    if st.button("Next Question"):
        new_q = get_next_word()
        if new_q is not None:
            st.session_state.current_question = new_q
            st.session_state.shuffled_options = [
                new_q["correct_meaning"], new_q["option1"], new_q["option2"], new_q["option3"]
            ]
            random.shuffle(st.session_state.shuffled_options)
            st.session_state.show_feedback = False
            st.rerun()
        else:
            st.info("🎉 No more words left!")
            st.write(f"**Final Score:** {st.session_state.score}/{st.session_state.attempts}")
            if st.button("Restart Quiz"):
                for key in defaults.keys():
                    st.session_state[key] = defaults[key]
                st.rerun()

