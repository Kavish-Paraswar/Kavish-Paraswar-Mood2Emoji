# Mood2Emoji
Built a Kid-safe Text-Mood Detector using Streamlit + TextBlob (rule based) .Created a simple web app that takes a short sentence and returns a kid-friendly emoji (😀 😐 😞) giving a one-line explanation. 
Suitable for students aged 12–16.


Project summary

Mood2Emoji is a compact, educational web application that converts a short, age-appropriate sentence into one of three mood outcomes — happy, neutral, or sad — accompanied by a brief explanatory phrase. The application is intentionally lightweight: it uses a local safety filter and straightforward sentiment analysis (TextBlob) with a minimal negation heuristic. It is designed for classroom demonstration and small hands-on exercises for learners aged 12–16.

Key features

Single input box for a short sentence.

Local safety filter that neutralizes inappropriate content.

Lightweight sentiment extraction using TextBlob polarity.

Simple negation handling to improve basic accuracy on phrases such as “not happy.”

Deterministic mapping of polarity scores to the three mood outputs.

Optional Teacher Mode that presents token-level evidence and a concise process diagram for instruction.

Why this is suitable for learners (12–16)

The application demonstrates an end-to-end text processing pipeline in a transparent and reproducible way. Students can:

Observe how raw text is tokenized and filtered for safety.

See how a sentiment score is computed and interpreted.

Experiment with inputs and develop hypotheses about why the system returns a given mood.

Discuss ethical considerations such as content safety and the limits of automated interpretation.

Setup and run instructions (precise)

Clone the repository and change directory:

git clone https://github.com/<USERNAME>/firstname-lastname-mood2emoji.git
cd firstname-lastname-mood2emoji


Create and activate a Python 3.9+ virtual environment:

python3 -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1


Install dependencies:

pip install -r requirements.txt


(Optional) If TextBlob requests additional corpora, run this once:

python -m textblob.download_corpora


Launch the application:

streamlit run app.py

Open the URL printed by Streamlit (commonly http://localhost:8501).
