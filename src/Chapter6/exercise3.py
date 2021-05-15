def count(word,letter_count):
    count = 0
    for letter in word:
        if letter==letter_count:
            count = count + 1
    print(count)

word=input("Enter word:")
letter_count=input("Enter letter to be counted:")
count(word,letter_count)

