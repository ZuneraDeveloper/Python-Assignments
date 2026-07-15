celsius = "1. Celsius to Fahrenheit" # option to choose
fahrenheit = "2. Fahrenheit to Celsius"
print(celsius) # print the Option
print(fahrenheit)
tem_conversion = input("Which conversion do you want? (number 1 or 2) ") # Ask for the option
if tem_conversion == "1": # if tem_conversion equal to "1"
  celsius_temperature = float(input("What is your Temperature? ")) # Get the temperature from user
  cel_to_farh = (celsius_temperature * 9/5) + 32 # Celsius to Fahrenheit formula
  print("Temperature converted from Celsius to Fahrenheit ",cel_to_farh,"°C") # Print the formula result
elif tem_conversion == "2": # if tem_conversion equals to "2"
  fahrenheit_temperature = float(input("What is your Temperature? ")) # Ask the user for temperature
  fahr_to_cel = (fahrenheit_temperature - 32) * 5/9 # Fahrenheit to Celsius formula
  print("Temperature converted from Fahrenheit to Celsius ",fahr_to_cel,"°F") # Print the results of formula
else:
  print("An invalid option") # Otherwise this will print