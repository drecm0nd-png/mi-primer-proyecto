class User :

  def __init__(self, name):
    self.name = name

  def view_name (self):
    print (f'Hello mi name is {self.name}')

user_one = User('Damian')
user_one.view_name()
