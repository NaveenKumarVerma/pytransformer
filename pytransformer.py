import copy


def list_of_list_to_dict(list_of_lists, key_index, value_index=None):
    """
        Function to convert list of list to dictionary of list/values
        :param list_of_lists: The list of list which is to be converted to dictionary
        :type list_of_lists: List of lists
        :param key_index: takes the key whose value will be the key value to the converted dictionary
        :type key_index: integer
        :param value_index:The key whose value will be used as resultant dict's value
        :type value_index:integer/list
    """
    try:
        transformed_dict = {}
        if value_index:
            if type(value_index) == list:
                for row in list_of_lists:
                    transformed_dict[row[key_index]] = [row[index]
                                                        for index in value_index]
            elif type(value_index) == int:
                for row in list_of_lists:
                    transformed_dict[row[key_index]] = row[value_index]
        else:
            for row in list_of_lists:
                temp_list = copy.deepcopy(row)
                del(temp_list[key_index])
                transformed_dict[row[key_index]] = temp_list
        return transformed_dict
    except Exception as e:
        msg = """list_of_list_to_dict: Can't convert due to Error: {error}""".format(
            error=str(e))
        raise Exception(msg)


def dict_to_list_of_list(input_dict):
    """
        Function to convert dictionary of list/values to list of list
        :param input_dict: The dictionary which is to be converted into list of list
        :type input_dict: dictionary
    """
    return [[key, value] for key, value in input_dict.iteritems()]


def list_of_dict_to_dict(data, aggregate_key, select_key=None):
    """
        Converts list of dict to dict with aggregate_key's value as key
        :param data: The data to be transformed
        :type data: list of dict
        :param aggregate_key: The key whose value will be used as resultant dict's key
        :type aggregate_key: string
        :param select_key: The key whose value will be used as resultant dict's value
        :type select_key: string
        :param complete: If True the whole dict will be used as resultant dict's value
        :type complete: bool
        :returns tranformed dict
    """
    try:
        transformed_dict = {}
        if select_key:
            if type(select_key) == list:
                for row in data:
                    if row.get(aggregate_key):
                        transformed_dict[row[aggregate_key]] = [
                            row[key] for key in select_key]
            else:
                for row in data:
                    if row.get(aggregate_key):
                        transformed_dict[row[aggregate_key]] = row[select_key]
        else:
            for row in data:
                if row.get(aggregate_key):
                    transformed_dict[row[aggregate_key]] = copy.deepcopy(row)
        return transformed_dict
    except Exception as e:
        msg = """list_of_dict_to_dict: Can't convert list of dict to dic for aggregate_key: {a_key},select_key: {s_key } due to Error: {error}""".format(
            a_key=aggregate_key, s_key=select_key, error=str(e))
        raise Exception(msg)


def dict_to_list_of_dict(input_dict, select_key_name):
    """
        Function to convert dictionary to list of dictionary
        :param input_dict: The dictionary which is to be converted into list of dictionary
        :type input_dict: dictionary
    """
    transformed_list = []
    for key, value in input_dict.iteritems():
        temp_dict = copy.deepcopy(value)
        temp_dict[select_key_name] = key
        transformed_list.append(temp_dict)
    return transformed_list


def merge_dicts(merge_func, *dicts, merge_type='or'):
    try:
        if len(dicts) > 1:
            merged_dict = {}
            all_keys = set([])
            if merge_type == 'or':
                for input_dict in dicts:
                    all_keys = all_keys | set(input_dict.keys())
            elif merge_type == 'and':
                for input_dict in dicts:
                    all_keys = all_keys & set(input_dict.keys())
            else:
                raise Exception(msg)
            for key in all_keys:
                merged_dict[key] = merge_func(
                    [input_dict.get(key) for input_dict in dicts])
            return merged_dict
        elif len(dicts) = 1:
            return dicts[0]
        else:
            raise Exception(msg)
    except Exception as e:
        msg = """merge_dicts: Can't convert due to Error: {error}""".format(
            error=str(e))
        raise Exception(msg)


def sum(input_list):
    total = 0
    for value in input_list:
        if type(value) == int or type(value) == float:
            total += value

    return total
