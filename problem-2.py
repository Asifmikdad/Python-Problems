# encript the following code using ascii value
# to check any ascii valu of any character use ord()

data = "ai"
shift = 1
output = ""
for character in data:
    output += chr((ord(character) + shift - 97) % 26 + 97)

print(output)