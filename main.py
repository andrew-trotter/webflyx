import sys
from stats import get_num_words, get_book_text, print_char_list

if(len(sys.argv) < 2):
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

print("============ BOOKBOT ============")
contents = get_book_text(sys.argv[1])

print("----------- Word Count ----------")
get_num_words(contents)

print("--------- Character Count -------")
print_char_list(contents)

print("============= END ===============")