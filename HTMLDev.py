# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 17:18:06 2023

@author: muthu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:28:53 2022

@author: muthu
"""

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import webbrowser
from tkcolorpicker import askcolor

# tag # tags #Next update should be settings...

root = Tk()
w, h = root.winfo_width(), root.winfo_height()
root.state('zoomed')
root.title('Editor')
con=''
current_font_size = 10
dirnames=[]
colors = {'green': '#34eb52',
          'ele_gray': '#616b63',
          'matt_gray': '#3d403d',
          'mango': '#3d403d',
          'orange': '#fca103',
          'sky_blue': '#6995db',
          'leaf_green': '#00bd4f',
          'pink': 'pink',
          'bgreen':'#3FCC00',
          'yellow':'#FFFF00',
          'black':'black',
          'white':'white',
          'mild_yellow':'#e4e693'}

themec = [0]
tag = ["<a>","<img","/>","<meta", "</a>","<abbr>", "</abbr>","<acronym>", "</acronym>","<address>", "</address>","<area>", "</area>","<b>", "</b>","<base>", "</base>","<bdo>", "</bdo>","<big>", "</big>","<blockquote>", "</blockquote>","<body>", "</body>","<br>", "</br>","<button>", "</button>","<caption>", "</caption>","<cite>", "</cite>","<code>", "</code>","<col>", "</col>","<colgroup>", "</colgroup>","<dd>", "</dd>","<del>", "</del>","<dfn>", "</dfn>","<div>", "</div>","<dl>", "</dl>","<DOCTYPE>", "</DOCTYPE>","<!Doctype>","<!DOCTYPE html>","<!DOCTYPE HTML>","<dt>", "</dt>","<em>", "</em>","<fieldset>", "</fieldset>","<form>", "</form>","<h1>", "</h1>","<h2>", "</h2>","<h3>", "</h3>","<h4>", "</h4>","<h5>", "</h5>","<h6>", "</h6>","<head>", "</head>","<html>", "</html>","<hr>", "</hr>","<i>", "</i>","<img>", "</img>","<input>", "</input>","<ins>", "</ins>","<kbd>", "</kbd>","<label>", "</label>","<legend>", "</legend>","<li>", "</li>","<link>", "</link>","<map>", "</map>","<meta>", "</meta>","<noscript>", "</noscript>","<object>", "</object>","<ol>", "</ol>","<optgroup>", "</optgroup>","<option>", "</option>","<p>", "</p>","<param>", "</param>","<pre>", "</pre>","<q>", "</q>","<samp>", "</samp>","<script>", "</script>","<select>", "</select>","<small>", "</small>","<span>", "</span>","<strong>", "</strong>","<style>", "</style>","<sub>", "</sub>","<sup>", "</sup>","<table>", "</table>","<tbody>", "</tbody>","<td>", "</td>","<textarea>", "</textarea>","<tfoot>", "</tfoot>","<th>", "</th>","<thead>", "</thead>","<title>", "</title>","<tr>", "</tr>","<tt>", "</tt>","<ul>", "</ul>","<var>", "</var>"]
properties = ['']
spec = ['"',"'","<",">","{","}","[","]","(",")","=",";",":"]
css = ['background', 'background-attachment', 'background-color', 'background-image', 'background-position', 'background-repeat', 'border', 'border-collapse', 'border-color', 'border-spacing', 'border-style', 'border-width', 'border-***', 'border-***-color', 'border-***-style', 'border-***-width', 'bottom', 'C', 'caption-side', 'clear', 'color', 'content', 'cursor', 'D', 'direction', 'display', 'E', 'empty-cells', 'F', 'filter', 'float', 'font', 'font-family', 'font-size', 'font-style', 'font-variant', 'font-weight', 'H', 'height', 'L', 'left', 'letter-spacing', 'line-height', 'list-style', 'list-style-image', 'list-style-position', 'list-style-type', 'M', 'margin', 'margin-***', 'max-height', 'max-width', 'min-height', 'min-width', 'O', 'overflow', 'overflow-***', 'P', 'padding', 'padding-***', 'page-break-***', 'position', 'R', 'right', 'ruby-align', 'ruby-overhang', 'ruby-position', 'S', 'scrollbar-***-color', 'T', 'table-layout', 'text-align', 'text-decoration', 'text-indent', 'text-justify', 'text-overflow', 'text-transform', 'text-underline-position', 'top', 'U', 'unicode-bidi', 'V', 'vertical-align', 'visibility', 'W', 'white-space', 'width', 'word-break', 'word-spacing', 'word-wrap', 'Z', 'z-index', 'zoom']

def choose_color():
    # variable to store hexadecimal code of color
    global color_code

    askcolor((255, 255, 0), root)


def theme():
    global themec, st
    if(themec[-1]==0):
        st.config(foreground='white', background=colors['matt_gray'], insertbackground=colors['mango'])
        themec.append(1)
    else:
        st.config(foreground=colors['black'], background=colors['mild_yellow'], insertbackground=colors['green'])
        themec.append(0)

    main()


def get(n):
    print(n)


def run(dirname):
    filename = 'file:///' + dirname
    webbrowser.open_new_tab(filename)
    print(filename)

def fopen():
    global dirname, st, text, con,i

    dirname = filedialog.askopenfilename()
    _type = dirname.split('.')
    # if _type[-1] == 'html' or _type[-1] == 'htm':
    #     con=html2text.HTML2Text(dirname)
    # else:
    text = open(dirname, "r+")
    con = text.read()
    text.close()
    print(_type)
    passby()


def passby():
    global canvas
    canvas.pack_forget()
    main()

def highlight(e):
    global canvas, st, word
    for a in tag:
        word = a
        # word length use as offset to get end position for tag
        offset = '+%dc' % len(word)  # +5c (5 chars)

        # search word from first char (1.0) to the end of text (END)
        pos_start = st.search(word, '1.0', END)

    
        while pos_start:
            # create end position by adding (as string "+5c") number of chars in searched word
            pos_end = pos_start + offset
            # add tag
            st.tag_add('gre_tag', pos_start, pos_end)

            # search again from pos_end to the end of text (END)
            pos_start = st.search(word, pos_end, END)
        st.config(insertbackground='cyan')
    for a in spec:
        word = a
        # word length use as offset to get end position for tag
        offset = '+%dc' % len(word)  # +5c (5 chars)

        # search word from first char (1.0) to the end of text (END)
        pos_start = st.search(word, '1.0', END)

    
        while pos_start:
            # create end position by adding (as string "+5c") number of chars in searched word
            pos_end = pos_start + offset
            # add tag
            st.tag_add('yell_tag', pos_start, pos_end)

            # search again from pos_end to the end of text (END)
            pos_start = st.search(word, pos_end, END)
        st.config(insertbackground='cyan')
        
    for a in css:
        word = a
        # word length use as offset to get end position for tag
        offset = '+%dc' % len(word)  # +5c (5 chars)

        # search word from first char (1.0) to the end of text (END)
        pos_start = st.search(word, '1.0', END)

    
        while pos_start:
            # create end position by adding (as string "+5c") number of chars in searched word
            pos_end = pos_start + offset
            # add tag
            st.tag_add('cyan_tag', pos_start, pos_end)

            # search again from pos_end to the end of text (END)
            pos_start = st.search(word, pos_end, END)
        st.config(insertbackground='cyan')


def main():
    global canvas, st, word
       #var of selected tab tabControl.nametowidget(tabControl.select())
    canvas = Canvas(root, height=1000, width=2000)
    canvas.pack(pady=175)
    
    st = ScrolledText(root, height=35, width=165, wrap='word')#width=165
    canvas.create_window(685, 140, window=st)
    st.insert(INSERT, con)
    word = st.get(0.1, END)
    # create tag style NexaRustScriptL-0z
    st.tag_config("gre_tag", foreground='#13F613', relief="raised")
    st.tag_config("yell_tag", foreground='yellow', relief="raised")
    st.tag_config("cyan_tag", foreground="#03fcfc", relief="raised" )
    st.bind('<Key>', highlight)
    st.config(foreground='white', background=colors['matt_gray'], insertbackground=colors['mango'])
    
    # create tag style NexaRustScriptL-0
    highlight(1)
    


def html():
    tabs()


def save(dirname):
    print(dirname)
    try:
        f = open(dirname, 'w')
        f.write(st.get('1.0',END))
        f.close()
        print(showinfo("Edit Saved", "Your edit to this document was saved successfully."))
    except:
        dirname = filedialog.asksaveasfilename()
        f = open(dirname, 'w')
        f.write(st.get('1.0',END))
        f.close()
        print(showinfo("Edit Saved", "Your edit to this document was saved successfully."))
    main()


def new():
    global dirname, canvas
    close = askyesnocancel('Exit', "Would you like to Save the changes and quit?")
    if (close == True):
        f = open(dirname, 'w')
        f.write(st.get('1.0', END))
        f.close()
        canvas.pack_forget()
    elif (close == False):
        canvas.pack_forget()
    main()

def widgets():
    global ribbon, navbar, current_font_size
    navbar = Canvas(root, height=50, highlightthickness=0, width=1700, bg=colors['leaf_green'])
    title = Label(root, text='HTMLDev', fg='white', bg=colors['leaf_green'], font=("Arial", 15,"bold"))
    navbar.pack()
    navbar.create_window(70, 23, window=title)
    ribbon = Canvas(root, height=20, width=1600, highlightthickness=0)
    ribbon.pack(padx=0)
    bn = Button(root, height=1, width=10, text='Save',font=("Helvetica",10), fg='white', bg=colors['orange'], relief='flat',
                command=lambda:save(dirname))
    ribbon.create_window(1310, 25, window=bn)#1310,25
    col = Button(root, height=1, width=10, text='Color Picker', fg='white',font=("Helvetica",10), bg=colors['sky_blue'], relief='flat',
                 command=choose_color)
    ribbon.create_window(1210, 25, window=col)
    mode = Button(root, height=1, width=10, text='Theme', fg='white', font=("Helvetica", 10),
                 bg='#D207CC', relief='flat', command=theme)
    ribbon.create_window(1110, 25, window=mode)
    sar = Button(root, height=1, width=10, text='Run', fg='white', font=("Helvetica", 10),
                  bg='#43939A', relief='flat', command=lambda:run(dirname))
    ribbon.create_window(1010, 25, window=sar)
    # font_size = Spinbox(root, from_=10, to=50, increment=2)
    # current_font_size = font_size.get()
    main()

def tabs():
    menubar = Menu(root)
    # Adding File Menu and commands
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)
    file.add_command(label='New File', command=new)
    file.add_command(label='Open...', command=fopen)
    file.add_command(label='Save', command=lambda:save(dirname))
    file.add_separator()
    file.add_command(label='Exit', command=exit1)

    deploy = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Deploy', menu=deploy)
    deploy.add_command(label='Run', command=lambda:run(dirname))

    root.config(menu=menubar)
    widgets()

def exit1():
    close = askyesnocancel('Exit',"Would you like to Save the changes and quit?")
    if(close==True):
        f = open(dirname, 'w')
        f.write(st.get('1.0', END))
        f.close()
        root.destroy()
    elif(close==False):
        root.destroy()



if __name__=='__main__':
    dirname=''
    html()
    root.mainloop()
