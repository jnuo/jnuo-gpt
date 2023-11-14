# This is the entry point of the application
# from chat_gpt import ask_chat_gpt
# from job_advice import get_cv_advice
from movie_metadata import find_movie_metadata

def main():
    # prompt = "Translate the following English text to Spanish: 'Hello, how are you?'"
    # response = ask_chat_gpt(prompt)
    # print(response)

    # get_cv_advice()
    find_movie_metadata()

if __name__ == "__main__":
    main()
