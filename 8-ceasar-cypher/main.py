
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar_cypher(start_text, shift_amount, cypher_direction): 
    final_result = ""
    if cypher_direction == False:
        shift_amount *= -1
        operation = "decode"
    else:
        operation = "encode"
            
    for letter in start_text:
        position_of_letter= alphabet.index(letter)
        cyphered_letter_position = position_of_letter + shift_amount
        if cyphered_letter_position >= 26 or cyphered_letter_position <= 26: 
            cyphered_letter_position = cyphered_letter_position%26
        cyphered_letter =  alphabet[cyphered_letter_position]
        final_result += cyphered_letter
    print(f"result of {operation}d text is {final_result}")


word = input("choose a word to encode or decode:\n")
shift = input("shif: \n")
if shift == "":
    shift = 0  # Set default value to 0
else:
    shift = int(shift)
operation =  eval(input("encode : True , decode : False \n"))
ceasar_cypher(word.lower(), shift,  operation)