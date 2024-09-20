#!/usr/bin/env python
# coding: utf-8

# # Contenido
# 
# * [Diccionario de Datos](#diccionario)
# * [Introduccion](#introduccion)
# * [Dataframe](#dataframe)
#     * [Observacion](#observacion)
# * [Analisis de los Datos](#analisis)
#     * [1 Investigamos las proporciones de los distintos tipos de establecimientos.](#ipdte)
#         * [1.1 Observacion](#observacion2)
#     * [2 Investigamos las proporciones de los establecimientos que pertenecen a una cadena y de los que no.](#ipepc)
#         * [2.1 Observacion](#observacion3)
#     * [3 ¿Qué tipo de establecimiento es habitualmente una cadena?](#qtehc)
#         * [3.1 Observacion](#observacion4)
#         * [3.2 Observacion](#observacion4.1)    
#     * [4 ¿Qué caracteriza a las cadenas: muchos establecimientos con un pequeño número de asientos o unos pocos establecimientos con un montón de asientos?](#qccmepnapema)
#         * [4.1 Observacion](#observacion5)
#         * [4.2 Observacion](#observacion5.1)
#         * [4.3 Observacion](#observacion5.2)
#     * [5 Determinamos el promedio de número de asientos para cada tipo de restaurante. De promedio, ¿qué tipo de restaurante tiene el mayor número de asientos?](#dpnactrptrtmna)
#         * [5.1 Observacion](#observacion6)
#     * [6 Colocamos los datos de los nombres de las calles de la columna address en una columna separada.](#cdnccacs)
#     * [7 Trazamos un gráfico de las diez mejores calles por número de restaurantes](#tgdmcnr)
#         * [7.1 Observacion](#observacion7)
#     * [8 Encontramos el número de calles que solo tienen un restaurante.](#enctr)
#     * [9 Para las calles con muchos restaurantes, analizamos la distribución del número de asientos.](#pcmradna)
#         * [9.1 Observacion](#observacion8)
#         * [9.2 Observacion](#observacion8.1)
#         * [9.3 Observacion](#observacion8.2)
# * [Conclusion General](#conclusion)
# * [Recomendaciones](#recomendaciones)

# <div class="alert alert-block alert-success">
# <b>Review General. (Iteración 2) </b> <a class="tocSkip"></a>
# 
# Hola Cristhopher! Felicitaciones porque has corregido los detalles marcados en nuestra iteración anterior. Ahora si este proyecto está en total condiciones de ser aprobado, bien hecho!
#     
# Éxitos en tu camino dentro del mundo de los datos y saludos!

# <div class="alert alert-block alert-success">
# <b>Review General. (Iteración 1) </b> <a class="tocSkip"></a>
# 
# Cristhopher, siempre me tomo este tiempo al inicio del proyecto para comentar mis apreciaciones generales de esta primera iteración de la entrega.
# 
# Siempre me gusta comenzar dando la bienvenida al mundo de los datos a los estudiantes, te deseo lo mejor y espero que consigas lograr tus objetivos. Personalmente siempre me gusta brindar el siguiente consejo, "Está bien equivocarse, es normal y es lo mejor que te puede pasar. Aprendemos de los errores y eso te hará mejor programando ya que podrás descubrir cosas a medida que avances y son estas cosas las que te darán esa experiencia para ser mejor como Data Analyst"
#     
# Ahora si yendo a esta notebook. Quiero felicitarte y agradecerte por este proyecto Cristhopher, lo has resuelto de una forma espectacular, se ha notado a lo largo de todo el proceso tu gran manejo sobre python y las librerías que debían utilizarse. A la vez quiero destacar tu compromiso porque no solo has resuelto sino que lo has resuelto con creces. Más allá de algunos detalles a corregir el trabajo esta muy completo! Espero con ansias la próxima iteración.
# 
# Éxitos y saludos Cristhopher!

# <div class="alert alert-block alert-info">
# 
#  <b>Respuesta de estudiante.</b> <a class="tocSkip"></a>
#     
# Facundo, muchas gracias por tus palabras y tu detallada evaluación, Tus comentarios son muy valiosos para mí y me ayudarán a crecer como Data Analyst. Es muy motivador saber que mis esfuerzos son valorados y que he podido demostrar mis conocimientos en Python y las librerías. Agradezco enormemente tus consejos y tu guía a lo largo de este proyecto. Estoy comprometido a seguir mejorando y superando mis expectativas. ¡Espero con ansias la próxima etapa!

# # Diccionario de Datos <a id='diccionario'></a>
# 
# **Tabla rest_data:**
# 
# * object_name — nombre del establecimiento
# 
# * chain — establecimiento que pertenece a una cadena (TRUE/FALSE)
# 
# * object_type — tipo de establecimiento
# 
# * address — dirección
# 
# * number — número de asientos

# # Introducción <a id='introduccion'></a>
# 
# En el competitivo sector gastronómico, la ubicación y capacidad de los restaurantes juegan un papel crucial en el éxito del negocio. Este proyecto tiene como objetivo analizar la distribución del número de asientos en los restaurantes ubicados en las calles más comerciales de una ciudad, proporcionando una visión clara sobre las tendencias en la capacidad de los establecimientos en diferentes zonas.
# 
# El análisis se centra en las 10 calles con la mayor concentración de restaurantes, permitiendo identificar patrones, variabilidad en la capacidad de asientos, y la presencia de valores atípicos que podrían influir en la competitividad y estrategia de negocio. Al comprender estas dinámicas, es posible tomar decisiones más informadas sobre dónde abrir nuevos restaurantes, cómo segmentar el mercado y qué tipos de establecimientos podrían ser más exitosos en cada área.
# 
# A lo largo de este estudio, se ha utilizado un enfoque estadístico para explorar las diferencias entre las calles y cómo estas influyen en el tipo de oferta gastronómica disponible. Los resultados obtenidos nos permiten proponer recomendaciones estratégicas que pueden ser de gran utilidad tanto para los pequeños empresarios como para las grandes cadenas que busquen expandir o mejorar su presencia en estas calles comerciales.
# 
# Este proyecto ofrece no solo una descripción del estado actual de los restaurantes, sino también una base para decisiones futuras que optimicen la distribución y capacidad de los negocios en diferentes áreas de la ciudad, maximizando las oportunidades de éxito.

# In[1]:


import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np


# # DataFrame <a id='dataframe'></a>

# In[2]:


rest_date= pd.read_csv('/datasets/rest_data_us_upd.csv')
rest_date.head()


# In[3]:


#Realizamos una revision general de los datos.
rest_date.info()


# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Christhopher, bien realizada la importaciòn y una primera exploración de la base de datos!

# In[4]:


#Verificamos si tenemos presencia de datos ausentes.
rest_date.isna().sum()


# In[5]:


#Eliminamos los 3 datos ausentes de la columna 'chain' y verificamos si efectivamente se eliminaron.
rest_date= rest_date.dropna()
rest_date.isna().sum()


# In[6]:


#Verificamos ti tenemos presencia de datos duplicados.
rest_date.duplicated().sum()


# In[7]:


#Utilizamos el metodo describe en la columna number para tener una vision resumida de que contiene.
rest_date['number'].describe()


# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Y aquì un buen anàlisis para identificar duplicados y ver valores ausentes. Bien hecho!

# ### Observacion: <a id='observacion'></a>
# 
# Detectamos 3 datos ausentes los cuales corregimos eliminandolos del dataset, luego realizamos una busqueda de datos duplicados, no enconramos datos duplicados los supuestos datos duplicados en algunas columnas simplemente no lo son dado a que son datos que se pueden repetir dependiendo de si el establecimiento de encuentra en una misma calle que otros o si es una cadena o no etc.
# 
# Por ultimo revisamos un poco los datos de la columna number con el metodo duplicate para tener una mejor vision sobre que contiene nuentros datos numericos.

# #  Análisis de datos <a id='analisis'></a>

# ## Investigamos las proporciones de los distintos tipos de establecimientos. <a id='ipdte'></a>
# 

# In[8]:


# Calculamos las proporciones directamente con value_counts()
count_object_type = rest_date['object_type'].value_counts(normalize=True).reset_index()
count_object_type.columns = ['object_type', 'proportion']

# Formateamos las proporciones como porcentaje
count_object_type['proportion'] = (count_object_type['proportion'] * 100).round()

# Mostramos el resultado
count_object_type


# In[9]:


# Generamos un grafico circular

fig = px.pie(count_object_type, values='proportion', names='object_type', title="Proporciones de los distintos tipos de establecimientos")
fig.show()


# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Excelente análisis y comprensión del mismo, hemos logrado el objetivo de visualizar las proporciones de los establecimientos, excelente! 

# ### Observacion: <a id='observacion2'></a>
# 
# Como podemos observar en nuestro grafico los establecimientos con mayor proporcion son los restaurantes con un 75% luego le siguen los fast food solo con un 11% los demas establecimiento se situan entre un 5% y 3%.
# 
# Teniendo esto en cuenta podemos decir que en LA lo que sobran son Restaurantes.

# ## Investigamos las proporciones de los establecimientos que pertenecen a una cadena y de los que no. <a id='ipepc'></a>

# In[10]:


count_chain = rest_date[['object_type', 'chain']].value_counts(normalize=True).reset_index()
count_chain


# In[11]:


# Calculamos las proporciones directamente con value_counts()
count_chain = rest_date[['object_type', 'chain']].value_counts(normalize=True).reset_index()
count_chain.columns = ['object_type','chain', 'proportion']

# Formateamos las proporciones como porcentaje
count_chain['proportion'] = (count_chain['proportion'] * 100).round()

# Mostramos el resultado
print(count_chain)


# In[12]:


g = sns.catplot(
    data=count_chain, kind="bar",
    x="object_type", y="proportion", hue="chain",
     palette="viridis", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("", "Proporcion")
g.legend.set_title("Cadena")
g.fig.suptitle('Proporciones de los establecimientos que pertenecen a una cadena y de los que no', fontsize=10)


# ### Observacion: <a id='observacion3'></a>
# 
# Si bien los seis tipos de establecimientos pueden pertenecer a ambos segmentos, encontramos una marcada tendencia. Los restaurantes independientes son mayoría, mientras que en los establecimientos de comida rápida (fast food) y cafeterías predominan las cadenas. Los establecimientos de panadería (bakery) son operados exclusivamente por cadenas. Los bares, por su parte, son mayoritariamente independientes, y en las pizzerías ambos modelos coexisten en igual medida.  

# ## ¿Qué tipo de establecimiento es habitualmente una cadena? <a id='qtehc'></a>

# In[13]:


#Agrupamos los datos para obtener solo los establecimientos y si son cadenas o no. Luego valculamos la proporcion.
chain_object_type= round(rest_date.groupby('object_type')['chain'].value_counts(normalize=True)* 100)
# Renombramos la columna sin nombre a "Proporcion"
chain_object_type = chain_object_type.reset_index(name='proportion')
chain_object_type


# In[14]:


#Creemos un grafico para visualizar las proporciones de cada tipo de establecimiento
fig = px.sunburst(chain_object_type, path=['chain', 'object_type'], values='proportion', 
                  color='object_type', title='Proporciones de cada tipo de establecimiento')
fig.show()


# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Misma situación que la anterior, una conclusión que demuestra que anteriormente tu pudiste correr el código, debido a algun motivo que estaba rompiendo el mismo realicé un pequeño agregado para poder verlo y corroborarlo, felicitaciones!

# ### Observacion: <a id='observacion4'></a>
# 
# En este grafico circular podemos observar  que habitualmente pertecen a una cadena los establecimientos de Cafeteria, panaderia y comida rapida.
# 
# El grafico presenta las siguientes proporciones por establecimiento y tipo:
# 
# * Bakery:    100% True.
# 
# * Bar:        26% True, 74% False.
# 
# * Cafe:       61% True, 39% False.
# 
# * Fast Food:  57% True, 43% False.
# 
# * Pizza:      48% True, 52% False.
# 
# * Restaurant: 32% True, 68% False.
# 

# In[15]:


#Realizamos un grafico para visualizar las proporciones de cada establecimiento.
g = sns.catplot(
    data=chain_object_type, kind="bar",
    x="object_type", y="proportion", hue="chain",
     palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("", "Proporcion")
g.legend.set_title("Cadena")
g.fig.suptitle('Proporciones de cada tipo de establecimiento', fontsize=10)


# ### Observacion: <a id='observacion4.1'></a>
# 
# Los resultados de los análisis recientes corroboran la hipótesis de que las cadenas son predominantes en los sectores de panadería, cafetería y comida rápida. No obstante, en el segmento de pizzerías se observa una distribución más equilibrada, con una ligera ventaja para los establecimientos independientes.

# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 2)</b> <a class="tocSkip"></a>
# 
# Este gráfico está perfecto!

# ## ¿Qué caracteriza a las cadenas: muchos establecimientos con un pequeño número de asientos o unos pocos establecimientos con un montón de asientos? <a id='qccmepnapema'></a>

# In[16]:


# Crear un histograma para 'number' con diferentes colores para 'chain'
plt.figure(figsize=(10, 6))
sns.histplot(data=rest_date, x='number', hue='chain', kde=True, bins=20)
plt.title('Histograma de número de asientos por cadena')
plt.xlabel('Número de asientos')
plt.ylabel('Frecuencia')
plt.show()


# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
#     
# Excelente, esto es lo que se buscaba! La cantidad de bins puede variar, por lo general mientras mayor cantidad de bins mayor la precisión ya que tenems más intervalos agrupados, para este caso la cantidad es correcta!

# ### Observacion: <a id='observacion5'></a>
# 
# El análisis revela que la mayoría de los establecimientos, tanto cadenas como independientes, tienen una capacidad de entre 1 y 50 asientos (entre una frecuencia 800 y 1200 establecimientos en cada caso). Solo un número reducido (con frecuencia menos de 200) cuenta con una gran cantidad de asientos.

# In[17]:


#Realizamos un grafico de caja para visualizar como estan distribuidos nuestros datos
sns.boxplot(
    data=rest_date,
    x="object_type", y="number", hue="chain",
    palette="dark")
plt.title('Número de asientos por tipo y establecimiento', fontsize=10)


# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
#     
# Perfecto! Has podido resolver uno de los segmentos más complicados de este proyecto viendo la distribución de los asientos en tanto en las cadenas como no cadenas, contraste perfecto. Felicitaciones nuevamente!

# ### Observacion: <a id='observacion5.1'></a>
# 
# * Variación en el número de asientos: Existe una gran variación en el número de asientos para cada tipo de establecimiento, tanto para cadenas como para establecimientos independientes. Esto se evidencia por la longitud de las cajas y la presencia de valores atípicos (outliers).
# 
# * Mediana similar: La mediana del número de asientos es similar para Restaurantes que son cadenas y establecimientos independientes, en el resto de los establecimientos si se nota ladiferencia de su mediana
# 
# * Valores atípicos: Se observan valores atípicos en la mayoría de los tipos de establecimientos, lo que indica la presencia de algunos establecimientos con un número de asientos significativamente mayor como es el caso de los Restaurantes en cambio las cafeterias tienden a tener establecimientos con asientos por depajo de los 150.
# 
# * Diferencias entre tipos de establecimientos: Los restaurantes, Los Fast Food y los bares tienden a tener un mayor número de asientos en comparación con otros tipos de establecimientos, como cafeterías o panaderías.

# In[18]:


# Agrupamos los datos por tipo de establecimiento y cadena para obtener el promedio de asientos
average_seats= round(rest_date.groupby(['object_type', 'chain'])['number'].mean()).reset_index()
average_seats


# In[19]:


#Realizamos un grafico de barras
g = sns.catplot(
    data=average_seats, kind="bar",
    x="object_type", y="number", hue="chain",
    palette="bright", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("", "Numero de asientos")
g.legend.set_title("Cadena")
g.fig.suptitle('Promedio número de asientos por tipo de establecimiento y cadena', fontsize=10)


# ### Observacion: <a id='observacion5.2'></a>
# 
# * Se observa que los restaurantes, ya sean independientes o parte de una cadena, tienden a tener un mayor número de asientos en comparación con otros tipos de establecimientos.
# 
# * Los establecimientos de comida rápida, si bien tienen una cantidad considerable de asientos cuando son parte de una cadena, la cantidad disminuye significativamente cuando son independientes.
# 
# * Las cafeterías, panaderías y pizzerias, en general, tienen un número menor de asientos, independientemente de si son parte de una cadena o no.
# 
# * En el caso de los Bares, se observa una ligera diferencia, donde las cadenas tienden a tener un promedio menor de asientos en comparación con los bares independientes.
# 
# * En resumen, el tipo de establecimiento y si pertenece o no a una cadena influyen en el número promedio de asientos. Los restaurantes y los bares tienden a tener un mayor número de asientos, mientras que otros tipos de establecimientos, como cafeterías, panaderías, comida rapida y Pizzerias, suelen tener un número menor de asientos.
# 
# Podriamos Decir en base a nuestro analisis que lo que caracteriza a las franquicias en su gran mayoria son pocos establecimientos con un monton de asientos.

# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Perfecta visualización de los promedios Cristopher! Bien hecho!

# ## Determinamos el promedio de número de asientos para cada tipo de restaurante en general. De promedio, ¿qué tipo de restaurante tiene el mayor número de asientos? <a id='dpnactrptrtmna'></a>

# In[20]:


#Agrupamos los datos por object_type, y sacamos la media de el numero de asientos
number_mean= round(rest_date.groupby('object_type')['number'].mean()).reset_index().sort_values(by='number', ascending=False)
number_mean


# In[21]:


#Realizamos un grafico de barras con plotly.express
fig = px.bar(number_mean, x='object_type', y='number', color="object_type", title='Promedio de número de asientos para cada tipo de restaurante en general')
fig.show()


# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
#     
# Excelente! Simple y conciso.

# ### Observacion: <a id='observacion6'></a>
# 
# Los restaurantes lideran en cuanto a capacidad, con un promedio de 48 asientos. Les siguen los bares con 40, establecimientos de comida rápida 32, pizzerías 29, cafeterías 25 y, finalmente, las panaderías con 22 asientos en promedio.

# ## Colocamos los datos de los nombres de las calles de la columna address en una columna separada. <a id='cdnccacs'></a>

# In[22]:


# Usamos una expresión regular para eliminar los números al principio y al final de las direcciones.
rest_date['street_name'] = rest_date['address'].apply(lambda x: ' '.join(x.split()[1:]))
rest_date.head()


# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 2)</b> <a class="tocSkip"></a>
# 
# Ahora si! Podemos ver que los nombres se reflejan correctamente.

# ## Trazamos un gráfico de las diez mejores calles por número de restaurantes <a id='tgdmcnr'></a>

# In[23]:


#Calculamos cuantos restaurantes hay en cada calle con el metodo value_counts

filtered_number_rest= rest_date['street_name'].value_counts().head(10).reset_index()
filtered_number_rest.columns = ['street_name', 'number_rest']
filtered_number_rest


# In[24]:


#Realizamos el grafico
g = sns.catplot(
    data=filtered_number_rest, kind="bar",
    x="street_name", y="number_rest", hue="street_name",
     palette="viridis", legend=True
)
plt.xticks(rotation=80)
plt.title('Top 10 calles con mayor cantidad de restaurantes', fontsize=20)


# ### Observacion: <a id='observacion7'></a>
# 
# Las calles con mayor concentración de establecimientos gastronómicos son W Sunset Blvd y W Pico Blvd, ambas llegan casi a los 300 restaurantes. Le sigue HOLLYWOOD BLVD y WILSHIRE BLVD con poco más de 150. El resto de las calles analizadas presentan un rango de entre 150 y menos de 200 restaurantes.

# ## Encontramos el número de calles que solo tienen un restaurante. <a id='enctr'></a>

# In[25]:


#Filtramos las calles que solo tienen un restaurante.
street_one_rest= rest_date['street_name'].value_counts().reset_index()
street_one_rest.columns = ['street_name', 'number_rest']
one= street_one_rest[street_one_rest['number_rest'] == 1]

print('Numero de calles que tienen un solo restaurante: ', one['street_name'].nunique())
print('Porcentajes de los datos que pertecen a locales con calles que tienen 1 solo restaurante: ', round((one['street_name'].nunique() / rest_date['id'].count()) * 100, 2), '%')


# ### Observacion:
# 
# Luego de nuestro analisis podemos saber que un cuarto de nuestro datos son de calles en las cuales son hay presencia de 1 solo establecimiento.
# 

# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 2)</b> <a class="tocSkip"></a>
#     
# Ahora si! Has llegado al nùmerocorrecto de calles buscadas.

# ## Para las calles con muchos restaurantes, analizamos la distribución del número de asientos. <a id='pcmradna'></a>

# In[26]:


#Filtramos los datos para obtener solo los datos de las 10 calles con mayores restaurantes
top_10_streets_number = filtered_number_rest['street_name'].tolist()
rest_date_top_10_streets = rest_date[rest_date['street_name'].isin(top_10_streets_number)]
rest_date_top_10_streets.head()


# In[27]:


# Realizamos un grafico circular interactivo
fig = px.sunburst(rest_date_top_10_streets, path=['chain', 'street_name', 'object_type'], values='number', color='street_name',
                  title='Distribución del número de asientos del top 10 de las mejores calles')
fig.show()


# In[28]:


# prompt: generemos un grafico de barras con los datos del grafico circular 'Distribución del número de asientos del top 10 de las mejores calles'

# Obtener la suma de asientos por calle
seats_per_street = rest_date_top_10_streets.groupby(['street_name', 'chain'])['number'].sum().reset_index().sort_values(by='number', ascending=False)

g = sns.catplot(
    data=seats_per_street, kind="bar",
    x="street_name", y="number", hue="chain",
    palette="viridis", alpha=.6, height=6, legend=True
)
plt.xticks(rotation=80)
plt.title('Número de asientos en total del top 10 de las mejores calles', fontsize=15)
plt.ylabel('Asientos en Total')
plt.xlabel('Calles')
g.legend.set_title("Cadena")


# ### Observacion: <a id='observacion8'></a>
# 
# El análisis de nuestros datos revela que las calles con mayor concentración de asientos, pertenecen a los establecimientos independientes, las calles son W Sunset Blvd (10.145), W Pico Blvd (8.249), Wilshire Blvd (6.849) y Hollywood Blvd (6.495). Estos resultados corroboran los hallazgos de nuestro análisis previo.

# In[29]:


#Realizamos el grafico para visualizar la distribucion de asientos

sns.distplot(rest_date_top_10_streets['number'], bins=20)
plt.title('Distribución del número de asientos del top 10 de las mejores calles')
plt.xlabel('Número de asientos')
plt.ylabel('Frecuencia')


# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
#     
# Excelente! Efectivamente un gráfico de histograma es la elección adecuada para presentar estos datos. Felicitaciones!
#     

# ### Observacion: <a id='observacion8.1'></a>
# 
# Se observa una concentración de restaurantes con un número de asientos entre 0 y 50, con una disminución gradual a medida que aumenta el número de asientos. Esto sugiere que en las calles más concurridas, los restaurantes tienden a ser más pequeños, posiblemente debido a limitaciones de espacio o a una mayor demanda de opciones de comida rápida o informal.

# In[30]:


# prompt: ayudame a crear un grafico para poder analizar la distribución del número de asientos del top 10 de calles con mayor cantidad de restaurantes.

# Filtramos los datos para obtener solo los datos de las 10 calles con mayores restaurantes
top_10_streets_number = filtered_number_rest['street_name'].tolist()
rest_date_top_10_streets = rest_date[rest_date['street_name'].isin(top_10_streets_number)]

# Creamos el gráfico
plt.figure(figsize=(12, 6))
sns.boxplot(x='street_name', y='number', data=rest_date_top_10_streets)
plt.title('Distribución del número de asientos del top 10 de calles con mayor cantidad de restaurantes')
plt.xlabel('Nombre de la calle')
plt.ylabel('Número de asientos')
plt.xticks(rotation=45)
plt.show()


# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
#     
# Bien hecho!

# ### Observacion: <a id='observacion8.2'></a>
# 
# **Mediana del número de asientos:**
# 
# * Las medianas de todas las calles están por debajo de los 50 asientos. Esto sugiere que en la mayoría de los restaurantes de estas calles, la capacidad está por debajo de este umbral.
# 
# **Calles con mayor capacidad en restaurantes:**
# 
# * WILSHIRE BLVD parece tener la mayor capacidad de asientos, con una mediana ligeramente superior a otras calles.
# 
# * HOLLYWOOD BLVD y W SUNSET BLVD también presentan capacidades medianas relativamente altas en comparación con otras calles.
# 
# **Variabilidad en el número de asientos:**
# 
# * HOLLYWOOD BLVD, W SUNSET BLVD, y WILSHIRE BLVD tienen una mayor dispersión, lo que sugiere que los restaurantes en estas calles tienen una mayor diversidad en cuanto al número de asientos (desde restaurantes pequeños hasta grandes).
# 
# * En contraste, calles como SANTA MONICA BLVD y S VERMONT AVE tienen menos variabilidad, lo que sugiere una capacidad de asientos más homogénea.
# 
# **Presencia de outliers:**
# 
# * En casi todas las calles se observan muchos valores atípicos (outliers), lo que indica que algunos restaurantes tienen una capacidad de asientos considerablemente mayor en comparación con la mayoría.
# 
# **Calles con menor capacidad:**
# 
# * Calles como SANTA MONICA BLVD y S VERMONT AVE tienen la mediana más baja, lo que sugiere que, en promedio, los restaurantes en estas calles tienen menos asientos en comparación con otras calles del gráfico.
# 
# En resumen, aunque la capacidad de asientos varía de manera significativa entre las calles, WILSHIRE BLVD, HOLLYWOOD BLVD y W SUNSET BLVD parecen ser las calles con los restaurantes de mayor capacidad, mientras que otras como SANTA MONICA BLVD y S VERMONT AVE tienen restaurantes más pequeños en promedio.

# # Conclusion Generales <a id='conclusion'></a>
# 
# **Distribución general del número de asientos:**
# 
# * La mayoría de los restaurantes en las calles analizadas tienen una capacidad mediana de asientos relativamente baja, en su mayoría por debajo de los 50-100 asientos.
# 
# * Existen calles como WILSHIRE BLVD, HOLLYWOOD BLVD, y W SUNSET BLVD, que tienen restaurantes con una capacidad mediana y una alta dispersión, lo que indica la coexistencia de pequeños restaurantes junto con otros de gran capacidad.
# 
# * Por el contrario, calles como SANTA MONICA BLVD y S VERMONT AVE tienden a tener restaurantes con capacidades más homogéneas y generalmente más pequeñas.
# 
# **Presencia de valores atípicos:**
# 
# * En casi todas las calles, hay valores atípicos significativos que representan restaurantes con una cantidad de asientos muy superior a la media, lo que podría indicar algunos grandes establecimientos o cadenas.
# 
# **Tendencias y patrones:**
# 
# * Las calles más comerciales y céntricas, como WILSHIRE BLVD y HOLLYWOOD BLVD, tienden a tener una mayor capacidad promedio y una mayor dispersión en el tamaño de los restaurantes, lo que podría sugerir una oferta variada, tanto en tipo de restaurantes como en la experiencia gastronómica que ofrecen.
# 
# **Impacto potencial en los negocios:**
# 
# * Calles con mayor variabilidad en el tamaño de los restaurantes pueden ofrecer una oferta más diversa, atrayendo a un público más amplio y promoviendo la competencia entre grandes y pequeños establecimientos.
# 
# * Las calles con restaurantes más homogéneos podrían ofrecer una experiencia más estándar, pero podrían limitar la atracción de grandes grupos o eventos que requieren más espacio.

# # Recomendaciones <a id='recomendaciones'></a>
# 
# **Segmentación del mercado y estrategias diferenciadas:**
# 
# * Calles con mayor variabilidad como WILSHIRE BLVD y HOLLYWOOD BLVD podrían beneficiarse de una estrategia de segmentación, ofreciendo tanto restaurantes pequeños y exclusivos como grandes establecimientos para grupos y eventos.
# 
# * Las cadenas de restaurantes más grandes podrían beneficiarse de una presencia en estas áreas, donde los valores atípicos sugieren la aceptación de restaurantes con gran capacidad.
# 
# **Desarrollo de restaurantes en calles con menos variabilidad:**
# 
# * Para calles como SANTA MONICA BLVD y S VERMONT AVE, sería recomendable evaluar el mercado local para explorar la apertura de restaurantes más grandes o cadenas que puedan cubrir una posible necesidad de mayor capacidad en estas áreas.
# 
# * Estas calles podrían beneficiarse de la diversificación en la oferta gastronómica, introduciendo restaurantes temáticos o aquellos que ofrezcan experiencias diferentes para atraer a nuevos clientes.
# 
# **Aprovechar la presencia de outliers:**
# 
# * Los restaurantes que están en los valores atípicos (aquellos con mayor número de asientos) podrían ser promovidos como lugares para eventos especiales, aprovechando su capacidad para grupos grandes, lo que puede atraer una nueva clientela.
# 
# **Monitoreo continuo de tendencias:**
# 
# * Es importante seguir monitoreando la evolución del tamaño y capacidad de los restaurantes para adaptar las estrategias comerciales. En calles con rápido crecimiento, como HOLLYWOOD BLVD, podría haber cambios importantes en la competencia, lo que obligaría a ajustar las ofertas y estrategias de marketing.
# 
# Estas conclusiones y recomendaciones ayudarán a optimizar el desarrollo y expansión de restaurantes, dependiendo del tipo de calle y su perfil actual de capacidad de asientos.

# Link de la Presentacion: https://drive.google.com/file/d/1OnopAchB0faHQz_YfLfGJwjoDOZ8Uzbq/view?usp=sharing

# <div class="alert alert-block alert-success">
# 
# <b>Comentario del revisor. (Iteración 1)</b> <a class="tocSkip"></a>
# 
# Cristhopher, la presentación está muy clara. Está bien pensada la comunicación hacia un potencial cliente. Felicitaciones!
