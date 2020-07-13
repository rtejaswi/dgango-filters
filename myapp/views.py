from django.shortcuts import render
from myapp.models import School, Student
from myapp.froms import SchoolForms
# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    s = School.objects.order_by('first_name')
    stu = {'stu':s}
    return render(request, 'index.html', context = stu)

def form(request):
    form = SchoolForms()
    if request.method == "POST":
        form = SchoolForms(request.POST)
        if form.is_valid():
            form.save(commit = True)
        return index(request)

    return render(request, 'forms.html', {'form':form})
