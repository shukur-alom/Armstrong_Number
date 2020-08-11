try:
   from functools import reduce
   user_input_number = input("Number : ")
   number_list = [] 
   for c in range(len(user_input_number)):
      number_list.append(int(user_input_number[c])**3)
   red = reduce(lambda x,y: x+y,number_list)
   if int(user_input_number) == red: print(f"{user_input_number} is an armstrong number!")
   else: print(f"{user_input_number} is not an armstrong number!")
except ValueError: print(f"\n input int type number\n")