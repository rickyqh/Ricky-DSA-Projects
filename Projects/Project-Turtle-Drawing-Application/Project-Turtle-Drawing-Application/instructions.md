# Instructions 

1. In the ‘main.py’ file, we will be using the turtle library to draw a square, triangle, and rectangle
2. The configuration of the shapes will be stored in a JSON file
3. There will be 3 functions that will make this work:

load_config function

draw_shape function

main function

4. Load_config loads the configuration from the JSON file
5. draw_shape draws each shape based on its specifications. It distinguishes between shapes using conditional checks for 'square', 'triangle', and 'rectangle', applying appropriate drawing logic for each
6. main sets up the Turtle environment, iterates over each shape configuration, and draws them using Turtle graphics


# Hints
1. Store the width and height of the rectangle for the shape configuration into a list
2. Make sure that you use double quotations ” for string values in the JSON object
3. Recall some basic turtle functions like penup, pendown, goto, and title
4. Access shape_info to get size information on how much to move forward for the shapes
5. For the rectangle, it will have two values for the size information, one for the width and another for the height





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
