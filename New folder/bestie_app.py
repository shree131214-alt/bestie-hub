import streamlit as st
import random

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="The Bestie Hub",
    page_icon="✨",
    layout="centered"
)

# --- 2. Custom Styling (Only the displayed message box is black) ---
st.markdown("""
    <style>
    .quote-card {
        background-color: #f1f5f9;
        border-left: 5px solid #6366f1;
        padding: 16px 20px;
        border-radius: 8px;
        color: #000000 !important;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-top: 15px;
    }
    .quote-card strong {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. Initialize Session State ---
if "active_quote" not in st.session_state:
    st.session_state["active_quote"] = ""

# --- 4. Content Lists ---
MEMORIES = [
    "That one time we laughed so hard in class that we had to cover our faces.",
    "Our legendary 2 AM late-night talk where we solved literally all world problems.",
    "That chaotic trip/outing where nothing went to plan, but it was still 10/10.",
    "When you said something completely out of pocket with a straight face."
]

HYPE_UP = [
    "Reminder: You're doing incredible, even on days you feel like doing nothing.",
    "Whatever exam, deadline, or challenge is in front of you—you've got this.",
    "Your brain is sharp and you're far more capable than you give yourself credit for.",
    "Take a breath, fix your posture, and drink some water right now. 💧"
]

INSIDE_JOKES = [
    "Error 404: Brain cells not found whenever we're in the same room.",
    "Certified partner-in-crime since day one.",
    "Plot twist: We actually know what we're doing (just don't ask for proof)."
]

# --- 5. App Header ---
st.title("✨ The Bestie HQ")
st.write("A customized dashboard made exclusively for my favorite human.")
st.divider()

# --- 6. Tabs ---
tab_daily, tab_emergency, tab_trivia, tab_letter = st.tabs([
    "🎲 Daily Drop", 
    "🚨 Rough Day Rescue", 
    "🧠 Friendship Trivia",
    "💌 Secret Letter"
])

# --- Tab 1: Daily Drop ---
with tab_daily:
    st.subheader("Pick your mood:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Hype Me Up 🚀", key="btn_hype", use_container_width=True):
            st.session_state["active_quote"] = random.choice(HYPE_UP)
            
    with col2:
        if st.button("Random Memory 📸", key="btn_mem", use_container_width=True):
            st.session_state["active_quote"] = random.choice(MEMORIES)
            
    with col3:
        if st.button("Inside Joke 🤫", key="btn_joke", use_container_width=True):
            st.session_state["active_quote"] = random.choice(INSIDE_JOKES)

    # Bulletproof multiline f-string with triple quotes
    if st.session_state["active_quote"]:
        card_html = f"""<div class="quote-card">💡 <strong>Message:</strong> {st.session_state['active_quote']}</div>"""
        st.markdown(card_html, unsafe_allow_html=True)

# --- Tab 2: Rough Day Rescue Button ---
with tab_emergency:
    st.subheader("Having a rough day? Press the button.")
    if st.button("Press for Emergency Support ❤️", key="btn_emergency", use_container_width=True):
        st.balloons()
        st.success("🚨 Support Protocol Activated:")
        st.markdown("""
        1. **Stop overthinking** whatever just happened.
        2. Put on your comfort tracks or grab a warm drink.
        3. Remember you've survived 100% of your bad days so far.
        4. My inbox/call is open whenever you want to vent or just rant.
        """)
        st.markdown("[🎧 Open Comfort Playlist on Spotify](https://open.spotify.com)")

# --- Tab 3: Friendship Trivia Quiz ---
with tab_trivia:
    st.subheader("How well do you remember our lore?")
    
    q1 = st.radio(
        "Who usually comes up with the terrible ideas?",
        ["Select an answer...", "You, 100%", "Me, obviously", "A joint collaborative disaster"],
        index=0,
        key="radio_q1"
    )
    if q1 != "Select an answer...":
        st.success("Correct answer either way — we both enable each other.")
        
    q2 = st.text_input("Enter the secret code word (hint: try 'chaos'):", key="input_q2")
    if q2:
        if q2.strip().lower() == "chaos":
            st.success("Access Granted! You actually remembered! 🎉")
        else:
            st.error("Nope! Try again or ask for a hint.")

# --- Tab 4: Secret Letter / Message ---
with tab_letter:
    st.subheader("A Quick Note 💌")
    
    show_letter = st.checkbox("Unlock the letter", key="chk_letter")
    if show_letter:
        st.markdown("""
        > **Hey bestie,**
        > 
        > Just wanted to make a quick digital keepsake to say thanks for always being 
        > one of the most reliable and hilarious people in my life. Through every chaotic 
        > phase and random late-night rant, having you around makes everything way more fun.
        > 
        > Keep being you. 👊
        """)

# --- Footer ---
st.divider()
st.caption("Crafted with love by shree 🌹❤️ • Made specifically for you.")