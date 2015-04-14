test_name = open('test.txt')


def count_num_words(test_name):
    word_count = {} #open dictionary

    for line in test_name:
        line = line.strip()
        new_line = line.rstrip().split()
        for word in new_line:
            if word_count.get(word) == None: #if the value assigned to the word is none 
                word_count[word] = 1         #which they all are bc there is no values yet, assign value of 1
            else:                            #if the word(key) is in the dict again, value will count up by 1
                word_count[word] += 1  

    for word_name, count in word_count.iteritems(): #assigning word_name to key and count to value
        print word_name, count

count_num_words(test_name)