def enumerate_list(list):
    nlist=[]
    for index, elementos in enumerate(list):
        if elemento:
            nlist.append(f"{index}. {elemento}")
    return list


def enumerate_backwards(list):
    nlist=[]
    for index, elemento in enumerate(list[::-1]):
        nlist.append(f"{index}.{elemento[::-1]}")
    return list
