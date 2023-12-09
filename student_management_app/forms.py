from django import forms
from student_management_app.models import * 

class DateInput(forms.DateInput):
    input_type= 'date'

class AddStudentForm(forms.Form):
    email= forms.EmailField(label='Email',max_length=50, required=True,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password= forms.CharField(label='Password',max_length=50,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name= forms.CharField(label='First Name',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(label='Last Name',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    username= forms.CharField(label='Username',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    address= forms.CharField(label='Address',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_list=[]
    try:
        courses=Courses.objects.all()
        for course in courses:
            small_course=(course.id,course.course)
            course_list.append(small_course)
    except:
        course_list=[]

    session_list=[]
    try:
        sessions=SessionYearModel.objects.all()
        for session in sessions:
            small_session=(session.id,str(session.session_start_year)+"  -  "+str(session.session_end_year))
            session_list.append(small_session)
    except:
        session_list=[]

    gender_choice=(
        ('Male','Male'),('Female','Female')
    )

    course= forms.ChoiceField(label='Course',choices=course_list,widget=forms.Select(attrs={'class':'form-control'}))
    gender= forms.ChoiceField(label='Gender',choices=gender_choice,widget=forms.Select(attrs={'class':'form-control'}))
    session_year_id= forms.ChoiceField(label='Session Year',choices=session_list,widget=forms.Select(attrs={'class':'form-control'}))
    profile_pic= forms.FileField(label='Profile Picture',widget=forms.FileInput(attrs={'class':'form-control'}))

class EditStudentForm(forms.Form):
        email= forms.EmailField(label='Email',max_length=50, required=True,widget=forms.EmailInput(attrs={'class': 'form-control'}))
        first_name= forms.CharField(label='First Name',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
        last_name= forms.CharField(label='Last Name',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
        username= forms.CharField(label='Username',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
        address= forms.CharField(label='Address',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
        course_list=[]
        try:
            courses=Courses.objects.all()
            for course in courses:
                small_course=(course.id,course.course)
                course_list.append(small_course)
        except:
            course_list=[]

        session_list=[]
        try:
            sessions=SessionYearModel.objects.all()
            for session in sessions:
                small_session=(session.id,str(session.session_start_year)+"  -  "+str(session.session_end_year))
                session_list.append(small_session)
        except:
            session_list=[]

        gender_choice=(
            ('Male','Male'),('Female','Female')
        )

        course= forms.ChoiceField(label='Course',choices=course_list,widget=forms.Select(attrs={'class':'form-control'}))
        gender= forms.ChoiceField(label='Gender',choices=gender_choice,widget=forms.Select(attrs={'class':'form-control'}))
        session_year_id= forms.ChoiceField(label='Session Year',choices=session_list,widget=forms.Select(attrs={'class':'form-control'}))
        profile_pic= forms.FileField(label='Profile Picture',widget=forms.FileInput(attrs={'class':'form-control'}),required=False)


class AddStaffForm(forms.Form):
    email = forms.EmailField(label='Email',max_length=50,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name= forms.CharField(label='First Name',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(label='Last Name',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    username= forms.CharField(label='Username',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    address= forms.CharField(label='Address',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    

class EditStaffForm(forms.Form):
    email = forms.EmailField(label='Email',max_length=50,widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name= forms.CharField(label='First Name',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(label='Last Name',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    username= forms.CharField(label='Username',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    address= forms.CharField(label='Address',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))

class CourseForm(forms.Form):
    course_name = forms.CharField(label='Course Name',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))

class SubjectForm(forms.Form):
    subject_name = forms.CharField(label='Subject Name',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_list=[]
    try:
        courses=Courses.objects.all()
        for course in courses:
            small_course=(course.id,course.course)
            course_list.append(small_course)
    except:
        course_list=[]
    
    staff_list=[]
    try:
        staffs=CustomUser.objects.filter(user_type=2)
        for staff in staffs:
            small_staff=(staff.id,staff.username)
            staff_list.append(small_staff)
    except:
        staff_list=[]
    course= forms.ChoiceField(label='Course',choices=course_list,widget=forms.Select(attrs={'class':'form-control'}))
    staff= forms.ChoiceField(label='Staff',choices=staff_list,widget=forms.Select(attrs={'class':'form-control'}))
    
class AddSessionForm(forms.Form):
    session_start_year= forms.DateField(label='Session Start Year',widget=DateInput(attrs={'class':'form-control'}))
    session_end_year= forms.DateField(label='Session End Year',widget=DateInput(attrs={'class':'form-control'}))
