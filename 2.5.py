#!/usr/bin/env python

# firstname, M. lastname
first_name = str(input("Please enter your first name: "))
last_name = str(input("Please enter your last name: "))

first_name = first_name.capitalize()
last_name = last_name.capitalize()

name_format = "{first_name} {last_name}"
print(name_format.format(first_name = first_name, last_name=last_name))
