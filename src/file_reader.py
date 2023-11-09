import os

def write_to_new_file(input_file, output_file_base):
    # Check if the base output file exists and create a new name with increment if it does
    directory = os.path.dirname(output_file_base)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    output_file = output_file_base
    file_increment = 2  # Start incrementing from 2 since the base is considered the first
    while os.path.exists(output_file):
        output_file = f"{output_file_base.rsplit('.', 1)[0]}-{file_increment}.{output_file_base.rsplit('.', 1)[1]}"
        file_increment += 1
    
    # Read from the input file
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Write to the new output file
    with open(output_file, 'w') as file:
        file.write(content)
    
    return output_file
