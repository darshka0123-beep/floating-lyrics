import streamlit as st
import time
# Custon CSS for aesthetic pink card & font
st.markdown("""
    <style>
    @ import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

    .stApp{
    background-color: #FFD1DC;
    color: #FFFFFF;
    font-family:'Great Vibes', cursive;
    font-size: 38px;
    text-align: center;
    padding: 40px 20px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    margin: 30px auto;
    max-width:500px;
    min-height: 180px;
    display: flex;
    align-items: center;
    justify-content; center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("wave to earth - bad 🌸")

# Audio Player 
audio_file = open("bad.mp3", "rb")
st.audio(audio_file.read(), format="audio/mp3")

# Lyrics List
LYRICS = [
    (0, "how could my day be bad when i'm with you?"),
    (6, "you're the only one who makes me laugh!"),
    (13, "so how can my day be bad?"),
    (19, "it's a day for youuuu"),
    (30, "lately, life's so boring"),
    (34, "i've been watching netflix all day long :("),
    (40, "i thought there would be"),
    (45, "no things left to watch"),
    (48, "so i let myself out."),
    (57, "when i went out to the park"),
    (62, "i recognized you at a glance"),
    (70, "face to face, we just smiled"),
    (75, "we already know that we'll be together"),
    (82, "(we'll be togetherrr)"),
    (86, "how could my day be bad when i'm with you?"),
    (91, "you're the only one who makes me laugh!"),
    (98, "so how can my day be bad?"),
    (104, "it's a day for you"),
    (109, "oh, babe"),
    (116, "coffee in the morning"),
    (119, "you and the sun!"),
    (123, "there's a brown hue in your eyes"),
    (130, "how pretty it is?"),
    (132, "i think im in loveee"),
    (170, "when i went to the park"),
    (175, "i recognized you at a glance"),
    (182, "face to face"),
    (185, "we smiled and i finally..."),
    (191, "held your handss"),
    (195, "how could my day be bad when i'm with you?"),
    (201, "you're the only one who makes me laugh!"),
    (208, "so how can my day be bad?"),
    (214.5, "it's a day for you"),
    (219, "oh babe"),
    (224, "how can my day be bad when i'm with you?"),
    (229.5, "you're the only one who makes me laugh!"),
    (236, "so how can my day be bad when i'm with you?"),
    (243, "it's a day for you"),
    (248, "oh, babe"), 
]

# Sync Engine
card_placeholder = st.empty()
start_button = st.button("Start Lyrics Sync")

if start_button:
    start_time = time.time()
    for timestamp, text in LYRICS:
        # Wait until the track reaches the timestamp 
        while time.time() - start_time < timestamp:
            time.sleep(0.1)

        card_placeholder.markdown(
            f'<div class="lyric-card">{text}</div',
            unsafe_allow_html=True
        )
