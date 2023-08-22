import re   #library to match number with regex
def validate(number):
  """
  Validates a contact number using regular expressions.
  Args:
    number: The contact number to be validated.
  Returns:
    true if the contact number is valid, false otherwise.
  """

  # regular expression pattern for a valid contact number
  pattern = r'^(\+?\d{1,3}[-. ]?)?\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}$'
  # Use re.match to check if the number matches the pattern or not
  if re.match(pattern, number):
      return True
  else:
      return False


# Get the contact number from the user.
number_list = [
    '2124567890',
    '212-456-7890',
    '(212)456-7890',
    '(212)-456-7890',
    '212.456.7890',
    '212 456 7890',
    '+12124567890',
    '+12124567890',
    '+1 212.456.7890',
    '+212-456-7890', 
    '1-212-456-789'
    ]
result = []
for i in number_list:
# Validate the contact numbers in the list
    result.append(validate(i))

# Print the resultant validations
print(result)