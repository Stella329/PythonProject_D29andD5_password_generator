# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import pandas
import csv
import random
import pyperclip

FONT_TYPE = 'Arial'
FONT_SIZE = 10

# ---------------------------- PASSWORD GENERATOR -D5------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # randint(start, stop)
    # random.choices(sequence, k=个数） -- sequnce: list, tuples, strings, choose from which
    char_list = [random.choice(letters) for _ in range (random.randint(4,8))]
    ## OR
    ## char_list = [char for char in random.choices(letters, k=num_letters)]
    symbols_list = [random.choice(symbols) for _ in range (random.randint(2,4))]
    numn_list = [random.choice(numbers) for _ in range (random.randint(2,4))]

    password_list = char_list+symbols_list+numn_list
    random.shuffle(password_list)

    password = ''.join(password_list) ##--into string

    pw_entry.insert(0,password)
    # if加密：encrypted = '*'* len(password) ##--这里显示明文，不用

    pyperclip.copy(password)  ## auto copy to clickboad

    if len(pw_entry.get()) > 8+4+4: ##二次点击：重新生成
        pw_entry.delete(0,END)
        generate_password()




# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password(web_input, email_input, pw_input):
    with open('my_password_notebook.csv','a') as csv_file: #自动close; 首次自动创建；a=append

        pw_dict = {'website': [web_input],
                    'Email/Username': [email_input],
                    'password': [pw_input]
                    }

        # append a df to an existing CSV:
        ## df.to_csv('log.csv', mode='a', index=False, header=False)
        pw_df = pandas.DataFrame(pw_dict)

        read_mode = open('my_password_notebook.csv', 'r') ## 判断csv file是否为空 --是否添加header
        if len(read_mode.readlines())<3:
            pw_df.to_csv(csv_file, mode='a', index=False)

        else:
            pw_df.to_csv(csv_file, mode='a',index=False, header=False)

        print(pw_df)
        print(csv_file)


# MY METHOD: 想直接用CSV-> dataframe，但是有问题
# def save_password(website, email, password):
#
#     with open('my_password_notebook.csv','a'):
#
#         try: # 判断是否为空，需要首次创建设定首行：
#             pw_table = pandas.read_csv('my_password_notebook.csv', index_col=0)
#
#         except pandas.errors.EmptyDataError:
#             default = {'website': [None],
#               'Email/Username': [None],
#               'password': [None]
#               }
#             pw_df = pandas.DataFrame(default)
#         else:
#             pw_df = pandas.DataFrame(pw_table)
#
#         pw_df.loc[len(pw_df.index)] = [website, email, password]  # new row=定位结尾，添加only one row
#         pw_df['website'] = pw_df['website'].astype('string') ## unsolved问题：datatype显示为decimal
#
#         pw_df.to_csv('my_password_notebook.csv')
#         print(pw_df)


# ANGELA'S TXT
# def save_password (web_input, email_input, pw_input):
#     with open ('my_password_book.txt','a') as data_file:
#         data_file.write(f'{web_input} | {email_input} | {pw_input}')


# 2.BUTTON ACTIONS ------------------------------- #

def action_add():
    # get hold of values
    web_input = web_entry.get()
    email_input = email_entry.get()
    pw_input = pw_entry.get()


    # POP-UP WINDOWS: messagebox
    messagebox.askokcancel(title='Check Your Password', message=(f'Your password details are as follow: \nWebsite: {web_input} \nEmail: {email_input} \nPassword: {pw_input}  '))
    if len(web_input) == 0: ##判断空值
        messagebox.showerror(title='error', message='You forget to add the Website information.')
    elif len(pw_input) == 0:
        messagebox.showerror(title='error', message='You forget to add the Password information.')

    # SAVE PASSWORD and CLEAR
    else:
        save_password(web_input, email_input, pw_input)
        clean_out()

def clean_out():
    web_entry.delete(0,END)
    pw_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('My Password Manager')
window.config(padx=50, pady=50)  ## padding btw window vs. canvas

canvas = Canvas(width=300, height=233)
locker_img = PhotoImage(file='logo.png')
canvas.create_image(150,120,image=locker_img)
canvas.grid(column=1,row=0)

#TEXTS
website_txt = Label(text='Website: ')
website_txt.grid(column=0, row=1)

email_txt = Label(text='Email/Username: ')
email_txt.grid(column=0, row=2)

password_txt = Label(text='Password: ')
password_txt.grid(column=0, row=3)


# INPUT BOX
web_entry = Entry(width = 35)
web_entry.focus()  ## add curser
web_entry.grid(column=1, row=1, columnspan=2, sticky=EW) # stciky=EW --align

email_entry = Entry(width = 35)
email_entry.insert(0, 'stella33299@gmail.com')  # pre-populated text
email_entry.grid(column=1, row=2, columnspan=2, sticky=EW)

pw_entry = Entry(width=18)
pw_entry.grid(column=1, row=3, sticky=EW)

button = Button(text='Add', command=action_add, width=35)
button.grid(row=4, column=1, columnspan=2, sticky=W)

password = Button(text='Generate Password', command=generate_password)
password.grid(column=2, row=3, sticky=EW)


# ----------------------------------------------------------- #
window.mainloop()