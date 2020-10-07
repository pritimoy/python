# String

# Accessing String Character

title = "I learn Python"
title1 = "I know Dart"

print(title)
print(title1)

# Access first and last character
print(title[0],title[1],title[2],title[3],title[4], title[5],title[6], title[-1], title[-2])

# String Operation
print(title.title() ) # For first character capital
print(title.upper() )
print(title.lower() )

# String Concatenation
discription = title + ' ' + title1
print(discription)

print( title+ ' ' + title1)

# Newline
print(title + "\n" + title1)

# WhiteSpace
name = "     Mr. Y     "
print('_' + name + '_')
print('_' + name.lstrip() + '_') #left side space/whitespace remove
print('_' + name.rstrip() + '_') #Right side space remove
print('_' + name.strip() + '_') # Both side space romove
print('_' + name.lstrip().rstrip() + '_') #Bothe left and right side space remove

#Printing single and Double quote
shop_name = "Robin's Shop"
print(shop_name)

shop_name = 'Rabin"s Shop'
print(shop_name)

shop_name = 'Robin\'s Shop'
print(shop_name)

# Matching text at start and at the end
filename = 'bigdata.txt'
print(filename.endswith('.txt') )
print(filename.startswith('bi') )
print(filename.startswith('xi') )

#Find Word in a sentence
sentence = "A quick brown fox jumps over the lazy dog"
print( sentence.find('fox') )
print ( sentence.find('foxs') ) # -1 the value not found

# Replace in string
sentence = sentence.replace('fox', 'tiger')
print ( sentence)

# Print seperator
x = 'Dhaka'
y = 'Faridpur'
z = 'Magura'

print(x + '| ' + y + '| ' + z)
print (x, y, z, sep='| ')

# String interpolation
# old style

person = '%s\'s age is %d'
print(person %('Bill', 25))

# New style
person = '{name}\'s age is {age}'
print(person.format(name='Bill', age= 24))
print(person.format(name='Steve', age= 55))

# Formatted string literal python 3.6 +
name = 'Mark'
age = 32
person = f'{name}\'s age is {age}'
print(person)

# String Slice
name1 = "Taylor Swift"
print (name1[0: 6])
print (name1[:6])
print (name1[7:])
print (name1[7: -1])