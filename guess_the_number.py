def binary_search(num, element_list):
    no_of_guesses = 0
    low = 0
    high = len(element_list) - 1
    while(high >= low):
        mid = (high + low) // 2
        no_of_guesses += 1
        if(element_list[mid] == num):            
            return no_of_guesses
        elif(element_list[mid] < num):
            low = mid + 1
        else:
            high = mid - 1
    return no_of_guesses
print('Number found in',binary_search(43,[10,23,30,43,50,78]), 'guesses')