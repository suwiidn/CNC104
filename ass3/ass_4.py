#6809658138
#ให้gemini ช่วยคับ

def is_legistimate_code(code_string):
    code_letters = ["S", "B", "N", "T", "P"]
    min_for_each_letter = [1, 3, 4, 0, 3]
    max_for_each_letter = [7, 9, 6, 7, 5]

    if len(code_string) == 0:
        return False

    first_char = code_string[0]

    letter_index = -1
    for i in range(len(code_letters)):
        if code_letters[i] == first_char:
            letter_index = i
            break  

    if letter_index == -1:
        return False

    min_val = min_for_each_letter[letter_index]
    max_val = max_for_each_letter[letter_index]

    has_number = False  
    
    for i in range(1, len(code_string)):
        char = code_string[i]

        if char == " ":
            continue
            
        if char.isdigit() == False:
            return False 
            
        num = int(char)
        
        if num < min_val or num > max_val:
            return False
            
        has_number = True

    if has_number == False:
        return False

    return True
print("1.", is_legistimate_code('B747346'))
print("2.", is_legistimate_code('N  444  454 '))
print("3.", is_legistimate_code('T 400 4854'))
print("4.", is_legistimate_code('S   444S454'))
print("5.", is_legistimate_code('P    '))
print("6.", is_legistimate_code('T  0   '))