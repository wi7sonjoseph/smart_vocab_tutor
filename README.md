# SmartVocabTutor  

An **AI-powered personalized vocabulary tutor** built with **Streamlit** and a simple **ML model** (Logistic Regression).  
The app adaptively selects questions based on your past performance and difficulty prediction.  

---

## Features
- Quiz-style vocabulary learning  
- Adaptive difficulty powered by ML  
- Score tracking & feedback  
- Restartable sessions  
- Extendable dataset  

---

## Project Structure
```
smart_vocab_tutor/
│── smart_vocab_tutor.py     # Main Streamlit app
│── model.py                 # ML model (Logistic Regression)
│── vocab_dataset.csv        # Vocabulary dataset
│── learner_history.csv      # Simulated learner history (training data)
│── requirements.txt         # Dependencies
README.md                    # Documentation
Proposal.pdf
```

---

## Installation  

1. **Clone the project / move into directory**  
   ```bash
   cd smart_vocab_tutor
   ```

2. **Create a virtual environment (recommended)**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

## Requirements  

`requirements.txt`  

```
streamlit
pandas
scikit-learn
```

---

## Running the App  

From inside the project folder:  
```bash
streamlit run smart_vocab_tutor.py
```

Your browser will open at: http://localhost:8501  

---

## Data Files  

### `vocab_dataset.csv`  
Stores words, meanings, and difficulty levels.  

```csv
word,part_of_speech,correct_meaning,option1,option2,option3,difficulty
diligent,adjective,showing care in doing one's work,careless and hasty,rare and valuable,related to animals,easy
hypothetical,adjective,based on or serving as a hypothesis,true beyond doubt,completely proven,related to government,medium
eloquent,adjective,fluent or persuasive in speaking,silent and reserved,awkward in movement,related to money,hard
```

---

### `learner_history.csv`  
Simulated learner history used to train the ML model.  

```csv
student_id,word,difficulty,correct,time_taken,attempts
1,diligent,easy,1,8,1
1,hypothetical,medium,0,15,2
1,eloquent,hard,0,20,3
2,diligent,easy,1,10,1
2,hypothetical,medium,1,12,1
```

---

## How It Works
1. **ML Model** → Logistic Regression predicts probability of success for easy/medium/hard words.  
2. **Adaptive Question Selection** → Tutor picks next word based on predicted performance.  
3. **Quiz Flow** → User answers → feedback shown → next question selected.  
4. **Session State** → Streamlit tracks score, attempts, and asked words.  

---

## Future Enhancements
- Save user attempts automatically into `learner_history.csv` for continuous learning  
- Add **spaced repetition** scheduling  
- Generate distractor options using word embeddings (Word2Vec / BERT)  
- Multi-user support with login  

---
