#
# class German:
#     print("luti")
#     def __init__(self): #constructor
#         self.height = 160
#         print("German :Sunglasses:")
# first_german = German()
#
# print(first_german.height)

# class Student:
#     amount_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students += 1
#
# german = Student()
# sasha = Student(height = 158)
# print(german.height)
# print(sasha.height)
# print(german.amount_of_students)









import random
class Student:
    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True #dead inside
    def to_study(self):
        print("Time to study")
        self.progress += 0.20
        self.gladness -= 3
    def to_sleep(self):
        print("Time to rest")
        self.gladness += 3
    def to_chill(self):
        print("time to play")
        self.gladness += 20
        self.progress -= 0.1
    def is_alive(self):
        if self.progress < -0.5:
            print("cast out")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...(ditki uchitesa)")
            self.alive = False
        elif self.progress > 5:
            print("Passed extern")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress {round(self.progress, 2)}")
    def live(self, day):
        day = "Day" + str(day) + "of  " + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_chill()
        elif live_cube == 3:
            self.to_sleep()
            self.end_of_day()
            self.is_alive()
German = Student(name="Nick")
for day in range(365):
    if German.alive == False:
        break
    German.live(day)












