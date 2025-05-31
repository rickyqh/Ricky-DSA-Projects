# Instructions 

1. In your `main.py` file, add exception handling to the read names exercise we did previously.
2. Attempt to open and read the file.
3. Add specific exception handling statements to handle the following exceptions:
   a. The case where the file cannot be found

   b. The case where the file is not accessible (permission issue)

   c. Any other exceptions that might occur (general exception)


# Hints
1. Use try and except keywords
2. For the second exception, use PermissionError

## Expected Output
```python
Alice
Bob
Charlie
David
Eva
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
