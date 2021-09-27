#!/usr/bin/env python
# coding: utf-8

# In[7]:


a = 2
a = 4
a = 6
print(a + a + a)

#ans=18


# In[8]:



a = 1
_a = 2
_a2 = 3
2a = 4

#2a dec is wrong


# In[6]:



a = 1
b = 2
print(a == b)
print(b == c)
#c is not defined


# In[3]:



a = "1"
b = 2
print(b + int(a))
#case a as int


# In[4]:


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[1])


# In[5]:


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[3:6])


# In[9]:


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[:3])


# In[10]:


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-2])


# In[14]:


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-3:])


# In[12]:


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[::2])


# In[20]:


print([i for i in range(21)])


# In[19]:


my_range = range(1, 21)
print([item*10 for item in my_range])


# In[24]:


my_range = range(1, 21)
print(list(map(str,my_range)))


# In[25]:


a = ["1", 1, "1", 2]
s=set(a)
print(list(s))


# In[30]:


a={'a':1,'b':2}
a


# In[33]:


d = {"a": 1, "b": 2}
print(d.get('b'))


# In[34]:


d = {"a": 1, "b": 2, "c": 3}
print(d['a']+d['b'])


# In[ ]:


d = {"Name": "John", "Surname": "Smith"}
#print(d["Smith"])
#print(d["Surname"])


# In[35]:


d = {"a": 1, "b": 2}
d['c']=3
print(d)


# In[40]:


d={'a': 1, 'b': 2, 'c': 3}
a=d.values()
print(type(a))
sum(d.values())


# In[54]:


d={'a': 1, 'b': 2, 'c': 3}
c={k:v for (k,v) in d.items() if v==1}
print(c)


# In[59]:


from pprint import pprint
d={}
d['a']=list(range(10))
d['b']=list(range(11,21))
d['c']=list(range(21,31))
pprint(d)


# In[64]:


from pprint import pprint
 
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

pprint(d)
print(d['b'][2])


# In[70]:


d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
for k,v in d.items():
    print(f"{k} has value of {v}")


# In[76]:



# import string library function 
import string 
for letter in string.ascii_lowercase:
    print(letter)


# In[78]:


for i in range(11):
    print(i)


# In[79]:


def acc(v1,v2,t1,t2):
    return (v2-v1)/(t2-t1)
print(acc(0, 10, 0, 20))


# In[81]:


def foo(a, b):
  #  print(a + b) not correct need to return 
    return a+b

 
x = foo(2, 3) * 10
print(x)


# In[87]:


from math import pi
def sphereFill(h,r=10):
    return ((4*pi*r**3)/3)-((pi*h**2*(3*r-h)/3))
print(sphereFill(2))


# In[88]:


#def foo(a=2, b): put default params atlast
def foo( b,a=2):
    return a + b


# In[89]:


def foo(a=1, b=2):
    return a + b
 
#x = foo - 1 foo has to be called with ()
x = foo() - 1
print(type(foo))


# In[90]:


c = 1
def foo():
    return c
c = 3
print(foo())


# In[91]:


c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())


# In[103]:


def foo(): 
   global e
   e = 1 
   return e 
foo() 
print(e)


# In[105]:


def splitToWords(a):
    return len(a.split(" "))
print(splitToWords("How are you"))
    


# In[115]:


def countWordsInFile(filePath):
    with open(filePath) as f:
        print(len(f.read().split()))
countWordsInFile("/Users/callisto/Downloads/words1.txt")


# In[118]:


def countWordsInFile(filePath):
    with open(filePath) as f:
        print(len(f.read().replace(","," ").split()))
countWordsInFile("/Users/callisto/Downloads/words1.txt")


# In[119]:


import math
math.sqrt(9) # import math was missing


# In[132]:


import math
print(dir(math))
print(help(math.cos))
print(math.cos(1))


# In[135]:


import math
print(help(math.pow))
print(math.pow(3,2))


# In[156]:


with open("/Users/callisto/Downloads/words2.txt","w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter+"\n")
print(string.ascii_lowercase)
print(help(string.ascii_lowercase))


# In[165]:



a = [1, 2, 3]
b = (4, 5, 6)
for a,b in zip(a,b):
    print(a+b)


# In[182]:


a=string.ascii_lowercase[::2]
b=string.ascii_lowercase[1::2]
with open("/Users/callisto/Downloads/words3.txt","w") as file:
       for a,b in zip(a,b):
            print(a+b)
            file.write(a+b+"\n")


# In[193]:


a=string.ascii_lowercase[::3]
b=string.ascii_lowercase[1::3]
c=string.ascii_lowercase[2::3]+" " 
print(a)
print(b)
print(c)
with open("/Users/callisto/Downloads/words4.txt","w") as file:
       for a,b,c in zip(a,b,c):
            print(a+b+c)
            file.write(a+b+c+"\n")


# In[200]:


import os
  
for letter in string.ascii_lowercase:
        filename = "/Users/callisto/Downloads/alphabets/"+letter+".txt"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(letter)


   


# In[216]:


import os

l=os.listdir("/Users/callisto/Downloads/alphabets/")
l.sort()
a=[]
for file in l:
    with open("/Users/callisto/Downloads/alphabets/"+file,"r") as f:
        a.append(f.read())
print(a)


# In[224]:


import glob

searchText="python"
files=glob.glob("/Users/callisto/Downloads/alphabets/*.txt")
files.sort()
a=[]
for file in files:
    with open(file,"r") as f:
        text=f.read()
        if text in searchText:
            a.append(text)
print(a)


# In[226]:


for letter in "Hello":
    if letter == "e":
        print(letter)


# In[ ]:


pass = input("Please enter your password: ")  # cannot use pass as variable as it is a reserved keyword


# In[228]:


age = int(input("What's your age? "))
age_last_year = age - 1
print("Last year you were %s." % age_last_year)


# In[230]:


print(type("Hey".replace("ey","i")[-1]))


# In[237]:


firstname = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is %s and your second name is %s" %(firstname, secondname))


# In[239]:


d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
print(d["employees"][1]["lastName"])


# In[241]:


d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
d["employees"][1]["lastName"]="smooth"
print(d)


# In[244]:


d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
d["employees"].append({"firstName": "Vinay", "lastName": "k"})
pprint(d)


# In[283]:


import json
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

with open("/Users/callisto/Downloads/jsonfrompython.txt","w") as f:
        json.dump(d,f)


# In[273]:


import json
with open("/Users/callisto/Downloads/jsonfrompython.txt","r") as f:
         pprint(json.load(f))


# In[284]:


import json
with open("/Users/callisto/Downloads/jsonfrompython.txt","r+") as f:
         d=json.load(f)
         d['employees'].append({'firstName': 'Vinay', 'lastName': 'k'})
         pprint(d)
         f.seek(0)
         json.dump(d,f)


# In[289]:


a = [1, 2, 3]
for c,d in enumerate(a):
    print(f"item {d} has index {c}")


# In[291]:


while(True):
    print('hello')


# In[297]:


import time
for i in range(10):
    time.sleep(2)
    print("hello")


# In[298]:


import time
for i in range(10):
    print("hello")
    time.sleep(i)
    


# In[301]:


import time
for i in range(10):
    print("hello")
    time.sleep(i)
    if(i==3):
        break
print("End of Loop")


# In[304]:


while True:
    print("Hello")
    if(2>1):
        pass
    print("Hi")


# In[305]:


while True:
    print("Hello")
    if(2>1):
        continue
    print("Hi")


# In[308]:


i=input("enter a word to translate!!")
d = dict(weather = "clima", earth = "terra", rain = "chuva")
print(d[i])


# In[310]:


i=input("enter a word to translate!!")
d = dict(weather = "clima", earth = "terra", rain = "chuva")
try:
    print(d[i])
except:
    print("word doesnt exist")
    


# In[313]:


i=input("enter a word to translate!!").lower()
d = dict(weather = "clima", earth = "terra", rain = "chuva")
try:
    print(d[i])
except:
    print("word doesnt exist")
    


# In[314]:


import requests
 
headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pythonhow.com", headers = headers)
print(r.text[:100])


# In[340]:


import requests

response=requests.get("http://www.pythonhow.com/data/universe.txt",headers={"user-agent":"check"})
print(response.text)
#with open("/Users/callisto/Downloads/universe.txt","w") as f:
 #   f.write(response.text)


# In[344]:


import requests

response=requests.get("http://www.pythonhow.com/data/universe.txt",headers={"user-agent":"check"})
print(response.text.count("a"))
#with open("/Users/callisto/Downloads/universe.txt","w") as f:
 #   f.write(response.text)


# In[348]:


import webbrowser
i=input("Enter the search term!!!")
webbrowser.open('http://www.google.com/search?q='+i)


# In[379]:


import requests
import pandas as pd
'''response=requests.get("http://www.pythonhow.com/data/sampledata.txt",headers={"user-agent":"check"})
response1=requests.get("http://www.pythonhow.com/data/sampledata_x_2.txt",headers={"user-agent":"check"})
#http://pythonhow.com/data/sampledata_x_2.txt
print(response.text)
print(response1.text)
with open("/Users/callisto/Downloads/pandascheck.txt","w") as f:
    f.write(response.text)
with open("/Users/callisto/Downloads/pandascheck1.txt","w") as f:
    f.write(response1.text)
    
df=pd.read_csv("/Users/callisto/Downloads/pandascheck.txt")
df1=pd.read_csv("/Users/callisto/Downloads/pandascheck1.txt")
dfconcat=pd.concat([df,df1])
dfconcat.to_csv("/Users/callisto/Downloads/pandascheckconcat.txt")'''

#print(help(df.to_csv))

#above code can be rewritten like this:
df=pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
df1=pd.read_csv("http://www.pythonhow.com/data/sampledata_x_2.txt")
dfconcat=pd.concat([df,df1])
dfconcat.to_csv("/Users/callisto/Downloads/pandascheckconcat1.txt")




# In[382]:


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
print(df)
df.plot(x='x', y='y', kind='scatter')
plt.show()


# In[394]:


import datetime
x=datetime.datetime.now()
print(x.strftime("%A %B %d %Y"))


# In[400]:


from datetime import datetime,timedelta
i=int(input("Enter your age!!"))

currentDate=datetime.now()
birthyear=currentDate-timedelta(days=i*365)
print(str(birthyear.year))


# In[410]:


import random
a=string.ascii_letters+string.digits
print("".join((random.sample(a,10))))


# In[426]:


def passwordChecker(password):
    flag=flag1=False;
    for item in password:
        if(item.isdigit()):
            flag =True
        if(item.isupper()):
            flag1=True
    return flag and flag1 and len(password)>5
        
i=input("Enter new password!!")
if(passwordChecker(i)):
    print("Correct")
else:
    print("Wrong")


# In[431]:


while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)
   


# In[434]:


i=input("Enter Username:")
l=["test","test1","test2"]
if(i in l):
    print("User Exists")
else:
    while True:
        notes = []
        psw = input("Enter password: ")
        if not any(i.isdigit() for i in psw):
            notes.append("You need at least one number")
        if not any(i.isupper() for i in psw):
            notes.append("You need at least one uppercase letter")
        if len(psw) < 5:
            notes.append("You need at least 5 characters")
        if len(notes) == 0:
            print("Password is fine")
            break
        else:
            print("Please check the following: ")
            for note in notes:
                print(note)


# In[436]:


import ephem
jupiter = ephem.Jupiter()
jupiter.compute('1230/1/1')
distance_au_units = jupiter.sun_distance
distance_km = distance_au_units * 149597870.691
print(distance_km)


# In[454]:


import screeninfo
print(dir(screeninfo))
m=screeninfo.get_monitors()
print(help(m))
for mon in m:
   print(str(mon.width)+" "+str(mon.height))


# In[455]:


import pyglet
window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
@window.event
def on_draw():
    window.clear()
    label.draw()
    
pyglet.app.run()


# In[480]:



with open("/Users/callisto/Downloads/countries_raw.txt","r") as f:
    print(f.readlines())
#write the logic using list comprehension
   
    


# In[490]:


checklist = ["Portugal", "Germany", "Munster", "Spain"]
with open("/Users/callisto/Downloads/countries_clean.txt","r") as f:
        s=f.read()
        checklist=[item for item in checklist if item in s]
print(checklist)


# In[501]:


checklist = ["Portugal", "Germany", "Spain"]
with open("/Users/callisto/Downloads/countries_missing.txt","r+") as f:
        s=f.readlines()
        s=s+[item+"\n" for item in checklist]
        s.sort()
        print(str(s))
        f.seek(0)
        for i in s:
            f.write(i)
        


# In[522]:


import pandas as pd
#with open("/Users/callisto/Downloads/countries_by_area.txt","r") as f:
df=pd.read_csv("/Users/callisto/Downloads/countries_by_area.txt")
df['dense']=df['population_2013']/df['area_sqkm']
df = df.nlargest(5, "dense")
print(df)


# In[554]:


import sqlite3
  
connection = sqlite3.connect('/Users/callisto/Downloads/database.db')
cursor = connection.cursor()
  
# WHERE CLAUSE TO RETRIEVE DATA
cursor.execute("SELECT country FROM countries where area > '2000000'")
data=cursor.fetchall()
# printing the cursor data
for item in data:
    print(item[0])
  
connection.commit()
connection.close()


# In[542]:


import sqlite3
import pandas as pd
  
connection = sqlite3.connect('/Users/callisto/Downloads/database.db')
cursor = connection.cursor()
  
# WHERE CLAUSE TO RETRIEVE DATA
cursor.execute("SELECT * FROM countries where area > '2000000'")
data=cursor.fetchall()
df =pd.DataFrame.from_records(data)
df.columns=['Rank','Country','Area','Population']
df.to_csv('/Users/callisto/Downloads/countries.csv',index=False)
print(df)
connection.commit()
connection.close()


# In[568]:


import sqlite3
import pandas as pd
   
df=pd.read_csv("/Users/callisto/Downloads/ten_more_countries.txt")
#print(df)
connection = sqlite3.connect('/Users/callisto/Downloads/databaseins.db')
cursor = connection.cursor()
sql = ''' INSERT INTO countries('ID','Country','Area','population')
              VALUES(?,?,?,?) '''
for _,i in df.iterrows():
    print(i['ID'],i['Country'],i['Area'])
    cursor.execute(sql, (i['ID'],i['Country'],i['Area'],'null'))


connection.commit()
connection.close()


   
    


# In[570]:


import glob
l=glob.glob("/Users/callisto/Downloads/files/*.py")
print(len(l))


# In[574]:


import glob
l=glob.glob("/Users/callisto/Downloads/subdirs/**/*.py",recursive=True)
print(len(l))


# In[578]:


with open("/Users/callisto/Downloads/urls.txt","r") as f:
    s=f.readlines()
    for i in s:
        i=i.replace("s","",1)
        i=i[:5]+"/"+i[5:]
        print(i)
    


# In[582]:


i=input("enter planets comma seperated!!!")
i=i.split(",")
with open("/Users/callisto/Downloads/comma.txt","w") as f:
    for item in i:
        f.write(item+"\n")


# In[586]:


with open("/Users/callisto/Downloads/repeat.txt","w") as f:
    while(True):
        i=input("Enter CLOSE to terminate:")
        if(i=="CLOSE"):
            break
        else:
            f.write(i+"\n")


# In[593]:


f= open("/Users/callisto/Downloads/repeat.txt","a+")
l=[]
while(True):
    i=input("Enter CLOSE to terminate and SAVE to save:")
    l.append(i)
    if(i=="SAVE"):
        f= open("/Users/callisto/Downloads/repeat.txt","a+")
        for item in l:
            f.write(item+"\n")
        f.close()

    if(i=="CLOSE"):
        f= open("/Users/callisto/Downloads/repeat.txt","a+")
        for item in l:
            f.write(item+"\n")
        f.close()
        break


# In[1]:


from tkinter import *
 
window = Tk()
 
file = open("user_gui.txt", "a+")
 
def add():
    file.write(user_value.get() + "\n")
    entry.delete(0, END)
 
def save():
    global file
    file.close()
    file = open("user_gui.txt", "a+")
 
def close():
    file.close()
    window.destroy()
 
user_value = StringVar()
entry = Entry(window, textvariable=user_value)
entry.grid(row=0, column=0)
 
button_add = Button(window, text="Add line", command=add)
button_add.grid(row=0, column=1)
 
button_save = Button(window, text="Save changes", command=save)
button_save.grid(row=0, column=2)
 
button_close = Button(window, text="Save and Close", command=close)
button_close.grid(row=0,column=3)
 
window.mainloop()


# In[7]:


from flask import Flask
app = Flask(__name__)
  
# routing the decorator function hello_name
@app.route('/hello/<name>')  
def hello_name(name):
   return 'Hello %s!' % name
  
if __name__ == '__main__':
    print(dir(app))
    app.run(debug = True)


# In[1]:


import render_template


# In[13]:


#total score of exercise
import pandas as pd
df=pd.read_csv("/Users/callisto/Documents/Udemy/pythonexercise/score")
print(df["marks"].sum())
    


# In[ ]:




