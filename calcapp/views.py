from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


 #Create your views here.

# def index_view(request):
#     form = AuthenticationForm()
#    return render(request,"index.html", {"form": form})

def user_create_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index_view'))
        else:
            return render(request, "user_create_view.html", {"form": form})
    form = UserCreationForm()
    return render(request, "user_create_view.html", {"form": form})

@login_required
def profile_view(request):
    print(request.user)
    return render(request, 'profiles.html')


def home_view(request):
    return render(request, 'home.html')


def app_view(request):
    if request.POST:
        left = request.POST['left']
        right = request.POST['right']
        mathop = request.POST['operators']
        if mathop == 'add':
            value = int(left) + int(right)
        if mathop == 'subtract':
            value = int(left) - int(right)
        if mathop == 'multiply':
            value = int(left) * int(right)
        if mathop == 'divide':
            value = int(left) / int(right)

        context = {
            'total': value
        }
        print(request.POST)
        return render(request,'app_view.html', context)

    print(request.POST)
    return render(request, 'app_view.html')



