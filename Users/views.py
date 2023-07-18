from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from login.models import Medical, Admin, CO, Inmate, Visitor,med_visit,Shift, Cell, Charge,Education
from django.views.decorators.cache import never_cache

@never_cache
def admin_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        staff = Admin.objects.all()
        return render(request, 'users/admin.html', {'admin': staff})
        

@never_cache
def co_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('CO_login'))
    else:
        staff = CO.objects.all()
        return render(request, 'users/CO.html', {'CO': staff})
        
@never_cache    
def medical_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('med_login'))
    else:
        staff = Medical.objects.all()
        return render(request, 'users/med.html', {'med': staff})
       
@never_cache
def visitor_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('visit_login'))
    else:
        visitor = Visitor.objects.all()
        return render(request, 'users/visit.html', {'Visitor': visitor})
        
@never_cache    
def med_hist(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('med_login'))
    else:        
        if request.method == "POST":
            id = request.POST["inmate"]
            date = request.POST["date"]
            diag=request.POST["diagnosis"]

            patient=Inmate.objects.filter(Inmate_id=id)
            if patient.exists()==False:
                return render(request, 'users/med_hist.html',{'med_visit':med_visit.objects.all(),'message':True})
            
            doc = Medical.objects.get(med_id=request.user.username)
            med_visit.objects.create(patient=patient.first(),doctor=doc,diagnosis=diag,date=date )
            return render(request, 'users/med_hist.html',{'med_visit':med_visit.objects.all()})

        return render(request, 'users/med_hist.html',{'med_visit':med_visit.objects.all()})

@never_cache    
def COs_show(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        COs = CO.objects.all()
        shift=Shift.objects.all()
        return render(request, 'users/admin_funcs/COs_show.html', {'CO': COs,'options':shift})
        
@never_cache
def CO_update(request,id):
        if request.method=="POST":
            s_id=request.POST['shift']
            s=Shift.objects.get(shift_id=s_id)
            Co=CO.objects.get(CO_id=id)
            up_Co=CO(
                CO_id=id,first_name=Co.first_name,last_name=Co.last_name,dob=Co.dob,shift=s,contact_number=Co.contact_number,salary=Co.salary,password=Co.password
            )
            up_Co.save()
            return redirect(reverse('COs_show'))
            
@never_cache
def med_show(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        med = Medical.objects.all()
        visit=med_visit.objects.all()
        return render(request, 'users/admin_funcs/med_show.html', {'visit': visit,'med':med})
        
@never_cache
def Patient_hist(request,id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        patients=med_visit.objects.all()
        return render(request,'users/admin_funcs/patient_hist.html',{'id':id,'patients':patients})

@never_cache
def inmate_show(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        charges=Charge.objects.all()
        options= Cell.objects.all()
        inmate=Inmate.objects.all()
        courses=Education.objects.all()
        return render(request,'users/admin_funcs/inmate_show.html',{'inmate':inmate,'options':options,
                                                                    'charges':charges,'courses':courses})

@never_cache
def Delete_inmate(request,id):
    record = Inmate.objects.get(pk=id)
    record.delete()
    inmate=Inmate.objects.all()
    return redirect(reverse('inmate_show'))

@never_cache
def edit_inmate(request,id):
    inmate=Inmate.objects.get(pk=id)
    if request.method=="POST":
        risk=request.POST.get('risk','')
        Release=request.POST.get('Release','')
        cell=request.POST.get('cell','')
        add=request.POST.get('add','')
        remove=request.POST.get('remove','')
        program=request.POST.get('program','')
        completed=request.POST.get('Completed','')

        if risk=='':
            risk=inmate.Risk_level

        if Release=='':
            Release=inmate.release_date

        if program=='':
            program=inmate.education
        elif program!='':
            program=Education.objects.get(pk=program)

        if cell=='':
            cell=inmate.cell
        elif cell!='':
            cell=Cell.objects.get(pk=cell)

        if add!='':
            charge = Charge.objects.get(pk=add)
            inmate.charges.add(charge)

        if remove!='':
            charge = Charge.objects.get(pk=remove)
            inmate.charges.remove(charge)
        
        if completed!='':
            program_new=inmate.education
            new_inmate=Inmate(Inmate_id=inmate.Inmate_id,first_name=inmate.first_name,last_name=inmate.last_name,
                          dob=inmate.dob,arrival_date=inmate.arrival_date,release_date=Release,
                          Risk_level=risk,cell=cell,education=None)
            new_inmate.completed_courses.add(program_new)

        elif completed=='':
            new_inmate=Inmate(Inmate_id=inmate.Inmate_id,first_name=inmate.first_name,last_name=inmate.last_name,
                            dob=inmate.dob,arrival_date=inmate.arrival_date,release_date=Release,
                            Risk_level=risk,cell=cell,education=program)
        new_inmate.save()
        
        for charge in inmate.charges.all():
            new_inmate.charges.add(charge)

        for program in inmate.completed_courses.all():
            new_inmate.completed_courses.add(program)

        return redirect(reverse('inmate_show'))

@never_cache
def visit_pending(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        visitor=Visitor.objects.all()
        return render(request, 'users/admin_funcs/visit_pending.html', {'visitor': visitor})

@never_cache
def edit_visit(request,id):
    visit=Visitor.objects.get(pk=id)
    if request.method=="POST":
        yes=request.POST.get('yes')
        no=request.POST.get('no')
        date=request.POST.get('date')

        if yes is not None:
            new_visit=Visitor(CNIC=visit.CNIC,first_name=visit.first_name,last_name=visit.last_name,contact_number=visit.contact_number,
                              Inmate_visting=visit.Inmate_visting,password=visit.password,
                              relation_w_inmate=visit.relation_w_inmate,Visit_date=date,approval_status=True)
            new_visit.save()

        else:
            new_visit=Visitor(CNIC=visit.CNIC,first_name=visit.first_name,last_name=visit.last_name,contact_number=visit.contact_number,
                              Inmate_visting=visit.Inmate_visting,password=visit.password,
                              relation_w_inmate=visit.relation_w_inmate,approval_status=False)
            new_visit.save()
        
        return redirect(reverse('admin_view'))

@never_cache
def visit_yes(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        visitor=Visitor.objects.all()
        return render(request, 'users/admin_funcs/visit_yes.html', {'visitor': visitor})

@never_cache
def visit_no(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('admin_login'))
    else:
        visitor=Visitor.objects.all()
        return render(request, 'users/admin_funcs/visit_no.html', {'visitor': visitor})
