from django.db import models

'''### One to one relationship
class User(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key= True)
    language = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank= False, unique=True)

    def __str__(self):
        return str(self.email)
    
# u1 = User(name = "Anish")
# u2 = User(name = "Dev")
# p1 = Profile(user = u1, language = "English", email = "anish@gmail.com")
# p2 = Profile(user = u2, language = "Nepali", email = "dev@gmail.com")
# p1.user #gives Anish
# p2.user #gives Dev'''


from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=50, unique= True)
    
    def __str__(self):
        return f"{self.name}, {self.id}"

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='address')

    def __str__(self):
        return f"{self.street}, {self.city}"

class Company(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(Employee , related_name='projects')

    def __str__(self):
        return self.name

'''# Assuming we have created instances of Employee and Project earlier
employee1 = Employee.objects.get(name="John")
employee2 = Employee.objects.get(name="Alice")
project1 = Project.objects.get(name="Project A")
project2 = Project.objects.get(name="Project B")

# Associating employees with projects
project1.employees.add(employee1, employee2)
project2.employees.add(employee1)

# Accessing projects of an employee
projects_of_employee1 = employee1.projects.all()
projects_of_employee2 = employee2.projects.all()

# Accessing employees of a project
employees_of_project1 = project1.employees.all()
employees_of_project2 = project2.employees.all()
'''
