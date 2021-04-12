#!/usr/bin/env python
# coding: utf-8

# In[319]:


products = [2.99, 4.00, 5.42, 10.29, 9.32, 1.69, 12.40]

def first(x):
    
    x.sort()
    print(x)
    x.sort(reverse=True)
    print(x)


# In[320]:


first(products)


# In[61]:


from random import randint, sample    

def secondA(x, start = 1, end = 99):
    ''' funkcja, ktora jako parametry domyslne przyjmuje zakres pytan, czyli start i end.
    O parametrze x decyduje uzytkownik - jest to wartosc mowiaca o tym ile ma byc pytan'''
    
    arg = []
    temp = randint(start, end)
    for i in range(x):
        
        while temp in arg:
            temp = randint(start, end)
    
        arg.append(temp)
        arg.sort()
        
    return f'Twoja posortowana lista pytan: {arg}'


# In[63]:


secondA(9)


# In[126]:


my_list = ['1. Dynamika Newtona. Przestrzeń i czas. Zasady dynamiki, układy inercjalne i nieinercjalne. Ruch w polu sił centralnych, prawa Keplera.', '2. Transformacje Galileusza i Lorentza. Masa relatywistyczna. Energia relatywistyczna.', '3. Dynamika bryły sztywnej. Moment bezwładności. Prawo zachowania momentu pędu.', '4. I i II zasada termodynamiki. Energia wewnętrzna układu. Ciepło. Odwracalność procesów termodynamicznych. Temperatura absolutna. Entropia.', '5. Dyfrakcja światła, dyfrakcja Fresnela. Obraz dyfrakcyjny jako transformata Fouriera.', '6. Pole magnetyczne. Prawo Biota-Savarta. Dipol magnetyczny w polu magnetycznym. Przenikalność magnetyczna. Energia pola magnetycznego. Prawo indukcji Faraday’a.', '7. Równania Maxwella i ich sens fizyczny.', '8. Sieć Bravais, struktury krystalograficzne, odwrotna i jej związek z siecią rzeczywistą, techniki badań struktur krystalograficznych.9. Struktura pasmowa kryształów.', '10. Wiązania w materii skondensowanej.', '11. Twierdzenie Clausiusa, entropia, potencjały termodynamiczne, układy ze zmienną liczbą cząstek, potencjał chemiczny, równanie Gibbsa-Duhema, równowaga termodynamiczna, reguła faz Gibbsa, równanie Clausiusa-Clapeyrona.', '12. Rozkład Maxwella-Boltzmanna.', '13. Zespoły statystyczne (mikrokanoniczny, kanoniczny, wielki kanoniczny), ich równoważność w granicy termodynamicznej.', '14. Gazy doskonałe (Fermiego-Diraca, Bosego-Einsteina, relatywistyczny gaz Fermiego, gaz fotonów, gaz fononów, kondensaty Bosego-Einsteina).', '15. Równanie Pauliego dla cząstki o spinie 1/2,sprzężenie spin-orbita.', '16. Atom wieloelektronowy w zewnętrznym polu elektromagnetycznym.', '17. Model standardowy cząstek elementarnych.']


# In[202]:


def secondB(pytania): 
    
    k = int(input('ile pytań mam wylosować? '))
    
    return sample(pytania, k)


# In[203]:


secondB(my_list)


# In[342]:


products_dict = {'mleko':2.99, 'jaja':4.00, 'chleb':5.42, 'ryba':10.29, 'wino':9.32, 'lizak':1.69, 'papier':12.40}

def third(x):

    print('posortowane po nazwie produktu')
    for i in sorted(products_dict):
        print(i, products_dict[i])

    print("\n")

    print('posortowane po cenie produktu ')   
    y = sorted(products_dict.items(), key = lambda pd:(pd[1], pd[0]))
    for i,j in y:
        print(i,j)


# In[343]:


third(products_dict)


# In[425]:


def fourth(x):
    '''produkt co drugi'''
    op = sorted(products_dict.items(), key = lambda pd:(pd[1], pd[0]))
    print(op[0::2])


# In[426]:


fourth(products_dict)


# In[427]:


def fifth(x):
    '''produkty dla ktorych cena wynosi ponad 5zl'''
    
    y = sorted(products_dict.items(), key = lambda pd:(pd[1], pd[0]))
    for i,j in y:
        if j>5:
            print(i,j)


# In[428]:


fifth(products_dict)


# In[ ]:




