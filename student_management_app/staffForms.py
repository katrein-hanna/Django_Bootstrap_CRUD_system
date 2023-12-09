from django import forms
from student_management_app.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TakeAttendanceForm(forms.Form):
    subject = forms.ChoiceField(label='Subject', choices=(), widget=forms.Select(attrs={'class': 'form-control','id': 'subject'}))
    session_year_id = forms.ChoiceField(label='Session Year', choices=(), widget=forms.Select(attrs={'class': 'form-control','id': 'session_year'}))
    # attendance_date = forms.DateField(label='Attendance Date', widget=DateInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super(TakeAttendanceForm, self).__init__(*args, **kwargs)

        if user_id:
            subjects = Subjects.objects.filter(staff_id=user_id)
            print("Subjects QuerySet:", subjects)  # Debug print statement

            subject_list = [(subject.id, subject.subject_name) for subject in subjects]
            print("Subject List:", subject_list)  # Debug print statement

            self.fields['subject'].choices = subject_list

        sessions = SessionYearModel.objects.all()
        session_list = [(session.id, f"{session.session_start_year} - {session.session_end_year}") for session in sessions]
        self.fields['session_year_id'].choices = session_list