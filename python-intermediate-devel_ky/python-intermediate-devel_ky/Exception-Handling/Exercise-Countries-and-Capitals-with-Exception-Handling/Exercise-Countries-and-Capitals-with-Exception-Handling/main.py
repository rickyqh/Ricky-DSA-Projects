def print_countries_and_capitals(filename):
  # Attempt to 0pen the file in read mode
  
      with open(filename, 'r') as file:
          line = file.readline()
          while line:
            # Attempt to split each line into country and capital
            
              country, capital = line.strip().split(', ')
              print(f"The capital of {country} is {capital}.")
            # Handle the case where a line does not contain exactly two elements
            
              
            line = file.readline()
  # Add other exceptions here
  # Handle the case where the file does not exist
  
  # Handle the case where the file is not accessible (permissions issue)
  
  # Handle any other exceptions that might occur
  


filename = 'countries_and_capitals.txt'
print_countries_and_capitals(filename)
