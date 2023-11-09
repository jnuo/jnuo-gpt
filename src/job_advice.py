from chat_gpt import ask_chat_gpt
import file_reader as fr

def get_cv_advice():
    f_job_description = 'data/job-post.txt'
    f_my_experience = 'data/your-job-xp.txt'
    output_filename_base = 'data/output.txt'  # Replace with your desired output file path
    
    # Read content from the input file
    job_description = fr.read_file(f_job_description)
    job_experience = fr.read_file(f_my_experience)
    
    prompt = f"""
    Please check the job description 
    {job_description}
    
    Please also check my current cv in the text format
    {job_experience}

    Taking into considerations of both, please provide me a new cv format, that is suitable for the job description I'm currently applying to.
    You can remove some information from my cv, add more lines to it, change anything you like. 
    Please highlight important achievements in my career to make a great match for the company and the job post and make sure I'll get in the interview phase!

    And finally, please add a summary at the end. Explain what you did, what you removed or added with the reasoning behind.
    """
    response = ask_chat_gpt(prompt)
    
    # Write content to a new output file
    new_output_file = fr.write_to_file(output_filename_base, response)
    print(f"Content written to {new_output_file}")
