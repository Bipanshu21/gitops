print('hello world')


class Car:
    color = 'anything'

    def __init__(self):
        print(f'the color of the car is {self.color}')


c1 = Car()




def printFib(limit):
    firstTerm = 0
    secondTerm = 1
   
    result = [firstTerm, secondTerm]

    for i in range(limit):
        nextTerm = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = nextTerm
 
        result.append(nextTerm)

    return result    
    
       
data = printFib(10)

print(data)

