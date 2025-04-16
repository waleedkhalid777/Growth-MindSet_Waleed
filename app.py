import streamlit as st

# Page configuration
st.set_page_config(page_title="Growth Mindset Journey", page_icon="🌱")

# Title and welcome
st.title("🌟 Growth Mindset Challenge with Streamlit")
st.header("Welcome to Your Personal Growth Journey 🚀")
st.write("Embrace every challenge, and keep learning beyond limits.")

# Daily quote
st.header("🌞 Today's Growth Mindset Quote")
st.write("“Reflect on a past failure and the lesson it taught you.”")

# Challenge input
st.header("🚧 What's a Challenge You're Currently Facing?")
challenge = st.text_input("Describe a challenge you're dealing with:")

if challenge:
    st.success(f"You’re working through: **{challenge}**. Keep moving forward — you've got this!")
else:
    st.warning("Let's get started! Share a challenge you're currently facing.")

# Reflection section
st.header("🧠 Reflect on Your Learning")
reflection = st.text_area("Take a moment to reflect. What have you learned recently?")

if reflection:
    st.success(f"Powerful reflection! You shared: _{reflection}_")
else:
    st.info("Reflection leads to growth. Share something you've learned!")

# Achievements
st.header("🏆 Celebrate Your Wins!")
achievement = st.text_input("Share something you’ve accomplished recently:")

if achievement:
    st.success(f"👏 Amazing! You achieved: **{achievement}**")
else:
    st.info("Whether it's big or small, every achievement matters. Share yours!")

# Footer
st.write("---")
st.write("✨ Keep believing in yourself. Growth is a journey, not a destination.")
st.caption("Created with ❤️ by Waleed Khalid")
