from django.shortcuts import render
from assignment2_app.data import *
from .models import Project
from .forms import ThesisForm
from django.http import HttpResponseRedirect
from django.urls import reverse
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
         save_new_thesis(form)
         return HttpResponseRedirect(reverse('homepage'))
      else:
         page_data = { 'val_errors': form.errors, }
   
   return render(request, app_name + 'done.html', page_data)

def save_new_thesis(form):   # Step 3
   
   new_thesis_object = form.save()

def edit_thesis(request, key=1):   # Step 3
    
   # Fetch exixting publisher record from database
   thesis = Project.objects.get(id=int(key))
   
   if request.method == 'POST':
      
      form = ThesisForm(request.POST, instance=thesis)
      if form.is_valid() != True:
         page_data = {
               'thesisForm': form
         }
      else:   # Form is valid
         form.save()
         return HttpResponseRedirect(reverse('homepage'))
   
   else:         # GET request from entering URL
      
      form = ThesisForm(instance=thesis)
      page_data = {
         'thesisForm': form
      }
   
   return render(request, app_name + 'edit_thesis.html', page_data)

def delete_publisher(request,key):
    
    # Fetch exixting publisher record from database
    thesis = Project.objects.get(id=int(key))
    
    if request.method == 'POST':
        
        thesis.delete()
        
        return HttpResponseRedirect(reverse('homepage'))
    
    else:         # GET request from entering URL
        
        form = ThesisForm(instance=thesis)
        page_data = {
            'thesisForm': form
        }
    
    return render(request, app_name + 'edit_thesis.html', page_data)

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



def show_thesis_topic(request, TID):

   theses = Project.objects.all()

   thesis_selected = None

   for thesis in theses:
      if thesis.TID == TID:
         thesis_selected = thesis
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