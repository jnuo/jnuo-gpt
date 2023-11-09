import os
from src.file_reader import write_to_new_file

def test_write_to_new_file():
    # Setup: Create a dummy input file
    input_content = 'Hello, World!'
    input_file = 'test_input.txt'
    with open(input_file, 'w') as f:
        f.write(input_content)

    # Define the base name for the output file
    output_file_base = 'test_output.txt'

    # Execute: Call the function to test
    output_file = write_to_new_file(input_file, output_file_base)

    # Verify: Check if the output file contains the expected content
    with open(output_file, 'r') as f:
        output_content = f.read()
    assert output_content == input_content, "Output content should match input content"

    # Cleanup: Remove the test input and output files
    os.remove(input_file)
    os.remove(output_file)

# You might want to add more tests to check for edge cases, errors, etc.
