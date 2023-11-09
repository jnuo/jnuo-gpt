import os

def read_file(input_file):
    """Reads content from a file and returns it."""
    with open(input_file, 'r') as file:
        content = file.read()
    return content

def write_to_file(output_file_base, content):
    """Writes content to a new file with incrementing filename if needed."""
    directory = os.path.dirname(output_file_base)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    output_file = output_file_base
    file_increment = 2  # Start incrementing from 2 since the base is considered the first
    while os.path.exists(output_file):
        output_file = f"{output_file_base.rsplit('.', 1)[0]}-{file_increment}.{output_file_base.rsplit('.', 1)[1]}"
        file_increment += 1

    with open(output_file, 'w') as file:
        file.write(content)
    
    return output_file

# Example usage:
if __name__ == "__main__":
    input_filename = 'path_to_your_input_file.txt'  # Replace with your actual input file path
    output_filename_base = 'path_to_your_output_file.txt'  # Replace with your desired output file base path
    
    # Read content from the input file
    file_content = read_file(input_filename)

    # Write content to a new output file
    new_output_file = write_to_file(output_filename_base, file_content)
    print(f"Content written to {new_output_file}")
