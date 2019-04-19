# you probably know FizzBuzz
# this solution is easy to extend

n = 105
words = {3:'Fizz', 5:'Buzz', 7:'Bang'}

for i in range(1, n+1):
    s = ''
    for key in words:
        if i % key == 0:
            s += words[key]
    print(s if len(s) > 0 else i)
