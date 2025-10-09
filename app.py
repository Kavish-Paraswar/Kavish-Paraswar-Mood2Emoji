
import streamlit as st
from textblob import TextBlob
import re




BAD_WORDS = {
    "hate", "idiot", "stupid", "kill", "damn", "shit", "bitch", "crap",
    "trash", "suck", "fool", "fuck", "asshole", "dumb", "moron"
}

NEUTRAL_THRESHOLD = 0.3
NEGATION_TOKENS = {"not", "never", "no", "n't", "cannot", "cant", "don't", "dont"}


DIAGRAM = """
digraph Mood2Emoji {
  rankdir=LR;
  node [shape=box, style=rounded, fontname="Arial", fontsize=11];
  Input [label="1. Input\\n(user sentence)", shape=oval];
  Tokenize [label="2. Tokenize\\n(split into words)"];
  Safety [label="3. Safety filter\\n  (check BAD_WORDS)", shape=diamond];
  Sentiment [label="4. Sentiment\\n  (TextBlob polarity)"];
  Negation [label="5. Negation check\\n( flip polarity if needed)", shape=diamond];
  Mapping [label="6. Mapping\\n(|polarity| < threshold ->   neutral\\nelse happy  /  sad)"];
  Output [label="7. Output\\n(emoji + line)", shape=oval];
  Fallback [label="Fallback: Neutral\\n(inappropriate )", shape=oval, fillcolor="#f2f2f2"];

  Input -> Tokenize;
  Tokenize -> Safety;
  Safety -> Fallback [label="bad word found", color="#d9534f"];
  Safety -> Sentiment [label="no bad words", color="#5cb85c"];
  Sentiment -> Negation;
  Negation -> Mapping;
  Mapping -> Output;
  Mapping -> Fallback [label="|polarity| < threshold", color="#f0ad4e"];
}
"""
def clean_text(text:  str) -> str:
    return text.strip()

def tokenize(text:   str):
    return re.findall(r"\w+", text.lower())

def contains_bad_word(text: str) -> bool:
    toks = tokenize(text)
    return any(w in BAD_WORDS for w in toks)

def has_negation(text: str) -> bool:
    toks = tokenize(text)
    return any(n  in toks for n in NEGATION_TOKENS)

def sentiment_to_mood(  polarity: float):
    """
    Map polarity to trio with neutral threshold.
    polarity: float in [-1,1]
    """
    if abs(polarity) < NEUTRAL_THRESHOLD:
        return "neutral", "Sounds neutral."
    if polarity >= NEUTRAL_THRESHOLD:
        return "happy", "Sounds happy!"
    return "sad", "Sounds sad."

def emoji_for_mood(mood_key: str) ->    str:
    mapping = {"happy": "😀", "neutral": "😐", "sad": "😞"}
    return mapping.get(mood_key, "😐")

# -----  UI of project (streamlit) -----
st.set_page_config(page_title="Mood2Emoji (kid-safe)", layout="centered")
st.title("Mood2Emoji")
st.title("Text → emoji in just a click")
st.markdown("Type a sentence  and get a kid-friendly emoji + eplanation.")
user_input = st.text_input("Enter thee  sentence:", "")
teacher_mode = st.checkbox("Teacher Mode (For  evidence)")

if user_input:
    text = clean_text(user_input)

    if contains_bad_word(text):
        st.warning("Your message contains words that are not age-appropriate. Please rephrase the sentence for better results  ")
        st.markdown("**Output:** 😐 — Neutral ")
    else:
        # Get sentiment
        blob = TextBlob(text)
        polarity = round(blob.sentiment.polarity, 3)
        subjectivity = round(blob.sentiment.subjectivity, 3)

        if has_negation(text) and abs(polarity) > 0:
            polarity = round(-polarity, 3)

        mood_key, explanation = sentiment_to_mood(polarity)
        emoji = emoji_for_mood(mood_key)

        st.markdown("### Result")
        st.markdown(f"**{emoji}  {explanation}**")
        st.caption(f"(polarity={polarity}, subjectivity={subjectivity})")

        if teacher_mode:
            toks = tokenize(text)
            st.markdown("---")
            st.subheader("Teacher Mode — Evidence")
            # st.write("Tokens:", toks)
            st.write("Negation present:", has_negation(text))
            st.write("Bad words present:", contains_bad_word(text))
            st.write("Polarity:", polarity)
            st.write("Subjectivity:", subjectivity)
            st.markdown("""
            **How it works/ decides:**
            1. Tokenize the input.  
            2. Safety filter: if any bad word → neutral fallback.  
            3. Use TextBlob polarity (small negation   applied).  
            4. If |polarity| < 0.25 = neutral fallback,  else happy / sad.  
            5. Show emoji + one-line explanation.
            """)

            st.markdown("** Process diagram **")
            try:
                st.graphviz_chart(DIAGRAM)
            except Exception:

                st.info("Graphviz is not available in this runtime. Diagram:")
                st.markdown("""
                Input → Tokenize → Safety  ──yes──> Fallback (Neutral)
                                         └─   no─> Sentiment → Negation → Mapping → Output
                """)

else:
    st.info("Enter   a sentence:- ")
