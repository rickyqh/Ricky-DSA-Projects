# Instructions 

1. In the `main.py` file, add a few student grades as JSON objects, and display them.
2. Add the JSON file in the filename variable. The filename is `student_grades.json`
3. Open the JSON file in append mode.
4. Within a while loop, get the user's inputs on the name and grade.
5. If the user enters 'q' in the name input, break out of the while loop.
6. Add the inputs into the data variable and convert it into a JSON string.
7. Write the JSON string into the JSON file
8. Read and display the name and grades in the file
9. Enter the following name and grades:

   Kevin, B+
   
   Sam, A
   
   John, B-

# Hints
1. Use the dumps method to to convert the data into a JSON string
2. Add a new line character `\n` when writing it into the JSON file
3. Use the loads method and a for loop when displaying the name and grades

## Expected Sequence and Output 
```txt
Enter the student's name: Kevin
Enter the student's grade: B+
Grade for Kevin added/updated successfully.
Enter the student's name: Sam
Enter the student's grade: A
Grade for Sam added/updated successfully.
Enter the student's name: John
Enter the student's grade: B-
Grade for John added/updated successfully.
Enter the student's name: q
{'Kevin': 'B+'}
{'Sam': 'A'}
{'John': 'B-'}
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
