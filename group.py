

# Purpose: Groups elements of an integer array into sublists of 3 elements each
# Input: `array` - list of integers
# Output: A list of lists, where each sublist contains up to 3 integers from `array`
# Data Representation: Takes a list of integers and returns a list of lists,
#                      with each inner list containing groups of 3 integers
def groups_of_3(array:list[int])->list[list[int]]:
    list_of_list=[]
    for i in range(((len(array))//3)+1):
        list_of_list.append(array[i*3:(i+1)*3])
    return list_of_list

print(groups_of_3([1,2,3,5,2,1,3,1,5,5,2,3,2,3]))