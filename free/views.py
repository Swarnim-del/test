from django.shortcuts import render,redirect 
from django.contrib.auth.models import User,auth 
from django.contrib import messages 
from django.http import HttpResponse
from . models import jacms,jaccs,video,jacps,jatps,jatcs,jatms,jamms,jamcs,jamps

def index(request):
    return render(request,'index.html')
def jacp(request):
    videos=jacps.objects.all()
    return render(request,'jacp.html',{'videos':videos})
def jacc(request):
    videos=jaccs.objects.all()
    return render(request,'jacc.html',{'videos':videos})
def jacm(request):
    videos=jacms.objects.all()
    return render(request,'jacm.html',{'videos':videos})
def jamp(request):
    videos=jamps.objects.all()
    return render(request,'jamp.html',{'videos':videos})
def jamc(request):
    videos=jamcs.objects.all()
    return render(request,'jamc.html',{'videos':videos})
def jamm(request):
    videos=jamms.objects.all()
    return render(request,'jamm.html',{'videos':videos})
def jatp(request):
    videos=jatps.objects.all()
    return render(request,'jatp.html',{'videos':videos})
def jatc(request):
    videos=jatcs.objects.all()
    return render(request,'jatc.html',{'videos':videos})
def jatm(request):
    videos=jatms.objects.all()
    return render(request,'jatm.html',{'videos':videos})
def neet(request):
    return render(request,'neet.html')
def boards(request):
    return render(request,'boards.html')
def copy(request):
    videos=video.objects.all()
    return render(request,'copy.html',{'videos':videos})
# ****************neet******************
def namp(request):
    return render(request,'namp.html')
def namc(request):
    return render(request,'namc.html')
def namb(request):
    return render(request,'namb.html')
def natp(request):
    return render(request,'natp.html')
def natc(request):
    return render(request,'natc.html')
def natb(request):
    return render(request,'natb.html')
# *****************boards*******************
def bamp(request):
    return render(request,'bamp.html')
def bamc(request):
    return render(request,'bamc.html')
def bamb(request):
    return render(request,'bamb.html')
def bamm(request):
    return render(request,'bamm.html')
def batm(request):
    return render(request,'batm.html')
def batp(request):
    return render(request,'batp.html')
def batc(request):
    return render(request,'batc.html')
def batb(request):
    return render(request,'batb.html')

def profile(request):
    return render(request,'profile.html')
    
def logout(request):
     auth.logout(request)
     return redirect('/')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')



def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2 and name!=' ':
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('signup')
    else:
        return render(request,'signup.html')



# Create your views here.
# videos:[12,15,36]
# for video in videos:
#     print(video)