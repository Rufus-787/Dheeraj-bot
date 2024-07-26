import streamlit as st
import google.generativeai as genai

def generate_poem(theme, tone):
    try:
        genai.configure(api_key="AIzaSyAtpFSgqIOfBtXs3egxSOEVtcc2lFQRIEc")
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction="You are a poet. Create a poem that captures the essence of the given theme and tone.",
        )
        prompt = f"Write a poem about {theme} with a {tone} tone."
        response = model.generate_content(prompt)
        poem_text = response.text
        return poem_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

st.title("Poem Generator")

st.write("Enter the theme and tone of the poem you'd like to generate:")

theme = st.text_input("Theme")
tone = st.selectbox("Tone", ["Happy", "Sad", "Nostalgic", "Other"])

if st.button("Generate Poem"):
    poem = generate_poem(theme, tone)
    if poem:
        st.write("Generated Poem:")
        st.write(poem)
    else:
        st.write("Error generating poem. Please try again.")