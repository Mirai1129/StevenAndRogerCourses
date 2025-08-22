def reverse_list(input_list):
    reversed_list = []
    
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list

def sort_list(input_list: list):
    return sorted(input_list)

def main():
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(sample_list)
    print("Original List:", sample_list)
    print("Reversed List:", reversed_list)
    
    sorted_list = sort_list(sample_list)
    print("Sorted List:", sorted_list)

if __name__ == "__main__":
    main()
