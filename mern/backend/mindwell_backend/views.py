from django.shortcuts import render
from dotenv import dotenv_values, load_dotenv, find_dotenv
import openai
import os
import json


# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def format_emotion_response(response_text):
    emotions = response_text.split('\n')
    formatted_response = "Emotions displayed in your entry:\n"

    for emotion in emotions:
        if emotion.strip():
            formatted_response += f"{emotion}\n"

    return formatted_response

def pass_entry_to_openai(text):
    prompt = (
        "In the following journal entry, analyze my emotions and report the most prevalent ones in the text. If you don't have enough information to make a decision, please say \"Not enough information, please write more!\". DO NOT hallucinate the journal entry, only use what is given to you. \n "
        "Your response must be formatted in the following manner: "
        "1. Emotion 1: \n"
        "    - Instance 1 \n"
        "    - Instance 2 \n"
        "    - Instance 3 \n"
        "2. Emotion 2(new line)"
        "    - Instance 1 \n"
        "    - Instance 2 \n"
        "    - Instance 3 \n"
        "Only do this for how ever many emotions you find in the text. \n"
        "Journal Entry (use only this for the source of your response): \n"
        f"{text}"
    )
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=250,
        temperature=0.0,
        n=1,
        stop=None
    )
    generated_text = response.choices[0].text.strip()
    return generated_text

@csrf_exempt
def create_entry(request):
    if request.method == 'POST':
        # Your logic to create a new entry goes here
        # You can access the data sent from the frontend using request.POST or request.body

        journal_data = request.body
        journal_decoded = json.loads(journal_data)

# Now you can access the value using the key
        entry = journal_decoded['key']
        print(entry)

        openai_response = pass_entry_to_openai(entry)
        formatted_response = format_emotion_response(openai_response)
        print(formatted_response)
        return JsonResponse({'message': formatted_response})
        

        # Return a JsonResponse with a success message

    # If the request method is not POST, return an error message
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def check_api_key(api_key):
    try:
        openai.api_key = api_key
        openai.Engine.list()
        return True
    except Exception as e:
        return False
    
@csrf_exempt
def submit_api_key(request):
    if request.method == 'POST':
        api_key_json = request.body.decode('utf-8')
        key_loaded = json.loads(api_key_json)
        api_key = key_loaded['apiKey']
        openai.api_key = api_key
        is_valid = check_api_key(api_key)
        if is_valid:
            openai.api_key = api_key
            return JsonResponse({'status': 'success', 'message': 'API key saved successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid API key'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid Request Method'})