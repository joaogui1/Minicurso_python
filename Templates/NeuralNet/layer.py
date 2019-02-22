import numpy as np

# Activation functions
def tanh(x):
  return np.tanh(x)

# Derivative of tanh from its output
def dtanh(y):
  return 1 - y ** 2

# The neural network framework
class Layer:
  def __init__(self, num_inputs, num_outputs):
    # Init all weights between [-1 .. 1].
    # Each input is connected to all outputs.
    # One line per input and one column per output.
        pass

  def forward(self, input):
      pass
  def computeGradient(self, error):
      pass
  def updateWeights(self, input, learning_rate):
      pass
