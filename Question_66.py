brothers_age = 20
sisters_age = 21
print(type(brothers_age))
print(type(sisters_age))

# <class 'int'>
# <class 'int'>

if brothers_age > sisters_age: # como brothers_age > sisters_age, pula esse bloco
    print('Older Brother')
elif brothers_age == sisters_age:
    print('Same age')
else: # roda esse bloco
    print('Yonger Brother')
    
# Older Brother
