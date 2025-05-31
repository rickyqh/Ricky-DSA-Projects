# --------Do not edit these lines of code-----------
import json
# --------Do not edit these lines of code-----------

def main():
  filename = 'student_grades.json'
  # TO DO: Attempt to open the json file in append and read mode
  
    with open(filename, 'a') as file:
      while True:
        # TO DO: Attempt to get the student's name and grade, then add it into the JSON file
        
          name = input("Enter the student's name (enter 'q' to quit): ")
          if name.lower() == 'q':
            break
          grade = input("Enter the student's grade: ")
          data = {name: grade}
          json_string = json.dumps(data)
          file.write(json_string + '\n')
          print(f"Grade for {name} added/updated successfully.")
        # TO DO: Handle the error for the JSON object, if it is unable to be read
        
        # TO DO: Handle case where user interrupts the input (e.g., Ctrl+C)
        
        # TO DO: General exception for unexpected issues during input handling
        

    with open(filename, 'r') as file:
      for line in file:
        # TO DO: Attempt to load every line and print it
        
          grade = json.loads(line)
          print(grade)
        # TO DO: Handle the error for the JSON object, if it is unable to be read
        
        # TO DO: General exception for unexpected issues during input handling
        
  # TO DO: Exception if the specified file or directory does not exist
  
  # TO DO: Exception if there is a permission error accessing the file
  
  # TO DO: General exception for other file opening-related errors
  

# --------Do not edit these lines of code-----------
if __name__ == "__main__":
    main()
# --------Do not edit these lines of code-----------

    ```