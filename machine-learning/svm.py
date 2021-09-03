import numpy as np # pip install numpy
import pandas as pd # pip install pandas
from sklearn.svm import SVC # pip3 install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import time
import warnings

warnings.filterwarnings('ignore')

def get_performance(svm, set_type, x, y):
	print(f'\t\t\t{set_type}')
	print('_'*54)
	predictions = svm.predict(x)
	conf_matrix = confusion_matrix(y, predictions)
	print(conf_matrix)
	print(classification_report(y, predictions))
	print(f'Falsos positivos: {conf_matrix[0][1]} ({conf_matrix[0][1]/17.02}%)')
	print(f'Falsos negativos: {conf_matrix[1][0]} ({conf_matrix[1][0]/17.02}%)')

def run_svm(x_train, x_test, y_train, y_test):
	svm = SVC(	C = 5.0,
				kernel = 'sigmoid',
				gamma = 'auto', # Se 'scale', então usa 1/(n_features*x.var()) como valor de gama. Se 'auto', usa 1/n_features.
				coef0 = 4,
				tol = 0.01, # Tolerância para encerramento do treino.
				shrinking = True, # Uso da heurística de encolhimento.
				probability = False, # Usa 5-fold cross validation.
				cache_size = 2048, # Tamanho da cache do kernel (em MB).
				verbose = False, # Visualização dos resultados intermediários do treino.
				max_iter = -1) # Limite rígido nas iterações no solver ou -1 para nenhum limite.
	start = time.time() # Marcando o tempo de início do treino.
	svm.fit(x_train, y_train) # Executando o treino.
	end = time.time() # Marcando o tempo de fim do treino.
	print(f'Tempo de treino: {end-start} segundos')
	print('_'*54)
	get_performance(svm, 'Treino', x_train, y_train) # Apresentando o desempenho alcançado sobre o próprio conjunto de treino.
	print('_'*54)
	get_performance(svm, 'Teste', x_test, y_test) # Apresentando o desempenho alcançado sobre o conjunto de teste.

def run(file_path, name):
	dataframe = pd.read_excel(file_path, engine='openpyxl') # Carregando os dados.
	x = dataframe.iloc[:, :-1] # Conjunto de valores X (entradas).
	y = dataframe.iloc[:, -1] # Conjunto de valores Y (saídas).
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 25) # Dividindo os dados entre conjunto de teste e de treino.
	print(f'{"_"*54}\n{name}\n{"_"*54}')
	run_svm(x_train, x_test, y_train, y_test)

run('diabetes.xlsx', ' \t\t Dados sem tratamento')
run('diabetes2.xlsx', ' \t\tDados com normalização')
run('diabetes3.xlsx', ' \t Dados com normalização e distribuição igual')
run('diabetes4.xlsx', ' \t      Dados com distribuição igual')