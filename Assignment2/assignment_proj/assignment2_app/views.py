from django.shortcuts import render
from .Data import *
# Create your views here.


def page2(request):

    
    
    project_data = { 
       'proj_1' : proj_1,
       'proj_2' : proj_2,
       'proj_3' : proj_3, 
       'proj_4' : proj_4, 
       'proj_5' : proj_5, 
       'proj_6' : proj_6, 
       'proj_7' : proj_7, 
    }                          
                                                                               
                                
    return render(request, 'assignment2_app/page2.html', project_data)

######################################################################################

def about(request):
   
   context = {
      'list': create_members,
   }
   
   return render(request, 'assignment2_app/about.html', context)

# Define Member class
class Member:
   def __init__(self, role, name, student_id, course):
      
      self.role = role
      self.name = name
      self.student_id = student_id
      self.course = course

# Function to create list of Member objects
def create_members():
   
   list = []
   
   list.append(Member('Leader',
                      'Vendal Gomes',
                      's321266',
                      'Bachelor of IT'))
   
   list.append(Member('Scribe',
                      'Louis Bajarias',
                      's366704',
                      'Bachelor of IT'))
   
   list.append(Member('Presenter',
                      'Syarif Aiman Lubis',
                      's362319',
                      'Bachelor of IT'))
   
   list.append(Member('Editor',
                      'James Paul',
                      's343288',
                      'Bachelor of Computer Science'))
   
   list.append(Member('Timekeeper',
                      'Miguel Lalim',
                      's323016',
                      'Bachelor of Computer Science'))
   
   return list

