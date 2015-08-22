import numpy as np

# 
# Your previous Plain Text content is preserved below:
# 
# 
# N x M Matrix 
# Point located at x;y coordinate
# 
# After K moves, What is the probability the point is dead 
# 
# x=1
# y=0
# 
initial_matrix = np.array([[1, 2, 3],
                 [4, 5, 6]])
# 
# K=1
# Initial Matrix 
# 
# M = [[0.50, 0.75, 0.50]
#  [0.75, 1.00, 0.75]
#  [0.50, 0.75, 0.50]]


def probability_point_is_dead(point):
    x, y = point

def compute_probability_matrix(initial_matrix):
#     TODO: Check for IndexError when initial_matrix is empty
    N, M = initial_matrix.shape
    result = np.ones(initial_matrix.shape)
    result[0, 0] = 0.5
    
    return result

print(compute_probability_matrix(initial_matrix))

def compute_transition_matrix(probability_matrix):
    pass


# K=2
#    0.25                0.375
# [[0.50*.25*(.5+.75+.75)  , 0.75*.25(.5+1+.5), 0.50]
#  [0.75, 1.00, 0.75]
#  [0.50, 0.75, 0.50]]
# 
# K=3
# [[0.50*.25*(.5+.75+.75)*.25*(.5+.75+.75)  , 0.75*.25(.5+1+.5), 0.50]
#  [0.75, 1.00, 0.75]
#  [0.50, 0.75, 0.50]]
# 
# K=4
# [[0.50*.25*(.5+.75+.75)*.25*(.5+.75+.75) *(.5+.75+.75) , 0.75*.25(.5+1+.5), 0.50]
#  [0.75, 1.00, 0.75]
#  [0.50, 0.75, 0.50]]
#  
# Transition Matrix
# T = [[]]
# 
# p = probability of moving to that cell = 1/4
# 
# Final Matrix = M .* (p .* T)^k
# 
# 
# probability of dying in the next step:
# 
# 
# 
# 
# 
# for each cell:
#   take the initial probability
#     multiply by 1/4
#     multiply by the sum of all the neighboring probabilities
#     



# 
