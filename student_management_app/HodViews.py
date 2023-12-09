from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from student_management_app.models import *  #CustomUser,Staffs,Courses,Subjects,Students
from django.core.files.storage import FileSystemStorage
from student_management_app.forms import * #AddStudentForm,EditStudentForm,AddStaffForm,EditStaffForm,CourseForm,SubjectForm

def admin_home(request):
    return render(request,'hod_template/home_content.html')

def add_staff(request):
    form=AddStaffForm()
    return render(request,'hod_template/add_staff_template.html',{'form':form})

def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        form= AddStaffForm(request.POST,request.FILES)
        if form.is_valid():
            first_name= form.cleaned_data['first_name']
            last_name= form.cleaned_data['last_name']
            username= form.cleaned_data['username']
            email= form.cleaned_data['email']
            password= form.cleaned_data['password']
            address= form.cleaned_data['address']
            try:
                user= CustomUser.objects.create_user(password=password,username=username,first_name=first_name,last_name=last_name,email=email,user_type=2)
                user.staffs.address=address
                user.save()
                messages.success(request,"Staff Add Successfully")
                return HttpResponseRedirect("/add_staff")
            except:
                messages.error(request,"Faild to Add Staff")
                return HttpResponseRedirect("/add_staff")
        else:
            form=AddStaffForm(request.POST)
            return render(request,'hod_template/add_staff_template.html',{'form':form})

def add_course(request):
    form=CourseForm()
    return render(request, 'hod_template/add_course_template.html',{'form':form})

def add_course_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        course_name = request.POST.get('course_name')
        try:
            course_model= Courses(course=course_name)
            course_model.save()
            messages.success(request,"Course Add Successfully")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request,"Faild to Add Course")
            return HttpResponseRedirect("/add_course")

def add_student(request):
    form= AddStudentForm()
    return render(request, 'hod_template/add_student_template.html',{'form':form})

def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        form= AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name= form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username= form.cleaned_data['username']
            email= form.cleaned_data['email']
            password=form.cleaned_data['password']
            address=form.cleaned_data['address']
            gender=form.cleaned_data['gender']
            session_year_id=form.cleaned_data['session_year_id']
            course_id=form.cleaned_data['course']
            profile_pic= request.FILES['profile_pic']
            fs= FileSystemStorage()
            filename= fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)

            try:
                user= CustomUser.objects.create_user(password=password,username=username,first_name=first_name,last_name=last_name,email=email,user_type=3)
                user.students.address=address
                user.students.gender=gender
                course_obj=Courses.objects.get(id=course_id)
                user.students.course_id=course_obj
                session_obj=SessionYearModel.objects.get(id=session_year_id)
                user.students.session_year_id=session_obj
                user.students.profile_pic=profile_pic_url
                user.save()
                messages.success(request,"Student Add Successfully")
                return HttpResponseRedirect("/add_student")
            except:
                messages.error(request,"Faild to Add Student")
                return HttpResponseRedirect("/add_student")
        else:
            form= AddStudentForm(request.POST)
            return render(request, 'hod_template/add_student_template.html',{'form':form})


def add_subject(request):
    form= SubjectForm()
    return render(request, 'hod_template/add_subject_template.html',{'form':form})

def add_subject_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        form= SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            subject_name = form.cleaned_data['subject_name']
            course_id= form.cleaned_data['course']
            staff_id= form.cleaned_data['staff']
            course_obj=Courses.objects.get(id=course_id)
            staff_obj=CustomUser.objects.get(id=staff_id)

            try:
                subject_model= Subjects(subject_name=subject_name,course_id=course_obj,staff_id=staff_obj)
                subject_model.save()
                messages.success(request,"Subject Add Successfully")
                return HttpResponseRedirect("/add_subject")
            except:
                messages.error(request,"Faild to Add Subject")
                return HttpResponseRedirect("/add_subject")
        else:
            form= SubjectForm(request.POST)
            return render(request, 'hod_template/add_subject_template.html',{'form':form})


def manage_staff(request):
    staffs=Staffs.objects.all()
    return render(request, 'hod_template/manage_staff_template.html',{'staffs':staffs})

def manage_student(request):
    students=Students.objects.all()
    return render(request, 'hod_template/manage_student_template.html',{'students':students})

def manage_course(request):
    courses=Courses.objects.all()
    return render(request, 'hod_template/manage_course_template.html',{'courses':courses})

def manage_subject(request):
    subjects=Subjects.objects.all()
    return render(request, 'hod_template/manage_subject_template.html',{'subjects':subjects})

def edit_staff(request,staff_id):
    request.session['staff_id'] = staff_id
    staff=Staffs.objects.get(admin=staff_id)
    form= EditStaffForm()
    form.fields['email'].initial=staff.admin.email
    form.fields['first_name'].initial=staff.admin.first_name
    form.fields['last_name'].initial=staff.admin.last_name
    form.fields['username'].initial=staff.admin.username
    form.fields['address'].initial=staff.address
    return render(request, 'hod_template/edit_staff_template.html',{'form':form,'id':staff_id,'username':staff.admin.username})

def edit_staff_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2> Method Not Allowed </h2>')
    else:
        staff_id= request.session.get('staff_id')
        if staff_id == None:
            return HttpResponseRedirect("/manage_staff")
    
        form= EditStaffForm(request.POST,request.FILES)
        if form.is_valid():
            first_name= form.cleaned_data['first_name']
            last_name= form.cleaned_data['last_name']
            username= form.cleaned_data['username']
            email= form.cleaned_data['email']
            address= form.cleaned_data['address']
            try:
                user= CustomUser.objects.get(id=staff_id)
                user.first_name=first_name
                user.last_name= last_name
                user.username=username
                user.email=email
                user.save()
                staff_model=Staffs.objects.get(admin=staff_id)
                staff_model.address=address
                staff_model.save()
                messages.success(request,"Staff Updated Successfully")
                return HttpResponseRedirect("/manage_staff")
            except:
                messages.error(request,"Faild to Updated Staff")
                return HttpResponseRedirect("/manage_staff")
        else:
            staff=Staffs.objects.get(admin=staff_id)
            form= EditStaffForm(request.POST)
            return render(request, 'hod_template/edit_staff_template.html',{'form':form,'id':staff_id,'username':staff.admin.username})

def edit_student(request,student_id):
    request.session['student_id'] = student_id
    student=Students.objects.get(admin=student_id)
    form= EditStudentForm()
    form.fields['email'].initial=student.admin.email
    form.fields['first_name'].initial=student.admin.first_name
    form.fields['last_name'].initial=student.admin.last_name
    form.fields['username'].initial=student.admin.username
    form.fields['address'].initial=student.address
    form.fields['course'].initial=student.course_id.id
    form.fields['gender'].initial=student.gender
    form.fields['session_year_id'].initial=student.session_year_id
    form.fields['profile_pic'].initial=student.profile_pic
    return render(request, 'hod_template/edit_student_template.html',{'id':student_id,'form':form,'username':student.admin.username})

def edit_student_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2> Method Not Allowed </h2>')
    else:
        student_id= request.session.get('student_id')
        if student_id == None:
            return HttpResponseRedirect("/manage_student")
        
        form=EditStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name= form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username= form.cleaned_data['username']
            email= form.cleaned_data['email']
            address= form.cleaned_data['address']
            gender= form.cleaned_data['gender']
            session_year_id= form.cleaned_data['session_year_id']
            course_id= form.cleaned_data['course']
            if request.FILES.get('profile_pic',False):
                profile_pic= request.FILES['profile_pic']
                fs= FileSystemStorage()
                filename= fs.save(profile_pic.name,profile_pic)
                profile_pic_url=fs.url(filename)
            else:
                profile_pic_url=None
            try:
                user= CustomUser.objects.get(id=student_id)
                user.first_name=first_name
                user.last_name= last_name
                user.username=username
                user.email=email
                user.students.profile_pic=profile_pic_url
                user.save()
                student_model= Students.objects.get(admin=student_id)
                student_model.address = address
                student_model.gender= gender
                session_obj=SessionYearModel.objects.get(id=session_year_id)
                student_model.session_year_id = session_obj
                course_obj=Courses.objects.get(id=course_id)
                student_model.course_id = course_obj
                if profile_pic_url != None:
                    student_model.profile_pic=profile_pic_url
                student_model.save()

                messages.success(request,"Student Updated Successfully")
                return HttpResponseRedirect("/manage_student")
            except:
                messages.error(request,"Faild to Updated Student")
                return HttpResponseRedirect("/manage_student")
        else:
            form=EditStudentForm(request.POST)
            student=Students.objects.get(admin=student_id)
            return render(request, 'hod_template/edit_student_template.html',{'id':student_id,'form':form,'username':student.admin.username})


def edit_subject(request,subject_id):
    request.session['subject_id'] = subject_id
    subject=Subjects.objects.get(id=subject_id)
    form= SubjectForm()
    form.fields['subject_name'].initial=subject.subject_name
    form.fields['course'].initial=subject.course_id.id
    form.fields['staff'].initial=subject.staff_id.id
    return render(request, 'hod_template/edit_subject_template.html',{'form':form,'id':subject_id})

def edit_subject_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2> Method Not Allowed </h2>")
    else:
        subject_id= request.session.get('subject_id')
        if subject_id == None:
            return HttpResponseRedirect("/manage_subject")
        
        form= SubjectForm(request.POST,request.FILES)

        if form.is_valid():
            subject_name= form.cleaned_data['subject_name']
            course_id= form.cleaned_data['course']
            course_obj=Courses.objects.get(id=course_id)
            staff_id= form.cleaned_data['staff']
            staff_obj=CustomUser.objects.get(id=staff_id) 
            try:
                subject_model= Subjects.objects.get(id=subject_id)
                subject_model.subject_name= subject_name
                subject_model.course_id=course_obj
                subject_model.staff_id=staff_obj
                subject_model.save()
                messages.success(request,"Subject Updated Successfully")
                return HttpResponseRedirect("/manage_subject")
            except:
                messages.error(request,"Faild to Updated Subject")
                return HttpResponseRedirect("/manage_subject")
        else:
            form= SubjectForm(request.POST)
            return render(request, 'hod_template/edit_subject_template.html',{'form':form,'id':subject_id})


def edit_course(request,course_id):
    request.session['course_id'] = course_id
    course=Courses.objects.get(id=course_id)
    form= CourseForm()
    form.fields['course_name'].initial=course.course
    return render(request, 'hod_template/edit_course_template.html',{'form':form,'id':course_id})

def edit_course_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2> Method Not Allowed </h2>")
    else:
        course_id= request.session.get('course_id')
        form= CourseForm(request.POST,request.FILES)
        if form.is_valid():
            course_name= form.cleaned_data['course_name']
            try:
                course_model= Courses.objects.get(id=course_id)
                course_model.course= course_name
                course_model.save()
                messages.success(request,"Course Updated Successfully")
                return HttpResponseRedirect("/manage_course")
            except:
                messages.error(request,"Faild to Updated Course")
                return HttpResponseRedirect("/manage_course")
        else:
            form= CourseForm(request.POST)
            return render(request, 'hod_template/edit_course_template.html',{'form':form,'id':course_id})


def manage_session(request):
    form= AddSessionForm()
    return render(request, 'hod_template/manage_session_template.html',{'form':form})

def add_session_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2> Method Not Allowed </h2>")
    else:
        form= AddSessionForm(request.POST,request.FILES)
        if form.is_valid():
            session_start_year=form.cleaned_data['session_start_year']
            session_end_year= form.cleaned_data['session_end_year']
            try:
                sessionyear= SessionYearModel(session_start_year=session_start_year, session_end_year=session_end_year)
                sessionyear.save()
                messages.success(request,"Session Updated Successfully")
                return HttpResponseRedirect("/manage_session")
            except:
                messages.error(request,"Faild to Updated Session")
                return HttpResponseRedirect("/manage_session")
        else:
            form= AddSessionForm(request.POST)
            return render(request, 'hod_template/manage_session_template.html',{'form':form})

