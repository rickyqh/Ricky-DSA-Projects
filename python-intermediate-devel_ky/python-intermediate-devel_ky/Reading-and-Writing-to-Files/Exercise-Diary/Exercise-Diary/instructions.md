# Instructions

1. In the `main.py` file, we will be appending a sentence into the `diary.txt` file
2. First access the `diary.txt` file using relative paths. The working directory is currently in the DummyFolder2 folder.
3. Open the file in append mode.
4. Create a variable to get the user's input. Add in the sentence "I am now learning how to append things into files."
5. Break out of the loop if the user inputs "exit".
6. Write the entry into the file, and add a new line character

# Hints

1. Use keywords like with, open, a, and as.
2. As we need to access the DiaryEntries folder, we need to go upwards in the directory tree
3. To do so, use ../ at the beginning of the relative path.
4. Check if the user's input is equal to 'exit'. If it is, then use the break keyword to break out of the while loop.
5. Write to the `diary.txt` file using the write keyword, and add a new line character '\n'

## Expected Output in diary.txt

```txt
Dear diary,

I love coding with python.
I am now learning how to append things into files.
```

## Final Note

- Before submitting, make sure that your program correctly asks for the user's name, forms the greeting and prints it to the console.
  ![image](submit.png)
