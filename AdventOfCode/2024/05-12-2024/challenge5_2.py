'''
--- Part Two ---
While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

75,97,47,61,53 becomes 97,75,47,61,53.
61,13,29 becomes 61,29,13.
97,13,75,29,47 becomes 97,75,47,29,13.
After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?

'''
def check(nums, dict, number):

    if nums == None:
        return False

    for num in nums:
        if num in dict.keys():
            if number in dict[num]:
                return True
            
    return False

def take_before(i, candidate):
    if i != 0:
        return candidate[:i]
    else: return None

def take_after(i, candidate):
    if i != len(candidate)-1:
        return candidate[i+1:]
    else: return None

def valid(candidate, dict_first, dict_second):

    for i, number in enumerate(candidate):
        num_to_check_before = take_before(i, candidate)
        num_to_check_after = take_after(i, candidate)
        if check(num_to_check_before, dict_second, number) or check(num_to_check_after, dict_first, number):
            return False

    return True

def swap_array(value1, value2, array):

    index1 = array.index(value1)
    index2 = array.index(value2)

    array[index1], array[index2] = array[index2], array[index1]

def swap(nums, dict, number, arr):
    
    if nums == None:
        return 

    for num in nums:
        if num in dict.keys():
            if number in dict[num]:
                swap_array(number, num , arr)
                return
            
def swapp_order(candidate, dict_first, dict_second):

    for i, number in enumerate(candidate):
        num_to_check_before = take_before(i, candidate)
        num_to_check_after = take_after(i, candidate)
        swap(num_to_check_before, dict_second, number, candidate)
        swap(num_to_check_after, dict_first, number, candidate)
            
queue = open("inputpuzzle5_1.txt", "r")
updates = open("inputpuzzle5_2.txt", "r")

queue_dict_first = {}
queue_dict_second = {}
update_list= []

for pair in queue:
    first, second = map(int, pair.split('|'))
    if first not in queue_dict_first.keys():
        queue_dict_first[first] = [second]
    else:
        queue_dict_first[first].append(second)

    if second not in queue_dict_second.keys():
        queue_dict_second[second] = [first]
    else:
        queue_dict_second[second].append(first)

for update in updates:
    update_list.append([ int(number) for number in update.strip().split(',') ])

mids_number = []
wrong_cand = []

for candidate in update_list:
    if not valid(candidate, queue_dict_first, queue_dict_second) :
        wrong_cand.append(candidate)

def reorder(candidate_to_reorder, dict1, dict2):
    ordered =False
    while not ordered:
        swapp_order(candidate_to_reorder, dict1, dict2)
        ordered = valid(candidate_to_reorder, dict1, dict2)
        
for to_order in wrong_cand:
    reorder(to_order, queue_dict_first, queue_dict_second)
    mids_number.append(to_order[len(to_order)//2])

print(sum(mids_number))
