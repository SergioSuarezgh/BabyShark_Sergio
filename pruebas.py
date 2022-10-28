
import re
import pandas as pd
import numpy as np
import pylab as plt
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

shark=pd.read_csv('attacks.csv', encoding= 'latin1')



shark.Age.fillna('unknow', inplace=True)



print(shark.Age.isnull().sum())

print('Numero de valores antes de formula',shark.value_counts())

#print(shark.columns)

'''def edad(x):
    i=str(x).lower()
    
    num=re.findall('\d+', i)
    numlet=re.findall('\d+\D+',i)
    espacios=re.findall('\s+',i)
    
    
    
    if len(i)<=2:
        if i.isalpha():
            return 'no numero'
        elif i==re.findall('\d\D',i):
            return 'numero y letra'
        else:
            return x
    else:
        if i in numlet:
            return "".join(num)
        elif i=='teen':
            return '15'
        elif i in 'young':
            return '15'
        elif i in'mid':
            return '40'
        elif i in 'adult':
            return '30'
        elif '&' in i:
            return "".join(num[0])
        elif 'or' in i:
            return "".join(num[0])
        elif 'Both' in i:
            return "".join(num[0])
        elif i in espacios:
            return 'espacio'
        else:
            return 'unknown'
            '''
            
from statistics import mean
def mean_Age(x):
    x = x.lower()
    num=re.findall('\d+', x)[:5]
    res = [eval(i) for i in num]
    if num:
        return mean(res)
    elif "teen" in x:
        return 15.5
    elif "young" in x:
        return 18.5
    elif "adult" in x:
        return 49
    elif "elderly" in x:
        return 70
    elif "middle" in x :
        return 50
    elif "18months" in x:
        return 1.5
    elif "9months" in x:
        return 0.75
    elif "2to3months" in x:
        return 0.2
    else:
        return 0
            

#print(edad('40 months'))
#print('Revision de datos')
#print(shark.Age[shark.Age==type('list')])


print('Funcion')
shark.Age=shark.Age.apply(mean_Age)
  
print(shark.Age.unique())



#print(shark.Age.unique())
print('Valores salida',shark.Age.value_counts())

#print('Datos',shark[shark.Age=='17'])





'''

for i in shark.Age:
    
    
    num=re.findall('\d+', i)
    numlet=re.findall('\d+\D+',i)
    
    
    if len(i)<=2:
        None
    else:
        if i in numlet:
            print("".join(num))
        elif i=='Teen' or i=='teen':
            print('teen 15')
        elif i in 'young':
            print('young 15')
        elif i in'mid':
            print('mid 40')
        elif i in 'adult':
            print('sdult 30')
        elif '&' in i:
            print('&',"".join(num[0]))
        elif 'or' in i:
            print('or', "".join(num[0]))
        elif 'Both' in i:
            print('Both', "".join(num[0]))
        else:
            print('unknown')'''
            
            
def tipo_ataque(x):
    if x=='Boat':
        return'Boating'
    elif x=='Boatomg':
        return 'Boating'
    elif x=='Invalid':
        return 'unknown'
    
    
print(shark.columns)   
def year_comparacion(x):
    print(x)
    key=re.findall('\d+',x)
    
    return "".join(key[0])

print(year_comparacion('1852.10.23'))

shark.Year=shark['Case Number'].apply(year_comparacion)

        
