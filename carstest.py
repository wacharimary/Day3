class Car(object):
  

 def __init__(self, name='General', model='GM', car_type=None):
    self.name = name
    self.model = model
    self.car_type = car_type
    self.speed = 0

    if self.name in ['Porshe', 'Koenigsegg']:
        self.num_of_doors = 2
    else:
        self.num_of_doors = 4

    if self.car_type == 'trailer':
        self.num_of_wheels = 8
    else:
        self.num_of_wheels = 4
      
def is_saloon(self):
    if self.car_type is not 'trailer':
        return False
        self.car_type == 'saloon'
        return True
      

def speed(self, spd):
    if self.car_type == 'trailer':
        self.speed = spd * 11
    else:
        self.speed = 10 ** spd
        return self
 

