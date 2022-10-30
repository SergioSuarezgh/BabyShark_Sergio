#    ![Ironhack logo](https://i.imgur.com/1QgrNNw.png) 



#                                                 PROJECT-SHARK
![img](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4_TnS44suTB8Yk99Q7KV4pwItIJadfe8jFP9YzlRx4A&s)


## OBJETIVO DEL PROYECTO

Conocer las especies que más ataques produce, cuantos son mortales y desglosar los ataques mortales por las actividades donde más incidentes hay

## PASOS A SEGUIR...

1) Se va a limpiar el dataframe original donde están todos los datos, extraídos de este [SHARK LINK!](https://www.kaggle.com/datasets/teajay/global-shark-attacks).

2) Solamente se ha podido eliminar las dos columnas unnamed que cumplían los criterios señalados de más del 80% nulos

3) Se han tratado de limpiar todas las columnas lo mejor posible utilizando principalmente funciones con regex para filtrar los datos de las columnas y dejarlas lo más limpias posibles

    3.1) Primero se han limpiado los duplicados lo cual ha dejado las filas aproximadamente en unas 6300, cifra próxima al número de filas minimas permitidas que eran 6000

    3.2) Criterios utilizados por columnas. En todas se han limpiado nulos y se h a dejado principalmente como alternativa en textos unkwnow

    3.3) Vamos con las columnas
        3.3.1) En la columna DATE se ha utilizado una función para dejar solo las cifras de 4 digitos
        3.3.2) En la columna CASENUMBER se ha utilizado una función para igualar las fechas y dejar en los casos donde la fecha no fuera clara el formato 0000.00.00. Postetiormente estas columnas se han copiado en CASENUMBER1 Y CASENUMBER2
        3.3.3) En la columna AGE se ha usado función que sacaba la media donde aparecían varios numeros y a los string más habituales se le ha dado un valor como young 18.5. En el caso de lo que no entraba en la búsqueda se le ha puesto el valor de 0
        3.3.4) En la columna TYPE se ha pasado una función para afinar la string Boat
        3.3.5) En la columna YEAR  se le ha dado un tratamiento parecido a AGE pero solo con una busqueda por 4 digitos y lo que se saliera de eso dejarlo como desconocido
        3.3.6) Las columnas COUNTRY, AREA, LOCATION, INVESTIGATOR OR SOURCE solamente hemos realizado una limpieza superficial quitando algunos caracteres extraños o quitando string que hemos detectado como extraños
        3.3.7) En la columna ACTIVITY hemos cogido los valores más habituales y les hemos dado formato el resto los hemos pasado a other
        3.3.8) La columna NAME se le ha dado un tratamiento también superficial limpiando algunas palabras habituales con significado genérico por unkwnow
        3.3.9) La columna SEX tenía pocos valores por lo que se ha realizado una limpieza más manual cambiando directamente los 4 valores erroneos
        3.3.10) En la columna INJURTY he decido dejar solo 2 valores o bien FATAL  o bien INJURY. Lo mismo en la columna FATAL(y/n) con solo Y o N
        3.3.11) En la columna TIME se ha dejado el formato 00:00 y se ha modificado por una función los rangos de tiempo más usuales por una hora concreta y las desconocidas por 00:00
        3.3.12) En la columna SPECIES se ha pasado un función para dejar solo la palabra delante de shark y shark
        3.3.13) Las columnas PDF, HREF,HREF_FORMULA Y ORIGINAL NUMBER no las he tocado ya que no las he considerado lo suficientemente importantes para una limpieza

4) Se ha detectado si había datos constantes o con baja varianza pero no se ha detectado ninguno

5) Se ha trazado los outliers sobre la columna de DATE y gtras aplicar la formula me han salido que los outliers superiores estaban en 2099. Este dato no tenia sentido por lo que se ha establecido el outlier superior en 2022 y el inferior en 1846.
    Hemos pasado de 6312 a 6121 filas


![img](outliers.png)



## CONCLUSIONES

Para las conclusiones hemos eliminado las columnas donde no había especies de tiburones ya que eso falseaba el estudio y nos hemos quedado con unas 1500 filas. Ya que nuestra principal fuente de información son las especies y las actividades para sacar conclusiones

Sobre las conclusiones obtenidas podemos indicar que los 3 tiburores con más tipos de ataque son:

![img](rankshark.png)

### Tiburon blanco  ![img](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-ZlstPfioF9FT5pbwX7LcYQF1oQ2FYYdybg&usqp=CAU)
### Tiburon Tigre ![img](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKIwZSTucvlqblh91tvkUHX0eT_bRKJU6d4Q&usqp=CAU)
### Tiburon Toro ![img](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYlGkYUeKhig2pDBIviSNHwAjg3uvjfsPrCg&usqp=CAU)



Las actividades cuatro donde más ataques se han producido son las siguientes. Hemos dejado other como computo de muchas actividades menores:

![img](activity.png)

Podemos saber que de todos los ataques aproximadamente el 15% han sido fatales y que dentro de las actividades principales el 26% de los mismos han sido fatales










