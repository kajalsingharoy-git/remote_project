from django.shortcuts import render
from apolloApp.forms import PatientForm
from apolloApp.forms import Patient
from django.http import HttpResponseRedirect

# Create your views here.

def retrive_view(request):
    list_pat=Patient.objects.all()
    return render(request,'apolloApp/retrive.html',{'list_pat':list_pat})

def create_view(request):
    form=PatientForm()
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'apolloApp/create.html',{'form':form})


def delete_view(request,id):
    patient=Patient.objects.get(id=id)
    patient.delete()
    return HttpResponseRedirect('/')

def update_view(request,id):
    patient=Patient.objects.get(id=id)
    if request.method=='POST':
        form=PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request,'apolloApp/update.html',{'patient':patient})
