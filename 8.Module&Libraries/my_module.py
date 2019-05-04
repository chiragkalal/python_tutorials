
print('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):   # define index(0,1,2 ...) and values given by to_search
        if value == target:                 # if target value is in value of search then return index.
            return i

    return -1