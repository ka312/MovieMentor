from chatbot import handle_interaction

def main():
    print("Chatbot ready! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        movie_recommendations, bot_response = handle_interaction(user_input)
        
        if movie_recommendations:
            print("Movies found:")
            for movie in movie_recommendations:
                print(f"- {movie}")
        
        print(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()
