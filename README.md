# pytransformer
**Transform complicated Python Data Structures**

**pytransformer** is a library written in Python for transforming complicated  Data structures in Python
## Installation
***
To install the package, type the following -

	pip install pytransformer
***

##### Functionalities Provided
-  **Transform List of List into Dict of List/Values**
        
    - Function to convert list of list to dictionary of list/values
        - param list_of_lists: The list of list which is to be converted to
dictionary
        - type list_of_lists: List of lists
        - param key_index: takes the key whose value will be the key value to the converted dictionary
        - type key_index: integer
        - param value_index:The key whose value will be used as resultant dict's value
        - type value_index:integer/list
        - returns:transformed_dict    
-  Transform  Dict of List/Values to List of List

    - Function to convert dictionary of list/values to list of list
        - param input_dict: The dictionary which is to be converted into list of list
        - type input_dict: dictionary
        - returns:transformed dictionary
-  Transform  List of Dict to Dict of Dict
    - Converts list of dict to dict with aggregate_key's value as key
        - param data: The data to be transformed
        - type data: list of dict
        - param aggregate_key: The key whose value will be used as resultant dict's key
        - type aggregate_key: string
        - param select_key: The key whose value will be used as resultant dict's value
        - type select_key: string
        - returns tranformed dictionary
-  Transform  Dict of Dict to List of Dict
    - Function to convert dictionary to list of dictionary
        - param input_dict: The dictionary which is to be converted into list of dictionary
        - type input_dict: dictionary
        - param select_key_name:the key whose value key of converted list of dictionary will be named
        - type select_key_name:string
        - returns:transformed list
    
-  Merge Dictionaries
    - Function to merge two/more Dictionaries
        - param merge_func:the functin to be performed(like addition/substraction/multiplication) for the same key values in the Dictionaries
        - type merge_func:function
        - param merge_type:Whether to perform union or intersection while merging Dictionaries
        - type merge_type:string ('or'/'and')
        - returns:merged_dict
        
More contents here : https://pypi.python.org/pypi/pytransformer/1.0
    
