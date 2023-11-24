# import pytest
# from src.main import sum, is_greater_than

# def test_sum():
#     assert sum(2,5) == 7
#     assert sum(-1, 1) == 0

# def test_is_grater_than():
#     assert is_greater_than(3, 2)

# def test_sum_params(inputx, inputy, expected):
#     assert sum(inputx, inputy) == expected


#repgunta 1
lst = [2,4,1,3]

new = lst
lst[0] = 9
print(new)



#pregunta 4

class HackerEarth:
    def __init__(self, HackNew = 1):
        
        self.HackNew = HackNew

    def set(self, HackNew):
        self.HackNew = HackNew
        return HackNew

Hack = HackerEarth()
print(Hack.set(Hack.HackNew + 1))


## preugnta 5

def create_tuple(exercise_list):
    result = [(num, num**2) for num in exercise_list]
    return result

input_list = [1,2,3,4,5]

output = create_tuple(input_list)
print(output)

