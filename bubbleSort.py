def bubble_sort(num_list):
    global no_of_passes,no_of_swaps
    end_index=len(num_list)
    for index1 in range(0, end_index-1):
        swapped=False
        no_of_passes+=1
        for index2 in range(0, (end_index-index1-1)):
            if(num_list[index2]>num_list[index2+1]):
                temp = num_list[index2]
                num_list[index2] = num_list[index2+1]
                num_list[index2+1] = temp
                no_of_swaps+=1
                swapped=True
        if(swapped==False):
            break
        print("At the end of pass-",no_of_passes,":",num_list)
no_of_swaps=0
no_of_passes=0
num_list=[5,4,3,2,1]
print("In the beginning:",num_list)
print("______________________________________________")
bubble_sort(num_list)
print("______________________________________________")
print("At the end:",num_list)
print("______________________________________________")
print("No. of swaps:", no_of_swaps)
print("No. of passes:",no_of_passes)
