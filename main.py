# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open("./story.txt", "r") as openfile:
        read_file_content = openfile.read()
    
    return read_file_content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    split_txt = text.split()
    
    total = {}
    for i in split_txt:
        if i in total:
            total[i] += 1

        else:
            total[i] = 1

    return total

print(count_words())
