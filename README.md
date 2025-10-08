# Mood2Emoji

**Kid-safe Text-Mood Detector**  
Convert any short sentence into a kid-friendly emoji with a quick explanation.

---

![image1](image1)

## Features

- **Text ➔ Emoji in one click:**  
  Enter a sentence and instantly get a kid-friendly emoji (😀 / 😐 / 😞) plus a simple explanation.
- **Safety-first:**  
  Local filter blocks explicit/inappropriate words (neutral fallback if triggered).
- **Simple sentiment analysis:**  
  Uses [TextBlob](https://textblob.readthedocs.io/en/dev/) to detect mood, with a rule for handling negation.
- **Teacher Mode:**  
  Shows evidence and process for transparency and teaching.

![image2](image2)

---

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
    Open the address provided by Streamlit (usually [http://localhost:8501](http://localhost:8501)).

---

## License

This project is licensed under the MIT License.

---

## Contact

Kavish Paraswar  
📧 [kavishp9721@gmail.com](mailto:kavishp9721@gmail.com)  
📱 +91 93226 45212
