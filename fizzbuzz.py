#Define function fizzbuzz; input variable: max
#For multiples of 3, print Fizz
#For Multiples of 5, print Buzz
#For neither, print number

def fizzbuzz(max):
  for x in range(1, max + 1):
    if x % 3 == 0 and x % 5 == 0:
      print('FizzBuzz')
    else: 
      if x % 3 == 0:
       print('Fizz')
      else:
        if x % 5 == 0:
          print('Buzz')
        else:
          print(x)


fizzbuzz(100)