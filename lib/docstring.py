# docstrings : 설명(description)

# ctrl + shift + p -> docstring
def list_add(l : list) -> int:
    """_summary_                        (함수 설명)

    Args:                               (파라메터 설명)
        l (list): _description_

    Returns:                            (반환값 설명)
        int: _description_
    """    
    
    temp = 0
    for i in l:
        temp += i
    return temp


print(list_add([1,2,3]))






        
