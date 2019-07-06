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
                if '5' in str(i):
                    if '3' in str(i):
                        if str(i).index('3') < str(i).index('5'):
                            result.append('Fizz')
                        else:
                            result.append('Buzz')
                    else:
                        result.append('Buzz')
                elif '3' in str(i):
                    result.append('Fizz')
                else:
                    result.append(i)


        return result
