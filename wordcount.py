test_name = open('test.txt')


# def count_num_words(test_name):
#     word_count = {} #open dictionary

for line in test_name:
    line = line.strip()
    new_line = line.rstrip()
    space_out = new_line.replace(" ", "\n") 
    
   
    """needed to strip blank lines in between each line in addition to 
    rstrip. Didn't know until ran for loop and printed the entire text doc"""
        
    print space_out
 #    for w in words:
 #         if word_count.get(w) == None:
 #             word_count[w] = 1
 #         else:
 #             word_count[w] += 1

 #     print word_count

 # count_num_words('test.txt')