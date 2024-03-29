from django.shortcuts import render
from .Data import *
# Create your views here.
def hello(request):
 return render(request, 'hello.html')





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
                                                                               
                                
    return render(request, 'page2.html', project_data)
