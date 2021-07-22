# Importing modules.
import random
import string
import matplotlib.pyplot as plt

# Complete string set.
# Not using digits and other punctuations as it increases the 
# running time.
string_data = string.ascii_lowercase + string.ascii_uppercase \
            + ' ' +  ',' + '!' + '.'

# Creating a function for generating parents.
def gen_parent(string_data, target_string):
    '''Generates a parent string.  
       Input  - 1. Population data.
                2. Target data.
       Output - Returns a randomly generated string with size 
                equal to the target data.
    '''  
    # Length of target string.
    l = len(target_string)

    if l > len(string_data):
        raise Exception('Provided input string is larger than population.')                     
    
    # Creating random parent.
    parent = random.sample(string_data, l)   
    return ''.join(parent)                     

# Creating function to calculate fitness.
def fitness(parent, target_string):
    '''Calculates fitness of the string.
       Input  - 1. Randomly generated string. 
                2. Target data.
       Output - Returns fitness value of the randomly generated string
                by comparing it with target data.
    '''
    return sum(1 for i in range(len(target_string)) \
               if target_string[i] == parent[i])

# Creating function for mutation.
def mutate(parent):
    '''Mutates a value of the string.
       Input  - Randomly generated string.
       Output - Returns mutated string after performing one-point
                crossover mutation.
    '''
    # Selecting a random index for mutation.
    index = random.randrange(0, len(parent))
    child_list = list(parent)

    # If the mutation value is same as index value then
    # assign it with alternate value.
    mutate_value, alternate_value = random.sample(string_data, 2)

    if child_list[index] != mutate_value:
        child_list[index] = mutate_value 
    else:
        child_list[index] = alternate_value 

    return ''.join(child_list)

# Creating function for best gene.
def best_gene(iterations, parent, parent_fitness, target_string):
    '''Loop for finding best solution.
       
       Inputs - 1. max iterations.
                2. Randomly generated string.
                3. initial Fitness value.
                4. target data.
       Output - Best solution. 
    '''
    # For breaking the loop after reaching a specified 
    # number of iteration.
    i = 0

    # Storage for fitness values.
    fitness_list = []

    # Loop for finding best genes.
    while True:
        i += 1

        # Breaking the loop after reaching specified number of iteration.
        if i >= iterations:
            sol_iteration, best_sol, fit_val = i, child, child_fitness
            print(f'Iteration no. {sol_iteration}')
            print(f'Best solution is "{best_sol}" with fitness value {fit_val}.')
            
            return fitness_list
            break

        child = mutate(parent)
        child_fitness = fitness(child, target_string)
        fitness_list.append(child_fitness)

        # Selecting the improved genes.
        if parent_fitness >= child_fitness:
            continue
        if child_fitness >= parent_fitness:
            parent = child
            parent_fitness = child_fitness

        # Breaking the loop after successful run.
        if child_fitness >= len(target_string):
            sol_iteration, best_sol, fit_val = i, child, child_fitness
            print(f'Iteration no. {sol_iteration}')
            print(f'Traget string is: "{target_string}"')
            print(f'Best solution is: "{best_sol}"')
        
            return fitness_list
            break

# Target string.
target_string = 'Hello, I am Parmeshwar a Data Scientist.'

# Parent data.
parent = gen_parent(string_data, target_string)
parent_fitness = fitness(parent, target_string)

# Iterations number.
iterations = 100000

# Finding the solution.
fitness_list = best_gene(iterations, parent, 
                         parent_fitness, target_string)

# Plotting the values.
plt.plot(range(len(fitness_list)), fitness_list)
plt.title('Fitness value over iterations.')
plt.xlabel('Iterations')
plt.ylabel('Fitness value')
plt.show()


