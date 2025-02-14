# MovieMentor
Chatbot for Movie recommendation

# Movie Mentor Chatbot

Movie Mentor is an AI-driven chatbot designed to recommend movies based on user input. It integrates with MongoDB to store and fetch movie data, and uses OpenAI's GPT-based model to generate responses. The chatbot provides recommendations and interacts with users in a conversational manner, offering a personalized experience.
![MovieMentor](screenshot.png)

## Project Overview

This project is divided into several modules:
- **Movie Search**: Uses MongoDB to search for movie data based on the user's query.
- **Chatbot Interaction**: Powered by OpenAI's GPT-4 model (via the LangChain API), it generates responses and provides movie recommendations.
- **Interaction Logging**: Stores the user’s input, chatbot responses, and movie recommendations in a MongoDB database.
- **User Interface**: A simple interface to interact with the chatbot and get movie suggestions.

## Requirements

Before running the project, ensure you have the following dependencies installed:

- **Python 3.8+**
- **MongoDB Atlas** account (for hosting the movie database and logging interactions)
- **OpenAI API Key** (for accessing GPT models)

### Install Dependencies

You can install the required libraries by running the following:

```bash
pip install -r requirements.txt


## File Breakdown

### 1. `database.py`
This module handles the connection to MongoDB Atlas and interacts with the movies collection in the `sample_mflix` database.

**Functions:**
- **`get_mongo_client()`**: Establishes a connection to MongoDB using the URI stored in the `.env` file.
- **`get_movies_collection()`**: Returns the movie collection from MongoDB.
- **`search_movies(query)`**: Searches the movie collection for titles that match the user query.

### 2. `chatbot.py`
The `chatbot.py` file interacts with the LangChain-based GPT-4 model to generate responses and retrieve movie recommendations.

**Functions:**
- **`get_llm_response(user_input)`**: Takes user input, sends it to GPT-4 via LangChain, and returns the bot’s response.
- **`get_movie_recommendations(query)`**: Queries the database for movie recommendations based on the user’s input.

### 3. `main.py`
The main script that runs the chatbot. It continuously asks for user input and provides responses and movie recommendations.

**How it works:**
- The program waits for the user to input a query.
- It fetches movie recommendations based on the query.
- The chatbot generates a response and provides it to the user.
- Logs the interaction (both user input and bot response) into MongoDB.

### 4. `config.py`
This file contains configuration settings for connecting to MongoDB and OpenAI APIs. It loads the connection details from the `.env` file.

### 5. `chatbot_ui.py` (for Streamlit-based UI)
A simple UI using Streamlit to interact with the chatbot. It provides:
- A text input for the user’s query.
- Displays movie recommendations.
- Shows the chatbot’s response.

### 6. `.env`
A hidden file that contains environment variables such as:
- **`MONGO_URI`**: MongoDB URI.
- **`OPENAI_API_KEY`**: OpenAI API Key.

### 7. `requirements.txt`
This file lists all the necessary Python libraries to install via pip.
