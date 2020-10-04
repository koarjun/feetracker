from django.urls import path

from . import views

app_name='students'

urlpatterns = [
	path('',views.index,name='index'),

	path('view_students/',views.view_students,name='view_students'),	
	path('modify_students/',views.modify_students,name='modify_students'),
	path('',views.view_students,name='view_student_details'),
	path('students_form/',views.students_form,name='students_form'),
	path('<int:id>/',views.students_form,name='edit_students'),
	path('delete/<int:id>/',views.delete_students,name='delete_students'),


	path('view_transactions/',views.view_transactions,name='view_transactions'),	
	path('transactions_form/',views.transactions_form,name='transactions_form'),
	path('modify_transactions/',views.modify_transactions,name='modify_students'),
	path('<int:id>/',views.transactions_form,name='edit_transactions'),
	path('delete/<int:id>/',views.delete_students,name='delete_students'),
]