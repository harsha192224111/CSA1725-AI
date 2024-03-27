
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class FeedForwardNN:
    def __init__(self, num_inputs, num_hidden_units, num_outputs):
        self.num_inputs = num_inputs
        self.num_hidden_units = num_hidden_units
        self.num_outputs = num_outputs

        self.weights_input_hidden = np.random.rand(self.num_inputs, self.num_hidden_units)
        self.weights_hidden_output = np.random.rand(self.num_hidden_units, self.num_outputs)

    def forward_pass(self, inputs):
       
        self.hidden_activation = sigmoid(np.dot(inputs, self.weights_input_hidden))
        self.output_activation = sigmoid(np.dot(self.hidden_activation, self.weights_hidden_output))
        return self.output_activation

num_inputs = 3
num_hidden_units = 4
num_outputs = 2

model = FeedForwardNN(num_inputs, num_hidden_units, num_outputs)

input_data = np.random.rand(1, num_inputs)

output_data = model.forward_pass(input_data)

print("Output:", output_data)
