def character_frequency(string):
    string = string.upper()
    
    frequency_dict = {}
    
    for char in string:
        
        if char.isalpha():
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
    
    return frequency_dict

if __name__ == "__main__":
    test_string = "I WILL BE BACK IN A MINUTE!"
    print(character_frequency(test_string))
