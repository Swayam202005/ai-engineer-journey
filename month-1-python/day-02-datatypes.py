# 1. Basic data types
age = 21 # int
gpa = 8.75 # float
name = 'Swayam' # str
is_student = True # bool
score = None # NoneType
print(type(age), type(gpa), type(name), type(is_student))

# 2. Type casting
x = '42'
print(int(x) + 8) # 50
print(float(x)) # 42.0
print(str(100)) # '100'
print(bool(0)) # False
print(bool(1)) # True

# 3. f-strings (very important — use these always)
name = 'Swayam'
age = 21
gpa = 8.75
print(f'Hi, I am {name}')
print(f'Age: {age}, GPA: {gpa:.2f}')
print(f'In 5 years I will be {age + 5}')

# 4. String methods
s = ' Hello World '
print(s.strip()) # removes spaces
print(s.lower()) # hello world
print(s.upper()) # HELLO WORLD
print(s.replace('World', 'AI')) # Hello AI
print(s.split()) # ['Hello', 'World']
print('Python' in s) # False
print(len(s.strip())) # 11