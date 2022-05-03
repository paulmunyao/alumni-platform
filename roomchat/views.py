from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewChatForm, NewRoomForm
from django.urls import reverse
from .models import Room,Roomchat

# Create your views here.
# @login_required(login_url='/accounts/register/')
def home(request):
    return render(request,'home.html')

def new_room(request):
    current_user = request.user
    if request.method == "POST":
        form = NewRoomForm(request.POST,request.FILES)
        form.instance.admin = request.user
        print(form)
        if form.is_valid():
            form.save()

            return redirect('rooms')
    else:
        form = NewRoomForm()
    
    return render(request,'newroom.html',{"form":form})

def rooms(request):
    current_user = request.user
    rooms = Room.objects.all()
    return render(request,'room.html',{"rooms":rooms,'current_user':current_user})

def group(request,id):
    chats = Roomchat.objects.all()
    cohorts = Room.objects.get(id=id)
    chats = Roomchat.objects.filter(room=cohorts)

    return render(request,'roomchat.html',{"chats":chats,"cohorts":cohorts})

def new_chat(request,id):
    current_user = request.user
    if request.method == 'POST':
        chat_form = NewChatForm(request.POST,request.FILES)
        if chat_form.is_valid():
            chat_form.instance.user = request.user
            chat_form.author = Room.objects.filter(id=id)
            chat_form.save()
            next=request.GET.get('next', reverse('group'))
            return HttpResponseRedirect(f'/my_group/{id}')
    else:
        chat_form = NewChatForm()
    return render (request,'chat.html',{"chat_form":chat_form})
