import random
import math

class Person():
    def __init__(self,id):
        self.id = id
        self.x = random.uniform(0,100)
        self.y = random.uniform(0,100)
        self.choose()
    def choose(self):
        while True:
            self.a = random.randint(0,3)
            if self.a!=self.id:
                break
            else:
                print("a ve id eşit çıktı",self.id,self.a)
        print("id: ",self.id)   
        print("a: ",self.a)  
        while True:
            self.b = random.randint(0,3)
            if self.b!=self.id and self.a!=self.b:
                break
            elif self.id==self.b:
                print("b ve id eşit çıktı",self.id,self.b)
            else:
            
                print("b ve a eşit çıktı",self.a,self.b)
        print("id: ",self.id)   
        print("b: ",self.b)
    def move(self):
        slope = (persons[self.a].y - persons[self.b].y) / (persons[self.a].x - persons[self.b].x)
        middle_x = (persons[self.a].x + persons[self.b].x) / 2
        middle_y = (persons[self.a].y + persons[self.b].y) / 2
        print("middle:", middle_x, middle_y)
        print("ilk konum:",persons[self.id].x, persons[self.id].y)
        # P noktasından orta noktaya giden vektörü hesaplayalım
        vector_x = middle_x - self.x
        vector_y = middle_y - self.y
        
        # Bu vektörün birim vektörünü hesaplayalım
        magnitude = math.sqrt(vector_x**2 + vector_y**2)
        unit_v_x = vector_x / magnitude
        unit_v_y = vector_y / magnitude
        
        # P noktasını bu birim vektör boyunca istediğimiz adım kadar taşıyalım
        # Burada adım büyüklüğünü 1 olarak alıyoruz (P'nin tam orta noktaya gitmesi için)
        step = 1
        new_p_x = self.x + unit_v_x * step
        new_p_y = self.y + unit_v_y * step
        new_p = (new_p_x, new_p_y)
        self.x = new_p_x
        self.y = new_p_y

        print(self.id, " kişisinin yeni konumu:", new_p)
        
persons=[]
for i in range (4):
    persons.insert(i,Person(i))
print(persons[2].x)

for i in range(10):
    for person in persons:
        person.move()
        print(person.x)

 
 