from django.shortcuts import render , HttpResponse
import openai, os
import requests
from dotenv import load_dotenv
load_dotenv()

arr =[]
api_key= os.getenv("OPENAI_KEY", None)
# print(api_key)
# def chatbot(request):
#     chatbot_response = None
#     if api_key is not None and request.method =='POST' :
#         openai.api_key = api_key
#         user_input = request.POST.get('user_input')
#         print(user_input)
#         prompt = user_input
# #response = openai.Completion

#         response = openai.Completion.create(
#             engine = 'text-davinci-003',
#             prompt = prompt,
#             max_tokens=256 ,
#             temperature=0.5,
#             # stop='.',
#             )
#         print(response)
#     return render (request,'chat_bot.html',{})

def chatbot(request):
   
    user_message = request.POST.get('message')
    print(user_message)
    print('**************************')
 
    # Construct the data payload
    data = {
        "model": "gpt-3.5-turbo-0301",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    }
 
    # Set the API key and headers
    # api_key = "YOUR_API_KEY"
    print(api_key)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
 
    # Make the API request
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=data
    )
 
    # Parse the response
    response_json = response.json()
    print(response_json)
    # reply = response_json['choices'][0]['message']['content']
    reply = ""
    print ("******G*%$533")
    choices = response_json.get('choices')
    if choices and len(choices) > 0:
      message = choices[0].get('message')
      if message:
        reply = message.get('content')
        print(reply)
      else:
        print("No message found.")  
    else:
       print("No choices found.")
    arr.append(user_message) 
    arr.append(reply)
    context = {
       "arr" : arr
    }
    

 
    # Return the reply as the response to the user
    return render(request, 'chat_bot.html',context)