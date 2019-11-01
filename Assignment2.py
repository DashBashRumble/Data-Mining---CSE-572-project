
# coding: utf-8

# In[369]:


import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import pywt # Discrete Wavelet Transform  
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA


# In[370]:


pd_datenum = pd.read_csv('CGMDatenumLunchPat1.csv', delimiter=',')
pd_cgm = pd.read_csv('CGMSeriesLunchPat1.csv', delimiter=',')


# In[372]:


rows, columns = pd_cgm.shape
featureMatrix = []

pd_cgm = pd_cgm[::-1]  #flipping the rows
pd_cgm = pd_cgm.iloc[:, ::-1]  #flipping the columns

max_points = 4 # Max Points

for index, cgm_row in pd_cgm.iterrows():
    
    featureVector = []
    
    # CGM Velocity
    cgmDiffValues = [0]
    for ind in range(columns-1):
        cgmDiffValues+=[cgm_row[ind+1]-cgm_row[ind]]
    
    cgmDiffValues.sort(reverse=True)    
    cgmDiffMaxValues = cgmDiffValues[:max_points]
    
    # Moving RMS Velocity
    cgmRmsMoving = [((cgm_row**2).rolling(window=5).mean()).apply(numpy.sqrt)]
    cgmRmsMoving[4:].sort(reverse=True)  #Problem : not sorting may be because we have nan values 
   
    
    # Discrete Wavelet Transform
    #(cA, cD) = pywt.dwt(cgm_row, 'db1', mode='sym')
    
    
    featureVector = featureVector + cgmDiffMaxValues
    featureMatrix.append(featureVector)

