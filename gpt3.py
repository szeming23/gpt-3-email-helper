import openai
from archive.save import save_to_json
openai.api_key = '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'

def model(task:str, body:str, save=True):
    '''
    Inputs:
        task: "Improve English in the following email: \n"
        body: the email
        save: if true, will save the prompt and model response to json file
    Output:
        gpt3 response
    '''
    prompt = task + body #input("Prompt >>> ")
    # Run the model
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt = prompt,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0,
    echo=False
    )
    clean_response = response.choices[0].text
    # print(clean_response)
    if save:
        save_to_json(prompt, clean_response)
    return clean_response

# if __name__ == '__main__':
#     # task: help to improve email
#     instruction = "Improve English in following email: \n"
#     # get user email
#     email = get_user_input()
#     print("-"*80)
#     print("Improved email below:")
#     print("-"*80)
#     model(task=instruction, body=email)
#     print("-"*80)
