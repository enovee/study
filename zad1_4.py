#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


# ZADANIE 1

a = int(input('Podaj a = '))
b = int(input('Podaj b = '))

x = np.arange(-10,10,0.5)
y = a*x+b

plt.plot(x,y)
plt.ylabel('y')
plt.xlabel('x')
plt.legend(["Funkcja liniowa"])
plt.title('f(x) = a*x + b')

if a < 0:
    f = 'funkcja malejąca'
elif a > 0:
    f = 'funkcja rosnaca'
else:
    f = 'funkcja stala'
    
plt.text(3,1,f)
plt.grid(True)
plt.show()


# In[3]:


# ZADANIE 2

a = int(input('Podaj a = '))
x = np.arange(-10,10,0.5)
y1 = x/(-3)+a
y2 = x*x/3

fig = plt.figure()
ax = plt.gca()

ax.plot(x,y1, label ='x/(-3)+a')
ax.plot(x,y2, label ='x^2/3')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


ax.grid(True)

plt.xlim(-10,10)
plt.ylabel('os y')
plt.xlabel('os x')
plt.title('Wykresy funkcji')
ax.legend(loc='upper left')
plt.show()


# In[386]:


# ZADANIE 3

n = int(input("Ile ruchów ma wykonac czasteczka? "))
x = y = 0
lx = [0]
ly = [0]

for i in range(0, n):
    # stopnie na radiany
    rad = float(random.randint(0, 360)) * np.pi / 180
    x = x + np.cos(rad)
    y = y + np.sin(rad)
    
    lx.append(x)
    ly.append(y)

print(lx, ly)

# wektor przesunięcia
przemieszczenie = np.fabs(np.sqrt(x**2 + y**2))
print("Wektor przesunięcia:", s)


plt.plot(lx, ly, "o:", color="green")
plt.plot((0,lx[-1]),(0,ly[-1]), '-r')
plt.legend(["Dane x, y\nPrzemieszczenie: " + str(przemieszczenie)], loc="upper left")
plt.xlabel("lx")
plt.ylabel("ly")
plt.title("Ruchy Browna 2D - symulacja")
plt.grid(True)
plt.tight_layout()
plt.show()


# In[387]:


# ZADANIE 4

labels = ['A', 'B', 'C', 'D']
Grazyna = np.random.randint(0,200,4)
Janusz = np.random.randint(0,200,4)

x = np.arange(len(labels))
width = 0.40

fig, ax = plt.subplots()
r1 = ax.bar(x - width/2, Janusz, width, color='blue', label= 'Janusz')
r2 = ax.bar(x + width/2, Grazyna, width, color='green', label='Grazyna')


ax.set_ylabel('Wyniki')
ax.set_xlabel('Osoba')
ax.set_title('Wyniki testu IQ')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='upper right')


fig.tight_layout()
plt.show()


# In[393]:


n = int(input('Wprowadz liczbe'))
x = np.arange(n)

def nasza_funkcja(x)
    return 1-x/float(n)


negative_data = []
positive_data = []

for i in range(x):
    dd = nasza_funkcja(x)
    if



fig = plt.figure()
ax = plt.subplot(111)
ax.bar(count, negative_data, width=1, color='r')
ax.bar(count, positive_data, width=1, color='b')


# In[406]:


ujemne = [-4, -2, -1]
dodatnie = [3, 2, 1]

plt.hist(dodatnie)
plt.hist(ujemne)


# In[ ]:




