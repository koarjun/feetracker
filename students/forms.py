from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .models import Student, Transaction

class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('Name','Email','Phone','Skypeid','Location')



class TransactionForm(forms.ModelForm):

	class Meta:
		model = Transaction
		fields = ('Name', 'Class_Date')
		widgets = {
            'Class_Date': DatePickerInput(),
        }
