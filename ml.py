# import numpy as np
# def sigmoid(x):
#   return 1/(1+np.exp(-x))

# training_inputs = np.array([[0,0,1],
#                             [1,1,1],
#                             [1,0,1],
#                             [0,1,1]])

# training_outputs = np.array([[0,1,1,0]]).T

# np.random.seed(1)

# synaptic_weight = 2 * np.random.random((3,1)) - 1

# print("коеф")
# print(synaptic_weight)

# for i in range(20000):
#   input_leyer = training_inputs
#   outputs = sigmoid(np.dot(input_leyer, synaptic_weight))

#   err = training_outputs - outputs
#   adjustments = np.dot(input_leyer.T, err * (outputs * (1 - outputs)))

#   synaptic_weight += adjustments

# print("коеф після навчання")
# print(synaptic_weight)

# print("результат")
# print(outputs)