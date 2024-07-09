# class Dog:
#    def __init__(self, name, breed):
#       self.name=name
#       self.breed=breed
#    def brak(self):
#       return "Haw Haw"
   
# dog1=Dog("Belechu", "this is the greatest dog")
# dog2=Dog("Faro","The oldest germnay dog")
# print(f"{dog1.name} is {dog1.breed} is {dog1.brak()}")
# print(f"{dog2.name} is {dog2.breed} is {dog2.brak()}")


# class Animal:
#     def __init__(self, name):
#         self.name=name

#     def speak(self):
#         pass
# class lion(Animal):
#     def speak(self):
#         return f"{self.name} lion said towor"
# class Elephane(Animal):
#     def speak(self):
#         return f"{self.name} elephant said maw"
    
# z00=[
#     lion("black_lion"),
#    Elephane("The tallest")]
# for animals in z00:
#     print(f"{animals.speak()}")



# class Studet:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def studentInformation(self):
#         return f"{self.name} is {self.age}"
# class grade10(Studet):
#      def studentInformation(self):
#          return f"{self.name} is {self.age}"
# class grade12(Studet):
#     def studentInformation(self):
#         return f"{self.name} is {self.age}"

# students=[
#           grade10("kebede",15),
#           grade12("almaz",21)]
# for Stude in students:
#         print(Stude.studentInformation())
        
        

# class Product:
#     def __init__(self,name, price, quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#     def quantity(self):
#         result=self.price*self.quantity
#         return f"{self.name} price is {result} for quntity of {self.quantity}"
# mango= Product("mango",120,2)
# papye=Product("papaye",200,4)
# print(mango.quantity())
# print(papye.quantity())

class Student:
    def __init__(self,name ,age):
        self.name=name
        self.age=age

    def student_info(self):
        print(f"{self.name} is {self.age} years old")
    
stu1=Student("kebede",20)
stu2=Student("lema",21)
stu3=Student("tolosa",90)
stu4=Student("yared",24)

stu1.student_info()
stu2.student_info()
stu3.student_info()
stu4.student_info()
print("_"*40)


class Product:
    total=0
    def __init__(self,name,price, quality):
        self.name=name
        self.price=price
        self.quantity=quality
    def product_name(self):
    
        return f"{self.name}"
    def mango(self):
        total=self.price*self.quantity
        print(total)
    def orange(self):
        total1=self.price*self.quantity
        print(total1)
    # def total_price(self):
    #     total_sum=total+total1
    #     print(total_sum)
mango1=Product("mango",120,100)
orang=Product("orange",200,25)
mango1.product_name()
mango1.mango()
orang.orange()
# mango1.total_price()
orang.product_name()
# orang.total_price()
print("_"*40)

class BankAccount:
    def __init__(self ,owner ,number, balance,):
        self.owner=owner
        self.number=number
        self.balance=balance
    def account_owner(self):
        print("The customer Information")
        print("_"*40)
        print(f"{self.owner}")
        print(f"{self.number}")
        print(f"{self.balance}")
        print("_"*40)
    def deposite(self, amount):
        self.balance+=amount
        return f"{self.balance} is inserted successfully"
    def transfer(self, amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"{amount} birr is transfered,remained amount is {self.balance}")
    def withdraw(self, amount):
            if self.balance>amount:
                self.balance-=amount
                print(f"{self.balance} is left, you withdraw {amount}")
            else:
                print("insufficient amount you asked !")
    def checkbalance(self):
           print(self.balance)
kebede=BankAccount("kebede","0904324561",2000)
kebede.account_owner()
print(kebede.deposite(500))
kebede.checkbalance()
kebede.deposite(3000)
kebede.withdraw(5500)
kebede.checkbalance()
kebede.transfer(1000)

        

        



        
    
       