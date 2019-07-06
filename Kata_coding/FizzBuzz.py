class FizzBuzz:
    def getNumber(self,n):
        result = []
        for i in range(1,n+1):
            if(i % 3 == 0):
                if(i % 5 == 0):
                    result.append('FizzBuzz')
                else:
                    result.append('Fizz')
            elif(i % 5 ==0):
                result.append('Buzz')
            else:
                result.append(i)
        return result
if __name__=='__main__':
    fb = FizzBuzz()
    n = int(input("Enter the limit : "))
    result = fb.getNumber(n)
    print(result)