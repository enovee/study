#!/usr/bin/env python
# coding: utf-8

# In[9]:


dna = 'ATGCAATTGCTCGATTAG'


# In[32]:


def counter(kod_dna):
    
    dna_items = ['CG', 'AT']
    how_many = {}
    myDict = {key: None for key in dna_items}
    
    myDict['CG'] = kod_dna.count('CG')
    myDict['AT'] = kod_dna.count('AT')
    
    return myDict


# In[33]:


with open('statystyki.txt', 'w') as f:
    print(counter(dna), file=f)

