import os
import requests

URL = 'https://api.openai.com/v1/chat/completions'

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
    #   {
    #     "role": "user",
    #     "content": f"Hello! I would like to learn more about {input()}"
    #   },
      {
        "role": "user",
        "content": f"Act as Socrates and convince me, using the Socratic Method, about the nature of {input()}.
        This has to be done using a question by question approach.
        Wait for me to answer you in order to give me a response guiding me towards your definition."
      }],
      "temperature" : 1.0,
      "n" : 1,
      "stream" : False,
      "presence_penalty" : 0,
      "frequency_penalty" : 0,
  }

headers = {
    "Content-Type" : "application/json",
    "Authorization" : f"Bearer {os.getenv('OPENAI_KEY')}"
}

response = requests.post(URL, headers=headers, json=payload, stream=False)
