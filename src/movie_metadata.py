import pandas as pd
from chat_gpt import ask_chat_gpt

def find_movie_metadata():
    print('hello movies')
    df = pd.DataFrame(columns=['spi_code', 'region', 'title', 'year', 'director', 'local_title', 'synopsis'])
    df.loc[0] = ['SPI107696', 'TURKISH', 'KNIVES OUT', 2019, 'Rian Johnson', None, None]
    df.loc[1] = ['SPI106981', 'TURKISH', 'PEOPLE YOU MAY KNOW', 2017, 'Sherwin Shilati', None, None]

    print(df)

    for index, row in df.iterrows():
        print(f"""
            Row {index}: \t  
            SPI Code: {row['spi_code']} \t   
            Region: {row['region']} \t   
            Title: {row['title']}   
            Director: {row['director']}
            Year: {row['year']}
        """)

        prompt = f"""
            I will provide some information to you about a movie and ask for some info about the movie.
            This is a movie with the name {row['title']}. This movie's production year is {row['year']} and the director's name is {row['director']}.
            I want you to find this movie. And I want to give me a freshly produced synopsis, in the language {row['region']}. This synopsis should explain the movie's story and can also include some info about it or about the director or actors. It include some funny facts about the movie or trophies it won, or some remarks on why the movie is important for one of the actors. Stuff like that. However, if the side info is not that important, it's better to just give the synopsis and nothing else. You should not mention the name of the movie inside the synopsis, that is not necessary. You also don't need to mention the local name of the movie inside the synopsis, we are already mentioning that in another format.
            Likewise, I want you to give me the local name of the movie. You can insert a | character between the synopsis and the local title so that I will understand which is which. Please write None if you cannot generate the synopsis or if you cannot provide the local name. So, if you can't find either, I expect the value 'None | None' from you.
            """
        response = ask_chat_gpt(prompt)
        parts = response.split('|')
        synopsis = parts[0].strip()
        local_name = parts[1].strip()

        row['local_title'] = local_name
        row['synopsis'] = synopsis

        print(response)
    print(df)
