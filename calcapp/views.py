from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.

def index_view(request):
    form = AuthenticationForm()
    return render(request,"index.html", {"form": form})

def user_create_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form. is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index_view"))

        else:
            return render(request, "user_create_view.html", {"form": form})




def home_view(request):
    return render(request, 'home.html')

def app_view(request):
    return render(request, 'app_view.html')

