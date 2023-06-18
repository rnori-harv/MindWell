from django.shortcuts import render
from dotenv import dotenv_values, load_dotenv, find_dotenv
import openai
import os
import json


# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def pass_entry_to_openai(text):
    prompt = "In the following journal entry, analyze my emotions and report the most prevalent ones in the text. \n\n" + text + "\n\nEmotions: "
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
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
        return JsonResponse({'message': openai_response})

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