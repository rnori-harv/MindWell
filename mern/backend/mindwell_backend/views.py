from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_entry(request):
    if request.method == 'POST':
        # Your logic to create a new entry goes here
        # You can access the data sent from the frontend using request.POST or request.body

        # Return a JsonResponse with a success message
        return JsonResponse({'message': 'Entry created successfully'})

    # If the request method is not POST, return an error message
    return JsonResponse({'error': 'Invalid request method'}, status=400)