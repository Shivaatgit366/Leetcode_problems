from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_list_node_to_list(node1: ListNode) -> List[int]:
    output_list = []
    current_node = node1
    while current_node != None:
        output_list.append(current_node.val)
        current_node = current_node.next
    return output_list


def convert_list_to_listnode(list: List[int]) -> ListNode:
    # last_node = ListNode(val=list[0], next=None)
    # middle_node = ListNode(val=list[1], next=last_node)
    # first_node = ListNode(val=list[2], next=middle_node)

    current_node = None
    for value in list:
        prev_node = current_node
        current_node = ListNode(val=value, next=prev_node)
    return current_node


def list_to_int_maker(list_item):
    to_string = ""
    for item in list_item:
        to_string = to_string + str(item)
    return int(to_string[::-1])


def add_two_lists(list1, list2):  # list1 and list2 are the lists
    a = list_to_int_maker(list1)
    b = list_to_int_maker(list2)
    c = a + b
    d = str(c)
    output_listt = [int(m) for m in d]
    return output_listt[::-1]

if __name__ == '__main__':

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    list_1_third_node = ListNode(val=3)
    list_1_second_node = ListNode(val=4, next=list_1_third_node)
    list_1_first_node = ListNode(val=2, next=list_1_second_node)

    list_2_third_node = ListNode(val=4)
    list_2_second_node = ListNode(val=6, next=list_2_third_node)
    list_2_first_node = ListNode(val=5, next=list_2_second_node)

    list1 = convert_list_node_to_list(list_1_first_node)
    print(list1)
    list2 = convert_list_node_to_list(list_2_first_node)
    print(list2)

    output_list = add_two_lists(l1, l2)
    print("output_list", output_list)

    output_first_node = convert_list_to_listnode(output_list[::-1])
    print(output_first_node.val)