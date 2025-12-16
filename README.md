# Medical Chatbot (Streamlit)

A simple medical question-answer chatbot built using Python, Streamlit, and a medical Q&A dataset.  
The chatbot searches relevant medical questions from a dataset and returns the best matching answer.

## Features
- Streamlit-based web interface
- Medical question-answer retrieval from CSV dataset
- Simple and lightweight implementation
- Easy to run locally using VS Code

## Project Structure
medical-chatbot/
├─ chat_model/
│ ├─ init.py
│ └─ rules.py
├─ data/
│ └─ data.csv
├─ app.py
├─ requirements.txt
└─ README.md

## Installation

### 1. Clone the repository
git clone https://github.com/raniamula/end-to-end-medical-chatbot

cd medical-chatbot

### 2. Create virtual environment
python -m venv venv


### 3. Activate virtual environment
**Windows**
venv\Scripts\Activate.ps1



### 4. Install dependencies
pip install -r requirements.txt


## Run the Application
streamlit run app.py



The app will open in your browser at:
http://localhost:8501


## Dataset
The dataset should be placed inside the `data/` folder as `data.csv`.

Required columns:
- `question`
- `answer`

## Disclaimer
This project is for educational purposes only and does not provide medical advice.
 Replace USERNAME with your actual GitHub username.

FINAL CHECK (IMPORTANT)
Before pushing:

venv/ is ignored

README.md exists

App runs with streamlit run app.py

