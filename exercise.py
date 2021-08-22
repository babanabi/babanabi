#Check if list contains integer x: True or False
mylist = [23,59,132,41,78,4,4,59,3,5,6,2,41]
print(132 in mylist)


#Find dublicate number in integer list
def find_dublicate(numbers):
    seen, dublicate =[] ,[]
    for number in numbers:
        if number in seen:
            dublicate.append(number)
        seen.append(number)
    return dublicate

#Check if two string are anagrams: True or False
def check_anagram(s1,s2):
    if set(s1)==set(s2):
        return True
    return False


#Remove all dublicates from list
oldlist = ['Tom','Maria','Alex',34,'Tom',23,11,'Cali','Jhon','Alex',23]
newlist = list(set(oldlist))
print(newlist)

#Find pairs integer in list so that their sum is equal to integer x
def find_pairs(numberlist,x):
    pairs =[]
    for i,n in enumerate (numberlist):
        for i2,n2 in enumerate (numberlist[i+1:]):
            if n + n2 == x:
                pairs.append((n,n2))
                
    return pairs


#Check if is a string palindrome: True or False
def is_palindrome(check):
    if check == check[::-1]:
        return True
    return False

print(is_palindrome("abba"))


#Get missing number in Range(limit): returns List 
def find_missing_number(nlist,limit=100):
    return [x for x in list(range(1,limit)) if x not in nlist ]

#Get missing number in list: returns set
def check_s(plis):
    return list(set(range(plis[len(plis)-1])[1:]) - set(plis))


#Compute the intersection two lists
def intersect(l1,l2):
    inter, l2_copy = [], l2
    for i in l1:
        if i in l2:
            inter.append(i)
            l2.remove(i)
    return inter



#Reverse string using recursion
def reverse(word):
    if len(word) <= 1: return word
    return reverse(word[1:]) + word[0]


#Compute the n fibonacci numbers
def fibonacci(n):
    fib=[]
    a,b = 1,1
    for i in range(n+1):
        fib.append(a)
        a,b =b,a+b
    return fib

#Sort list with Quicksort algorithm
def qsort(l):
    if len(l) == 0: return []
    return qsort([x for x in l[1:] if x < l[0]]) + l[0:1] + qsort([x for x in l[1:] if x >= l[0]])
    
        

#Find all Permutation s in string return list
def get_permutation(s):
    if len(s) <= 1 :return list()
    smaller = get_permutation(s[1:])
    perms = set()
    for x in smaller:
        for pos in range(0,len(x)+1):
            perm = x[:pos] + s[0] + x[pos:]
            perms.add(perm)
    return list(perms)
