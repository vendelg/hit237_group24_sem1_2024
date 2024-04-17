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

## making the homepage class below - VG
class homepage:
   def __init__(self, messages):
      self.messages = messages
      