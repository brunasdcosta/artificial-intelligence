import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

file_path = 'diabetes.xlsx'
dataframe = pd.read_excel(file_path, engine='openpyxl')

x = dataframe.iloc[:, :-1]
y = dataframe['Diagnóstico'].values

scaler = MinMaxScaler()
x_transformed = scaler.fit_transform(x)

for i in range(len(x_transformed)):
	for j in range(len(x_transformed[i])):
		if x_transformed[i][j]==0 and x.iat[i,j]!=0:
			print(f'[{i}][{j}] - 0 - {x_transformed[i][j]} - {x.iat[i,j]}')
		if x_transformed[i][j]==1 and x.iat[i,j]!=1:
			print(f'[{i}][{j}] - 1 - {x_transformed[i][j]} - {x.iat[i,j]}')
		if x_transformed[i][j]<0:
			print(f'[{i}][{j}] - negativo - {x_transformed[i][j]}')
		if x_transformed[i][j]>1:
			print(f'[{i}][{j}] - maior que 1 - {x_transformed[i][j]}')

transformed = x_transformed.tolist()

for i in range(len(transformed)):
	transformed[i].append(y[i])
	for j in range(len(transformed[i])):
		if transformed[i][j]!=0 and transformed[i][j]!=1:
			transformed[i][j] = float(str(round(transformed[i][j], 2)))

columns_names = ['Gravidez','Glicose','Pressão','Pele','Insulina','Massa Corpórea','Genealogia','Idade','Diagnóstico']
dataframe = pd.DataFrame(transformed, columns=columns_names)
dataframe.to_excel('diabetes-normalizada2.xlsx', index=False)