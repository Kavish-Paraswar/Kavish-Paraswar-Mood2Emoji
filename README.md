## Mood2Emoji

## What the project does
Mood2Emoji is a simple tool that maps a user's mood to fun emojis.  
- Kids interact with it to see how feelings can be expressed visually.  
- Promotes emotional awareness and digital expression.
  
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

## How kids learn from it
- Kids learn about emotions and how they can be represented using emojis.
- They get hands-on experience with interactive web tools.
- Encourages creativity and helps children relate emotions to visual cues.
- Opens discussion about feelings in a simple, friendly way.

## How to teach it in 60 minutes
1. **Introduction (10 min):**  
   Briefly explain emotions and emojis.
   - Ask kids about their favorite emojis.
2. **Demo (10 min):**  
   Show Mood2Emoji, let kids try mapping moods to emojis.
   - Demonstrate how the tool works with a few examples.
3. **Explore (20 min):**  
   Kids experiment, share what emojis they chose for different moods.
   - Encourage group sharing and discussion.
4. **Discuss (10 min):**  
   Talk about why certain emojis fit certain moods.
   - Explore how different people might pick different emojis for the same mood.
5. **Wrap-up (10 min):**  
   Recap concepts, encourage kids to think about expressing emotions.
   - Suggest ways to use emojis in daily digital conversations.

## Known limitations
- Only basic moods/emojis supported; users can't add custom moods or emojis, and the choices are limited to a small preset list.
- No advanced features or data storage.
- Limited to browser usage.
- Not designed for large datasets or complex folders, keeping it minimal and clean.

Thank you for visiting.
