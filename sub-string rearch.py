def count_substring(string, sub_string):
    count = 0
    start = 0
    
    # Loop to find each occurrence of the substring
    while start < len(string):
        # Find the next occurrence of sub_string starting from 'start' index
        start = string.find(sub_string, start)
        
        # If find() returns -1, no more occurrences are found
        if start == -1:
            break
        
        # Increment the count for this occurrence
        count += 1
        
        # Move start index forward to continue searching for the next occurrence
        start += 1
    
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    # Call the function to count occurrences of the substring
    count = count_substring(string, sub_string)
    
    # Output the count
    print(count)
