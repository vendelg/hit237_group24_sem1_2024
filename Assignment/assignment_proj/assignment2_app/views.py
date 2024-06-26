from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from assignment2_app.data import *
from .models import Project, ThesisApplication, Student, Accounts
from .forms import ThesisForm, ApplicationForm, StudentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash 
from .models import Accounts
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


#Redirect
from django.shortcuts import redirect


from . forms import AccAuthForm

#Authenticate 
from django.contrib.auth import authenticate, login, logout
# Create your views here.

app_name = 'assignment2_app/'

########################################################################

# Function to create lists :
def create_members():
   
   list = []
   
   list.append(Member('static/images/VendalPlH.png' ,'Leader',
                      'Vendal Gomes',
                      's321266',
                      'Bachelor of IT'))
   
   list.append(Member('static/images/Louis.png','Scribe',
                      'Louis Bajarias',
                      's366704',
                      'Bachelor of IT'))
   
   list.append(Member('static/images/Aiman.png','Presenter',
                      'Syarif Aiman Lubis',
                      's362319',
                      'Bachelor of IT'))
   
   list.append(Member('static/images/James.png','Editor',
                      'James Paul',
                      's343288',
                      'Bachelor of Computer Science'))
   
   list.append(Member('static/images/Miguel.png','Timekeeper',
                      'Miguel Lalim',
                      's323016',
                      'Bachelor of Computer Science'))
   
   return list

def homemessages():
   messages = []

   messages.append(homepage('HIT237 Group 24 respectfully acknowledges the traditional custodians of the land on which we live and work in the Northern Territory, Australia. We pay our respects to the Aboriginal peoples, the traditional owners and custodians of this land, past, present, and emerging.', ))
   messages.append(homepage('This website was created for Charles Darwin University masters degree level Information Technology students who are looking to complete their theses. The website allows the students to be able to view all available thesis subjects and the teacher who will be the one to guide/support them throughout the length of their thesis. The website created will also allow users to see which lecturers are available to assist for different thesis subjects.', ))
   messages.append(homepage('The available theses can be found in the Thesis tab. The About Us page will show details about HIT237 Group 24.  This is standard across many different higher education institutes, with the lecturer contacts being provided to the student as well. This will allow them to contact the corresponding lecturer so they will be able to apply for a thesis that they would be interested in completion for their master’s in information technology degree.', ))

   return messages 



















# Requests:











#BaseView


def base(request, *args, **kwargs):
   
   user_id = kwargs.get("user_id") 
      
   account=Accounts.objects.all(pk = user_id)
   
   
   context = {
      'user' : account ,
      
   }

   return render(request, context)



def about(request):
   
   context = {
      'list': create_members,
   }
   
   return render(request, 'assignment2_app/about.html', context)


def home(request):
   

   home_context = {
      'homemessages' : homemessages,
   }

   return render(request, 'assignment2_app/homepage.html', home_context)

#ThesisInteractionsViews


def view_thesis(request, tid):  # Step 2
   
   thesis = Project.objects.get(id=tid)
   
   page_data = {
      'thesis': thesis
   }
   
   return render(request, 'assignment2_app/view_thesis.html', page_data)

def add_thesis(request):
   page_data = {'thesisForm': ThesisForm()}
   user= request.user
   is_supervisor = False
   is_coordinator = False
   if user.role == Accounts.Role.Supervisor :
      is_supervisor = True
      page_data['is_supervisor'] = is_supervisor
      return render(request, app_name + 'add_thesis.html', page_data)
   elif user.role == Accounts.Role.Coordinator:
      is_coordinator = True
      page_data['is_coordinator'] = is_coordinator

     
   
      return render(request, app_name + 'add_thesis.html', page_data)
   else: return HttpResponse("You dont have the right permission.")

def add_thesis_request(request):

   if request.method != 'POST':
      return HttpResponseRedirect('/add/thesis/')
   else:
      form = ThesisForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect(reverse('homepage'))
      else:
         return HttpResponse("Already exist")


def modify_thesis(request, tid):
   thesis = Project.objects.get(tid=int(tid))
   
   page_data = None
   user= request.user
   is_supervisor = False
   

   if request.method == 'POST':
      if 'edit' in request.POST:
         print("edit")
         print(tid)
         form = ThesisForm(request.POST, instance=thesis)
         page_data = edit_thesis(form)
      elif 'delete' in request.POST:
         page_data = delete_thesis(thesis)
      return HttpResponseRedirect(reverse('page2'))
   else:
      # This request is not generated by a form's Submit button.
      # Display the Form containing the queried record.
      form = ThesisForm(instance=thesis)
      page_data = {'thesisForm': form,}

   if user.role == Accounts.Role.Supervisor :
      is_supervisor = True
      page_data['is_supervisor'] = is_supervisor
      return render(request, app_name + 'edit_thesis.html', page_data)
   elif user.role == Accounts.Role.Coordinator:
      is_coordinator = True
      page_data['is_coordinator'] = is_coordinator
      return render(request, app_name + 'edit_thesis.html', page_data)
   else: return HttpResponse("Wrong Permission")


def edit_thesis(form):

    page_data = {}

    if form.is_valid() != True:
        # Validation failed. Redisplay the form.
        page_data = {'thesisForm': form, }
    else:
        # Validation passed. Save the data.
        form.save()

    return page_data


def delete_thesis(pub):
    pub.delete()
    return None

def page2(request):

   theses = Project.objects.all()
   user = request.user
   is_supervisor = False
   is_coordinator = False
   if user.is_authenticated: 
      if user.role == Accounts.Role.Supervisor :
         is_supervisor = True
      elif user.role == Accounts.Role.Coordinator:
         is_coordinator = True
   
   page_data = {
      "theses": theses,
      "is_supervisor" : is_supervisor,
      "is_coordinator": is_coordinator

   }
                                                                                                      
   return render(request, 'assignment2_app/page2.html', page_data)



def show_thesis_topic(request, tid):

   thesis = Project.objects.all()
   thesis_selected = None

   for topics in thesis:
      if topics.tid == tid:
         thesis_selected = topics
         break
         
   
   context = {
      'thesis': thesis_selected,
   }

   return render(request, 'assignment2_app/page3.html', context)



#Login/LogoutViews


def logout_view(request):
   logout (request)
   return redirect ('homepage')

def login_view(request, *args, **kwargs):

   context = {}
   user = request.user 
   if user.is_authenticated: 
      return redirect("homepage")
   
   if request.POST:
      form = AccAuthForm(request.POST)
      if form.is_valid():
         email = request.POST['email']
         password = request.POST['password']
         user = authenticate(email=email, password=password)
         if user:
            login(request, user)
            destination = get_redirect(request)
            if destination:
               return redirect(destination)
            return redirect ("homepage")
         
      else:
         context['login_form'] = form
   return render (request, "assignment2_app/login.html", context)

def get_redirect(request):
   redirect = None
   if request.GET:
      if request.GET.get("next"):
         redirect = str(request.GET.get("next"))
         
   return redirect

#Thesis Application for Student
@login_required
def thesis_application(request, tid):
   
   thesis = Project.objects.all()
   thesis_selected = None

   for topics in thesis:
      if topics.tid == tid:
         thesis_selected = topics
         break
      
   user= request.user
   is_student = False
   is_supervisor = False
   is_coordinator = False
   if user.role == Accounts.Role.Student :
      is_student = True
   if user.role == Accounts.Role.Supervisor:
      is_supervisor = True
   if user.role == Accounts.Role.Coordinator:
      is_coordinator = True
     

      if user.role == Accounts.Role.Student :
          is_student = True
      if user.role == Accounts.Role.Supervisor:
         is_supervisor = True
      if user.role == Accounts.Role.Coordinator:
         is_coordinator = True

   context = { 
     "application_form" : ApplicationForm(),
     "thesis" :thesis_selected,
     "is_student": is_student,
     "is_supervisor": is_supervisor,
     "is_coordinator": is_coordinator,
   }                
   return render(request, 'assignment2_app/apply_thesis.html', context)
   


def application_submit(request):
   data = ThesisApplication.objects.all()
   
   if request.method != 'POST':
      return HttpResponse("Invalid UserID/GroupID")
   elif request.method == None:
      return HttpResponse("Invalid UserID/GroupID")
   else:
      context = {
         'data' : data,
         }
      form = ApplicationForm(request.POST)

      if form.is_valid():
         save_application(form)
      else:
         context = {'val_errors': form.errors, }
         return HttpResponseRedirect('../../apply/thesis') and HttpResponse("Invalid UserID/GroupID")
      
          
      
   return render(request, 'assignment2_app/notice.html', context)

def save_application(form):
   new_thesis_application_object = form.save()



#Student Registration

def student_registration(request):

   context = { 
     "student_form" : StudentForm(),
   }                
   return render(request, 'assignment2_app/register_student.html', context)

def registration_submit(request):
   data = Student.objects.all()
   
   if request.method != 'POST':
      return HttpResponseRedirect('register/student/done/')
   else:
      context = {'data' : data}
      form = StudentForm(request.POST)
      if form.is_valid():
         form.save()
      else:
         context = {'val_errors': form.errors, }
      
   return render(request, 'assignment2_app/done.html', context)



#ProfileViews

def dashboard(request, *args, **kwargs):
   
   context = {}
   user_id = kwargs.get("user_id")
   try:
      account=Accounts.objects.get(pk = user_id)
   except Accounts.DoesNotExist:
      return HttpResponse("That user does not exist")

   if account:
      context['id'] = account.is_admin
      context['username'] = account.username
      context['email'] = account.email
      context['hide_email'] = account.hide_email


   
      user = request.user
      

      if user.is_authenticated and user != account:
         return redirect ("homepage")
      elif not user.is_authenticated:
         return redirect ("homepage")
      
      context ['user'] = account
   
   return render(request, 'assignment2_app/dashboard.html', context)

#notifications

def notification(request, *args, **kwargs):

   thesis = Project.objects.all()

   context = {}
   user_id = kwargs.get("user_id")
   try:
      account=Accounts.objects.get(pk = user_id)
   except Accounts.DoesNotExist:
      return HttpResponse("That user does not exist")

   if account:
     
      context['id'] = account.is_admin
      context['username'] = account.username
      context['email'] = account.email
      context['hide_email'] = account.hide_email
   
      user = request.user
      if user.is_authenticated and user != account:
         return redirect ("homepage")
      elif not user.is_authenticated:
         return redirect ("homepage")
    
      user = request.user
      is_coordinator = False
      if user.is_authenticated: 
         if user.role == Accounts.Role.Coordinator :
            is_coordinator = True

      context ['thesis'] = thesis
      context ['is_coordinator'] = is_coordinator

   return render(request, 'assignment2_app/notification.html', context)

#change password

class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('homepage')
    template_name = 'assignment2_app/change_password.html'

def base(request, *args, **kwargs):
   
   user_id = kwargs.get("user_id") 
   

def Requests (request, tid):
   
   thesis = Project.objects.all()
   thesis_selected = None

   for topics in thesis:
      if topics.tid == tid:
         thesis_selected = topics
         break
         
   user = request.user
   is_coordinator = False
   if user.is_authenticated: 
      if user.role == Accounts.Role.Coordinator :
         is_coordinator = True

   page_data = {
      'thesis': thesis_selected,
      "is_coordinator" : is_coordinator
   }

   if request.method == 'POST':
      if request.POST.get("Approve"):
         for i in Project.objects.all():
             if i.is_approved == False and i.is_request == True and i.tid == tid:
               i.is_approved = True
               i.is_request = False
               i.save()
         return HttpResponseRedirect('/')
         
      elif request.POST.get("Decline"):
         for i in Project.objects.all():
            if i.is_approved == False and i.is_request == True and i.tid == tid:
                  i.delete()
         return HttpResponseRedirect('/')
   
                                                                                                      
   return render(request, 'assignment2_app/request.html', page_data)
