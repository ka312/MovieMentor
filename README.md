# MovieMentor
Chatbot for Movie recommendation using LLM'S and MongoDB Atlas

# MovieMentor Chatbot

MovieMentor is an AI-driven chatbot designed to recommend movies based on user input. It integrates with MongoDB to store and fetch movie data, and uses OpenAI's GPT-based model to generate responses. The chatbot provides recommendations and interacts with users in a conversational manner, offering a personalized experience.
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

## Technologies Used

- **Python**: The main programming language for the chatbot.
- **MongoDB Atlas**: Cloud-based NoSQL database to store movie data and user interactions.
- **OpenAI GPT-4**: Used for generating chatbot responses.
- **Streamlit**: A Python library to build the user interface.
- **LangChain**: A library to integrate the GPT model with the chatbot.

### Install Dependencies

You can install the required libraries by running the following:

```bash
pip install -r requirements.txt
```

## How to Run the Project

### 1. Set Up MongoDB Atlas
- Create a MongoDB Atlas account if you don’t have one.
- Create a new project and set up a cluster.
- Add your connection string to the `.env` file in the `MONGO_URI` variable.
- Use the `sample_mflix` database, which contains movie data.

### 2. Set Up OpenAI API Key
- Create an OpenAI account if you don’t have one.
- Generate an API key from the OpenAI dashboard.
- Add the API key to the `.env` file in the `OPENAI_API_KEY` variable.

### 3. Install Dependencies
Run the following to install all required libraries:

```bash
pip install -r requirements.txt
```

### 4. Run the Chatbot
You can either run the chatbot in the terminal or use the Streamlit-based UI.

#### Terminal Version:
To run the chatbot directly in the terminal:

```bash
python main.py
```

#### Streamlit UI Version:
To run the Streamlit interface:

1. First, make sure you are in the project directory.
2. Run the following command:

```bash
streamlit run chatbot_ui.py
```

3. This will launch the UI in your web browser where you can interact with the chatbot.

![MovieMentor](Screenshot%202025-02-14%20001200.png)

## Contact

Connect to me on [LinkedIn]https://www.linkedin.com/in/karan-sai-goud-katam-ab93161b7/
Email: karan.katam16@gmail.com
