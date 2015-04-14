test_name = open('test.txt')


# def count_num_words(test_name):
word_count = {} #open dictionary

for line in test_name:
    line = line.strip()
    new_line = line.rstrip().split()
    for word in new_line:
        if word_count.get(word) == None:
            word_count[word] = 1
        else:
            word_count[word] += 1

print word_count
    

