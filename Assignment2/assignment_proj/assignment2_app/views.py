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
                                                                               
                                
    return render(request, 'assignemt2_app/page2.html', project_data)
