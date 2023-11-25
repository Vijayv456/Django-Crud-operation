from django.shortcuts import render,redirect
from .models import employee
# Create your views here.


def create(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        phonenumber =  request.POST['phonenumber']
        address = request.POST['address']
        dob = request.POST['dob']
        email = request.POST['email']


        std = employee()
        std.FirstName = firstname
        std.LastName = lastname 
        std.Age = age
        std.PhoneNumber = phonenumber
        std.Address =address
        std.DateOfBirth = dob
        std.Email = email
        std.save()
        return redirect('view')
    return render(request,'create.html')


def view(request):
    
    obj = employee.objects.all()
    return render(request,'view.html',{'students': obj})

def edit(request,id):
    data = employee.objects.get(id=id)
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        phonenumber =  request.POST['phonenumber']
        address = request.POST['address']
        #dob = request.POST['dob']
        email = request.POST['email']
         
        data.FirstName = firstname
        data.LastName = lastname 
        data.Age = age
        data.PhoneNumber = phonenumber
        data.Address = address
        #data.DateOfBirth = dob
        data.Email = email
        data.save() 
        return redirect('view')
    return render(request,'edit.html',{'data':data})

def delete(request,id):
    data = employee.objects.get(id=id)
    data.delete()
    return redirect('view')




