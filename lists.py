# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
    elif len(list_to_remove_elements) >= 5:
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
    elif len(list_to_remove_elements) >= 4:
        del list_to_remove_elements[0]
    return list_to_remove_elements
    

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements
    
def is_empty(list_to_check):
    return len(list_to_check) == 0


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) > 2 and len(list_to_compare2) > 2:
        return list_to_compare1[2] == list_to_compare2[2]
    return False

def list_of_lists(list_of_lists_to_modify):
    list0 = list_of_lists_to_modify[0]
    list1 = list_of_lists_to_modify[1]
    list2 = list_of_lists_to_modify[2]

    if len(list0) >= 2:
        first_list = list0[0:2]
    elif len(list0) == 1:
        first_list = list0[0:1]
    else:
        first_list = []

    if len(list1) >= 4:
        second_list = list1[1:4]
    elif len(list1) == 3:
        second_list = list1[1:3]
    elif len(list1) == 2:
        second_list = list1[1]
    else:
        second_list = []

    if len(list2) >= 2:
        third_list = list2[-2:len(list2)]
    elif len(list2) >= 1:
        third_list = list2[-1:len(list2)]
    else:
        third_list = []

    return [first_list] + [second_list] + [third_list]
