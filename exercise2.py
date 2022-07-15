# ex.2 a :
# Lists with at least one repeat member are returned False.
def repeat_number(lst):
    if len(lst) != len(set(lst)):
        return False
    else:
        return True

lst1 = [11, 7, 5, 8, 5, 37, 11, 5]
lst2 = [22, 8, 10, 1, 11]
lst3 = [ 71, 3, 22, 8, 2, 14, 1]

rep_list1 = repeat_number(lst1)
rep_list2 = repeat_number(lst2)
rep_list3 = repeat_number(lst3)

print(f' list 1 is : {rep_list1}')
print(f' list 2 is : {rep_list2}')
print(f' list 3 is : {rep_list3}')

# ex.2 b :
# Common values that found in listes there not returned False from all lists.
inter_lists = []
if rep_list1 is False and rep_list2 is False and rep_list3 is False:
    print("all lists is False!")
else:
    if rep_list1 is True:
        if rep_list2 is True:
            inter_lists += list(set(lst1).intersection(set(lst2)))
        if rep_list3 is True:
            inter_lists += list(set(lst1).intersection(set(lst3)))
    if rep_list2 is True:
        if rep_list3 is True:
            inter_lists += list(set(lst2).intersection(set(lst3)))

common_values = set(inter_lists)

if len(common_values) == 0:
    print("There are no common values ")
else:
    print(f' The common values are --> {common_values}')
