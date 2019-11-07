"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python

The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
"""
from fizzbuzz import fizzbuzz



#----START OF SCRIPT
if __name__=='__main__':
    fizzbuzz(100)


"""a. I didn't get any clue.

b. i googled the error"'module' object is not callable" and got the answer.

c.I learned that while calling the module we should specify the name. 
If we just write"import fizzbuzz" from where it should import so if we write "import fizzbuzz from fizzbuzz" 
it'll come to know that there is a class named as fizzbuzz.(This explaination is according to my understandings)"""