from stats import get_num_words, get_book_text, print_char_list

print("============ BOOKBOT ============")
contents = get_book_text()

print("----------- Word Count ----------")
get_num_words(contents)

print("--------- Character Count -------")
print_char_list(contents)

print("============= END ===============")