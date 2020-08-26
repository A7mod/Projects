pear = 7
peach = 8

def main():
    apple = 4
    orange = 5
    """if apple + pear <= orange :

        print("One,", end='')
        print("Two and Three")
    """
    while orange >= 0 :
        print(orange, "***") 
        orange = orange - 2
    print(apple, pear, peach, "BEFORE FUNCTION")
    retVar = ExamTwoFunction(apple)
    print(peach, pear, retVar, "AFTER FUNCTION")

def ExamTwoFunction(banana):
    global pear
    pear = 10
    banana = 12
    peach = 14
    print(banana, pear, peach, "INSIDE FUNCTION")
    return peach + banana
main()