from django.db import models

class Student(models.Model):
	Name		= models.CharField("Student Name",max_length=50)
	Email		= models.EmailField(max_length=50,null=True,blank=True)
	Phone		= models.CharField(max_length=15,null=True,blank=True)
	Skypeid		= models.CharField("Skype Id",max_length=50,null=True,blank=True)
	Location	= models.CharField("Location (Country, State, City)",max_length=50,null=True,blank=True)
	created_ts	= models.DateTimeField(auto_now_add=True,null=True,blank=True)
	updated_ts	= models.DateTimeField(auto_now=True,null=True,blank=True)


	def __str__(self):
		return self.Name


class Transaction(models.Model):
	Name				= models.ForeignKey(Student,on_delete=models.CASCADE)
	Class_Date			= models.DateField(null=False, blank=False)
	created_ts			= models.DateTimeField(auto_now_add=True,null=True,blank=True)
	updated_ts			= models.DateTimeField(auto_now=True,null=True,blank=True)

	def __str__(self):
		return self.Name