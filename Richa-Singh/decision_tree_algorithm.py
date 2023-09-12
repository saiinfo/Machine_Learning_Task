#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
# cancer.head()
cancer.keys()


# In[15]:


cancer


# In[17]:


# cancer['DESCR']

print(cancer['DESCR'])


# In[5]:


cancer['feature_names']


# In[21]:


df_feat = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
df_feat.info()
df_feat.head()


# In[18]:


cancer['target']


# In[30]:


df_target = pd.DataFrame(cancer['target'], columns=['Cancer'])

# df_target = pd.DataFrame(cancer['target'],columns=cancer['feature_names'])
df_target.info()
# df_feat.head()
df_target.head()


# In[22]:


from sklearn.preprocessing import StandardScaler
scaler= StandardScaler()
scaler.fit(df_feat)


# In[24]:


scaled_features = scaler.transform(df_feat)
df_feat_scaled = pd.DataFrame(scaled_features, columns=df_feat.columns)
df_feat_scaled.head()


# In[26]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(scaled_features,np.ravel(df_target),test_size=0.30,random_state=105)
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))
error_rate= []
for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors =i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))
    plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue',linestyle='dashed',marker='o',markerfacecolor='red', markersize=10)
plt.title('error rate vs. kvalue')
plt.xlabel('K')
plt.ylabel('error rate')


# In[ ]:


# decision tree algorithm


# In[35]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline#for encoding
# from sklearn.preprocessing import LabellEncoder #for train test splitting
# from sklearn.modes_selection import train_test_split #for decision tree object
# from sklearn.tree import DecisionTreeClassifier #for checking test results
# from sklearn.metrics import classification_report, confusion_matrix #for visualizing tree
# from sklearn.tree import plot_tree
iris = sns.load_dataset('iris')
iris.head()


# In[36]:


iris.info()
iris.shape


# In[37]:


iris.isnull().any()


# In[40]:


sns.pairplot(data=iris, hue = 'species')


# In[41]:


sns.heatmap(iris.corr())


# In[66]:


target = iris['species']
df1 = iris.copy()
df1 = df1.drop('species', axis =1)
# df1 = df1.drop('petal_length', axis = 1)


# In[62]:


X = df1


# In[53]:


target


# In[67]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
target = le.fit_transform(target)
target


# In[68]:


y = target


# In[73]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,random_state = 42)
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Assuming y contains the string labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)
dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)
print('decision TreeCLassifier created')


# In[ ]:




