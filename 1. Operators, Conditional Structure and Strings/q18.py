my_str=input("Enter a String: ").lower()

a_count=my_str.count('a')
e_count=my_str.count('e')
i_count=my_str.count('i')
o_count=my_str.count('o')
u_count=my_str.count('u')
count=a_count+e_count+i_count+o_count+u_count
print(f'There are {count} number of vowel in the given string')