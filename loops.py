def index_of_by_index(word, list, index):
    if word in list[:index+1]:
        return list.index(word)
    else:
        return -1


def index_of_empty(list):
    for index, elemento in enumerate(list):
        if elemento=="":
            return index
    return -1


def index_of(word, list):
    for index, elemento in enumerate(list):
        if elemento==word:
            return 1
    return -1


def put(word, list):
    for index, elemento in enumerate(list):
        if not elemento:
            list[index]=word
            return index
    return -1


def remove(word, list):
    if count>0:
        list=[elemento for elemento in list if elemento!=word]
        return count
    else:
        return -1
