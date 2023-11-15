import os
import pandas as pd

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

def read_excel_to_df(file_path):
    """
    Reads an Excel file into a pandas DataFrame.
    
    Parameters:
    - file_path: str, the path to the Excel file.
    
    Returns:
    - df: DataFrame, the data read from the Excel file.
    """
    df = pd.read_excel(file_path)
    return df

def write_df_to_excel(df, file_path):
    """
    Writes a pandas DataFrame to an Excel file, overwriting any existing file content.
    
    Parameters:
    - df: DataFrame, the DataFrame to write to the Excel file.
    - file_path: str, the path to the Excel file.
    """
    with pd.ExcelWriter(file_path, mode='w', engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
