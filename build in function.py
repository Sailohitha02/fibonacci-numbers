# returns the absolute value of integer
integer = -20
print('Absolute value of -20 is:', abs(integer))

# all 
l = [1, 3, 4, 5]
print(all(l))

# any
l = [1, 3, 4, 0]
print(any(l))

#ascii
normalText = 'Python is interesting'
print(ascii(normalText))

#bin
number = 5
print('The binary equivalent of 5 is:', bin(number))

#bool
test = [0]
print(test,'is',bool(test))

#bytearray
string = "Python is interesting."
arr = bytearray(string, 'utf-8')
print(arr)

#complex
z = complex(2, -3)
print(z)

#dict
numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))

#divmod
print('divmod(8, 3) = ', divmod(8, 3))

#enumerate
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)
print(type(enumerateGrocery))
print(list(enumerateGrocery)
      
#exec
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)
      
#format
print(format(123, "d"))
      
#hash
print('Hash for 181 is:', hash(181))
      
#input
inputString = input()
print('The inputted string is:', inputString)
      
#len
testList = []
print(testList, 'length is', len(testList))
      
#ininstance
class Foo:
  a = 5 
fooInstance = Foo()
print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))
      
#list
print(list())
vowel_string = 'aeiou'
print(list(vowel_string))
      
#max
number = [3, 2, 8, 5, 10, 6]
largest_number = max(number);
print("The largest number is:", largest_number)
      
#min
number = [3, 2, 8, 5, 10, 6]
smallest_number = min(number);
print("The smallest number is:", smallest_number)
      
#open
f = open("test.txt")
      
#print
a = 5
print("a =", a)
      
#range
print(list(range(10))
      
#reversed
seq_string = 'Python'
print(list(reversed(seq_string)))
      
#slice
result1 = slice(3)
print(result1)
      
#sorted
py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True))
      
#str
result = str(10)
print(result)
      
#tuple
t2 = tuple([1, 4, 6])
print('t2 =', t2)
      
 #type
 numbers_list = [1, 2]
print(type(numbers_list))
      
 #vars
 class Foo:
  def __init__(self, a = 5, b = 10):
    self.a = a
    self.b = b
  
object = Foo()
print(vars(object))
      
#zip
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']
result = zip()
      
#import
mathematics = __import__('math', globals(), locals(), [], 0)
print(mathematics.fabs(-2.5))
