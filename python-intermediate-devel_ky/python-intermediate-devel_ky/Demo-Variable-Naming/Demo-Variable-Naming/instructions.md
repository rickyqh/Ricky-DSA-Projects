# Python Programming: Variables

## **Variables in Python**
### **Instructions:**
- Follow the instructor's walkthrough to learn about Variables and how to use them.
- Execute the code in `main.py` to see the behavior of variables and how to manipulate them.
- Use shortcuts to comment and uncomment lines of code:
    1. **Windows:** `Ctrl + /`
    2. **Mac:** `Cmd + /`
- After the walkthrough, attempt the Exercises on Variables.

### **Overview:**
Variables are containers for storing data values, and they are created the moment you first assign a value to them.

### **Variable Naming Rules:**
1. **Must start with a letter or underscore.**
    ```python
    my_age = 14
    _my_age = 15
    ```
2. **Cannot start with a number.**
    ```python
    # 1st_name = "Tom"  # Invalid
    ```
3. **Can only contain alphanumeric characters and underscores.**
    ```python
    # first$name = "Tim"  # Invalid
    ```
4. **Are case-sensitive.**
    ```python
    my_name = "Jenny"
    My_name = "James"
    ```
5. **Avoid using Python keywords and function names.**
    ```python
    # print = "Print Function"  # Avoid
    # input = "Input Function"  # Avoid
    ```

### **Example:**
```python
first_name = "Tom"
last_name = "Tan"
print("My name is " + first_name + " " + last_name)
