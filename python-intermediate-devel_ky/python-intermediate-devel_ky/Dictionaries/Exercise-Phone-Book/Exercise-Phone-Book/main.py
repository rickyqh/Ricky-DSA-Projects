phonebook = {
  "Jill" : "90904554",
  "Kevin" : "88839009",
  "jakob" : "98832231",
  "Robert" : "90983232",
  "Caleb" : "84430029",
  "Bryan" : "88410021",
  "David" : "88432098",
  "Jamie" : "94331209",
  "Yasmin" : "83326778",
  "Joshua" : "88112278"
}
# Given the above dictionary of people's phone numbers, use a for loop to create a new dictionary of everyone's number for people whose name begins with a 'J'

# Hint: create an empty dictionary to add the key-value pair of people whose name begins with a 'J'
# Hint: loop through the key and value pairs of the original dictionary
# Hint: check if the first letter of the name starts with a 'J' by using string indexing


for  in phonebook :
  if  == "J":
    

# add a new person, Jerome, whose phone number is 98765432, into the new dictionary

print(J_name_phonebook)

# then fill up this function which helps to retrieve the person's number based on a user's input
def lookup_number():
  # add an input to ask the user what name they would like to look up in the new dictionary
  name = input()
  # get the number based on the name they have inputted using the .get() method
  number = 
  if number:
    # print out a statement to tell the user the number
    print("The number for " + name + " is " + str(number))
  else:
     # print out a statement to tell the user that the number is not in the phonebook
    print("Sorry, that name is not in the phonebook.")

lookup_number()


