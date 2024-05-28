from django.shortcuts import render
from assignment2_app.data import *
from .models import Project, ThesisApplication, Student, Accounts
from .forms import ThesisForm, ApplicationForm, StudentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm 
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash 
from .models import Accounts


#Redirect
from django.shortcuts import redirect

#LoginForm
from . forms import LoginForm, AccAuthForm

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

# def thesis_topics():
#    the_topics = []

#    the_topics.append(Thesis(1, 'As we use internet more, the data produced by us is enormous. But are these data being secure? The goal of applying machine learning or intelligence is to better risk modelling and prediction and for an informed decision support. Students will be working with either supervised or unsupervised machine learning approaches to solve the problem/s in the broader areas of Cyber Security.',
#                               'Machine Learning Approaches for Cyber Security',
#                   'As we use internet more, the data produced by us is enormous. But are...',
#                   'Bharanidharan Shanmugam', ))
#    the_topics.append(Thesis(9, 'Informetric studies are concerned with the quantitative aspects of information. The applications of advanced machine learning, information retrieval, network science and bibliometric techniques on various information artefacts have contributed fresh insights into the evolutionary nature of research fields. This project aims at discovering informetric properties of multidisciplinary research literature using various machine learning, network analysis, data visualisation and data wrangling tools.',
#                            'Informetrics Applications in Multidisciplinary Domain',
#                   'Informetrics studies are concerned with the quantitative aspects of information. The applications of advanced machine learning, information retrieval, network science and bibliometric techniques on various information artefact have contributed fresh insights into...',
#                   'Yakub Sebastian', ))
#    the_topics.append(Thesis(16,'A virtual reality system could be used to objectively test the binaural hearing ability of humans (the ability to hear stereo and locate the direction and distance of sound). This project aims to design, implement and evaluate a VR system using standard off-the-shelf components (VR goggle and headphones) and standard programming techniques.',
#                            'Development of a Virtual Reality System to Test Binaural Hearing',
#                   'A virtual reality system could be used to objectively test the binaural hearing ability of...',
#                   'Sami Azam' ))
#    the_topics.append(Thesis(41, 'Cryptomining is the process of mining crypto currencies by running a sequence of algorithms. Traditionally, to mine new crypto coins, a person (or group of people) would buy expensive computers and spend a lot of time and money running them to perform the difficult calculations to generate crypto coins. Some website owners have started taking a different approach; they have put the software which runs those difficult calculations into their website's Javascript. This then causes the computers belonging to the visitors of their website to run those calculations for them, instead of running them themselves. In other words, when you visit a website with an embedded crypto-miner in it, your computer and electricity is used to try to generate crypto-coins for the owners of that website. Although there are various measures being applied to stop these illegitimate minings, the trend is still increasing. This research aims to find out potential gaps in current methodologies and develop a solution that can fulfil the gap. It also aims to find out: what type of crypto mining methodologies are being applied; apart from crypto-mining, what other security risks may it introduce, such as cryptojacking; and how current web standards are tackling this problem?',
#                             'Current Trends on Cryptomining and Its Potential Impact on Cryptocurrencies',
#                   'Cryptomining is the process of mining crypto currencies by running a sequence of algorithms. Traditionally, to mine new crypto coins, a person (or group of people) would buy expensive computers and spend a lot of time and money running them to perform the difficult...',
#                   'Sami Azam', ))

#    the_topics.append(Thesis(176,'The project aims to use multiple publicly available health datasets to formulate a different dataset that may have features from the original set along with new ones developed through feature engineering. The dataset will then be used to build predictive model based on both general and deep learning based algorithms. The findings will be analysed and compared to similar research works. ', 
#                             'Artificial Intelligence in Health Informatics',
#                   'The project aims to use multiple publicly available health datasets to formulate a different dataset that may have features from the original set along with new ones...',
#                   'Asif Karim', ))
#    the_topics.append(Thesis(180, 'The proposed system will present a two-cluster solution from a given dataset which will group toddlers based on multiple common medical traits. In depth literature survey of similar studies, both supervised and unsupervised will be carried out before the cluster-based model is implemented. The solution will be validated using both External and Internal validation measures and statistical significance tests.',
#                             'Unsupervised Model Development from Autism Screening Data ',
#                   'The proposed system will present a two-cluster solution from a given dataset which will group toddlers based on multiple common medical traits. In depth literature survey of similar studies...',
#                   'Asif Karim', ))
#    the_topics.append(Thesis(226, 'Artificial Intelligence has been used in many applications to solve certain problems through out the academia and the industry – from electricity to writing text. AI has a multitude of applications and this project will pick up a problem and explore the applications of AI with minimal human intervention. Examples of applications include -building a bot, predicting the power usage, spam filtering and the list is endless.',
#                             'Applying Artificial Intelligence to Solve Real World Problems',
#                   'Artificial Intelligence has been used in many applications to solve certain problems through out the academia...',
#                   'Bharanidharan Shanmugam', ))

#    return the_topics

def homemessages():
   messages = []

   messages.append(homepage('HIT237 Group 24 respectfully acknowledges the traditional custodians of the land on which we live and work in the Northern Territory, Australia. We pay our respects to the Aboriginal peoples, the traditional owners and custodians of this land, past, present, and emerging.', ))
   messages.append(homepage('This website was created for Charles Darwin University masters degree level Information Technology students who are looking to complete their theses. The website allows the students to be able to view all available thesis subjects and the teacher who will be the one to guide/support them throughout the length of their thesis. The website created will also allow users to see which lecturers are available to assist for different thesis subjects.', ))
   messages.append(homepage('The available theses can be found in the Thesis tab. The About Us page will show details about HIT237 Group 24.  This is standard across many different higher education institutes, with the lecturer contacts being provided to the student as well. This will allow them to contact the corresponding lecturer so they will be able to apply for a thesis that they would be interested in completion for their master’s in information technology degree.', ))

   return messages 

# Requests:
def view_thesis(request, tid):  # Step 2
   
   thesis = Project.objects.get(id=tid)
   
   page_data = {
      'thesis': thesis
   }
   
   return render(request, 'assignment2_app/view_thesis.html', page_data)

def add_thesis(request):
   
   page_data = {'thesisForm': ThesisForm(), }
   
   return render(request, app_name + 'add_thesis.html', page_data)

def add_thesis_submit(request):
   if request.method != 'POST':
      return HttpResponseRedirect('/add/thesis/')
   else:
      page_data = {}
      form = ThesisForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect(reverse('homepage'))
      else:
         page_data = { 'val_errors': form.errors, }
   
   return render(request, app_name + 'done.html', page_data)

def modify_thesis(request, tid):
   thesis = Project.objects.get(tid=int(tid))
   
   page_data = None

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

   return render(request, app_name + 'edit_thesis.html', page_data)


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
   
   page_data = {
      "theses": theses
   }
                                                                                                      
   return render(request, 'assignment2_app/page2.html', page_data)


def about(request):
   
   context = {
      'list': create_members,
   }
   
   return render(request, 'assignment2_app/about.html', context)



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

def home(request):
   

   home_context = {
      'homemessages' : homemessages,
   }

   return render(request, 'assignment2_app/homepage.html', home_context)


#LoginView
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

def thesis_application(request, tid):
   
   thesis = Project.objects.all()
   thesis_selected = None

   for topics in thesis:
      if topics.tid == tid:
         thesis_selected = topics
         break
         
   context = { 
     "application_form" : ApplicationForm(),
     "thesis" :thesis_selected,

   }                
   
   return render(request, 'assignment2_app/apply_thesis.html', context)

def application_submit(request):
   data = ThesisApplication.objects.all()
   
   if request.method != 'POST':
      return HttpResponseRedirect('apply/thesis')
   else:
      context = {
         'data' : data,

         }
      form = ApplicationForm(request.POST)

      if form.is_valid():
         save_application(form)
      else:
         context = {'val_errors': form.errors, }
         return HttpResponseRedirect('../../apply/thesis')
          
      
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


def notification(request, *args, **kwargs):

   context = {}
   user_id = kwargs.get("user_id")
   try:
      account=Accounts.objects.get(pk = user_id)
   except Accounts.DoesNotExist:
      return HttpResponse("That user does not exist")

   if account:
     
      user = request.user
      if user.is_authenticated and user != account:
         return redirect ("homepage")
      elif not user.is_authenticated:
         return redirect ("homepage")
      
      context ['user'] = account

   return render(request, 'assignment2_app/notification.html')

def change_password(request, user_id):  
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was updated')
            return redirect('profile', user_id=user_id)
        else:
            messages.error(request, 'error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'assignment2_app/change_password.html', {
        'form': form,
        'user': Accounts
    })

def base(request, *args, **kwargs):
   
   user_id = kwargs.get("user_id") 
      
   account=Accounts.objects.all(pk = user_id)
   
   
   context = {
      'user' : account ,
      
   }

 
      
   return render(request, context)
   