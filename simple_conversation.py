# OPENAI API Key = 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
# Google API Key = AIzaSyAKy8V-jlHwpeofwVc0yoBclmss22AZA9M
# Google CSE ID = a443276dd997842c2

import openai
import requests
import json

from datetime import datetime


# set up the API key for openai
openai.api_key = "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"

# set up the API key and custom search engine ID for the Google Search API
google_api_key = "AIzaSyAKy8V-jlHwpeofwVc0yoBclmss22AZA9M"
cse_id = "a443276dd997842c2"

# get the current date

timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
end_date = timestamp

# define the AI's name
AI_name = "MiQu"

# ask for the user's name
user_name = input(f"{AI_name}: What is your name?\n ")

# define the initial prompt for the model
prompt = (f"{AI_name}: Hello {user_name}, how can I help you today? You can ask me questions about anything and when you're done just type 'quit'.\n ")


while True:
    # get the user's input
    user_input = input(prompt)
    
    # check if the user wants to quit
    if user_input.lower() == "quit" or user_input.lower() == "no":
        break
    
    # make a GET request to the Google Search API
    context = user_input
    params = {
        "q": user_input, 
        "key": google_api_key, 
        "cx": cse_id,
        "timestamp" : timestamp,
        "dateRestrict": f"d{end_date}",
        "sort" : "date",
        "lr":"lang_en",
        "siteSearch": "",
        "siteSearchFilter":"i",
        "excludeTerms":"example"
    }
    r = requests.get("https://www.googleapis.com/customsearch/v1", params=params)

    # parse the JSON response
    data = json.loads(r.text)

    # check if the data object contains the 'items' key
    if 'items' not in data:
        prompt = f"{AI_name}: {user_input}\n{user_name}:"
        response = openai.Completion.create(engine="text-davinci-002", max_tokens=2048)
        print(response["choices"][0]["text"])
        prompt = f"{AI_name}: Is there anything else you would like to know {user_name}? "
        continue
    try:
        # Extracting useful parts of search results
        title = data["items"][0]["title"]
        link = data["items"][0]["link"]
        context = f"{title}\n{link}"
    except KeyError:
        print(f"{AI_name}: Sorry {user_name}, I couldn't find any results for your query.")
        prompt = f"{AI_name}: How can I help you {user_name}?"
        continue

    # create the prompt for the model
    prompt = f"{AI_name}: {user_input}\n{context}\n{user_name}: "
    
    # get the response from the model with additional context
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=2048)
    
    # print the response
    print(response["choices"][0]["text"] + "\n")

    # ask if there is anything else the user would like to know
    prompt = f"{AI_name}: Is there anything else you would like to know {user_name}? If not, simply type 'no' and have a great day {user_name}!\n "

