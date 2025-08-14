

import streamlit as st

import numpy as np
import scipy  
import seaborn as sns
import matplotlib.pyplot as plt

from connect_data_warehouse import query_dwh, query_dwh_price, execute_query

#import get_data_for_histogram

from gethistogram import get_data, get_data_ok

#from get_gata_for_histogram

from streamlit_echarts import st_echarts

steg1 = 1

def main():
    st.markdown("# This is out Real Estate Curve")


    st.dataframe(query_dwh())


    option = st.selectbox(
     'How many rooms?',
     (1, 2, 3, 4))

    st.write('You selected:', option)

    rooms = option
    #query_1 = 

    data = execute_query(f"SELECT cleaned_price AS ok FROM stagging_table.cars where cleaned_bedrooms = {rooms}", return_type="df")


    #st.dataframe(data)


    #st.dataframe(query_dwh_price())

    ok = query_dwh_price()['cleaned_price']

    #counts2, bin_edges3 = get_data()

    x = data['ok']

    set_pair = get_data(x)

    set_pair2  = get_data(x)

    stelios = get_data_ok(x)

    print("stelios_0", stelios[0])
    print("stelios_1", stelios[1])

    #varX, varY = get_data_ok(x)

    #print("ok22", set_pair2)

    #one_set, two_set = get_data2(x)

    #print(counts2)



    options2 = {
  "xAxis": [
    {
      "type": 'value',
    }
  ],
  "yAxis": [
    {
      "type": 'value'
    }
  ],
  "series": [
    {
      "name": 'Direct',
      "type": 'bar',
      "barWidth": '80%',
      "data": set_pair
    }
  ]
    }

    st_echarts(options=options2, height="500px")



    options3 = {
  "xAxis": {
    "type": 'category',
    "data":  stelios[0],
    #"markLine": {
    #        "data": [
    #          {"name": 'start', "yAxis": 1200, "xAxis": '0'},
    #          {"name": 'end', "yAxis": 1200, "xAxis": '1'},
    #        ]
    #},




  },
  "yAxis": {
    "type": 'value'
  },
  "series": [
    #{
    #  "name": 'Bar Data',
    #  "type": 'bar',
    #  "data": stelios[1]
    #
    #},
    {
      "name": 'Line Data',
      "type": 'line',
      "data": stelios[1],
       "markLine": {
      "data": [
        {
          "name": 'Vertical Line at B',
          "xAxis": '276344.38381316897',# // or  xAxis: 1  (if 'B' is the second category)
          "yAxis":"0.00021000",
          "label": {"show": "false"},
          "lineStyle": {
            "type": 'dashed',
            "color": 'blue',}
        }
      ]
    },

      #"markLine": {
      #      "data": [
      #        {"name": 'start', "xAxis": 1200, "yAxis": '0.000003'},
      #        # { "name": 'xxxx', "xAxis": 2000 },
      #        {"name": 'end', "xAxis": 1200, "yAxis": '1'},
      #      ]
    #},
    },
    
    {
        "name":' SourceThree',
        "type":'scatter',
        "data":[
            [0, 0.0000003], [100, 0.000006]
        ],
        "markLine" : {
            "silent": "true", #// ignore mouse events
            "data" : [
            #// Horizontal Axis (requires valueIndex = 0)
            {"type" : 'average', "name": 'Marker Line', "valueIndex": 0, "itemStyle":{"normal":{"color":'#1e90ff'}}},
            ]
        }
        },
     {
      "name": 'Line Data',
      "type": 'line',
      "data": stelios[2]
    },
    #{
    #  "type": "custom",
    #  "data": [[1, 1, 3]],
    #  "renderItem": "render"
    #},

    {
        "data": "data",
        "type": "line",
        "markLine": {
          "data": [
          [
            { "name": "Imp Day 01", "xAxis": '439000',"yAxis": 0  },
            { "name": "end", "xAxis": '439000',  "yAxis":'max' },
          ],
          #[
          #  { "name": "Imp Day 02", "xAxis": '1998-08-01', "yAxis": 0 },
          #  { "name": "end", "xAxis": '1998-08-01', "yAxis":'max' },
          #]
          ],
        },
        "lineStyle": {
          "color": "rgba(242, 145, 72, 1)",
        },
      },
  ]
    }
    

    


    st_echarts(options=options3, height="500px")




if __name__ == '__main__':
    main()