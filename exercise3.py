# ex.3
# Print the numbers in the list in  ascending or descending order.
lst = [31, 99, 3, 1943]

lst2 = []
for num in lst:
    # for i in num:
    print(num)
    while num > 0:
        x = int(num % 10)
        if x not in lst2:
            lst2.append(x)
        num = int(num / 10)
print(lst2)
asc_or_desc = input("What do you want in ascending (asc) or descending (desc) order?")
if asc_or_desc == "asc":
    lst2.sort()
    print(lst2)
elif asc_or_desc == "desc":
    lst2.sort(reverse=True)
    print(lst2)
else:
    print("wrong writing (asc /desc)")


