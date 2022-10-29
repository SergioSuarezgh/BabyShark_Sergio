##PREPARAMOS LIBRERIAS Y EL ENTORNO DE TRABAJO
from cleaning import *

import re
import pandas as pd
import numpy as np
import pylab as plt
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


##IMPORTAMOS EL ARCHIVO Y HACEMOS UNA COPIA PARA TRABAJAR

shark_orin=pd.read_csv('attacks.csv', encoding= 'latin1')

shark=shark_orin.copy()


##EXPLORAMOS EL ARCHIVO

shape_original=shark.shape

shark.columns

'''Las columnas son:
'Case Number', 'Date', 'Year', 'Type', 'Country', 'Area', 'Location',
       'Activity', 'Name', 'Sex ', 'Age', 'Injury', 'Fatal (Y/N)', 'Time',
       'Species ', 'Investigator or Source', 'pdf', 'href formula', 'href',
       'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22',
       'Unnamed: 23'''
       
shark.head()

shark.dtypes

'''Case Number                object
Date                       object
Year                      float64
Type                       object
Country                    object
Area                       object
Location                   object
Activity                   object
Name                       object
Sex                        object
Age                        object
Injury                     object
Fatal (Y/N)                object
pdf                        object
href formula               object
href                       object
Case Number.1              object
Case Number.2              object
original order            float64
Unnamed: 22                object
Unnamed: 23                object'''

shark.info(memory_usage='deep')

'''<class 'pandas.core.frame.DataFrame'>
RangeIndex: 25723 entries, 0 to 25722
Data columns (total 24 columns):
 #   Column                  Non-Null Count  Dtype
---  ------                  --------------  -----
 0   Case Number             8702 non-null   object
 1   Date                    6302 non-null   object
 2   Year                    6300 non-null   float64
 3   Type                    6298 non-null   object
 4   Country                 6252 non-null   object
 5   Area                    5847 non-null   object
 6   Location                5762 non-null   object
 7   Activity                5758 non-null   object
 8   Name                    6092 non-null   object
 9   Sex                     5737 non-null   object
 10  Age                     3471 non-null   object
 11  Injury                  6274 non-null   object
 12  Fatal (Y/N)             5763 non-null   object
 13  Time                    2948 non-null   object
 14  Species                 3464 non-null   object
 15  Investigator or Source  6285 non-null   object
 16  pdf                     6302 non-null   object
 17  href formula            6301 non-null   object
 18  href                    6302 non-null   object
 19  Case Number.1           6302 non-null   object
 20  Case Number.2           6302 non-null   object
 21  original order          6309 non-null   float64
 22  Unnamed: 22             1 non-null      object
 23  Unnamed: 23             2 non-null      object
dtypes: float64(2), object(22)
memory usage: 22.8 MB
None'''

shark.describe(include='all').T

'''                       freq         mean          std  min     25%     50%   \
Case Number             2400          NaN          NaN  NaN     NaN     NaN
Date                      11          NaN          NaN  NaN     NaN     NaN
Year                     NaN  1927.272381   281.116308  0.0  1942.0  1977.0
Type                    4595          NaN          NaN  NaN     NaN     NaN
Country                 2229          NaN          NaN  NaN     NaN     NaN
Area                    1037          NaN          NaN  NaN     NaN     NaN
Location                 163          NaN          NaN  NaN     NaN     NaN
Activity                 971          NaN          NaN  NaN     NaN     NaN
Name                     550          NaN          NaN  NaN     NaN     NaN
Sex                     5094          NaN          NaN  NaN     NaN     NaN
Age                      154          NaN          NaN  NaN     NaN     NaN
Injury                   802          NaN          NaN  NaN     NaN     NaN
Fatal (Y/N)             4293          NaN          NaN  NaN     NaN     NaN
Time                     187          NaN          NaN  NaN     NaN     NaN
Species                  163          NaN          NaN  NaN     NaN     NaN
Investigator or Source   105          NaN          NaN  NaN     NaN     NaN
pdf                        2          NaN          NaN  NaN     NaN     NaN
href formula               2          NaN          NaN  NaN     NaN     NaN
href                       4          NaN          NaN  NaN     NaN     NaN
Case Number.1              2          NaN          NaN  NaN     NaN     NaN
Case Number.2              2          NaN          NaN  NaN     NaN     NaN
original order           NaN  3155.999683  1821.396206  2.0  1579.0  3156.0
Unnamed: 22                1          NaN          NaN  NaN     NaN     NaN
Unnamed: 23                1          NaN          NaN  NaN     NaN     NaN

                           75%     max
Case Number                NaN     NaN
Date                       NaN     NaN
Year                    2005.0  2018.0
Type                       NaN     NaN
Country                    NaN     NaN
Area                       NaN     NaN
Location                   NaN     NaN
Activity                   NaN     NaN
Name                       NaN     NaN
Sex                        NaN     NaN
Age                        NaN     NaN
Injury                     NaN     NaN
Fatal (Y/N)                NaN     NaN
Time                       NaN     NaN
Species                    NaN     NaN
Investigator or Source     NaN     NaN
pdf                        NaN     NaN
href formula               NaN     NaN
href                       NaN     NaN
Case Number.1              NaN     NaN
Case Number.2              NaN     NaN
original order          4733.0  6310.0
Unnamed: 22                NaN     NaN
Unnamed: 23                NaN     NaN'''

##COMENZAR A GESTIONAR EL FICHERO

##Vamos a poner los nombres sin espacios y en minusculas

shark_columns=DataCleaning.modificar_nombres_columnas(shark)

shark.columns=shark_columns


#Primero vamos a eliminar las columnas de unnamed ya que no nos dan informacion

shark.drop(columns=['unnamed:22', 'unnamed:23'], inplace=True)

#Vamos a limpiar los duplicados


shark=shark.drop_duplicates()





#nuevo shape (6311, 22)


##COLUMNA CASENUMBER


shark.casenumber[(shark.casenumber.notna()) & (shark.casenumber!='0')]


#Hacemos una funcion que sustituye las fechas extrañas por 000.00.00 para poder pasar luego
#la columna a date



print
def limpiar_fecha(x):
    x=str(x)
    contador=0
    
    num=re.findall('\d+.\d+.\d+', x)
    num="".join(num)
    
    if num=='':
        contador=0
    elif num in x:
        contador+=1

    if contador==1:
        return str(num)
    elif contador==0:
        return '0000.00.00'
    
  
shark.casenumber=shark.casenumber.apply(limpiar_fecha)

shark[shark.casenumber=='0000.0725 ']='0000.00.00'

##Como Date, CaseNumber1 y CaseNumber2 son lo mismo las igualamos


shark.date=shark.casenumber
shark['casenumber.1']=shark.casenumber
shark['casenumber.2']=shark.casenumber




##Vamos a limpiar la edad

shark.age.unique()

from statistics import mean
def mean_Age(x):
    x = str(x).lower()
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
    
shark.age=shark.age.apply(mean_Age)

shark.age.unique()


##LIMPIAR LA COLUMNA TYPE
#Quitando los valores Boat y Boatomg por Boating e invalid
#lo vamos a pasar a 'unknown
shark.type.unique()

#Primero cambiamos nulos a 'unknown'

shark.type.isnull().sum()

shark.type.fillna(value='unknown', inplace=True)



def tipo_ataque(x):
    if x =='Boat':
        return'Boating'
    elif x =='Boatomg':
        return'Boating'
    elif x=='Invalid':
        return 'unknown'
    else:
        return x
    
shark.type=shark.type.apply(tipo_ataque)

shark.type.unique()

##COLUMNA YEAR

#Copiamos los años de la columna casenumber

def year_comparacion(x):
   
    key=re.findall('\d+',x)
    return "".join(key[0])



shark.year=shark.casenumber.apply(year_comparacion)

##COLUMNA COUNTRY

#En este caso limpiamos los Nan y los ponemos como unknwon


shark.country.isnull().sum()

shark.country.fillna(value='unknwon', inplace=True)

#Ponemos todo en mayusculas y quitamos los interrogantes

shark.country=shark.country.str.upper()

shark.country=shark.country.str.replace("?","")

shark.country.unique()

#COLUMNA AREA

#Primero gestionamos los nulos
shark.area.unique()

shark.area.isnull().sum()

shark.area.fillna(value='unknwon', inplace=True)

##En este caso vamos a gestionar dos valores que aparecen con caracteres extraños nada más de forma 
#dirercta ya que es complicado establecer regiones geográficas al haber ataques en alta mar
#'d\x92Étang-Salé'
#'Vava\x92u'

keyword='d\x92Étang-Salé'
select3=shark[shark.area.str.contains(keyword, regex=True)]

shark.iloc[2356]='Vavau'
shark.iloc[2362]='Vavau'
shark.iloc[2515]='Vavau'

shark.iloc[447]='dÉtang-Salé'
shark.iloc[607]='dÉtang-Salé'

##COLUMNA LOCATION

#Comprobamos si la columna tiene nulos y los modificamos por 'unkwnow'

shark.location.isnull().sum()

shark.location.fillna(value='unkwnow', inplace=True)

##En este caso no limpiamos nada más ya que las localizaciones al igual 
# que las areas son de dificil localizacion

##COLUMNA ACTIVITY

#Comprobamos si la columna tiene nulos y los modificamos por 'unkwnow'

shark.activity.isnull().sum()

shark.activity.fillna(value='unkwnow', inplace=True)

#Cogemos cierto patron de actividades y lo pasamos por una función para que cambie los nombres,
# el resto los consideramos como otros

def actividad(x):
    dicc_actividades = {"Fishing":re.search(".*[Ff](ishing|ISHING).*",str(x)),
                    "Swimming":re.search(".*[Ss](wimming|WIMMing).*",str(x)),
                    "Kite":re.search(".*[Kk](ite|ITE).*",str(x)),
                    "Walking":re.search(".*[Ww](alking|ALKING).*",str(x)),
                    "Boogie Board":re.search(".*[Bb](oogie|OOGIE).*",str(x)),
                    "Body Boarding":re.search(".*[Bb](ody|ODY).*",str(x)),
                    "Wind Surfing":re.search(".*[wW](ind|IND).*",str(x)),
                    "Boat":re.search(".*[Bb](oat|OAT).*",str(x)),
                    "Interact with sharks":re.search(".*[Ss](hark|HARK).*",str(x)),
                    "Diving":re.search(".*[Dd](iving|IVING).*",str(x)),
                    "Standing in water":re.search(".*[Ss](tand|TAND).*",str(x)),
                    "Paddling":re.search(".*[Pp](addl|ADDL).*",str(x)),
                    "Bathing":re.search(".*[Bb](athing|ATHING).*",str(x)),
                    "OverBoard":re.search(".*[Oo](verb|VERB).*",str(x)),
                    "Bathing":re.search(".*[Bb](athing|ATHING).*",str(x)),
                    "Floating":re.search(".*[Ff](loat|LOAT).*",str(x)),
                    "Jumping":re.search(".*[Jj](ump|UMP).*",str(x))}
    for key,values in dicc_actividades.items():
        if values:
            return key
    return "other"

shark.activity=shark.activity.apply(actividad)


##COLUMNA NAME

#Como siempre limpiamos nulos y los dejamos como 'unkwnow'

shark.name.isna().sum()

shark.name.fillna(value='unkwnow', inplace=True)

#Esta columna no tiene mucha relevancia para los estudios pero intetamos limpiarla de la mejor forma posible


def name(x):
    x=x.lower()
    
    if re.findall('male',x):
        return 'unkonwn'
    elif x=='':
        return 'unkonwn'
    elif x==None:
        return 'unkonwn'
    elif 'marine' in x:
        return 'unkonwn'
    elif  'girl' in x:
        return 'unkonwn'
    elif 'boy' in x:
        return 'unkonwn'
    elif '_' in x:
        return 'unkonwn'
    elif '..' in x:
        return 'unkonwn'
    elif 'people' in x:
        return 'unkonwn'
    elif 'teacher' in x:
        return 'unkonwn'
    elif x=='':
        return 'unkonwn'
    elif 'citizen' in x:
        return 'unkonwn'
    elif '*' in x:
        return 'unkonwn'
    elif 'anonymus' in x:
        return 'unkonwn'
    elif 'japanese' in x:
        return 'unkonwn'
    elif re.findall('^\d+', x):
        return 'unkonwn'
    else:
        return x
    
name('marine dsddsdsd')

shark.name=shark.name.apply(name)

##COLUMNA SEXO

#limpiamos los nulos

shark.sex.fillna(value='unkwnow', inplace=True)

#Al ser poco los valores erroneos los modificamos directamente

shark[shark.sex=='M ']='M'
shark[shark.sex=='N']='M'
shark[shark.sex=='.']='unkwnow'
shark[shark.sex=='lli']='unkwnow'

##COLUMNA INJURY

#Limpiamos nulos
shark.injury.unique()
shark.injury.isna().sum()
shark.injury.nunique()
shark.injury.fillna(value='unkwnow', inplace=True)

#Tomo la decisión de si hay un texto escrito y no han puesto fatal lo tomo como no mortal y lo modifico

def injury(x):
    
    x=str(x.lower())
    if "fatal" in x:
        return 'fatal'
    elif "No injury" or 'no injury' in x:
        return 'no injury'
    elif 'injury' in x:
        return 'injury'
    elif 'unkwnow':
        return 'unkwnow'
    else:
        return 'injury'
    
shark.injury=shark.injury.apply(injury)

shark.injury.unique()


##COLUMNA FATAL

#En este caso primero igualamos donde hay algun dato en injury ponemos N en fatal

shark['fatal(y/n)'][shark.injury=='injury']='N'

#Luego limpiamos los nulos

shark['fatal(y/n)'].isna().sum()

shark['fatal(y/n)'].fillna(value='UNKWNOW', inplace=True)

#Convertimos todo en mayusculas y quitamos los espacios

shark['fatal(y/n)']=shark['fatal(y/n)'].str.strip().str.upper()

#Al tener que modificar en pocos casos los hacemos directamente

shark[shark['fatal(y/n)']=='UNKNOWN']='UNKWNOW'
shark[shark['fatal(y/n)']=='M']='N'
shark[shark['fatal(y/n)']=='2017']='UNKWNOW'

#COLUMNA TIME















    




