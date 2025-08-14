

steg1 = 0

from connect_data_warehouse import query_dwh, query_dwh_price




df_final_cleaned = query_dwh_price()

print(df_final_cleaned)


#df_final_cleaned_ = df_final_cleaned[(df_final_cleaned['cleaned_Bedrooms'] == 2) ]


import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


import streamlit as st

import numpy as np
import scipy  
import seaborn as sns
import matplotlib.pyplot as plt


def get_data(x2):
    
    x = x2
    
    #df_final_cleaned['cleaned_price']


    values = x
    fig, ax = plt.subplots(figsize=(12, 6))

    (counts, bin_edges, _bars) = plt.hist(values, bins=168) # .set_title(f"number_of_rooms={number_of_rooms} Cumulative Distribution and Histogram")#, rwidth=0.01) #, width=2)


    counts2 = counts

    counts2= list(counts2.flatten())

    bin_edges3 = list(bin_edges.flatten())

    list_new = list(zip(bin_edges3, bin_edges3[1:]))

    listed_bins = [] 
    for item in list_new:
        listed_bins.append((item[0] + item[1])/ 2)

    set_pair = []

    for item in counts2:
    #print(item)
        index2 = counts2.index(item)

        indi_v = [counts2[index2], listed_bins[index2]]
        indi_v2 = [listed_bins[index2], counts2[index2]]
        
        set_pair.append(indi_v2)

    return set_pair




def get_data_ok(x2):
    
    x = x2
    
    #df_final_cleaned['cleaned_price']


    values = x
    fig, ax = plt.subplots(figsize=(12, 6))

    (counts, bin_edges, _bars) = plt.hist(values, bins=168) # .set_title(f"number_of_rooms={number_of_rooms} Cumulative Distribution and Histogram")#, rwidth=0.01) #, width=2)


    ax2 = ax.twinx()

    p = sns.kdeplot(values, ax=ax2, fill=False)

    
    #ax2.set_ylabel('Y Values of the Fitted Cumulative Curve', color='r')
    #ax.set_ylabel('Counts', color='r')
    



    x1 = ax2.lines[-1].get_xdata()
    y1 = ax2.lines[-1].get_ydata()
    
    cdf = scipy.integrate.cumulative_trapezoid (y1, x1, initial=0)
    nearest_005 = np.abs(cdf-0.95).argmin()

    x_value_005 = x1[nearest_005]




    list_y = list(y1[0:])
    list_x = list(x1[0:])

    list_x2 = x_value_005


    #list_x = list(x1[0:])
    for i in range(len(list_x)):
        pass
        #print(list_x[i], list_y[i])

    #print(list_x, )


    counts2 = counts

    counts2= list(counts2.flatten())

    bin_edges3 = list(bin_edges.flatten())

    list_new = list(zip(bin_edges3, bin_edges3[1:]))

    listed_bins = [] 
    for item in list_new:
        listed_bins.append((item[0] + item[1])/ 2)

    set_pair = []

    one_set = []
    two_set= []

    '''
    for item in counts:
    #print(item)
        index2 = counts2.index(item)

        indi_v = [counts2[index2], listed_bins[index2]]
        indi_v2 = [listed_bins[index2], counts2[index2]]
        
        set_pair.append(indi_v2)

        one_set.append(listed_bins[index2])
        two_set.append(counts2[index2])
    '''
    return list_x, list_y, list_x2