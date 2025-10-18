
# Arithmetic operator 
a = 17
b = 5

print("a + b =", a + b)   
print("a - b =", a - b)    
print("a * b =", a * b)   
print("a / b =", a / b)    
print("a // b =", a // b)  
print("a % b =", a % b)    
print("a ** b =", a ** b)  

# Relational / comparison operators

x = 10
y = 20

print(x == y)   
print(x != y)   
print(x > y)   
print(x < y)   
print(x >= y)   
print(x <= y)   


# Logical operators

p = True
q = False

print(p and q)  
print(p or q)   
print(not p)    


age = 18
has_id = True
print(age >= 18 and has_id)  


# Bitwise operators

a = 6   # binary 110
b = 3   # binary 011

print(a & b)   
print(a | b)   
print(a ^ b)   
print(~a)      
print(a << 1)  
print(a >> 1)  


# Assignment operators

n = 10
n += 5  
print(n)
n *= 2   
print(n)
n %= 7   
print(n)

# Identity operators

a = [1, 2, 3]
b = a           
c = [1, 2, 3]   

print(a is b)     
print(a is c)      
print(a == c)      
print(a is not c)  

# Membership operators

s = "hello world"
lst = [1, 2, 3, 4]

print('hello' in s)    # True
print('x' not in s)    # True
print(3 in lst)        # True
print(5 not in lst)    # True

# Operator Precedence

print(2 + 3 * 4)    
print((2 + 3) * 4)   
print(2 ** 3 ** 2)   





