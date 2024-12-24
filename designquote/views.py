from django.shortcuts import render, redirect
from .forms import DesignQuoteRequestForm
from django.contrib import messages

def design_quote_request(request):
    if request.method == 'POST':
        form = DesignQuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your request has been submitted.")
            return redirect('quote_thank_you')
    else:
        form = DesignQuoteRequestForm()
    return render(request, 'designquote/design_quote_request.html', {'form': form})

def quote_thank_you(request):
    return render(request, 'quote_thank_you.html')
