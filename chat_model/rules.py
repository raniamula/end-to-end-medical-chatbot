import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"

def _load_data():
    try:
        # Load only first 5000 rows to avoid memory issues
        df = pd.read_csv(DATA_PATH, nrows=5000)
        return df
    except Exception as e:
        print(f"Warning: Could not load data from {DATA_PATH}: {e}")
        return pd.DataFrame(columns=["Description", "Doctor"])

_data = _load_data()

def get_prediction(question: str) -> str:
    if not question:
        return "Please provide a question."
    
    question_lower = question.lower().strip()
    question_words = set(question_lower.split())
    
    best_match = None
    best_score = 0
    
    for _, row in _data.iterrows():
        # Use Description column as the question
        row_q = str(row.get("Description", "")).lower().strip()
        # Use Doctor column as the answer
        row_a = str(row.get("Doctor", ""))
        
        if not row_q:
            continue
        
        row_words = set(row_q.split())
        matching_words = len(question_words & row_words)
        
        if matching_words > best_score:
            best_score = matching_words
            best_match = row_a
    
    if best_match and best_score >= 1:
        return best_match
    
    return "Sorry, I dont know the answer."
