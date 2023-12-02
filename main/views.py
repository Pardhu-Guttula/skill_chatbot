from django.shortcuts import render

from .models import Conversation
from .forms import UserInputForm
from open_ai import demo

def chatbot_view(request):
    form = UserInputForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        user_input = form.cleaned_data['user_input']
        
        # Getting model response
        model_response = demo.get_model_response(user_input)
        
        # Extracting the 'message' part from the model_response dictionary
        message = model_response.get('message') if model_response else ''
        
        # Creating a new Conversation object
        Conversation.objects.create(user_input=user_input, model_response=message)
        
        return render(request, 'main/chatbot_view.html', {'form': form, 'model_response': message})
    
    return render(request, 'main/chatbot_view.html', {'form': form, 'model_response': None})