# Alexza Jean R. Catanoy
# BSCPE 1-4
# Lab Exercise No. 1.2

#Title
print("\033[0;36m*" * 70)
print("\033[1;97mDecrypt a Encrypted Text".center(77)) 
print("\033[0;36m*" * 70)

print("\033[1;32m\nHello! Your programmers name is Alexza Jean.")
print("\033[1;32m\nShe's from BSCPE 1-4.")
print("-" * 70)

# Request for users encrypted input and then save it
input_str = input("\033[0;33m\nKindly type in a encrypted text that I can decrypt?\n")
output_str = ""

# Put every character and its corresponding value
for i in range(len(input_str)):
#   if *, change a
    if input_str[i] == "*":
        output_str += "a"
#   if &, change e
    elif input_str[i] == "&":
        output_str += "e"  
#   if #, change i
    elif input_str[i] == "#":
        output_str += "i" 
#   if +, change o
    elif input_str[i] == "+":
        output_str += "o"
#   if !, change u
    elif input_str[i] == "!":
        output_str += "u"


