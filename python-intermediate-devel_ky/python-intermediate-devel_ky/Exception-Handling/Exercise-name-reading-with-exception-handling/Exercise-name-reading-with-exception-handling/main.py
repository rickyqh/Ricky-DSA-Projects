def print_names_from_file(filename):
  # Attempt to open and read the file
  
    with open(filename, 'r') as file:
      for line in file:
        print(line.strip())

# Add exceptions here
# Handle the case where the file does not exist

# Handle the case where the file is not accessible (permissions issue)

# Handle any other exceptions that might occur

filename = 'names.txt'


print_names_from_file(filename)