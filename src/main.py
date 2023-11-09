# This is the entry point of the application
from file_reader import write_to_new_file
from chat_gpt import ask_chat_gpt

def main():
    # Example usage of the write_to_new_file function
    # input_filename = 'data/input.txt'  # Replace with the path to your input file
    # output_filename_base = 'data/output.txt'  # Replace with your desired output file path
    # write_to_new_file(input_filename, output_filename_base)
        
    # print('hola mundo!')

    prompt = "Translate the following English text to Spanish: 'Hello, how are you?'"
    response = ask_chat_gpt(prompt)
    print(response)

if __name__ == "__main__":
    main()
