from FizzBuzz import FizzBuzz

def test_passing_test():
    pass

#def test_failing_test():
    #raise Exception()

def test_returns_a_list():
    fizzbuzz = FizzBuzz()
    assert type(fizzbuzz.getNumber(3)) is list
def test_list_contains_int():
    fizzbuzz = FizzBuzz()
    assert(int in [type(i) for i in fizzbuzz.getNumber(3)])
def test_list_contains_str():
    fizzbuzz = FizzBuzz()
    assert(str in [type(i) for i in fizzbuzz.getNumber(3)])
def test_Fizz():    
    fizzbuzz = FizzBuzz()
    for i in range(101):
        number = fizzbuzz.getNumber(i)
        for index,element in enumerate(number):
            if ((index+1) % 3 == 0 and (index+1) % 5 != 0):
                assert(element == "Fizz")
def test_Buzz():    
    fizzbuzz = FizzBuzz()
    for i in range(101):
        number = fizzbuzz.getNumber(i)
        for index,element in enumerate(number):
            if ((index+1) % 5 == 0 and (index+1) % 3 != 0):
                assert(element == "Buzz")

               
def test_FizzBuzz():    
    fizzbuzz = FizzBuzz()
    for i in range(101):
        number = fizzbuzz.getNumber(i)
        for index,element in enumerate(number):
            if ((index+1) % 5 == 0 and (index+1) % 3 == 0):
                assert(element == "FizzBuzz")
            else:
                assert(element != "FizzBuzz")

def test_digit():
    fizzbuzz = FizzBuzz()
    for i in range(101):
        number = fizzbuzz.getNumber(i)
        for index,element in enumerate(number):
            if (index+1) % 5 != 0 and (index+1) % 3 != 0:
                digits = [digit for digit in str(index+1) if digit == '3' or digit == '5']
                if len(digits) > 0:
                    if digits[0] == '5':
                        assert(element == 'Buzz')
                    elif digits[0] == '3':
                        assert(element == 'Fizz')
                    else: 
                        raise Exception("shouldn't happen")

#'ef' in ['phone','hans']