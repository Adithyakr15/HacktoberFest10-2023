# reverse a string without using built in function

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
  
s = "SHREYASAJIET"
  
print("The original string is : ", end="")
print(s)
  
print("The reversed string(using loops) is : ", end="")
print(reverse(s))