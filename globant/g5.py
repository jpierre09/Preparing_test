"""

Este código crea una lista de tuplas, donde cada tupla contiene un número y su cuadrado. Para cada número en la lista exercise_list, se crea una tupla con el número y su cuadrado. Las tuplas se agregan luego a la lista result.

"""



def create_tuple(exercise_list):
    result = [(num, num**2) for num in exercise_list]
    # print(result)
    return result

input_list = [1,2,3,4,5]

output = create_tuple(input_list)
print(output)




