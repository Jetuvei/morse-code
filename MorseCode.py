# -*- coding: cp1252 -*-
## =================
## MorseCode.py
## =================
## 2012.09.07
## Justin Whitehouse
##

# -*- coding: cp1252 -*-

## *****************
## Morse Code = INTERNATIONAL Morse Code
## *****************

## -----------------
##
##  Program to convert text into morse code.
##  e.g. if the user types in:
##
##      'Morse Code'
##
##  the program should print
##
##      -- --- ·-· ··· ·       -·-· --- -·· ·
##
## -----------------

## =================
##
##  How to implement this?
##  ----------------------
##
##  1.  need a 'master' function (convert?), so that we can do:
##
##  >>> MorseCode.convert("Morse Code")
##  '-- --- ·-· ··· ·       -·-· --- -·· ·'
##
##  2.  function like 'convertCharacter' which takes a single character
##      and looks up the morse code string for the character, adds to it
##      the 'LETTER_END' character, and gives it back to the first
##      function.
##
##  3.  so, do something like:
##
##      def convert(string):
##          morse_out = ''
##          for s in string:
##              morse_out += convertCharacter(s)
##          return morse_out
##
## =================

## -----------------
##
## Timings in Morse Code:
##
#          1         2         3         4         5         6         7         8
# 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
#  
# M------   O----------   R------   S----   E       C----------   O----------   D------   E
# ===.===...===.===.===...=.===.=...=.=.=...=.......===.=.===.=...===.===.===...===.=.=...=
#    ^               ^    ^       ^             ^
#    |              dah  dit      |             |
# symbol space                letter space    word space
#
## ------------------

## ------------------
##
## Morse Code Map:
##
##  A   ·-	    |   J   ·---    |	S   ···	    |   1   ·----   |   Period [.]	        ·-·-·-  |   Colon [:]	        ---···
##  B 	-···	    |   K   -·-     |	T   -       |   2   ··---   |   Comma [,]	        --··--  |   Semicolon [;]	-·-·-·
##  C 	-·-·	    |   L   ·-··    |	U   ··-	    |   3   ···--   |   Question mark [?]	··--··  |   Double dash [=]	-···-
##  D 	-··	    |   M   --	    |   V   ···-    |   4   ····-   |   Apostrophe [']	        ·----·  |   Plus [+]	        ·-·-·
##  E 	·	    |   N   -·	    |   W   ·--	    |   5   ·····   |   Exclamation mark [!]	-·-·--  |   Hyphen, Minus [-]   -····-
##  F 	··-·	    |   O   ---     |	X   -··-    |   6   -····   |   Slash [/], Fraction bar	-··-·   |   Underscore [_]      ··--·-
##  G 	--·	    |   P   ·--·    |	Y   -·--    |   7   --···   |   Parenthesis open [(]	-·--·   |   Quotation mark ["]  ·-··-·
##  H 	····	    |   Q   --·-    |	Z   --··    |   8   ---··   |   Parenthesis closed [)]	-·--·-  |   Dollar sign [$]	···-··-
##  I 	··	    |   R   ·-·     |	0   -----   |   9   ----·   |   Ampersand [&], Wait	·-···   |   At sign [@]	        ·--·-·

MORSE_A="·-"	    
MORSE_B="-···"	    
MORSE_C="-·-·"	    
MORSE_D="-··"	    
MORSE_E="·"	    
MORSE_F="··-·"	    
MORSE_G="--·"	    
MORSE_H="····"	    
MORSE_I="··"	    
MORSE_J="·---"
MORSE_K="-·-"
MORSE_L="·-··"
MORSE_M="--"	
MORSE_N="-·"	
MORSE_O="---" 
MORSE_P="·--·"   
MORSE_Q="--·-"
MORSE_R="·-·" 
MORSE_S="···"	  
MORSE_T="-"  
MORSE_U="··-"
MORSE_V="···-"
MORSE_W="·--"	
MORSE_X="-··-"
MORSE_Y="-·--"
MORSE_Z="--··"

MORSE_0="-----"
MORSE_1="·----" 
MORSE_2="··---"
MORSE_3="···--" 
MORSE_4="····-" 
MORSE_5="·····" 
MORSE_6="-····"
MORSE_7="--···"
MORSE_8="---··" 
MORSE_9="----·"

MORSE_PERIOD="·-·-·-"
MORSE_COMMA="--··--"
MORSE_QUSETION="··--··"
MORSE_APOSTROPHE="·----·"
MORSE_EXCLAMATION="-·-·--"
MORSE_SLASH="-··-·"
MORSE_PAREN_OPEN="-·--·"
MORSE_PAREN_CLOSE="-·--·-"
MORSE_AMPERSAND="·-···"
MORSE_COLON="---···"
MORSE_SEMICOLON="-·-·-·"
MORSE_EQUAL="-···-"
MORSE_PLUS="·-·-·"
MORSE_MINUS="-····-"
MORSE_UNDERSCORE="··--·-"
MORSE_QUOTATION="·-··-·"
MORSE_DOLLAR="···-··-"
MORSE_AT="·--·-·"

MORSE_LETTER_END=" " #1 space after each letter
MORSE_SPACE="       " #6 spaces
# letter end + space = 7 spaces between words

## ------------------

TEXT_TO_MC = {  "a":MORSE_A,    "A":MORSE_A,    "b":MORSE_B,    "B":MORSE_B,    "c":MORSE_C,    "C":MORSE_C,
                "d":MORSE_D,    "D":MORSE_D,    "e":MORSE_E,    "E":MORSE_E,    "f":MORSE_F,    "F":MORSE_F,
                "g":MORSE_G,    "G":MORSE_G,    "h":MORSE_H,    "H":MORSE_H,    "i":MORSE_I,    "I":MORSE_I,
                "j":MORSE_J,    "J":MORSE_J,    "k":MORSE_K,    "K":MORSE_K,    "l":MORSE_L,    "L":MORSE_L,
                "m":MORSE_M,    "M":MORSE_M,    "n":MORSE_N,    "N":MORSE_N,    "o":MORSE_O,    "O":MORSE_O,
                "p":MORSE_P,    "P":MORSE_P,    "q":MORSE_Q,    "Q":MORSE_Q,    "r":MORSE_R,    "R":MORSE_R,
                "s":MORSE_S,    "S":MORSE_S,    "t":MORSE_T,    "T":MORSE_T,    "u":MORSE_U,    "U":MORSE_U,
                "v":MORSE_V,    "v":MORSE_V,    "w":MORSE_W,    "W":MORSE_W,    "x":MORSE_X,    "X":MORSE_X,
                "y":MORSE_Y,    "Y":MORSE_Y,    "z":MORSE_Z,    "Z":MORSE_Z,

                "0":MORSE_0,    "1":MORSE_1,    "2":MORSE_2,    "3":MORSE_3,    "4":MORSE_4,
                "5":MORSE_5,    "6":MORSE_6,    "7":MORSE_7,    "8":MORSE_8,    "9":MORSE_9,

                ".":MORSE_PERIOD,       ",":MORSE_COMMA,        "'":MORSE_APOSTROPHE,
                "?":MORSE_QUSETION,     "!":MORSE_EXCLAMATION,  "/":MORSE_SLASH,
                "(":MORSE_PAREN_OPEN,   ")":MORSE_PAREN_CLOSE,  "&":MORSE_AMPERSAND,
                ":":MORSE_COLON,        ";":MORSE_SEMICOLON,
                "=":MORSE_EQUAL,        "+":MORSE_PLUS,         "-":MORSE_MINUS,
                "_":MORSE_UNDERSCORE,   "\"":MORSE_QUOTATION,   "$":MORSE_DOLLAR,   "@":MORSE_AT,

                0:MORSE_LETTER_END, # every letter should end with this
                " ":MORSE_SPACE,
                -1:None             # if the character in the text cannot be found here, it is mapped to 'None'
                                    # - actually this may be redundant
                }


def convertCharacter(char_str):
    morse_equiv = ''
    try:
        morse_equiv += TEXT_TO_MC[char_str]
    except KeyError:
        morse_equiv += char_str
    morse_equiv += TEXT_TO_MC[0]
    return morse_equiv

def convert(text_str):
    morse_out = ''
    for character in text_str:
        morse_out += convertCharacter(character)
    return morse_out




