#!/usr/bin/python3
#
# stats.py: 
# 
# by: Francis Kessie
#     
# Note: This program was created to run in python3
#
"""
A simple statistics calculator.

The program ask user to select one of (mean, mode, median, standard deviation,
range, variance) for calculations or press enter to terminate at anytime.
Afterwards the user is asked to select the parameter he wants the calculation 
done on. The Alcohol and Tobacco consumption data is hardcoded. The selected 
function is called on the user's input parameter and printed to screen
"""

import pandas as pd
from scipy import stats

def get_mean(inp):
    """return mean of column in dataframe"""
    return df[inp].mean()

def get_median(inp):
    """return median of column in dataframe"""
    return df[inp].median() 
       
def get_mode(inp):
    """return mode of column in dataframe"""
    mode = stats.mode(df[inp])
    for x in mode[0]:
        return x

def get_range(inp):
    """return range of column in dataframe"""
    return max(df[inp]) - min(df[inp])
    
def get_stdev(inp):
    """return standard deviation of column in dataframe"""
    return df[inp].std() 
    
def get_var(inp):
    """return variance of column in dataframe"""
    return df[inp].var()
    

if __name__ == "__main__":
    
    data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''
    
    data = data.splitlines()
    data = [i.split(', ') for i in data]
    column_names = data[0]
    data_rows = data[1::] 
    df = pd.DataFrame(data_rows, columns=column_names)
    df['Alcohol'] = df['Alcohol'].astype(float)
    df['Tobacco'] = df['Tobacco'].astype(float)
    
    switch = {"mean": get_mean,
              "median": get_median,
              "mode": get_mode, 
              "range": get_range,
              "variance": get_var,
              "stdeviation":get_stdev
         }
    options = switch.keys()
    option = ", ".join(options) 
    prompt = 'What would you want to calculate. Select({0}) or press enter to quit: '.format(option)
    message = "Nope, input is invalid or spelt wrongly!!"
    option2 = ['Tobacco', 'Alcohol']
    while True:
        print(" ")        
        inp1 = input(prompt)
        if not inp1:
            print(" ")
            print("Bye for now. Try another time if you want some calculations done!!.")
            print(" ")
            break
        if inp1 in option:
            print(" ")
            inp2 = input("You are calculating the " + inp1 + " for (select Tobacco or Alcohol): " ) 
            if not inp2:
                continue
            else:
                try: 
                   print(" ")                                          
                   print("The " + inp1+ " for the " + inp2+ " dataset is: " + str(switch[inp1.lower()](inp2.capitalize()))) 
                except KeyError:
                   print(message) 
        else:
            print(" ")
            print(message)
            continue  
            
            
            
