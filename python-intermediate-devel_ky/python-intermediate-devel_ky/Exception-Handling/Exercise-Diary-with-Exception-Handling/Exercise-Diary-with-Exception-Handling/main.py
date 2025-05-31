# --------Do not edit these lines of code-----------
import os
current_path = './Project/DummyFolder2'
os.chdir(current_path)
# --------Do not edit these lines of code-----------

relative_path = '../DiaryEntries/diary.txt'
# TO DO: Attempt to open the file in append mode
 
  with open(relative_path, 'a') as file:
    print("Welcome to your digital diary. Type 'exit' to quit.")
    while True:
      # TO DO: Attempt to get the diary entry
           
        entry = input("Enter your diary entry: ")
        if entry.lower() == 'exit':
          break
        file.write(entry + "\n")
        print("Your entry has been added to the diary.")
      # TO DO: Handle case where user interrupts the input (e.g., Ctrl+C)
      
      # TO DO: General exception for unexpected issues during input handling
      
# TO DO: Exception if the specified file or directory does not exist

# TO DO: Exception if there is a permission error accessing the file

# TO DO: General exception for other file opening-related errors


  






