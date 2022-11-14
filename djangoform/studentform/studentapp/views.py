from django.views.generic import View, ListView
from django.shortcuts import render, redirect
from studentapp.forms import StudentForm
from studentapp.models import Student

class StudentView(View):
    
    def get(self, request):
        form = StudentForm() # Unbound Instantiation
        return render(request, "stud/student.html", {"form": form})
    
    def post(self, request):
        form = StudentForm(request.POST) # Bound Instantiation
        if form.is_valid():
            instance = form.save()
            return render(request, "stud/success.html", {"data": instance})
        else:
            return render(request, "stud/student.html", {"form": form})

class ContactListView(ListView):
    template_name = "stud/contact-list.html"
    context_object_name = "records"
    queryset = Student.objects.all()

class ContactUpdateView(View):

    def get(self, request, id):
        form = StudentForm(instance=Student.objects.get(id=id))
        return render(request, "stud/student.html", {"form": form})
    
    def post(self, request, id):
        form = StudentForm(request.POST, instance=Student.objects.get(id=id))
        if form.is_valid():
            instance = form.save()
            return redirect("list-contact")
        else:
            return render(request, "stud/student.html", {"form": form})
