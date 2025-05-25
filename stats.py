def get_book_text():
  path_to_file = "books/frankenstein.txt"
  print(f"Analyzing book found at {path_to_file}...")
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents

def get_num_words(text): 
  total_words = len(text.split())
  print(f"Found {total_words} total words")
  return total_words

def get_char_count(text):
  char_dict = {}
  for char in text:
    normarlised_char = char.lower()
    if (normarlised_char not in char_dict):
      char_dict[normarlised_char] = 1
    else:
      char_dict[normarlised_char] += 1
  # print(char_dict)
  char_list = sort_char_count(char_dict)
  return char_list

def sort_on(dict):
  return dict["num"]

def sort_char_count(char_dict):
  char_list = []

  for char in char_dict:
    if(char.isalpha()):
      char_list.append({
        "char": char,
        "num": char_dict[char]
      })
  char_list.sort(reverse=True, key=sort_on)
  # print(char_list)
  return char_list

def print_char_list(contents):
  char_list = get_char_count(contents)
  for i in char_list:
    print(f'{i["char"]}: {i["num"]}')
