def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

print (factorial(5))

#------------------------------------------------

def fibonacci(n):
    result = []
    first = 1
    second = 1
    while len(result) < n:
        result.append(first)
        temp = first + second
        first = second
        second = temp
    return result
print (fibonacci(10))

#------------------------------------------------

def sum_of_digits(n):
    total = 0
    for i in range(0, len(str(n))):
        n=abs(n)
        total += n % 10
        n = n // 10
    return total
print (sum_of_digits(123))

#-----------------------------------------------

def fact_digits(n):
    result = 0
    while n !=0:
        a=n % 10
        result += factorial(a)
        n = n // 10
    return result
print (fact_digits(145))

#----------------------------------------------

def palindrome(obj):
    if str(obj) == str(obj)[::-1]:
        return True
    else:
        return False
print (palindrome("kapak"))

#----------------------------------------------

def to_digits(n):
    a = str(n)
    b = []
    for digit in a:
        b.append (int(digit))
    return b
print (to_digits(123))

#---------------------------------------------

def to_number(n):
    return int(''.join(str(i) for i in n))
print(to_number([1,2,3]))

#---------------------------------------------

def fibonacci_number(n):
    return to_number(fibonacci(n))
print (fibonacci_number(10))

#---------------------------------------------

def count_vowels(string):
    vowels = "aeiouyAEIOUY"
    ctr = 0
    for vowel in string:
        if vowel in vowels:
            ctr += 1
    return ctr
print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))

#--------------------------------------------

def count_consonants(str):
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    ctr = 0
    for consonant in str:
        if consonant in consonants:
            ctr += 1
    return ctr
print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

#--------------------------------------------

def char_histogram(string):
    result = {}
    for character in string:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result
print (char_histogram("AAAAaaab00a101"))

#-------------------------------------------

def p_score(n):
    if palindrome(n):
        return 1
    total = n + int(str(n)[::-1])
    return 1 + p_score(total)
print (p_score(48))

#--------------------------------------------
