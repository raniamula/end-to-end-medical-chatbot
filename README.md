# end-to-end-medical-chatbot

A Retrieval-Augmented Generation (RAG) based medical chatbot built using the MedQuAD dataset from Kaggle, FAISS for retrieval, and a transformer model for medical question answering.

## Features
- Uses MedQuAD medical question–answer dataset.
- Embeddings generated using SentenceTransformers.
- FAISS index for fast similarity search.
- Response generation using FLAN-T5 model.
- Flask API with a single endpoint: `/api/ask`.

## Project Structure
medical-chat-bot/
├─ data/
│ └─ medquad.csv
├─ models/
├─ src/
│ ├─ build_index.py
│ ├─ retriever.py
│ ├─ generator.py
│ └─ app.py
├─ requirements.txt
└─ README.md


## Installation
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\Activate.ps1 # Windows
pip install --upgrade pip
pip install -r requirements.txt


## Download Dataset
pip install kaggle
kaggle datasets download pythonafroz/medquad-medical-question-answer-for-ai-research -p data --unzip

csharp

Place the file here:
data/medquad.csv

## Build FAISS Index
python src/build_index.py


## Run API Server
python src/app.py


## API Endpoint
POST /api/ask
Content-Type: application/json
Body: {"question": "your medical question here"}


## Example cURL Request
curl -X POST http://localhost:8000/api/ask
-H "Content-Type: application/json"
-d '{"question":"What are the symptoms of diabetes?"}'



## Example Response
{
"answer": "generated answer text",
"confidence": 0.82,
"sources": [
{"score": 0.82, "question": "...", "answer": "..."},
{"score": 0.74, "question": "...", "answer": "..."}
]
}

## Requirements
flask
pandas
tqdm
sentence-transformers
faiss-cpu
transformers
torch
accelerate
python-dotenv

csharp


## Disclaimer
This project is for research and educational use only.
