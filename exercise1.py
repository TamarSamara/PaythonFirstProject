# ex.1 (a):
# Print the number of times each character appears in the string (str1).
def count_str(str1):
    count_dict = {}
    for i in str1:
        count_dict[i] = count_dict.get(i, 0) + 1
    print(count_dict)
    return count_dict

s = "dabaxyddab"
dict = count_str(s)
print(f' dict = {dict}')
sorted_dict = sorted(dict.items())
for x, y in sorted_dict:
    print(f'{x} - {y} ')

# ex.1 (b):
# Build an inverted dictionary (turn values into keys).
new_dict_asc = {}
dict_keys = sorted(dict, key=dict.get)

for i in dict_keys:
    new_dict_asc[i] = dict[i]
reversed_dict = {}
for x, y in new_dict_asc.items():
    if y not in reversed_dict.keys():
        add_list = list(x)
        reversed_dict.update({y: add_list})
    else:
        add_list.append(x)

print(reversed_dict)
