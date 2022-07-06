from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote
from django.template.loader import render_to_string

def author(request):
    quotes = Quote.objects.all()
    context = {
        'quotes_list':quotes
    }
    return render(request, "author_view.html", context)