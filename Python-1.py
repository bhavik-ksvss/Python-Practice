#!/usr/bin/env python
# coding: utf-8

# In[85]:


#Q1
from collections import Counter

input_str = """8
Leonardo DiCaprio,The Revenant
Christian Bale,Vice
Morgan Freeman,Shawshank Redemption
Leonardo DiCaprio,The Great Gatsby
Christian Bale,American Psycho
Morgan Freeman,The Dark Knight
Christian Bale,The Dark Knight
Samuel L. Jackson,Pulp Fiction"""

def top_actors(input_str):
    topactors=[]
    input_lines = input_str.strip().split('\n')

    num_lines = int(input_lines[0])

    actor_names = [line.split(',')[0] for line in input_lines[1:]]

    actor_count = Counter(actor_names)

    sorted_actors = sorted(actor_count.keys(), key=lambda actor: (-actor_count[actor], actor))

    for actor in sorted_actors[:3]:
        print(actor)
    
    return None

top_actors(input_str)


# In[70]:


#Q2
lst = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4]

def find_unique_elements(lst):
    dict_hash = {}
    unique_elements=[]
    for i in range(len(lst)):
        if lst[i] not in dict_hash.keys():
            dict_hash[lst[i]] = 1
        else:
            dict_hash[lst[i]] += 1
            
    return list(dict_hash.keys())

print("Unique Elements are",find_unique_elements(lst))


# In[71]:


#Q3
num1=[1,2]
num2=[1,9,8,7]

def sum_of_large(num1,num2):
    return max(num1)+max(num2)
    
print(sum_of_large(num1,num2))


# In[72]:


#Q4

def is_prime(num):
    value='Prime'
    if num<=1:
        value='Not Prime'
    else:
        for i in range(2,num//2+1):
            if num%i==0:
                value='Not Prime'
                break
    return value

print(is_prime(5))

