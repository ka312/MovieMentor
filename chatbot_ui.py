import streamlit as st
from chatbot import get_llm_response
from database import search_movies

# Function to display the chat UI and process user inputs
def main():
    st.title("MovieMentor")

    # Text input for the user query
    user_input = st.text_input("You: ", "")

    if user_input:
        # Get movie recommendations based on user input
        movies = search_movies(user_input)

        # Display movie recommendations if available
        if movies:
            st.subheader("Movies found:")
            for movie in movies:
                st.write(f"- {movie['title']} ({movie.get('year', 'Unknown')})")

        # Get response from LLM chatbot
        response = get_llm_response(user_input)
        st.subheader("Bot:")
        st.write(response)

    # Option to exit the chat
    if st.button("Exit"):
        st.write("Chatbot session ended.")

if __name__ == "__main__":
    main()
