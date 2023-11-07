from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User  # it is used import user model to save the user
from django.contrib.auth import authenticate, login as user_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import song
# Create your views here.


def index(request):
    allsongs=song.objects.all()
    if request.method=="GET":
        st=request.GET.get('abcd')
        if st!=None:
            allsongs=song.objects.filter(songName__icontains=st)
    

    return render(request,"index.html",context={"allsongs":allsongs})