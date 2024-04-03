from django.shortcuts import render

# Create your views here.




########################################################################

# Function to create lists :



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


def create_proj():

   proj_list = []

   proj_list.append(Projects('Machine learning approaches for Cyber Security',
                  'As we use internet more, the data produced by us is enormous. But are these data being secure?.',
                  'Bharanidharan Shanmugam', 
                  1))
   proj_list.append(Projects('Informetrics applications in multidisciplinary domain',
                  'Informetrics studies are concerned with the quantitative aspects of information. The applications of advanced machine learning, information retrieval, network science and bibliometric techniques on various information artefact have contributed fresh insights into the evolutionary nature of research fields.',
                  'Yakub Sebastian', 
                  9))
   proj_list.append(Projects('Development of a Virtual Reality System to Test Binaural Hearing',
                  'A virtual reality system could be used to objectively test the binaural hearing ability of humans (the ability to hear stereo and locate the direction and distance of sound).',
                  'Sami Azam', 
                  16))
   proj_list.append(Projects('Current trends on cryptomining and its potential impact on cryptocurrencies',
                  'Cryptomining is the process of mining crypto currencies by running a sequence of algorithms. Traditionally, to mine new crypto coins, a person (or group of people) would buy expensive computers and spend a lot of time and money running them to perform the difficult calculations to generate crypto coins',
                  'Sami Azam', 
                  41))
   proj_list.append(Projects('Artificial Intelligence in Health Informatics',
                  'The project aims to use multiple publicly available health datasets to formulate a different dataset that may have features from the original set along with new ones developed through feature engineering',
                  'Asif Karim', 
                  176))
   proj_list.append(Projects('Unsupervised Model Development from Autism Screening Data ',
                  'The proposed system will present a two-cluster solution from a given dataset which will group toddlers based on multiple common medical traits. In depth literature survey of similar studies, both supervised and unsupervised will be carried out before the cluster-based model is implemented.',
                  'Asif Karim', 
                  180))
   proj_list.append(Projects('Applying Artificial Intelligence to solve real world problems',
                  'Artificial Intelligence has been used in many applications to solve certain problems through out the academia and the industry from electricity to writing text.',
                  'Bharanidharan Shanmugam', 
                  226))
   
   return proj_list


#########################################################################


# These are the classes:

class Projects:
   def __init__(self, title, desc, sup_name, proj_num) :
      self.title = title
      self.desc = desc
      self.sup_name = sup_name
      self.proj_num = proj_num


class Member:
   def __init__(self, role, name, student_id, course):
      
      self.role = role
      self.name = name
      self.student_id = student_id
      self.course = course


########################################################################

# Requests:

def page2(request):


   proj_context = { 
     "proj_list" : create_proj,
   }                          
                                                                                                         
   return render(request, 'assignment2_app/page2.html', proj_context)





def about(request):
   
   context = {
      'list': create_members,
   }
   
   return render(request, 'assignment2_app/about.html', context)



