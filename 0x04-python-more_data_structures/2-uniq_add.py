#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = []
    for num in my_list:
        if num not in newlist:
            newlist.append(num)
    return sum(newlist)
