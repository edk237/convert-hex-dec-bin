source = None
translated = None

convert_opt = {
    'b': 'Binary',
    'd': 'Décimal',
    'x': 'Héxadecimal'
}

while source == translated:
    for i, value in enumerate(convert_opt): #Opiton's list
        print(i, '-', convert_opt[value])
    source = int(input("Quel est le format d'origine ? (0-2) :"))

        
    for i, value in enumerate(convert_opt): #Opiton's list
        print(i, '-', convert_opt[value])
    translated = int(input("Vers quel format traduire ? (0-2) :"))
    print("                              ")
    print("YOU CANT CONVERT THE SAME DATA")
    print("                              ")
    input("Press ENTER when you read...")


if source == 0:     #If we Choosed Binary
    value_source = input(f" You have choosed the {convert_opt['b']} format, What is it's value ? : ")
    while any(char != '0' and char != '1' for char in value_source):     # Loop if user enters anything else than 0 or 1
        print("Data needs to be 0 or 1")
        value_source = input("So? What's your binary value? : ")

elif source == 1:   #If we Choosed Decimal
    value_source = input(f" You have choosed the {convert_opt['d']} format, What is it's value ? : ")
    while type(value_source) == str or type(value_source) == float:     # Loop if user enters anything than a decimal
        try:
            value_source = int(value_source)
            break
        except ValueError:
            print("Please enter a valid integer value.")
            value_source = input("What is its value? : ")

elif source == 2:   #If we Choosed Hexa
    value_source = input("Enter an hexa value : ")   
    while not all(char.upper() in '0123456789ABCDEF' for char in value_source): #Verify Characters
        print("Veuillez entrer une valeur hexadécimale valide (0-9, A-F).")
        value_source = input("Enter an hexa value : ")

def dec_binary(d):     #Decimal to Binary
    print(bin(d))
def dec_hex(d):     #Decimal to Hexa
    print(hex(d))

def hex_binary(h):     #Hexa to Binary
    t = int(value_source, 9)
    print(t)
    print(bin(t))
def hex_dec(h):     #Hexa to Decimal
    t = int(value_source, 16)
    str(t)
    print(t)

# def bin_dec(b):
# def bin_hex(b):

if source == 1 and translated == 0 :    #Decimal To Binary
    print(f"You're going to tansform", {value_source}, "into Binary")
    dec_binary(value_source)

if source == 1 and translated == 2 :    #Decimal To Hexa
    print(f"You're going to tansform", {value_source}, "into Hexa")
    dec_hex(value_source)

if source == 2 and translated == 1 :    #Hexa To Decimal
    print(f"You're going to tansform", {value_source}, "into Hexa")
    hex_dec(value_source)

if source == 2 and translated == 0 :    #Hexa To Binary
    print(f"You're going to tansform", {value_source}, "into Hexa")
    hex_binary(value_source)
