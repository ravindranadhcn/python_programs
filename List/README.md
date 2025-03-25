#**List Methods in Python**

##.append(element): Adds an element to the end of the list

```
fruits = ['apple','banana','cherry']
fruits.append('orange')
print(fruits)
#Outpu: ['apple', 'banana', 'cherry', 'orange']
```
__.insert(index, element): Inserts an element at the specified index.__
```
fruits = ['apple','banana','cherry']
fruits.insert(1, 'orange')
print(fruits)
#Outpu: ['apple', 'orange', 'banana', 'cherry']
```
.extend(iterable): Adds all elements from an iterable to the end of the list.

```
fruits = ['apple','banana']
more_fruits = ['cherry', 'orange' ]
fruits.extend(more_fruits)
print(fruits)
#Outpu: ['apple', 'banana', 'cherry', 'orange']
```
__.remove(element): Remove the first occurrence of the specified element from the list.__
```
fruits = ['apple','banana','cherry', 'banana']
fruits.remove('banana')
print(fruits)
#Outpu: ['apple', 'cherry', 'banana']
```
__.pop(index): Removes and returns the element at the specified index. If no index is provided, it removes and returns the last element.

```
fruits = ['apple', 'banana', 'cherry']
removed_fruit = fruits.pop(1)
print(fruits) #Output: ['apple', 'cherry']
print(removed_fruit) #Output: 'banana'
 ```

__ .clear(): Removes all elements from the list __
```
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits) #output: []
```

__ .index(element): Returns the index of the first occurrence of the specified element in the list.

```
fruits = ['apple', 'banana', 'cherry']
index = fruits.index('banana')
print(index) #Output: 1
```
__ .sort(): Sorts the list in   ascending order. __
```
numbers = [5, 2, 8, 1, 6]
numbers.sort()
print(numbers) #Output: [1, 2, 5, 6, 8]
```

__ .reverse(): Reverses the order of the elements in the list. __
```
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
# Output: ['cherry', 'banana', 'apple']
```

__ .copy(): Returns a shallow copy of the list. __
```
fruits = ['apple', 'banana', 'cherry']
fruits_copy = fruits.copy()
print(fruits_copy)
# Output: ['apple', 'banana', 'cherry']
```

__ .count(element): Returns the number of times the specified element appears in the list. __

```
fruits = ['apple', 'banana', 'cherry', 'banana']
count = fruits.count('banana')
print(count) # Output: 2
```




