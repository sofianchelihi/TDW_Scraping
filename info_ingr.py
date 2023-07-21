import random
r = open("insert.txt", "a",encoding="utf-8")
for i in range(50):
    for j in range(3):
        r.write("("+str(i+1)+","+str(j+1)+",'2023-01-03',"+str(random.randint(0,10))+"),\n")