
import math
import numpy as np

class Neuron:
    
    def __init__(self, weights, inputs, bias):
        self.weights = weights
        self.inputs = inputs
        self.bias = bias
    
    def summation(self):
        weighted_inputs = ()
        for i in range(0, len(self.inputs)):
           weighted_inputs = weighted_inputs + ((self.weights[i] * self.inputs[i]),) 
        return sum(weighted_inputs) + self.bias

    def transfer_function(self):
        x = self.summation()
        sigmoid_output = 1/(1+(math.e ** x))
        return sigmoid_output

class Network:

    def __init__(self) -> None:
        pass
    
    '''
    x: input (vector of inputs)
    
    y: target output of network (also a vector)

    C: loss function 
    
    
    '''
    def cost_function(self):
        return 0

    def backprop(self):
        return 0

if __name__ == "__main__":
    weights = (-100,-300)
    inputs = (5,6)
    bias = 4
    neuron = Neuron(weights, inputs, bias)
    print(neuron.transfer_function())