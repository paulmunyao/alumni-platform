from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Fundroom,fundchat
from .forms import NewFundRoomForm,FundChatForm
# Create your views here.
def new_fund(request):
    current_user = request.user
    if request.method == "POST":
        new_form = NewFundRoomForm(request.POST,request.FILES)
        new_form.instance.admin = request.user
        print (new_form)
        if new_form.is_valid():
            new_form.save()

            return redirect('fundgroups')
    else:
        new_form = NewFundRoomForm()
    return render(request,'newgroup.html',{"new_form":new_form})


def fundgroups(request):
    current_user = request.user
    fundrooms = Fundroom.objects.all()
    return render(request,'fundrooms.html',{"fundrooms":fundrooms,'current_user':current_user})


def fundteam(request,id):
    teams = Fundroom.objects.get(id=id)
    fundchats = fundchat.objects.filter(fundgroup=teams)
    return render(request,'fundchat.html',{"fundchats":fundchats,"teams":teams})


def fund_chat(request,id):
    current_user = request.user
    print(current_user)
    if request.method == 'POST':
        fund_form = FundChatForm(request.POST,request.FILES)
        if fund_form.is_valid():
            # chat_form.instance.user = request.user
            fund_form.author = Fundroom.objects.filter(id=id)
            fund_form.save(commit=False)
            fund_form.author=current_user
            print(current_user)
            print(fund_form)
            fund_form.save()
            # next=request.GET.get('next', reverse('group'))

            return HttpResponseRedirect(f'/my_fundgroup/{id}')
    else:
        fund_form = FundChatForm()
    return render (request,'chat.html',{"fund_form":fund_form})



