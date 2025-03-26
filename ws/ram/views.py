from django.shortcuts import render, redirect
from .models import web  # Use the actual model name here

# Create your views here.
def web(request):
    if request.method == "POST":
        data = request.POST
        web_name = data.get('web_name')
        web_description = data.get('web_description')
        
        # Create a new entry in the database
        web.objects.(name=web_name, description=web_description)
        
        # Redirect after creating the entry
        return redirect('/web/')  # Adjust the URL if necessary
    
    queryset = web.objects.all()
    context = {
        'web': queryset
    }
    
    # Render the form if it's a GET request
    return render(request, 'web.html', context)


