import copy
from types import *


def list_to_dict(list_of_lists, key_index, inclusive_value="in", value_index=None):
    # if value_index:
    # 	dic = {list[key_index]: list[value_index]}
    # else:
    # 	re_dir_list = copy.deepcopy(list)
    # 	del(re_dir_list[key_index]
    # 	del(re_dir_list[value_index])
    # 	dic={list[key_index]: re_dir_list}
    # return dic
    final_dict = {}
    for rows in list_of_lists:
        if value_index:
            if type(value_index) == list:
                t_list = []
                for values in value_index:
                    t_list.append(rows[values])
                final_dict[rows[key_index]] = t_list
            else:
                final_dict[rows[key_index]] = rows[value_index]
        else:
            temp_list = copy.deepcopy(rows)
            if inclusive_value == "out":
                del(temp_list[key_index])
            final_dict[rows[key_index]] = temp_list
    return final_dict

names = [[1, 'naveen', 'bhopal', 24], [2, 'bunty', 'goa', 45],
         [3, 'nutan', 'xyz', 475], [4, 'ram', 'abc', 85]]
print list_to_dict(names, 0, "out", [1, 2, 3])
print list_to_dict(names, 0, "out", 1)


def dict_to_list(in_dict):
    final_list = []
    for keys in in_dict:
        final_list.append([keys, in_dict[keys]])
    return final_list

d = {1: 100, 2: 500, 3: 400}
v = {1: 20, 5: 90, 2: 600}
# c = {1: [10, 20, 30], 2: [40, 50, 60], 5: [70, 80, 90]}
# print dict_to_list(d)
# print dict_to_list(c)


def combine_dict(dict1, dict2):

    # for values in dict1:
    # 	for val in dict2:
    #		temp_dict1[values]
    # 		if values == val:
    # 			temp_dict1[values]=dict1[values]+dict2[val]
    # 			break
    #	temp_dict1[values]=dict1[value]
    # 	final_dict[value]

    #    return final_dict

    for val in dict1:
        for value in dict2:
            if val == value and dict1[val] == dict2[value]:
                dict1[val] = dict1[val] * 2
                dict2[value] = 0
                break
    temp_dict = dict(dict1.items() + dict2.items())
    for val in temp_dict:
       #   for vall in dict2:
        for value in dict1:
            if val == value and temp_dict[val] != dict1[value]:
                temp_dict[val] = temp_dict[val] + dict1[value]
                break
    return temp_dict


print"-----------------"
print combine_dict(d, v)
