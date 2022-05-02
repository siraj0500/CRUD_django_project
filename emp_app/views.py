from django.shortcuts import render, redirect
from .forms import EmpRegForm
from .models import Employee_reg


# Create your views here.
def empdb(request):
    empview = Employee_reg.objects.all()
    return render(request, 'view_emp_data.html', {'empview': empview})


def index(request):
    if request.method == 'POST':
        frm = EmpRegForm(request.POST or None, request.FILES or None)
        if frm.is_valid():
            name = frm.cleaned_data['name']
            address = frm.cleaned_data['address']
            contact_number = frm.cleaned_data['contact_number']
            email = frm.cleaned_data['email']
            pic = frm.cleaned_data['pic']
            register = Employee_reg(name=name, address=address, contact_number=contact_number, email=email, pic=pic)
            register.save()
            return redirect('empdb')
    else:
        frm = EmpRegForm()
    return render(request, "index.html", {'form': frm, })


# def empview(request):
#     if request.method == 'POST':
#         frm = EmpRegForm(request.POST or None, request.FILES or None)
#         if frm.is_valid():
#             name = frm.cleaned_data['name']
#             address = frm.cleaned_data['address']
#             contact_number = frm.cleaned_data['contact_number']
#             email = frm.cleaned_data['email']
#             image = frm.cleaned_data['image']
#             register = Employee_reg(name=name, address=address, contact_number=contact_number, email=email, image=image)
#             register.save()
#             return redirect('empdb')
#     else:
#         frm = EmpRegForm()
#     return render(request, "index.html", {'form': frm, })




def empdelete(request, id):
    if request.method == 'POST':
        delete_emp = Employee_reg.objects.get(id=id)
        delete_emp.delete()
        return redirect('empdb')


def empupdate(request, id):
    if request.method == 'POST':
        update = Employee_reg.objects.get(id=id)
        frm = EmpRegForm(request.POST, instance=update)
        if frm.is_valid():
            frm.save()
    else:
        update = Employee_reg.objects.get(id=id)
        frm = EmpRegForm(instance=update)
    return render(request, 'update_emp_data.html', {'form': frm})
