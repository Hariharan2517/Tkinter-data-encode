import tkinter as tk
from tkinter import ttk
#from threading import Timer
from tkinter import *

#(01)02112345670003(21)000000000001 - sample value

#Using decihex() for converting decimal => binary => hex format
def decihex():
    global val1_int, val3_int, finalvalue
    #getting entry value from tk
    res = gs1_entry.get()

    #Using slice method upto the value
    #GS1 company
    val1 = slice(5, 11)
    val1_str = res[val1]
    val1_int = int(res[val1])
    print(val1_int,"1")

    #concatenate 0 value
    val2_int = int(res[4])
    val2_str = res[4]
    print(val2_int,"2")

    #Item
    val3 = slice(11, 17)
    val3_str = res[val3]
    val3_int = int(res[val3])
    print(val3_int,"3")

    #Serial
    val4 = (slice(22, len(res)))
    #val4_str = res[val4]
    val4_int = int(res[val4])
    print(val4_int,"4")
    dec=val4_int
    bn = ""
    while dec > 0:
        bn = str(dec % 2) + bn # prepend, not append!
        dec = dec >> 1
        finalvalue = bn.rjust(38, "0")
    #Adding zero before for 38 bit    
    print(finalvalue)

    #Parse data for EPC Pure Identity URI Generation
    parse_data = val1_str+"."+val2_str+"."+val3_str+"."+str(val4_int)
    print(parse_data,"Parse Data")
    parse_entry.insert("1",parse_data)

    #EPC Pure Identity URI Generation format
    epc_uri = val1_str+"."+val2_str+val3_str+"."+str(val4_int)
    print(epc_uri,"EPC URI")
    epc_entry.insert("1",epc_uri)
    
    #Header,filterr,partition predefined value
    header = "00110000"
    filterr = "011"
    partition = "101"
    print(header,"HEADER 8")
    encode1_entry.insert("1",header)
    print(filterr,"FILTER 3")
    encode2_entry.insert("1",filterr)
    print(partition,"PARTITION 3")
    encode3_entry.insert("1",partition)

    #decibin() for converting GS1 Company into 20bits
    def decibin():
     global value1
     decimal = val1_int
     binary = 0
     ctr = 0
     temp = decimal  #copy input decimal

    #find binary value using while loop
     while(temp > 0):
        binary = ((temp%2)*(10**ctr)) + binary
        temp = int(temp/2)
        ctr += 1
        binary_str = str(binary)
        value1 = binary_str.rjust(20, "0")
    #output the result       
    #print("Binary of {x} is: {y}".format(x=decimal,y=binary))

    #decimalbinary() for converting (Item/indicator) into 24bits
    def decimalbinary():
     global value2
     decimal = val3_int
     binary = 0
     ctr = 0
     temp = decimal #copy input decimal

    #find binary value using while loop
     while(temp > 0):
        binary = ((temp%2)*(10**ctr)) + binary
        temp = int(temp/2)
        ctr += 1
        binary_str = str(binary)
        value2 = binary_str.rjust(24, "0")   

    #calling the above func()
    decibin()
    decimalbinary()

    #inserting value in tk 
    print(value1, "20bit")
    encode4_entry.insert("1",value1)
    print(value2, "24bit") 
    encode5_entry.insert("1",value2)
    print(finalvalue,"38bit")
    encode6_entry.insert("1",finalvalue)
    print(len(finalvalue))

    #Header,filterr,partition predefined value
    header = "00110000"
    filterr = "011"
    partition = "101"
    print(header,"HEADER 8")
    print(filterr,"FILTER 3")
    print(partition,"PARTITION 3")

    #EPC Binary data concatenation
    con_catenate = header+filterr+partition+value1+value2+finalvalue
    concatenate = con_catenate.rjust(96, "0")
    print(concatenate)
    concatenate_entry.insert("1",concatenate)
    print(len(concatenate))
    #Converting Binary digit to Hex format
    hexs = (f'{int(concatenate, 2):X}')
    print(hexs)
    #Inserting rfid tag entry in Tkinter
    rfid_entry.insert("1",hexs)

#reset() for clearing input field
def reset():
  gs1_entry.delete(0, 200)
  parse_entry.delete(0, 200)
  epc_entry.delete(0, 200)
  encode1_entry.delete(0, 200)
  encode2_entry.delete(0, 200)
  encode3_entry.delete(0, 200)
  encode4_entry.delete(0, 200)
  encode5_entry.delete(0, 200)
  encode6_entry.delete(0, 200)
  concatenate_entry.delete(0, 200)
  rfid_entry.delete(0, 200)



# root window
root = tk.Tk()
root.geometry("590x620")
root.title('Data-encode')
root.resizable(610, 640)
root.configure(bg='black')


# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

title_label = ttk.Label(root, text="GS1 Standard data Encode",font=('Times', 22),background='black', foreground='white')
title_label.grid(column=1, row=0, sticky=tk.N, padx=10, pady=30,ipadx=20, ipady=2.5,columnspan=3)

# GS1 Element string to EPC Pure Identity URI Generation
gs1_label = ttk.Label(root, text="GS1-GTIN14",font=('Times', 15),background='black', foreground='white')
gs1_label.grid(column=0, row=1,sticky=tk.E, padx=10, pady=10)

gs1_entry = tk.Entry(root,font=('Normal', 16),background='DodgerBlue', foreground='white')
gs1_entry.grid(column=1, row=1, sticky=tk.EW, padx=10, pady=5, columnspan=3,ipadx=2.5, ipady=2.5)

#convert button using command to call the func()
convert_button = tk.Button(root, text="convert",font=('Times', 12), command= decihex, background='white',foreground='blue',highlightcolor='black')
convert_button.grid(column=2, row=2, sticky=tk.NS, padx=5, pady=10)
#command = decihex

#Parse data for EPC Pure Identity URI Generation
parse_label = ttk.Label(root, text="Parse-data",font=('Times', 16),background='black', foreground='white')
parse_label.grid(column=0, row=3, sticky=tk.E, padx=10, pady=10)

parse_entry = tk.Entry(root,font=('Normal', 12),background='DodgerBlue', foreground='white')
parse_entry.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=10,columnspan=3,ipadx=2.5, ipady=2.5)

#EPC Pure Identity URI Generation format
epc_label = ttk.Label(root, text="EPC-URI",font=('Times', 16),background='black', foreground='white')
epc_label.grid(column=0, row=4, sticky=tk.E, padx=10, pady=10)

epc_entry = tk.Entry(root,font=('Normal', 12),background='DodgerBlue', foreground='white')
epc_entry.grid(column=1, row=4, sticky=tk.EW, padx=5, pady=10,columnspan=3,ipadx=2.5, ipady=2.5)

#EPC Tag URI TO EPC Binary Encoding format
encode_label = ttk.Label(root, text="Encoding",font=('Times', 16),background='black', foreground='white')
encode_label.grid(column=0, row=5, sticky=tk.E, padx=10, pady=5)

encode1_entry = tk.Entry(root,background='DodgerBlue', foreground='white')
encode1_entry.grid(column=1, row=5, sticky=tk.EW, padx=2, pady=5,ipadx=3, ipady=3)

encode2_entry = tk.Entry(root,background='DodgerBlue', foreground='white')
encode2_entry.grid(column=2, row=5, sticky=tk.EW, padx=2, pady=5,ipadx=3, ipady=3)

encode3_entry = tk.Entry(root,background='DodgerBlue', foreground='white')
encode3_entry.grid(column=3, row=5, sticky=tk.EW, padx=2, pady=5,ipadx=2.5, ipady=2.5)

encode4_entry = tk.Entry(root,background='DodgerBlue', foreground='white')
encode4_entry.grid(column=1, row=6, sticky=tk.EW, padx=2, pady=5,ipadx=3, ipady=3)

encode5_entry = tk.Entry(root,background='DodgerBlue', foreground='white')
encode5_entry.grid(column=2, row=6, sticky=tk.EW, padx=2, pady=5,ipadx=3, ipady=3)

encode6_entry = tk.Entry(root,background='DodgerBlue', foreground='white')
encode6_entry.grid(column=3, row=6, sticky=tk.EW, padx=2, pady=5,ipadx=2.5, ipady=2.5)

#EPC Binary data concatenation
concatenate_label = ttk.Label(root, text="Concatenation",font=('Times', 12),background='black', foreground='white')
concatenate_label.grid(column=0, row=7, sticky=tk.W, padx=10, pady=10)

concatenate_entry = tk.Entry(root,font=('Normal', 12),background='DodgerBlue', foreground='white')
concatenate_entry.grid(column=1, row=7, sticky=tk.EW, padx=5, pady=10,columnspan=3,ipadx=2.5, ipady=2.5)

#RFID tag in device
rfid_label = ttk.Label(root, text="RFID_Tag",font=('Times', 15),background='black', foreground='red')
rfid_label.grid(column=0, row=8, sticky=tk.E, padx=10, pady=0)

rfid_entry = tk.Entry(root,font=('Normal', 12),background='MediumSeaGreen', foreground='yellow')
rfid_entry.grid(column=1, row=8, sticky=tk.EW, padx=5., pady=5,columnspan=3,ipadx=2.5, ipady=2.5)

#reset button
reset_button = tk.Button(root, text="reset",font=('Times', 12), command=reset, background='white',foreground='blue',highlightcolor='yellow')
reset_button.grid(column=2, row=9, sticky=tk.NS, padx=5, pady=10)


root.mainloop()


