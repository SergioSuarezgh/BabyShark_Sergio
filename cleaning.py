import pandas as pd
import numpy as np
import seaborn as sns
import pylab as plt

class DataCleaning():
    
    '''
        Clase contenedora de funciones para Data Cleaning con las siguientes funciones:
        
        def modificar_nombres_columnas(df): Función que modifica las columnas de una tabla 
                                            dejandolas en minusculas y sin espacios. 
                                            La función retorna un dato que hay que guardar en una variable
                                            
        def get_constantes_num(df): Funcion que da como resultado las columnas que con constantes numéricas
        
        def get_constantes_nonum(df):Funcion que da como resultado las columnas que con constantes
                                    no numéricas
                                    
        def get_bajavarianza(df):Funcion que da como resultado las columnas con baja varianza
        
        def get_outliers(stats: pd.DataFrame, threshold: float = 1.5) -> pd.DataFrame:Esta funcion 
                                                            recibe un dataframe df.describe().T. y devuelve
                                                            los outliers
                                                            
        def get_colinealidad(df): Retorna las columnas con colinealidad
        
        def get_nuloxfila(df):Retorna los nulos por fila
        
        def get_mapa_calor(df):Genera un mapa de calor
        
        def separar_stringfecha(string):Función donde entra una fecha y se la separa en tres digitos 
                                        que deben entrar separados por comas. 
                                        Devuelve una lista que debe ser pasada por el siguiente bucle
                                        
        def get_hist(df): Genera un historiograma
        
        def check_nan(df: pd.DataFrame)[EN PROCESO]: Genera un boxplot con los porcentajes de las medias
        
        def get_boxplot(df): Genera un boxplot generico del DataFrame
        
        '''
             
    
    
    def modificar_nombres_columnas(df):
        
        '''
        Función que modifica las columnas de una tabla dejandolas en minusculas y sin espacios. 
        La función retorna un dato que hay que guardar en una variable
        
        PARAM:
         
         df--> Es el nombre del DataFrame
        '''
        
        
        return [c.lower().replace(' ', '') for c in df.columns]
    
    
    def get_constantes_num(df):
        '''
            Funcion que da como resultado las columnas que con constantes numéricas
            
            PARAM:
            
            df--> es el nombre del DataFrame
        '''
        
        cte_cols=[]

        for c in df.select_dtypes(include=np.number):   # para cada columna numerica
    
            if len(df[c].unique())==1:
                cte_cols.append(c)
        
        return cte_cols
    
    def get_constantes_nonum(df):
        
        '''
            Funcion que da como resultado las columnas que con constantes no numéricas
            
            PARAM:
            
            df--> es el nombre del DataFrame
        '''
        cte_str_cols=[]

        for c in df.select_dtypes(include='object'):   # para cada columna NO numerica
    
            if len(df[c].unique())==1:
                cte_str_cols.append(c)
                
        return cte_str_cols
    
    
    def get_bajavarianza(df):
        
        '''
            Funcion que da como resultado las columnas con baja varianza
            
            PARAM:
            
            df--> es el nombre del DataFrame
        '''
        low_var=[]

        for c in df.select_dtypes(include=np.number):  # para cada columna numerica....
    
    
            minimo=df[c].min()
    
            per_90=np.percentile(df[c], 90)
    
            if minimo >= per_90:
                low_var.append(c)
                
        return low_var
    
        
    def get_outliers(stats: pd.DataFrame, threshold: float = 1.5) -> pd.DataFrame:
    
        """
        Esta funcion recibe un dataframe df.describe().T.
        
        Devuelve un dataframe.
        
        :param: stats, pd.DataFrame
        :param: threshold, umbral del test de tukey
        
        :return: pd.DataFrame
        """
    
        outliers=pd.DataFrame(columns=stats.index)

        for c in stats.index:

            iqr=stats.at[c, 'IQR']

            cutoff=threshold * iqr  # test tukey

            lower=stats.at[c, '25%'] - cutoff
            upper=stats.at[c, '75%'] + cutoff

            res=df[(df[c] < lower) | (df[c] > upper)].copy()

            res['outliers']=c

            outliers=outliers.append(res, sort=True)

    
        return outliers
    
    
    def get_colinealidad(df):
        
        '''
            Retorna las columnas con colinealidad
            
            PARAM:
            
            df--> Es el Dataframe
        '''
        
        colineales=[]

        for c in df._get_numeric_data():
    
            for i in range(len(df.corr())):
        
                if abs(df.corr()[c][i])>0.9 and abs(df.corr()[c][i])<1:
            
                    colineales.append(c)
            
        colineales=list(set(colineales))
        
        return colineales
    
    def get_nuloxfila(df):
        
        '''
            Retorna los nulos por fila
            
            PARAM:
            
            df--> Es el Dataframe
        '''
        num_nan=[]

        for fila in df.itertuples():
    
            check=[]
    
            for e in fila:
        
                check.append(pd.isna(e))
        
            num_nan.append(sum(check))
    
        num_nan[:10]
        
    
    def get_mapa_calor(df):
        
        '''
            Genera un mapa de calor
            
            PARAM:
            
            df--> Es el Dataframe
        '''
        
        plt.figure(figsize=(10, 6))  # inicia la figura y establece tamaño

        sns.heatmap(df.isna(),  # mapa de calor
           yticklabels=False,
           cmap='viridis',
           cbar=False)

        plt.show()

    def separar_stringfecha(string):
        
        '''
            Función donde entra una fecha y se la separa en tres digitos que deben entrar
            separados por comas. 
            Devuelve una lista que debe ser pasada por el siguiente bucle
            
            lst=[]
            for e in airbnb.last_review:
                lst.append(limpiar(e))
            
            PARAM:
            string--> entra una cadena de texto con datos de fecha separados por '-'
        '''
    
        try:
            return string.split('-')
        except:
            return [np.nan, np.nan, np.nan]
        
    def get_hist(df):
        
        '''
            Genera un historiograma
            
            PARAM:
            
            df--> Es el Dataframe
        '''
        
        plt.figure(figsize=(10, 6))

        df.hist(bins=100)

        plt.ylabel('# Count')
        plt.xlabel('Price')
        
        plt.show()
        
        
    def check_nan(df: pd.DataFrame) -> None:
        
        '''
            Genera un boxplot con los porcentajes de las medias
            
            PARAM:
            
            df--> Es el Dataframe
        '''
    
        nan_cols=df.isna().mean() * 100  # el porcentaje
    
        display(f'N nan cols: {len(nan_cols[nan_cols>0])}')
        display(nan_cols[nan_cols>0])
    
        plt.figure(figsize=(10, 6))  # inicia la figura y establece tamaño

        sns.heatmap(df.isna(),  # mapa de calor
                yticklabels=False,
                cmap='viridis',
                cbar=False)

        plt.show()
        
    def get_boxplot(df):
            
        '''
            Genera un boxplot generico del DataFrame
            
            PARAM:
            
            df--> Es el Dataframe
        '''
            
        plt.figure(figsize=(10, 6))  # inicia la figura y establece tamaño

        sns.heatmap(df.isna(),  # mapa de calor
                yticklabels=False,
                cmap='viridis',
                cbar=False)

        plt.show()
        
            
 
    
df=pd.read_csv('attacks.csv', encoding_errors= 'replace')


print(df.columns)