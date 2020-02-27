class Transformer:
  def __init__(self, name, speed):
    self.name = name
    self.speed = speed

  def sayname(self):
   print("O my God")
  def myname(self):
   print("I am " + self.name)

class Autobot (Transformer):
    honor = 0
    x = '0'
    def sayname2(self):
        if self.name == 'Optimus':
            print('Yes, my name Optimus!')
            self.whoiam = False
        else:
            print('No, thanks!')

    def smeth(x):
        print(x)
    smeth = staticmethod(smeth)

    def smeth2(x):
        print(x)
    smeth2 = classmethod(smeth2)



Prime = Autobot("Optimus", 55)

Kal = Transformer("kal", 25)
print(Kal.name)
Prime.smeth('olololo')
Prime.smeth2()
Prime.myname()
Prime.sayname2()
print(Prime.honor)
print(Prime.name)
print(Prime.speed)
Kal.sayname()



