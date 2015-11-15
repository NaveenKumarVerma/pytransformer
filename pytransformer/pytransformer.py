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
        :returns:transformed_dict
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
        msg = """Can't convert Given List of List to Dictionary for key_index:{key_index} and value_index:{value_index} due to Error: {error}""".format(
            key_index=key_index, value_index=value_index, error=str(e))
        raise Exception(msg)


def dict_to_list_of_list(input_dict):
    """
        Function to convert dictionary of list/values to list of list
        :param input_dict: The dictionary which is to be converted into list of list
        :type input_dict: dictionary
        :returns:transformed dictionary
    """
    try:
        return [[key, value] for key, value in input_dict.iteritems()]
    except Exception as e:
        msg = """Can't convert Given Dictionary to List of List due to Error: {error}""".format(
            error=str(e))
        raise Exception(msg)


def list_of_dict_to_dict(data, aggregate_key, select_key=None):
    """
        Converts list of dict to dict with aggregate_key's value as key
        :param data: The data to be transformed
        :type data: list of dict
        :param aggregate_key: The key whose value will be used as resultant dict's key
        :type aggregate_key: string
        :param select_key: The key whose value will be used as resultant dict's value
        :type select_key: string
        :returns tranformed dictionary
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
        msg = """Can't convert Given List of Dict to Dictionary for aggregate_key: {a_key},select_key: {s_key } due to Error: {error}""".format(
            a_key=aggregate_key, s_key=select_key, error=str(e))
        raise Exception(msg)


def dict_of_dict_to_list_of_dict(input_dict, select_key_name):
    """
        Function to convert dictionary to list of dictionary
        :param input_dict: The dictionary which is to be converted into list of dictionary
        :type input_dict: dictionary
        :param select_key_name:the key whose value key of converted list of dictionary will be named
        :type select_key_name:string
        :returns:transformed list
    """
    try:
        transformed_list = []
        for key, value in input_dict.iteritems():
            temp_dict = copy.deepcopy(value)
            temp_dict[select_key_name] = key
            transformed_list.append(temp_dict)
        return transformed_list
    except Exception as e:
        msg = """Can't convert Given Dict to List of Dictionary for select_key_name: {select_key_name} due to Error: {error}""".format(
            select_key_name=select_key_name, error=str(e))
        raise Exception(msg)


def merge_dicts(merge_func, merge_type='or', *dicts):
    """
        Function to merge two/more Dictionaries
        :param merge_func:the functin to be performed(like addition/substraction/multiplication) for the same key values in the Dictionaries
        :type merge_func:function
        :param merge_type:Whether to perform union or intersection while merging Dictionaries
        :type merge_type:string ('or'/'and')
        :returns:merged_dict
    """
    try:
        if len(dicts) > 1:
            merged_dict = {}
            if merge_type == 'or':
                all_keys = set([])
                for input_dict in dicts:
                    all_keys = all_keys | set(input_dict.keys())
            elif merge_type == 'and':
                all_keys = set(dicts[0].keys())
                for input_dict in dicts:
                    all_keys = all_keys & set(input_dict.keys())
            else:
                msg = """Dictionaries can't be merged as merge_type:{merge_type} is other than 'or' and 'and' """.format(
                    merge_type=merge_type)
                raise Exception(msg)
            for key in all_keys:
                merged_dict[key] = merge_func(
                    [input_dict.get(key) for input_dict in dicts])
            return merged_dict
        elif len(dicts) == 1:
            return dicts[0]
        else:
            msg = """Please provide valid Dictionaries"""
            raise Exception(msg)
    except Exception as e:
        msg = """Dictionaries can't be merged due to Error: {error}""".format(
            error=str(e))
        raise Exception(msg)


def sum(input_list):
    """
        Function to add elements in the list
        :param input_list:list whose elementsare to be added
        :type input_list:list
        :returns: total
    """
    try:
        total = 0
        for value in input_list:
            if type(value) == int or type(value) == float:
                total += value
        return total
    except Exception as e:
        msg = """Sum function not working due to Error: {error}""".format(
            error=str(e))
        raise Exception(msg)
