from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ShortenedURL
import string
import random

def shorten_url(request):
    short_url = None

    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_id = generate_short_id()
        ShortenedURL.objects.create(long_url=long_url, short_id=short_id)
        short_url = request.build_absolute_uri('/') + short_id  # Build short URL

    return render(request, 'home.html', {'short_url': short_url})

def redirect_to_url(request, short_id):
    shortened_url = ShortenedURL.objects.get(short_id=short_id)
    return redirect(shortened_url.long_url)

def generate_short_id():
    characters = string.ascii_letters + string.digits
    short_id = ''.join(random.choice(characters) for _ in range(6))
    return short_id
