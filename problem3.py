
# coding: utf-8

# In[6]:

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
greater=[]
lesser=[]
for i in numbers:
    if i > 5:
        greater.append(i)
    elif i <= 2:
        lesser.append(i)
print("Number greater than 5 are:--->"+str(greater))
print("Number less than or equal to 2 are:--->"+str(lesser))

