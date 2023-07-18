from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Admin,CO,Medical,Visitor,Inmate
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def admin_login(request):
    if request.method == "POST":
        password = request.POST["password"]
        id = request.POST["id"]
        user=authenticate(request,username=id,password=password)
        user_exists = Admin.objects.filter(admin_id=id).exists()
        if  user is not None and user_exists:
            if (Admin.objects.get(admin_id=id).password==password):
                login(request,user)
                return HttpResponseRedirect(reverse('admin_view'))
            else:
                return render(request, 'login/admin_login.html',{'message':True})
        else:
            return render(request, 'login/admin_login.html',{'message':True})
    else:
        return render(request, 'login/admin_login.html',{'message':False})
    
@never_cache
def CO_login(request):    
    if request.method == "POST":
        password = request.POST["password"]
        id = request.POST["id"]    
        user=authenticate(request,username=id,password=password)
        user_exists = CO.objects.filter(CO_id=id).exists()
        if  user is not None and user_exists:
            if (CO.objects.get(CO_id=id).password==password):
                login(request,user)
                return HttpResponseRedirect(reverse('CO_view'))
            else:
                return render(request, 'login/CO_login.html',{'message':True})
        else:
            return render(request, 'login/CO_login.html',{'message':True})
    
    return render(request,'login/CO_login.html')

@never_cache    
def med_login(request):
    if request.method == "POST":
        password = request.POST["password"]
        id = request.POST["id"]
        user=authenticate(request,username=id,password=password)
        user_exists = Medical.objects.filter(med_id=id).exists()
        if  user is not None and user_exists:
            if (Medical.objects.get(med_id=id).password==password):
                login(request,user)
                return HttpResponseRedirect(reverse('med_view'))
            else:
                return render(request, 'login/med_login.html',{'message':True})
        else:
            return render(request, 'login/med_login.html',{'message':True})
    

    return render(request,'login/med_login.html')

@never_cache
def visit_login(request):
    if request.method == "POST":
        password = request.POST["password"]
        id = request.POST["id"]
        user=authenticate(request,username=id,password=password)
        user_exists = Visitor.objects.filter(CNIC=id).exists()
        if  user is not None and user_exists:
            if (Visitor.objects.get(CNIC=id).password==password):
                login(request,user)
                return HttpResponseRedirect(reverse('visit_view'))
            else:
                return render(request, 'login/visit_login.html',{'message':True})
        else:
            return render(request, 'login/visit_login.html',{'message':True})
        
    return render(request,'login/visit_login.html')

@never_cache
def visit_registor(request):
    if request.method=="POST":
        cnic=request.POST["cnic"]
        password=request.POST["password"]
        first=request.POST["f_name"]
        last=request.POST["l_name"]
        visiting=request.POST["Inmate"]
        rel=request.POST["relation"]
        contact=request.POST["phone"]
        
        inmate=Inmate.objects.filter(Inmate_id=visiting)
        if inmate.exists()==False:
            message=True
            return render(request,'login/reg.html',{'message':True})

        Visitor.objects.create(CNIC=cnic,first_name=first,last_name=last,Inmate_visting=inmate.first(),
                               relation_w_inmate=rel,contact_number=contact,password=password)

        User.objects.create_user(username=cnic, password=password)
        return render(request,'login/reg.html')
    
    else:
        return render(request,'login/reg.html')

@never_cache
def admin_logout(request):
    logout(request)
    return redirect(reverse('admin_login'))

@never_cache
def CO_logout(request):
    logout(request)
    return redirect(reverse('CO_login'))

@never_cache
def med_logout(request):
    logout(request)
    return redirect(reverse('med_login'))

@never_cache
def visit_logout(request):
    logout(request)
    return redirect(reverse('visit_login'))
