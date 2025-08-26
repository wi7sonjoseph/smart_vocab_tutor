import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


class SmartTutorModel:
    def __init__(self):
        self.model = LogisticRegression()
        self.label_enc = LabelEncoder()
        self.trained = False
        self.feature_names = ["difficulty_encoded", "time_taken", "attempts"]

    def train(self, history_file="learner_history.csv"):
        """Train the model on learner history CSV file"""
        df = pd.read_csv(history_file)

        # Encode difficulty as numeric
        df["difficulty_encoded"] = self.label_enc.fit_transform(df["difficulty"])

        X = df[self.feature_names]
        y = df["correct"]

        self.model.fit(X, y)
        self.trained = True

    def predict_success(self, difficulty, time_taken=10, attempts=1):
        """Predict probability of success for given learner context"""
        if not self.trained:
            raise Exception("Model not trained yet. Call train().")

        diff_encoded = self.label_enc.transform([difficulty])[0]

        # Use DataFrame to keep feature names consistent
        X = pd.DataFrame(
            [[diff_encoded, time_taken, attempts]],
            columns=self.feature_names
        )

        prob = self.model.predict_proba(X)[0][1]  # Probability of success
        return prob

