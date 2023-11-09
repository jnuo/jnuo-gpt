import os
import tempfile
import pytest
from src.file_reader import read_file, write_to_file

def test_read_file():
    # Create a temporary file with some content
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"Hello, World!")
        tmp_filename = tmp.name

    # Read the content using read_file function
    content = read_file(tmp_filename)

    # Clean up the temporary file
    os.remove(tmp_filename)

    # Assert the content read is correct
    assert content == "Hello, World!", "The content read should match the content written."

def test_write_to_file():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmp_dir:
        base_filename = os.path.join(tmp_dir, "test_output.txt")
        content_to_write = "Hello, World!"

        # Write the content using write_to_file function
        output_file = write_to_file(base_filename, content_to_write)

        # Check the file exists
        assert os.path.exists(output_file), "The output file should exist."

        # Read the content back
        with open(output_file, 'r') as file:
            content = file.read()

        # Assert the content written is correct
        assert content == content_to_write, "The content written should match the content read back."

if __name__ == "__main__":
    pytest.main()
