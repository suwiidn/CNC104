#6809658138
def get_longest_word(word_list):
    lg = ''
    for i in word_list:
        if len(i) >= 6 and len(i) >= len(lg):
            lg = i
    return lg

print("1.", get_longest_word(["Melissa", "Jessie", "Kath", "Amity", "Raeann"])) 
print("2.", get_longest_word(["Jo", "Jessie", "Penelope", "Jin", "Raeann", 
"Pamelita"])) 
print("3.", get_longest_word(["Alan", "Jess", "Amity", "Rosalie", "Rosetta"])) 
print("4. ", "***", get_longest_word(["Jo", "Jai", "Jen", "Jing", "Joey", "Jess"]), 
"***", sep = "") 
print("5. ", "***", get_longest_word([]), "***", sep = "")
print("6.", "***" + get_longest_word([""]) + "***")