from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Student, Transaction
from .forms import StudentForm, TransactionForm


def index(request):
	return render(request,'students/index.html')


def view_students(request):
	try:
		students_list	=	Student.objects.all().order_by('Name')
		
	except Student.DoesNotExist:	
		raise Http404('This student does not exist')

	if request.POST:
		student_id 			=	request.POST['selected_student']
		student_info 		=	Student.objects.get(pk=student_id)
		return render(request,'students/view_student_details.html',{'student_id': student_id,'student_info':student_info})


	return render(request,'students/view_students.html', {'students_list': students_list})



def modify_students(request):
	context = {'students_list':Student.objects.all().order_by('Name') }
	return render(request,"students/modify_students.html",context)
	

def students_form(request,id=0):
	if request.method == 'GET':
		if id == 0:	#Insert operation
			student_form = StudentForm()
					
		else:		#Update operation
			student 	=	Student.objects.get(pk=id)
			student_form = StudentForm(instance = student)

		return render(request,'students/students_form.html',{'student_form':student_form})

	else:
		if id == 0:
			student_form = StudentForm(request.POST)
		else:
			student 	=	Student.objects.get(pk=id)
			student_form = StudentForm(request.POST, instance = student)

		if student_form.is_valid():
			student_form.save()
		return redirect('/students/modify_students/')


def delete_students(request,id):
	student 	=	Student.objects.get(pk=id)
	student.delete()
	return redirect('/students/modify_students/')



def view_transactions(request,student_id):
	try:
		transactions 	=	Transaction.objects.all().get(id=student_id)
	except Transaction.DoesNotExist:
		raise Http404('No transactions exist for this student')
	
	return render(request,'/students/modify_transactions.html',{'transactions':transactions})



def modify_transactions(request,id=0):
	context = {'transactions_list':Transaction.objects.all().order_by('Name','Class_Date') }
	return render(request,"students/modify_transactions.html",context)
	

def transactions_form(request,id=0):
	if request.method == 'GET':
		if id == 0:		#Insert operation
			transaction_form = TransactionForm()
					
		else:			#Update operation
			transaction  =	Transaction.objects.get(pk=id)
			transaction_form = TransactionForm(instance = transaction)

		return render(request,'students/transactions_form.html',{'transaction_form':transaction_form})

	else:
		if id == 0:
			transaction_form = StudentForm(request.POST)
		else:
			transaction 	=	Transaction.objects.get(pk=id)
			transaction_form = TransactionForm(request.POST, instance = transaction)

		if transaction_form.is_valid():
			transaction_form.save()
		return redirect('/students/modify_transactions/')


def delete_students(request,id):
	transaction 	=	Transaction.objects.get(pk=id)
	transaction.delete()
	return redirect('/students/modify_transactions/')
