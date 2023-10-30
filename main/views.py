from django.shortcuts import render, redirect
from main.models import Url
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import string
import secrets

# Create your views here.
def CreateView(request):    

    if request.method == "POST":
        long_url = request.POST.get("long_url")

        if Url.objects.filter(long_url = long_url).exists():
            short_code = Url.objects.get(long_url = long_url).short_code 

        else: 
            validator = URLValidator()
            try:
                validator(long_url)
            except ValidationError as exception:
                error = "Enter a valid url!!!"
                return render(request, "create.html", {"error" : error})
            
            alpha_numeric = string.ascii_letters + string.digits
            short_code = ''.join(secrets.choice(alpha_numeric) for _ in range(8))
            while Url.objects.filter(short_code = short_code).exists():
                short_code = ''.join(secrets.choice(alpha_numeric) for _ in range(8))
            new_url = Url(long_url = long_url, short_code = short_code)
            new_url.save()

        context = {
            "long_url" : long_url,
            "short_url" : "localhost:8000/short_url/" + short_code
        }

        return render(request, "create.html", context)


    return render(request, "create.html")

def RedirectView(request, url):
    if Url.objects.filter(short_code = url).exists() :
        url_instance = Url.objects.get(short_code = url)
        return redirect(url_instance.long_url)    
    return render(request, "error.html")

def AllUrlView(request):
    url_list = Url.objects.all()
    if url_list:
        for instance in url_list:
            instance.short_code = "localhost:8000/short_url/" + instance.short_code + "/"
        context = {
            "url_list" : url_list
        }
    else:
        context = {}
    return render(request, "list.html", context)
