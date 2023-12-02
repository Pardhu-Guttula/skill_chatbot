from django.shortcuts import render
from .forms import UserInputForm
from chatbot import demo

def chatbot_view(request):
    form = UserInputForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        user_input = form.cleaned_data['user_input']
        
        # Getting model response
        model_response = demo.get_model_response(user_input)
        
        return render(request, 'main/chatbot_view.html', {'form': form, 'model_response': model_response})
    
    return render(request, 'main/chatbot_view.html', {'form': form, 'model_response': None})
