#6809658138 
#suwijuk bouchum

def get_number(num, spaces):
  num = str(num)
  range_spaces = spaces - len(num)
  range_num = ""
  for i in range(range_spaces):
    range_num = range_num + " "
  range_num = range_num + num  
  return range_num

def get_word(words, spaces):
  range_num = ((spaces-len(words))//2)
  range_spaces = ""

  if len(words) > range_num :
    return words
  
  else :

    if (range_num % 2) == 0 :
       for i in range (range_num):
         range_spaces = range_spaces + " "

       range_spaces = range_spaces + words

       for i in range (range_num):
         range_spaces = range_spaces + " "

       return range_spaces  

    else :

        for i in range (range_num+1):
         range_spaces = range_spaces + " "

        range_spaces = range_spaces + words

        for i in range (range_num-1):
         range_spaces = range_spaces + " "

        return range_spaces 



def get_row(num, size, spaces):

  if num==0 :
    print("     ",end="")
    str_num = ""
    for i in range(1,size+1):
     str_num  = str_num + (get_number(i, spaces))
    return str_num

  else :
    print(get_number(num, 2) + "  |", end="") 
    total  = 0
    for i in range (1 ,size+1):
      total = i * int(get_number(num, spaces))
      print(get_number(total, spaces),end="")
    print("")     




def display_separator(size, spaces):
  
  range_dy = (size+1)*spaces
  display = "" 
  for i in range(range_dy):
    display = display + "-"
  print(display)

def display_table(size, spaces):
  for i in range(1,size+1):
    get_row(i,size,spaces)

def get_user_input():
    input_user = int(input("Enter the size of the multiplication table (1-20): "))
  
    while input_user < 1 or input_user >20:
      print("Table size should be between 1 and 20.")
      input_user = int(input("Please try again: "))
    return int(input_user)  




def display_heading(size,spaces):
  display_separator(size,spaces)
  title = str(size) + "x" + str(size) + " Times Table"
  print(get_word(title, (size+1)*spaces))
  print(get_row(0, size,spaces))
  display_separator(size,spaces)  

def main():
  size = get_user_input()
  spaces = len(str(size*size))+2
  display_heading(size,spaces)
  display_table(size,spaces)
  display_separator(size,spaces)  

main()