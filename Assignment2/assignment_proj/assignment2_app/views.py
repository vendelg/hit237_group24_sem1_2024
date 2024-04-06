from django.shortcuts import render

# Create your views here.




########################################################################

# Function to create lists :



def create_members():
   
   list = []
   
   list.append(Member( 'assignment2_app/images/VendalPlH.png' ,'Leader',
                      'Vendal Gomes',
                      's321266',
                      'Bachelor of IT'))
   
   list.append(Member( 'assignment2_app/images/LouisPlH.png','Scribe',
                      'Louis Bajarias',
                      's366704',
                      'Bachelor of IT'))
   
   list.append(Member('assignment2_app/images/AimanPlH.png','Presenter',
                      'Syarif Aiman Lubis',
                      's362319',
                      'Bachelor of IT'))
   
   list.append(Member( 'assignment2_app/images/JamesPlH.png','Editor',
                      'James Paul',
                      's343288',
                      'Bachelor of Computer Science'))
   
   list.append(Member( 'assignment2_app/images/MiguelPlH.png','Timekeeper',
                      'Miguel Lalim',
                      's323016',
                      'Bachelor of Computer Science'))
   
   return list

def thesis_topics():
   the_topics = []

   the_topics.append(Thesis(1, 'As we use internet more, the data produced by us is enormous. But are these data being secure? The goal of applying machine learning or intelligence is to better risk modelling and prediction and for an informed decision support. Students will be working with either supervised or unsupervised machine learning approaches to solve the problem/s in the broader areas of Cyber Security.',
                              'Machine learning approaches for Cyber Security',
                  'As we use internet more, the data produced by us is enormous. But are these data being secure?.',
                  'Bharanidharan Shanmugam', ))
   the_topics.append(Thesis(9, 'Informetric studies are concerned with the quantitative aspects of information. The applications of advanced machine learning, information retrieval, network science and bibliometric techniques on various information artefacts have contributed fresh insights into the evolutionary nature of research fields. This project aims at discovering informetric properties of multidisciplinary research literature using various machine learning, network analysis, data visualisation and data wrangling tools.',
                           'Informetrics applications in multidisciplinary domain',
                  'Informetrics studies are concerned with the quantitative aspects of information. The applications of advanced machine learning, information retrieval, network science and bibliometric techniques on various information artefact have contributed fresh insights into the evolutionary nature of research fields.',
                  'Yakub Sebastian', ))
   the_topics.append(Thesis(16,'A virtual reality system could be used to objectively test the binaural hearing ability of humans (the ability to hear stereo and locate the direction and distance of sound). This project aims to design, implement and evaluate a VR system using standard off-the-shelf components (VR goggle and headphones) and standard programming techniques.',
                           'Development of a Virtual Reality System to Test Binaural Hearing',
                  'A virtual reality system could be used to objectively test the binaural hearing ability of humans (the ability to hear stereo and locate the direction and distance of sound).',
                  'Sami Azam' ))
   the_topics.append(Thesis(41, 'Cryptomining is the process of mining crypto currencies by running a sequence of algorithms. Traditionally, to mine new crypto coins, a person (or group of people) would buy expensive computers and spend a lot of time and money running them to perform the difficult calculations to generate crypto coins. Some website owners have started taking a different approach; they have put the software which runs those difficult calculations into their websites Javascript. This then causes the computers belonging to the visitors of their website to run those calculations for them, instead of running them themselves. In other words, when you visit a website with an embedded crypto-miner in it, your computer and electricity is used to try to generate crypto-coins for the owners of that website. Although there are various measures being applied to stop these illegitimate minings, the trend is still increasing. This research aims to find out potential gaps in current methodologies and develop a solution that can fulfil the gap. It also aims to find out:',
                            'Current trends on cryptomining and its potential impact on cryptocurrencies',
                  'Cryptomining is the process of mining crypto currencies by running a sequence of algorithms. Traditionally, to mine new crypto coins, a person (or group of people) would buy expensive computers and spend a lot of time and money running them to perform the difficult calculations to generate crypto coins',
                  'Sami Azam', ))

   the_topics.append(Thesis(176,'The project aims to use multiple publicly available health datasets to formulate a different dataset that may have features from the original set along with new ones developed through feature engineering. The dataset will then be used to build predictive model based on both general and deep learning based algorithms. The findings will be analysed and compared to similar research works. ', 
                            'Artificial Intelligence in Health Informatics',
                  'The project aims to use multiple publicly available health datasets to formulate a different dataset that may have features from the original set along with new ones developed through feature engineering',
                  'Asif Karim', ))
   the_topics.append(Thesis(180, 'The proposed system will present a two-cluster solution from a given dataset which will group toddlers based on multiple common medical traits. In depth literature survey of similar studies, both supervised and unsupervised will be carried out before the cluster-based model is implemented. The solution will be validated using both External and Internal validation measures and statistical significance tests.',
                            'Unsupervised Model Development from Autism Screening Data ',
                  'The proposed system will present a two-cluster solution from a given dataset which will group toddlers based on multiple common medical traits. In depth literature survey of similar studies, both supervised and unsupervised will be carried out before the cluster-based model is implemented.',
                  'Asif Karim', ))
   the_topics.append(Thesis(226, 'Artificial Intelligence has been used in many applications to solve certain problems through out the academia and the industry – from electricity to writing text. AI has a multitude of applications and this project will pick up a problem and explore the applications of AI with minimal human intervention. Examples of applications include -building a bot, predicting the power usage, spam filtering and the list is endless.',
                            'Applying Artificial Intelligence to solve real world problems',
                  'Artificial Intelligence has been used in many applications to solve certain problems through out the academia and the industry from electricity to writing text.',
                  'Bharanidharan Shanmugam', ))

   return the_topics


#########################################################################


# These are the classes:


class Member:
   def __init__(self, image, role, name, student_id, course):
      
      self.image = image
      self.role = role
      self.name = name
      self.student_id = student_id
      self.course = course

class Thesis:
   def __init__(self, id, text, title, desc, sup_name):
      self.id = id
      self.text = text
      self.title = title
      self.desc = desc
      self.sup_name = sup_name
      
########################################################################

# Requests:

def page2(request):


   proj_context = { 
     "proj_list" : thesis_topics,
   }                          
                                                                                                         
   return render(request, 'assignment2_app/page2.html', proj_context)


def about(request):
   
   context = {
      'list': create_members,
   }
   
   return render(request, 'assignment2_app/about.html', context)



def show_thesis_topic(request, thesisid):

   thesis = thesis_topics()

   thesis_selected = None

   for topics in thesis:
      if topics.id == thesisid:
         thesis_selected = topics
         break
         
   
   context = {
      'thesis': thesis_selected,
   }

   return render(request, 'assignment2_app/page3.html', context)







