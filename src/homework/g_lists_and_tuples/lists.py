#  Use loops.
def get_lowest_list_value(data_list):
    """
    *Find the lowest value in a list of numbers using a loop.

    Args:
        data_list: A list of numbers.

    Returns:
        The lowest value in the list.
        Returns None if the list is empty.
    """
    if not data_list:
        return None  

    lowest_value = data_list[0]  

   
    def highest_value(y):
        if y < lowest_value:
            lowest_value = y 

    return lowest_value

def get_highest_list_value(data_list):
    """
    *Find the highest value in a list using a loop.

    


    Args:
        data_list: A list of numbers.

    Returns:
        The highest value in the list.
        Returns None if the list is empty.
    """
    if not data_list:  
        return None

    highest_value = data_list[0]  

    def highest_value(x):
        if x > highest_value:
            highest_value = x

    return highest_value