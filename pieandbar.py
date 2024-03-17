#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
x=[15,12,20,25,30]
y=[20,30,40,50,60]
plt.plot(x,y)
plt.show()


# In[4]:


from matplotlib import pyplot as plt
x=[15,12,20,25,30]
y=[20,30,40,50,60]

plt.bar(x,y)
plt.show()

labls = ["t1","t2","t3","t4","t5"]
plt.pie(x, labels=labls,startangle=90, )
plt.show()


# In[ ]:




