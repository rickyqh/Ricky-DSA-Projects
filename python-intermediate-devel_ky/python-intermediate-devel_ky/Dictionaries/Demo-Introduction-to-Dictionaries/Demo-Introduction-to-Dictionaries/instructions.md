# Python Programming: Lists

## **Lists in Python**
### **Instructions:**
- Follow the instructor's walkthrough to learn about Lists and how to use them.
- Complete and execute the code in `main.py` to see the behavior of lists and how to use them.
- Use shortcuts to comment and uncomment lines of code:
    1. **Windows:** `Ctrl + /`
    2. **Mac:** `Cmd + /`
- After the walkthrough, attempt the Exercises on Lists.

### **Overview:**
Lists in Python are ordered, mutable collections of items that can store elements of different data types.

### **Creating a list:**
 **Square brackets are used to contain the elements in a list.**
  ```python
    friends = ["John", "Peter", "Lisa", "David"]
  ```

### **Accessing elements in a list:**
**We access elements using the index.**
```python
  print(friends[0])
```

### **Adding to a list:**
  **We can use `append` or `insert` to add items.**
  
  **`.append()` adds an element at the back of a list.**
  ```python
    friends.append("Tim")
  ```
**`.insert()` adds an element at a specified position. 2 is the specified index where 'Tim' will be added.**
```python
  friends.insert(2,"Tim")
```
  
 ### **Deleting from a list:**
**We can use `pop`, `del`, or `remove` to delete items from a list.**
  
  **`.pop()` deletes the last element.**
  ```python
    friends.pop()
  ```
  **`del` deletes the elements using the index.**        
  ```python
    del friends[2]
  ```
  **`.remove()` deletes the elements using the index.**
  ```python
    friends.remove("Peter")
  ```
### **Modifying an element in a list**
**Use the index to replace an element.**
```python
  friends[2] = "Jake"
```
 ### **Looping through lists**
 **For Loops**
 
 **Keywords `for` and `in` must be used. A variable name for an individual value like `friend` is also needed.**
  ```python
  for friend in friends:
    print(friend)
  ```
 **While Loops**

 **Keywords `while` and `in` must be used. The variable `index` is also needed, and will increase by 1 after every loop. The condition of the while loop must be less than the length of the list.**
  ```python
  index = 0
  while index < len(friends):
    print(friends[index])
    index += 1
  ```

### **List comprehensions:**

**This is similar to `for` loops. The only difference is that the output you want is stated at the start. In the following example, the output we want is squared numbers.**
```python
lower_case_friends = [friend.lower() for friend in friends]
print (lower_case_friends)
```
### **Other list methods**

**We can use the `len` function to get the number of elements in a list.**
```python
len(friends)
```
**To empty a list, we can use the `clear` method.**
```python
friends.clear()
```

**If we have a list of numbers, we can get the largest number using the `max` method.**
```python
numbers.max()
```
**We can get the smallest number using the `min` method.**
```python
numbers.min()
```