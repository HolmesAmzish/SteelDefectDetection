defect_dict = ["夹杂物","补丁","划痕","其他"]

def translate_defects(string_list):
    """
    Translate binary label array to specific defect names.
    Args:
        bool_list: A string representation of binary array like '[True False False True]'
                   or a list of boolean values
    Returns:
        list: A list of defect names found in the sample
    """

    if isinstance(string_list, str):
        bool_list = string_list.strip('[]').split()
        bool_list = [b == 'True' for b in bool_list]

    defects = []
    for i, is_defect in enumerate(bool_list):
        if is_defect:
            defects.append(defect_dict[i])
    
    return defects if defects else ["无缺陷"]

def format_defects(string_list):
    """
    Format the list of defects into a readable string.
    Args:
        defects: List of defect names
    Returns:
        str: Formatted string of defects
    """
    defects = translate_defects(string_list)
    return '、'.join(defects)
