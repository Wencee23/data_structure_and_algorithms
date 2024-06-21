def get_smallest_interger(my_list):
    smallest = my_list [0]
    for interger in my_list[1:]:
        if interger < smallest:
            smallest = interger 
    return smallest

my_list = [82,14,20,90]
print("Smallest interger is" ,get_smallest_interger(my_list))
