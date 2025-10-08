## Mood2Emoji

It is a compact, classroom-oriented web application that converts a short, age-appropriate sentence into one of three kid-friendly emojis (😀 / 😐 / 😞) accompanied by a single-line explanation.

The implementation is deliberately lightweight (Streamlit + TextBlob or a small rule-based approach) and prioritizes transparency and safety also is intended for learners aged 12–16.

<img width="1918" height="915" alt="image" src="https://github.com/user-attachments/assets/83325efb-c1cd-4001-aefa-23af51aff2c4" />

---

## Features

- **Text ➔ Emoji in one click:**  
  Enter a sentence and instantly get a kid-friendly emoji (😀 / 😐 / 😞) plus a simple explanation.
- **Safety-first:**  
  Local filter blocks explicit/inappropriate words (neutral fallback if triggered).
- **Simple sentiment analysis:**  
  Uses [TextBlob](https://textblob.readthedocs.io/en/dev/) to detect mood, with a rule for handling negation.
- **Teacher Mode:**  
  Shows evidence and process for transparency and teaching.

<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/3eabc390-e996-4d1b-9e89-dd092b55f9bd" />


## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Kavish-Paraswar/Kavish-Paraswar-Mood2Emoji.git
    cd Kavish-Paraswar-Mood2Emoji
    ```

2. **Create and activate a Python 3.9+ virtual environment:**
    ```sh
    python3 -m venv venv
    # macOS / Linux
    source venv/bin/activate
    # Windows (PowerShell)
    venv\Scripts\Activate.ps1
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **(Optional) Download TextBlob corpora if prompted:**
    ```sh
    python -m textblob.download_corpora
    ```

5. **Run the app:**
    ```sh
    streamlit run app.py
    ```
    Open the address provided by Streamlit (http://localhost:8501).
   
---

Thank you for visiting.
