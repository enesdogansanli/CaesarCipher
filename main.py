from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt

my_app = Tk()
my_app.title("Caesar Cipher App")
my_app.geometry("1300x800")

number_to_alphabet={0:"a", 1:"b", 2:"c", 3:"ç", 4:"d", 5:"e", 6:"f", 7:"g", 8:"ğ", 9:"h", 10:"ı",11:"i", 12:"j", 13:"k", 14:"l", 15:"m", 16:"n", 17:"o", 18:"ö", 19:"p", 20:"r",21:"s", 22:"ş", 23:"t", 24:"u", 25:"ü", 26:"v", 27:"y", 28:"z",29:"q",30:"w",31:"x"}
alphabet_to_number={"a":0, "b":1, "c":2, "ç":3, "d":4, "e":5, "f":6, "g":7, "ğ":8, "h":9, "ı":10, "i":11, "j":12, "k":13, "l":14, "m":15, "n":16, "o":17, "ö":18, "p":19, "r":20, "s":21, "ş":22, "t":23, "u":24, "ü":25, "v":26, "y":27, "z":28, "q":29, "w":30, "x":31 }

def encryption():
    result = ""
    my_text = entry_1.get()
    number_of_shift = int(entry_2.get())
    my_text = my_text.lower()
    for i in my_text:
        if i in alphabet_to_number:
            number = alphabet_to_number[i]
            number = (number+number_of_shift)%32
            result = result+number_to_alphabet[number]
        elif i==" ":
            result = result+i
        else:
            result += i
    
    entry_3.delete(0,END)
    entry_3.insert(0,result)

def analysis_letter_for_encryption_text():
    my_text = entry_3.get()
    my_text = my_text.lower()
    counter = {}
    for letter in my_text:
        counter[letter] = counter.get(letter, 0) + 1
    
    sourted_counter = sorted(counter.items(), key=lambda x:x[1],reverse=True)
    sourted_counter = dict(sourted_counter)

    if " " in sourted_counter:
        del sourted_counter[" "]

    names = list(sourted_counter.keys())
    values = list(sourted_counter.values())
    plt.bar(range(len(sourted_counter)), values, tick_label=names)
    plt.savefig('Cipher_text_letter_analysis.png',dpi= 60)

    # TODO: Bu iki kısmı ayırmak gerekebilir. Performans açısından daha iyi olabilir.

    my_image1 = ImageTk.PhotoImage(Image.open("Cipher_text_letter_analysis.png"))
    my_label1 = Label(image=my_image1)
    my_label1.grid(row=0,column=3)

    return sourted_counter

def analysis_letter_for_reference_text():
    my_text = entry_4.get()
    my_text = my_text.lower()
    counter = {}
    for letter in my_text:
        counter[letter] = counter.get(letter, 0) + 1
    
    sourted_counter = sorted(counter.items(), key=lambda x:x[1],reverse=True)
    sourted_counter = dict(sourted_counter)

    if " " in sourted_counter:
        del sourted_counter[" "]

    names = list(sourted_counter.keys())
    values = list(sourted_counter.values())
    plt.bar(range(len(sourted_counter)), values, tick_label=names)
    plt.savefig('Reference_text_letter_analysis.png',dpi= 60)

    # TODO: Bu iki kısmı ayırmak gerekebilir. Performans açısından daha iyi olabilir.

    my_image2 = ImageTk.PhotoImage(Image.open("Reference_text_letter_analysis.png"))
    my_label2 = Label(image=my_image2)
    my_label2.grid(row=0,column=4)

    return sourted_counter

def decryption_and_performance():
    decryption_text = ""
    my_cipher_text = entry_3.get()
    encrypt_text_dict = new_list1 = list(map(list,analysis_letter_for_encryption_text().items()))
    reference_text_dict = new_list2 = list(map(list,analysis_letter_for_reference_text().items()))
    for i in range(len(encrypt_text_dict)):
        encrypt_text_dict[i][1] = reference_text_dict[i][0]   

    encrypt_text_dict = dict(encrypt_text_dict)
    
    for i in my_cipher_text:
        if i in encrypt_text_dict:
            decryption_text = decryption_text+encrypt_text_dict[i]
        elif i==" ":
            decryption_text = decryption_text+i
    
    entry_5.delete(0,END)
    entry_5.insert(0,decryption_text)


plain_text_label = Label(my_app, text="Enter plain text: ")
plain_text_label.grid(column=0,row=0, sticky=W, padx=5, pady=5)

entry_1 = Entry(my_app,borderwidth=5)
entry_1.grid(column=1, row=0 ,sticky=EW,padx=5,pady=5)

key_number_label = Label(my_app, text="Enter key number: ")
key_number_label.grid(column=0,row=1, sticky=W, padx=5, pady=5)

entry_2 = Entry(my_app,borderwidth=5)
entry_2.grid(row=1,column=1,padx=5,pady=5,sticky=EW)

button_1 = Button(my_app,text="Encryption the text",command=encryption)
button_1.grid(row=2,column=1,sticky=EW)

cipher_text_label = Label(my_app, text="Cipher text: ")
cipher_text_label.grid(column=0,row=3, sticky=W, padx=5, pady=5)

button_2 = Button(my_app,text="Letter frequency analysis for cipher text",command=analysis_letter_for_encryption_text)
button_2.grid(row=4,column=0,sticky=EW)

entry_3 = Entry(my_app,borderwidth=5)
entry_3.grid(row=3,column=1,padx=10,pady=10,sticky=EW)

reference_text_label = Label(my_app, text="Enter reference text: ")
reference_text_label.grid(column=0,row=5, sticky=W, padx=5, pady=5)

entry_4 = Entry(my_app,borderwidth=5)
entry_4.grid(row=5,column=1,padx=10,pady=10,sticky=EW)

button_3 = Button(my_app,text="Letter frequency analysis for reference text",command=analysis_letter_for_reference_text)
button_3.grid(row=6,column=0,sticky=EW)

button_4 = Button(my_app,text="Decryption text and performance",command=decryption_and_performance)
button_4.grid(row=7,column=0,sticky=EW)

entry_5 = Entry(my_app,borderwidth=5)
entry_5.grid(row=7,column=1,padx=10,pady=10,sticky=EW)

my_app.mainloop()