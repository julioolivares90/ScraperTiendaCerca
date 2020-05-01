import pandas as pd
from pandas import read_excel

FILE_NAME = 'Datos.xlsx' #nombre del archivo de excel que contiene los datos en varias hojas
MY_SHEET ='Hoja1' #nombre de la una hoja selecconada

FILE_FINAL = 'DatosFinalFinal.xlsx' #nombre del excel final que contendra los datos del archivo anterior
df = read_excel(FILE_NAME,sheet_name=MY_SHEET)#lee el primer archivo de excel

datos = pd.DataFrame() #crea un objeto de tipo dataframe donde se copiaran los datos de FILE_NAME

diccionario = pd.read_excel(FILE_NAME,sheet_name=None)#lee el archivo excel de FILE_NAME

for nombre , columna in diccionario.items():#recorre el diccionario anterior
    datos = datos.append(columna,ignore_index=True) # asigna los valores al dataframe anterior

writer = pd.ExcelWriter(FILE_FINAL,engine='openpyxl')# prepara para escribir los datos del dataframe en el archivo excel usando el motor de openpyxl
datos.to_excel(writer)#escribe en el excel
writer.save()#guarda los datos