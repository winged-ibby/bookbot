def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    chars = {}
    
    for character in text:
        char = character.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    return chars

def get_dicts_list(dict):
    dicts_list = []
    new_dict = {}

    for key in dict:
        value = dict[key]
        new_dict["char"] = key
        new_dict["num"] = value
        dicts_list.append(new_dict)
        new_dict = {}
    
    return dicts_list

def sort_on(dict):
    return dict["num"]

def sort_dicts_list(dicts_list):
    dicts_list.sort(reverse=True, key=sort_on)
    return dicts_list

