def find_first_occurrence(my_list, num):
    try:
        return my_list.index(num)
    except ValueError:
        return None

# Test the function
if __name__ == "__main__":
    test_list = [1,3,5,7,9,11,13,15]
    num_to_find = 11
    print(find_first_occurrence(test_list, num_to_find))
