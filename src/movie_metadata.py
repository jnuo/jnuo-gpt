import pandas as pd
from chat_gpt import ask_chat_gpt
import file_reader as fr

def find_movie_metadata():
    excel_input = 'data/AI Synopsis Trial (1).xlsx'
    df = fr.read_excel_to_df(excel_input)

    for index, row in df.iterrows():
        if(row['LOCAL TITLE'] != 'local_name' and row['SYNOPSIS'] != 'synopsis'):
            continue

        prompt = f"""
            I will provide some information to you about a movie and ask for some info about the movie.
            This is a movie with the name {row['TITLE']}. This movie's production year is {row['PRODUCTION YEAR']} and the director's name is {row['DIRECTOR']}.
            I want you to find this movie. And I want to give me a freshly produced synopsis, in the language {row['LANGUAGE']}. This synopsis should explain the movie's story and can also include some info about it or about the director or actors. It include some funny facts about the movie or trophies it won, or some remarks on why the movie is important for one of the actors. Stuff like that. However, if the side info is not that important, it's better to just give the synopsis and nothing else. You should not mention the name of the movie inside the synopsis, that is not necessary. You also don't need to mention the local name of the movie inside the synopsis, we are already mentioning that in another format.
            Likewise, I want you to give me the local name of the movie. You can insert a | character between the synopsis and the local title so that I will understand which is which. Please write None if you cannot generate the synopsis or if you cannot provide the local name. 
            
            So, if you cannot find an answer, it is OK. In this case, I expect the value 'None | None' from you. 
            
            YOU SHOULD NEVER RETURN A RESPONSE WITHOUT the '|' CHARACTER, PLEASE!
            """
        
        try:
            # Simulating a function call to an API that could fail
            response = ask_chat_gpt(prompt)
            # If there's no '|' in the response, it will raise a ValueError
            parts = response.split('|')
            if len(parts) < 2:
                # Not enough parts, defaulting to None
                raise ValueError('Response does not contain the "|" character.')
            
            local_name = parts[1].strip()
            synopsis = parts[0].strip()

        except Exception as e:
            # Catching any exception and defaulting to None
            print(f"An error occurred: {e}")
            local_name = 'None'
            synopsis = 'None'
        
        df.at[index, 'LOCAL TITLE'] = local_name
        df.at[index, 'SYNOPSIS'] = synopsis
        print(f"""
            Row {index}: \t  
            SPI Code: {row['SPI CODE']} \t   
            Region: {row['LANGUAGE']} \t   
            Title: {row['TITLE']}   
            Director: {row['DIRECTOR']}
            Year: {row['PRODUCTION YEAR']}
            Local name: {local_name}
            Synopsis: {synopsis}
        """)
        fr.write_df_to_excel(df, excel_input)
    print(df)
