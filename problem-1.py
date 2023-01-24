# Clean the data and get sting output "a e i o u'

data = "arEinOyU"

new_data = data.lower()

output_data = ""

for letter in new_data:
    if (letter == "a") or (letter == "e") or (letter == "i") or (letter == "o") or (letter == "u"):
        output_data += letter +"_"

print(output_data)