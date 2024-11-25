sentence = input("Enter Sentance :")
most_repeating_character = None
max_count = 0
for i in range(len(sentence)):
    current_char = sentence[i]
    count=0
    for j in range(len(sentence)):
        if sentence[j]==current_char:
            count+=1
            if count>max_count:
                max_count=count
                most_repeating_character=sentence[j]
print(f"The Most Repeating Character is  ({most_repeating_character})  With  count {max_count}")
    