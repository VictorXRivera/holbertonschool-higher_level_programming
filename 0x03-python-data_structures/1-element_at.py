#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 1 or idx >= my_list[idx]:
        return None
    else:
        return my_list[idx]
