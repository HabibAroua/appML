from numpy import array
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
import subprocess
import webbrowser
import sys

url = 'https://www.facebook.com'
if sys.platform == 'darwin':    # in case of OS X
    subprocess.Popen(['open', url])
else:
    webbrowser.open_new_tab(url)


# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
	X, y = list(), list()
	for i in range(len(sequence)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the sequence
		if end_ix > len(sequence)-1:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)

# define input sequence
raw_seq = [57.5680, 99.5017, 100.000, 77.8002, 89.6547, 82.2569, 70.6391, 91.2530, 100.000 , 99.6325 , 80.2596]
# choose a number of time steps
n_steps = 3
# split into samples
X, y = split_sequence(raw_seq, n_steps)
# reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 1
X = X.reshape((X.shape[0], X.shape[1], n_features))
# define model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')
# fit model
model.fit(X, y, epochs=200, verbose=0)
# demonstrate prediction
x_input = array([min(raw_seq),(max(raw_seq)+(min(raw_seq))/2),max(raw_seq)])
x_input = x_input.reshape((1, n_steps, n_features))
yhat = model.predict(x_input, verbose=0)
print('the result is ')
print(yhat)
#https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/
