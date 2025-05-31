# Instructions 

1. In your `main.py` file, merge the two dictionaries together.
2. Find items that need restocking, whose quantity is 25 and below.
3. Filter items whose quantity is greater than 50.
4. Sort the merged dictionary by ascending quantity.


# Hints
1. Merge dictionaries using |
2. Use dictionary comprehension, and make sure the condition states that quantity is less than 25
3. Remember to use .items() to access the key-value pairs
4. Make sure the quantity is greater than 50 when filtering the large quantity items
5. Use the sorted function, as well as key = lambda to sort the dictionary by its value

## Example
### Example Output
```python
Combined Inventory: {'Apples': 60, 'Bananas': 30, 'Oranges': 20, 'Pineapples': 20, 'Pears': 30, 'Grapes': 55}
Restock Items: {'Oranges': 20, 'Pineapples': 20}
Large Stock Items: {'Apples': 60, 'Grapes': 55}
Sorted Inventory: {'Oranges': 20, 'Pineapples': 20, 'Bananas': 30, 'Pears': 30, 'Grapes': 55, 'Apples': 60}
```

## Test Your Code
### Running Tests
- To verify your program, run it and check if it provides the correct output based on the input.
   ![image](tests_tools.png)
- If the output is correct, and there are no errors, proceed to submit it.
   ![image](submit.png)

### Test Results
- If your code passes all the tests, you will see the following screen.
   ![image](pass.png)
- If any test case fails, analyze the `Results` section to identify the error and refine your code.
   ![image](fail_tests.png)
   ![image](results.png)

## Final Note
- Before submitting, make sure that your program correctly asks for the user's name, forms the greeting and prints it to the console.
   ![image](submit.png)
