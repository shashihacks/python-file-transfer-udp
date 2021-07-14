import csv
import pickle
import math
import random
def createRandom():
   data = [random.randint(-251264,-235328), 
          random.randint(1201041 ,1271041),
          random.randint(-1349478, -1149478),
     random.randint(-650808,-620808),
      random.randint(-696994,-656994), 
      random.randint(-515888,-485888), 
      random.randint(-200040,-190040),
       random.randint(-85725,-84725), 
       random.randint(31743,33743),
       random.randint(200326,210326),
       random.randint(-1066881,-966881),
         random.randint(-650808,-620808),
          random.randint(-32504,-31504),
         random.randint(-909417,-899417), 
          random.randint(-1349478, -1149478)]
   with open('eeg.csv', 'w', encoding='UTF8') as f:
       for x in range(500):
                writer = csv.writer(f)
                writer.writerow(data)


createRandom()

# print(random.randint(-251264,-235328))

# print(random.randint(1201041 ,1271041))

# print(random.randint(-1349478, -1149478))
# print(random.randint(-650808,-620808))
# print(random.randint(-696994,-656994))
# print(random.randint(-515888,-485888))
# print(random.randint(-200040,-190040))
# print(random.randint(-85725,-84725))
# print(random.randint(31743,33743))


