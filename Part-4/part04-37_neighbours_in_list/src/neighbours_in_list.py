def longest_series_of_neighbours(l):
    longest = 1
    current_longest = 1
    for i in range(len(l) - 1):
        if abs(l[i+1] - l[i]) == 1:
            current_longest += 1
        else:
            longest = max(longest, current_longest)
            current_longest = 1

    return max(current_longest, longest)

if __name__=="__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))