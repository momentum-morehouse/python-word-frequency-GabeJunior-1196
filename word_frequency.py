STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
import re
song = "praise_song_for_the_day.txt"
def print_word_freq(file):
    # """Read in `file` and print out the frequency of words in that file."""
    # Your code will go here. You can write additional functions if you want, and call them inside this function.
    # first open the file
    with open(file) as f:
        lyrics = f.readlines()
        
        word_list = [line.split() for line in lyrics]
        

        word_list = [n for short_list in word_list for n in short_list]
        
    cleaned_array = []
    for word in word_list:
        word = word.lower()
        word = re.sub(r'[^A-Za-z]', '', word)
        if word not in STOP_WORDS:
          cleaned_array.append(word)
    dict = {}    
    for word in cleaned_array:
        dict[word] = dict.get(word, 0) + 1  


        
    print(dict)      
        
        

# return(word_list)

# This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
