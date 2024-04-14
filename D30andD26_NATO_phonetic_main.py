# Exception Handling
# try:
#     sth
# except ERROR_NAME1:
#     carry out the code if sth went wrong -- there was an exception
# except ERROR_NAME2 as error_messages:
#     print(f'it catch the error message {error_message}')
# else:
#     carry out the block when nothing is failed anymore-- there were No exceptions
# finally:
#     run the block no matter what happened
# raise YourErrorType('define this error')
#     raise your own exceptions, so 系统会根据此提示错误

#NB:  if 'except' alone, it is going to skip all kinds of error even if except (solution) doesn't cover
#Aim: the whole block is to make sure it will sucess anyway


#---------------------------UPDATE PREVIOUS PROGRAM----------------------#
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# TODO Warn the input errors using exception handling

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)  ## {'A': 'Alfa', 'B': 'Bravo', ...}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def convert():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        convert()
    else:
        print(output_list)
convert()

