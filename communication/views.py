from base64 import urlsafe_b64encode
from readline import get_current_history_length
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from communication.tokens import AccountActivationTokenGenerator
# from .models import Profile
from .forms import SignUpForm

# # Create your views here.
# @login_required(login_url='/accounts/register/')
def index(request):
    return render(request,'home.html')


# def profile_update(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile= Profile.objects.filter(username=current_user)
#             print(profile)
#             if profile:
#                 print('profile exist')
#                 username = current_user
#                 useremail=form.cleaned_data['useremail']
#                 bio=form.cleaned_data['bio']
               
#                 profile_pic=form.cleaned_data['profile_pic']
#                 # AuthenticationError=form.cleaned_data['AuthenticationError']
#                 Profile.objects.filter(username=current_user).update(useremail=useremail, profile_pic=profile_pic,bio=bio)
#                 print('updated')
#             else:
#                 print('profile does not exist')
#                 profile=form.save(commit=False)
#                 profile.username= current_user
#                 profile.save()
#                 print('profile updated')

#             message='saved successfuly'
#             # profile_display(request)
#             return redirect(profile_display)
    
            
#     else:
#         form = ProfileForm()
        
#     return render(request, 'updateprofile.html',{'form':form})

# def profile_display(request):

#     current_user = request.user
#     profile= Profile.objects.filter(username_id=request.user.id)
   

#     return render(request, 'profile.html',{"profile":profile})

# def activation_sent_view(request):
#     return render(request, 'activation_sent.html')


# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     # checking if the user exists, if the token is valid.
#     if user is not None and account_activation_token.check_token(user, token):
#         # if valid set active true 
#         user.is_active = True
#         # set signup_confirmation true
#         user.profile.signup_confirmation = True
#         user.save()
#         login(request, user)
#         return redirect('home')
#     else:
#         return render(request, 'activation_invalid.html')


# def signup_view(request):
#     if request.method  == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             user.profile.first_name = form.cleaned_data.get('first_name')
#             user.profile.last_name = form.cleaned_data.get('last_name')
#             user.profile.email = form.cleaned_data.get('email')
#             # user can't login until link confirmed
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             subject = 'Please Activate Your Account'
#             # load a template like get_template() 
#             # and calls its render() method immediately.
#             message = render_to_string('activation_request.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_decode(force_bytes(user.pk)),
#                 # method will generate a hash value with user related data
#                 'token': account_activation_token.make_token(user),
#             })
#             user.email_user(subject, message)
#             return redirect('activation_sent')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


# # def activate(request, uidb64, token):
# #     try:
# #         uid = force_text(urlsafe_base64_decode(uidb64))
# #         user = User.objects.get(pk=uid)
# #     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
# #         user = None
# #     # checking if the user exists, if the token is valid.
# #     if user is not None and account_activation_token.check_token(user, token):
# #         # if valid set active true 
# #         user.is_active = True
# #         # set signup_confirmation true
# #         user.profile.signup_confirmation = True
# #         user.save()
# #         login(request, user)
# #         return redirect('home')
# #     else:
# #         return render(request, 'activation_invalid.html')