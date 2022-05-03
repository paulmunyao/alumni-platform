from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm

# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    return render(request,'home.html')


def profile_update(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile= Profile.objects.filter(username=current_user)
            print(profile)
            if profile:
                print('profile exist')
                username = current_user
                useremail=form.cleaned_data['useremail']
                bio=form.cleaned_data['bio']
               
                profile_pic=form.cleaned_data['profile_pic']
                # AuthenticationError=form.cleaned_data['AuthenticationError']
                Profile.objects.filter(username=current_user).update(useremail=useremail, profile_pic=profile_pic,bio=bio)
                print('updated')
            else:
                print('profile does not exist')
                profile=form.save(commit=False)
                profile.username= current_user
                profile.save()
                print('profile updated')

            message='saved successfuly'
            # profile_display(request)
            return redirect(profile_display)
    
            
    else:
        form = ProfileForm()
        
    return render(request, 'updateprofile.html',{'form':form})

def profile_display(request):

    current_user = request.user
    profile= Profile.objects.filter(username_id=request.user.id)
   

    return render(request, 'profile.html',{"profile":profile})