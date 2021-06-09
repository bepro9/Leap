# Reliance Fresh
```python
dash = '-'
star = '*'
space =' '
print(dash*15+star*3+dash*15)
print(space*4+'Welcome to Reliance Fresh'+space*4)
print(dash*15+star*3+dash*15)
print()


list = ['oil','butter','drinks','bread']
print('Items in Stock for Today')
for i in list:
    print(" -> "+i.capitalize())

print()
item = input('What would you like to buy Sir : ').lower()

if(list.__contains__(item)):
    print(f'Item bought : {item}')
    print()
    list.remove(item)  
else:
    print('Soory, Item not Available')
      
print('Available Items : ')
for i in list: print('-> '+i.capitalize())
```
