def replace_word(str):
    word_to_replace = input("Enter the word to replace in your sentence: ")
    word_replcement = input("Enter the word you want to replace with: ")
    print(str.replace(word_to_replace,word_replcement))

str = input("Enter a sentence: ")
replace_word(str)