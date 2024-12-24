from django.shortcuts import render

def contact(request):
    return render(request, 'contact/templates/contact/contact.html')
