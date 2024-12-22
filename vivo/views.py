from django.shortcuts import render
from vivo.models import student
# Create your views here.
def index(request):
       data=student.objects.all()
       context={"data":data}
       return render(request,"index.html",context)
def about(request):
       return render(request,"index.html")
       return render(request,"about.html")
def insertdata(request):
       if request.method=="POST":
           name=request.POST.get('name')
           email=request.POST.get('email')
           age=request.POST.get('age')
           gender=request.POST.get('gender')
           query=student(name=name,email=email,age=age,gender=gender)
           query.save()
           return redirect("/")
def updateData(request,id):
       x=student.objects.get(id=id)
       context={"x":x}
       if request.method=="POST":
              name=request.POST.get('name')
              email=request.POST.get('email')
              age=request.POST.get('age')
              gender=request.POST.get('gender')
              edit=student.objects.get(id=id)
              edit.name=name
              edit.email=email
              edit.age=age
              edit.gender=gender
              edit.save()
       return render(request,"edit.html",context)
def delete(request,id):
       x=student.objects.get(id=id)
       x.delete()