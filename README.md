# P-Markup
(c) 2018 Paulocarcy

## 1. Introduction
P-Markup is a text markup language to generate simple interactive JavaScript&HTML5 files. The P-Markup
program translates P-Markup text files into combined JavaScript&HTML5 files.

## 2. Installation
P-Markup is written in Python 3 using tkinter for its GUI. Therefore, you need Python 3 and the 
Python package tkinter in order to be able to run P-Markup.

## 3. Usage
All P-Markup text files must end with .txt. No non-markup files ending with .txt are allowed, as
every file of the input folder is copied into the output_folder in order to preserve data which is
linked in the P-Markup files.

In order to write a newline command in P-Markup, the character \ is used. Newlines written with RETURN
are ignored.

All other P-Markup commands have the following structure:
<pre>[COMMAND arguments]</pre>
e.g.
<pre>[LINK path_to_link link_text]</pre>
->LINK creates a hyperlink to the given path_to_link and the text given in link_text.

The other P-Markup commands are:
<pre>[REM  comment text]</pre>
-> Is ignored by P-Markup. It is used to explain markup files.
<pre>[IMG path]</pre>
-> Creates an image to the given apth.
<pre>[SET variable_name start_value]</pre>
-> Sets a global JavaScript variable with the given start value, which can be of any given type.
<pre>[INPUTNUMBER variable_name]</pre>
-> Creates an input field for a numeric variable (integer or float). Its start value is the            variable's start value.
<pre>[INPUTSTRING variable_name]</pre>
-> Creates an input field for a string variable. Its start value is the variable's start value.
<pre>[SCRIPTBUTTON text
    script
]</pre>
-> Creates a button with the given text. In the string section, all created variables can be accessed. The script needs      to return a value. This value will be the text ffor a text paragraph which is right behind the button.

You may also use any other simple HTML5 command using the following syntax:
<pre>[HTML5_COMMAND arguments]</pre>
e.g.
<pre>[H4 This is a text]</pre>
which will become
<h4>This is a text</h4>

As you wrote your markup files, use the Python 3 module in ./submodules/p_markup.py or run the GUI in
p_markup_GUI.py. The resulting HTML&JavaScript files will be created in the given output folder.

## 4. Usage example
See [./Input_Example/markup.txt](./Input_Example/markup.txt) and
[./Output_Example/markup.html](./Output_Example/markup.html) as well as
the associated [./Output_Example/index.html index file](./Output_Example/index.html).

## 5. Licensing
P-Markup is free and open-source. You can find its full license under [./LICENSE](./LICENSE). 