# Use the numpy library
import numpy as np


def prepare_inputs(inputs):
    # TODO: create a 2-dimensional ndarray from the given 1-dimensional list;
    #       assign it to input_array
    input_array = np.array(inputs).reshape(3,1)
    
    # TODO: find the minimum value in input_array and subtract that
    #       value from all the elements of input_array. Store the
    #       result in inputs_minus_min
    min=input_array[0]
    for i in input_array:
        if i<min:
            min=i
    inputs_minus_min = input_array-min

    # TODO: find the maximum value in inputs_minus_min and divide
    #       all of the values in inputs_minus_min by the maximum value.
    #       Store the results in inputs_div_max.
    max=inputs_minus_min[0]
    for i in inputs_minus_min:
        if i>max:
            max=i
    inputs_div_max = inputs_minus_min//max
    #inputs_div_max = np.divide(input_max_min,max)

    # return the three arrays we've created
    return input_array, inputs_minus_min, inputs_div_max
    

def multiply_inputs(m1, m2):
    # Check the shapes of the matrices m1 and m2. 
    # m1 and m2 will be ndarray objects.
    #
    # Return False if the shapes cannot be used for matrix
    # multiplication. You may not use a transpose
    if m1.shape[0] != m2.shape[1] and m1.shape[1] != m2.shape[0]:     
        return False

    # Have not returned False, so calculate the matrix product
    # of m1 and m2 and return it. Do not use a transpose,
    #       but you swap their order if necessary
    if m1.shape[1] == m2.shape[0]:
        return np.matmul(m1, m2)        
    else:
        return np.matmul(m2, m1)        

        
    
    

   

def find_mean(values):
    m=0
    for i in values:
        m+=i
        
    return m/len(values)


input_array, inputs_minus_min, inputs_div_max = prepare_inputs([-1,2,7])
print("Input as Array: {}".format(input_array))
print("Input minus min: {}".format(inputs_minus_min))
print("Input  Array: {}".format(inputs_div_max))

print("Multiply 1:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3],[4]]))))
print("Multiply 2:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3]]))))
print("Multiply 3:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1,2]]))))

print("Mean == {}".format(find_mean([1,3,4])))
