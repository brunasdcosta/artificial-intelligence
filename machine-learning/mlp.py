import numpy as np # pip install numpy
import pandas as pd # pip install pandas
from sklearn.neural_network import MLPClassifier # pip3 install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import time
import warnings

warnings.filterwarnings('ignore')

def get_performance(mlp, set_type, x, y, mark_time=False):
	print(f'\t\t\t{set_type}')
	print('_'*54)
	start = None
	end = None
	if mark_time:
		start = time.time()
	predictions = mlp.predict(x)
	if mark_time:
		end = time.time()
		print(f'Tempo de resposta: {end-start} segundos')
	conf_matrix = confusion_matrix(y, predictions)
	print(conf_matrix)
	print(classification_report(y, predictions))
	print(f'Falsos positivos: {conf_matrix[0][1]} ({conf_matrix[0][1]/17.02}%)')
	print(f'Falsos negativos: {conf_matrix[1][0]} ({conf_matrix[1][0]/17.02}%)')

def run(x_train, x_test, y_train, y_test):
	mlp = MLPClassifier(solver = 'sgd',
						activation = 'logistic', # Função de propagação.
						hidden_layer_sizes = (4), # Número e dimensão de camada escondida.
						alpha = 0.01,
						learning_rate = 'adaptive',
						learning_rate_init = 0.005,
						momentum = 0.9,
						nesterovs_momentum = True,
						tol = 1e-2, # Tolerância para encerramento do treino.
						max_iter = 1000, # Número máximo de iterações.
						verbose = False, # Visualização das etapas do treino.
						early_stopping = False, # Possibilidade de parar o treino antes dos 1000 ciclos.
						shuffle = True, # Embaralha o conjunto de treino a cada novo ciclo.
						n_iter_no_change = 20) # Parada antecipada caso não melhore em x ciclos consectivos.
	start = time.time() # Marcando o tempo de início do treino.
	mlp.fit(x_train, y_train) # Executando o treino.
	end = time.time() # Marcando o tempo de fim do treino.
	print(f'Tempo de treino: {end-start} segundos')
	print(f'Quantidade de ciclos realizados: {mlp.n_iter_}')
	print('_'*54)
	get_performance(mlp, 'Treino', x_train, y_train) # Apresentando o desempenho alcançado sobre o próprio conjunto de treino.
	print('_'*54)
	get_performance(mlp, 'Teste', x_test, y_test, True) # Apresentando o desempenho alcançado sobre o conjunto de teste.

file_path = 'diabetes.xlsx'
dataframe = pd.read_excel(file_path, engine='openpyxl') # Carregando os dados.
x = dataframe.iloc[:, :-1] # Conjunto de valores X (entradas).
y = dataframe.iloc[:, -1] # Conjunto de valores Y (saídas).
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 25) # Dividindo os dados entre conjunto de teste e de treino.
print(f'{"_"*54}\n \t\t Dados sem tratamento\n{"_"*54}')
run(x_train, x_test, y_train, y_test)