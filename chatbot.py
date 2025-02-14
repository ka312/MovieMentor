from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os
from database import store_interaction,search_movies

def get_llm_response(user_input):
    llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=os.getenv("OPENAI_API_KEY"))
    response = llm([HumanMessage(content=user_input)])
    return response.content

def get_movie_recommendations(query):
    movies = search_movies(query)
    movie_titles = [movie['title'] for movie in movies]  # Extract movie titles
    return movie_titles

def handle_interaction(user_input):
    # Get movie recommendations
    movie_recommendations = get_movie_recommendations(user_input)
    
    # Get bot response
    bot_response = get_llm_response(user_input)
    
    # Log the interaction in the database
    store_interaction(user_input, bot_response, movie_recommendations)
    
    return movie_recommendations, bot_response
