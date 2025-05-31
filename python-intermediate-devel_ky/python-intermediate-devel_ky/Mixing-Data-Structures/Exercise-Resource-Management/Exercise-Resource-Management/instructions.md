# Instructions

1. In your `main.py` file, we will create a resource management system for the IT and HR department.
2. Firstly, add the resource IDs for the IT and HR departments using sets.
3. The resource IDs for **IT** are R001, R002, R003, and R007.
4. The resource IDs for **HR** are R005, R002, R006, and R007.
5. Then initilaise a dictionary that holds another dictionary, each a description of each resource. Each tuple includes the name, department and priority of each resource.
6. Here are the information for each inner dictionary:

R001: Laptop, IT, High

R002: Projector, Shared, Medium

R003: Server, IT, Critical

R005: Health Benefits, HR, Low

R006: Training Manual', HR, Low

R007: Conference Room, Shared, High

7. Then use the union set method to find all of the unique resources.
8. Use the intersection set method to find resources that are shared between IT and HR.
9. Get an input from the user to enter a resource ID
10. Check if the inputted resource ID is in the all_resources set and use tuple unpacking to display the result.

# Hints

1. The dictionary key is the resource ID, and the value is the inner dictionary with 3 keys: `name`, `department` and `priority`
2. Use the special characters for union and intersection
3. Use the input function when asking for the user input
4. Use f-strings to display each description.

## Expected Output

```python
Enter a resource ID to get its details: R007
Resource Details - Name: Conference Room, Department: Shared, Priority: High
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
