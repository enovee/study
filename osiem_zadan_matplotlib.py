#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[440]:


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


# In[441]:


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


# In[442]:


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


# In[443]:


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


# In[538]:


# ZADANIE 5

p = int(input('podaj ile chcesz miec wynikow '))

u = np.arange(p)
f = 1-u/float(p)
dodatnie = f
print(dodatnie)


u2 = np.arange(p)
f2 = 1-u2/float(p)
ujemne = -1*f2
print(ujemne)


x = np.arange(len(dodatnie))

fig, ax = plt.subplots()
rr1 = ax.bar(x, dodatnie, width=0.9, color='blue', label='dodatnie', alpha=0.4)
rr2 = ax.bar(x, ujemne, width=0.9, color='red', label='ujemne',alpha=0.4)
plt.axhline(0, linewidth=3, color='white')
plt.legend()


def autolabel(rects):

    for j,k in enumerate(rects):
        height = k.get_height()
        plt.text(k.get_x()+k.get_width()/2., 1.02*height, '%s'% (dodatnie[j]),
                ha='center', va='bottom')
autolabel(rr1)


# In[564]:


# ZADANIE 6

tekst = "Nie ma dróg innych oprócz drogi dojścia. Krzaki aż uginają się od odpowiedzi. "

plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=False, fontsize=np.random.randint(0,12), rotation=random.randint(0,360),style='normal')
plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=True, fontsize=np.random.randint(0,12), rotation=random.randint(0,360), style='oblique')
plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=False, fontsize=np.random.randint(0,12), rotation=random.randint(0,360), style='italic', fontfamily='DejaVu Sans')
plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=True, rotation=random.randint(0,360),ha='left')
plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=True, rotation=random.randint(0,360),ha='right', style='italic')
plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=False, fontsize=np.random.randint(0,12), rotation=random.randint(0,360),style='normal')
plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=True, fontsize=np.random.randint(0,12), rotation=random.randint(0,360), style='oblique')
plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=False, fontsize=np.random.randint(0,12), rotation=random.randint(0,360), style='italic', fontfamily='DejaVu Sans')
plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=False, fontsize=np.random.randint(0,12), rotation=random.randint(0,360),style='normal')
plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=True, fontsize=np.random.randint(0,12), rotation=random.randint(0,360), style='oblique')
plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=False, fontsize=np.random.randint(0,12), rotation=random.randint(0,360), style='italic', fontfamily='DejaVu Sans')
plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=False, fontsize=np.random.randint(0,12), rotation=random.randint(0,360),style='normal')
plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=True, fontsize=np.random.randint(0,12), rotation=random.randint(0,360), style='oblique')
plt.text(x = np.random.randint(0, 5), y = np.random.randint(0, 5), s = text, wrap=False, fontsize=np.random.randint(0,12), rotation=random.randint(0,360), style='italic', fontfamily='DejaVu Sans')


plt.axis([0, 10, 0, 10])
plt.show()


# In[645]:


# ZADANIE 7

from math import pi, exp, cos
x = np.arange(0, 3, 0.05)

os1 = []
os2 = []

for ix in x:
    os1.append(math.cos((2*pi*ix))*exp(ix))
    os2.append(math.cos(2*pi*ix))

os1.reverse()
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Drgania tlumione i nietlumione')
ax1.plot(os1)
ax1.set(ylabel='Oscylacja harmoniczna')
ax2.plot(os2)
ax2.set(ylabel='Oscylator harmoniczny')
ax2.set(xlabel='czas (s)')


# In[685]:


# ZADANIE 8

u=0     
v=0   
a=2.     
b=1.5    

t = np.linspace(0, 2*pi, 100)

fig = plt.figure()
ax = plt.gca()

ax.plot( u+a*np.cos(t) , v+b*np.sin(t), 'r')

def cross_hair(x, y, ax=None, **kwargs):
    
    if ax is None:
        ax = plt.gca()
    horiz = ax.axhline(y, **kwargs)
    vert = ax.axvline(x, **kwargs)
    return horiz, vert


cross_hair(0, 0, color='blue')

