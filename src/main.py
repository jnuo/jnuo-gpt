# This is the entry point of the application
from file_reader import write_to_new_file

def main():
    # Example usage of the write_to_new_file function
    input_filename = 'data/input.txt'  # Replace with the path to your input file
    output_filename_base = 'data/output.txt'  # Replace with your desired output file path
    write_to_new_file(input_filename, output_filename_base)
    # print('hola mundo!')

if __name__ == "__main__":
    main()
