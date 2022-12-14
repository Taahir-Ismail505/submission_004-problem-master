
def find_min(element):
    """TODO: complete for Step 1"""
    if len(element) == 0 :
        return -1

    for e in element :
        if type(e) != int:
            return -1
    
    if len(element) == 1 :  
        return element[0]
    else: 
        if element[0] > element[1] :
            element.remove(element[0]) 
        elif element[1] > element[0] :
            element.remove(element[1])
        return find_min(element) 
        

def sum_all(element):
    """TODO: complete for Step 2"""
    if len(element) == 0 :
        return -1

    for e in element :
        if type(e) != int:
            return -1
    if len(element) == 1:
        return element[0]
    else:
        element[0] += element[1]
        element.remove(element[1])
        return sum_all(element)


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3""" 
    character_set_lenth= len(character_set) 
    for e in character_set :
        if type(e) != str:
            return []
 
    if character_set_lenth == 0:
        return []
 
    if(n==0):
        return [""]
    word = []
    try:
        for i in character_set:
            for k in find_possible_strings(character_set, n-1):
                word.append(i+k)
    except :
        return []
    return word


# def run_game():
#     char_set =["x","y"]    
#     # element = [6,5,2,3,1]    
#     # element1 = [5,4,2,3,1] 
#     # print(find_min(element))
#     # print(sum_all(element1))
#     possible_strings = find_possible_strings(char_set, 2)
#     print(possible_strings)
# if __name__ == "__main__":
#     run_game()

