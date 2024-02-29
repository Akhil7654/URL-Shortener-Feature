from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import URL
from .serializers import URLSerializer
import string
import random

def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code

from django.db import IntegrityError

@api_view(['POST'])
def shorten_url(request):
    if request.method == 'POST':
        original_url = request.data.get('original_url')
        try:
            url = URL.objects.get(original_url=original_url)
            serializer = URLSerializer(url)
            return Response(serializer.data)
        except URL.DoesNotExist:
            short_code = generate_short_code()
            while URL.objects.filter(short_code=short_code).exists():
                short_code = generate_short_code()
            url = URL(original_url=original_url, short_code=short_code)
            try:
                url.save()
                serializer = URLSerializer(url)
                return Response(serializer.data)
            except IntegrityError:
                return Response({"error": "Duplicate URL"}, status=status.HTTP_400_BAD_REQUEST)





def redirect_to_original_url(request, short_code):
    try:
        url = URL.objects.get(short_code=short_code)
        return redirect(url.original_url)
    except URL.DoesNotExist:
        return render(request, 'error.html', {'message': 'URL not found.'})


def index(request):
    shortened_url = None
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        if original_url:
            url = URL.objects.filter(original_url=original_url).first()
            if url:
                shortened_url = url.short_code
            else:
                shortened_url = generate_short_code()
                URL.objects.create(original_url=original_url, short_code=shortened_url)

    return render(request, 'mainpage.html', {'shortened_url': shortened_url})


