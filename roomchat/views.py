from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewChatForm, NewRoomForm,EmailForm
from django.urls import reverse
from .models import Room,Roomchat
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
@login_required(login_url='/accounts/register/')
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
@login_required(login_url='/accounts/register/')
def rooms(request):
    current_user = request.user
    rooms = Room.objects.all()
    return render(request,'room.html',{"rooms":rooms,'current_user':current_user})

def group(request,id):
    # chats = Roomchat.objects.all()
    cohorts = Room.objects.get(id=id)
    # cohort=cohorts.name
    chats = Roomchat.objects.filter(room=cohorts)

    return render(request,'roomchat.html',{"chats":chats,"cohorts":cohorts})

# def roomchat(request):
#     chats = Roomchat.objects.filter()

# @login_required(login_url='/accounts/register/')
def new_chat(request,id):
    current_user = request.user
    print(current_user)
    if request.method == 'POST':
        chat_form = NewChatForm(request.POST,request.FILES)
        if chat_form.is_valid():
            # chat_form.instance.user = request.user
            chat_form.author = Room.objects.filter(id=id)
            chat_form.save(commit=False)
            chat_form.author=current_user
            print(current_user)
            print(chat_form)
            chat_form.save()
            # next=request.GET.get('next', reverse('group'))

            return HttpResponseRedirect(f'/my_group/{id}')
    else:
        chat_form = NewChatForm()
    return render (request,'chat.html',{"chat_form":chat_form})



def sendMail(request):

    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Sending an email with Django"
            message = cd['message']

            # send the email to the recipent
            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, [cd['recipient']])

            # set the variable initially created to True
            messageSent = True

    else:
        form = EmailForm()

    return render(request, 'index.html', {

        'form': form,
        'messageSent': messageSent,

    })

# Create your views here.
