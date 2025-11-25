from django.shortcuts import render
from .models import ClassList


# Create your views here.
def add_student_view(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        admission_number=request.POST.get('admission_number')
        student=ClassList(name=name,admission_number=admission_number)
        student.save()
    return render(request,'add_student.html')
def class_list_view(request):
    classlist=ClassList.objects.all()
    context={'classlist':classlist}
    return render(request,'class_list.html',context)
