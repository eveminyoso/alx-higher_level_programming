#!/usr/bin/python3
def element_at(my_list, idx):
    len_ = len(my_list)

    if idx < 0 or idx > len_:
        return None
    cnt = 0
    for i in my_list:
        if cnt == idx:
            return i
        cnt += 1
    return None
