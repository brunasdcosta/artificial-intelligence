import numpy as np # pip install numpy
import pandas as pd # pip install pandas
from imblearn.over_sampling import SMOTE # pip install imbalanced-learn

def run(file_path, out_name):
	dataframe = pd.read_excel(file_path, engine='openpyxl') # Carregando os dados.

	x = dataframe.iloc[:, :-1] # Conjunto de valores X (entradas).
	y = dataframe.iloc[:, -1] # Conjunto de valores Y (saídas).

	sm = SMOTE(random_state = 25)

	x_transformed, y_transformed = sm.fit_resample(x, y)

	# print(f'''Shape of X before SMOTE: {x.shape}
	# Shape of X after SMOTE: {x_sm.shape}''')

	# print('\nBalance of positive and negative classes (%):')
	# print(y_sm.value_counts(normalize=True) * 100)

	transformed = x_transformed.values.tolist()
	y_list = y_transformed.values.tolist()

	for i in range(len(transformed)):
		transformed[i].append(y_list[i])

	columns_names = ['Gravidez','Glicose','Pressão','Pele','Insulina','Massa Corpórea','Genealogia','Idade','Diagnóstico']
	dataframe = pd.DataFrame(transformed, columns=columns_names)
	dataframe.to_excel(out_name, index=False)

run('diabetes2.xlsx', 'diabetes3.xlsx') # Sobre os dados normalizados.
run('diabetes.xlsx', 'diabetes4.xlsx') # Sobre os dados sem tratamento.