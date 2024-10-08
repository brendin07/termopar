import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_excel("calibracao_termopar.xlsx")


x_Sens1 = df[['sensor 1 mV']]
y_temp = df['Temperatura °C']  


modelo = LinearRegression()
modelo.fit(x_Sens1, y_temp)

x_Sens2 = df[['sensor 2 mV']]
y_temp = df['Temperatura °C']  

modelo2 = LinearRegression()
modelo2.fit(x_Sens2,y_temp)


y_pred1 = modelo.predict(x_Sens1)
print('modelo 1', y_pred1)


y_pred2 = modelo2.predict(x_Sens2)
print('modelo2', y_pred2)

plt.scatter(x_Sens1, y_temp, color = 'blue', label = 'sensor 1 mV')
plt.plot(x_Sens1, y_pred1, color = 'blue', label = 'linha de regressao 1')


plt.scatter(x_Sens2, y_temp, color = 'blue', label = 'sensor 2 mV')
plt.plot(x_Sens2, y_pred2, color = 'blue', label = 'linha de regressao 2')

plt.xlabel('tensao em (mV)')
plt.ylabel('temperatura em (°C)')
plt.title('regressao linear : temperatura (°C) vs. tensao (mV)')
plt.legend()
plt.show()


resultados_df = pd.DataFrame ({                 
    'sensor 1 mV' : x_Sens1 ['sensor 1 mV'],
    'sensor 2 mV' : x_Sens2 ['sensor 2 mV'],
    'Temperatura °C':y_temp,
    'Modelo 1 ' : y_pred1,
    'Modelo 2' :  y_pred2
})

resultados_df.to_excel(' Modelagem.xlsx', index=False)