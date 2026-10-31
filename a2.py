# 1) Create variables to store different types of values:
#    - `name` as text (string)
#    - `age` as a whole number (integer)
#    - `is_student` as True/False (boolean)
#    - `weight` as a decimal number (float)
name="arya"
age=13
isStudent=True
weight=50.34
# 2) Print each variable’s value.
print("name is",name)
print("age is",age)
print("isStudent is",isStudent)
print("weight is",weight)
# 3) Print the datatype of each variable using `type()`.
print("name data type is ",type(name))
print("age data type is ",type(age))
print("isStudent data type is ",type(isStudent))
print("weight data type is ",type(weight))
# 4) Show a message that type casting will happen next.
print("type casting is going to happen next")
# 5) Convert `age` from an integer to a string and store it back in `age`.
str1=str(age)
# 6) Print `age` and print its datatype again to confirm it changed.
print("age is ",str1,"data type of age is",type(str1))
# 7) Convert `weight` from a float to an integer and store it back in `weight`.
weight=int(weight)
# 8) Print `weight` and print its datatype again to confirm it changed.
print("weight is ",weight,"data type of weight is",type(weight))