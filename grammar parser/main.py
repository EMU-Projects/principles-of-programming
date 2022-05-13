import os
from os import listdir
from os.path import isfile, join

# G -> E
# E -> T R
# R -> + T R | - T R | empty_str
# T -> F S
# S -> * F S | / F S | empty_str
# F -> ( E ) | N
# N -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 

# Global variables to use inside the parser
input_str = ""
pointer = -1;
perror = False
next_token= ''

# Lex function makes the pointer point to the next character
def lex():
    global pointer
    global next_token
    pointer += 1
    next_token = input_str[pointer]
    
    # Skip pointer to next character if it is empty_string or new_line
    if (next_token == ' ' or next_token == '\n'):
        lex()
    
# Get the rest of the string that couldn't be parsed
def unconsumed_input():
    return input_str[pointer:len(input_str)-1]

# This function initializes the global variables and runs the grammar by calling G()
def analyze(string):
    print("Analyzing:",string)
    global pointer
    global perror
    global next_token
    global input_str
    pointer = -1
    perror = False
    next_token = ''
    input_str = string
    G()

def G():
    global perror
    lex()
    print("G -> E")
    E()
    if (next_token=='$' and not perror ):
        print("success")
    else:
        print("failure: unconsumed input= ", unconsumed_input())

# E -> T R 
def E(): 
    global perror
    if (perror):
        return 0
    print("E -> T R")
    T()
    R()

# R -> + T R | - T R | e 
def R():
    global perror
    if(perror):
         return 0
    if (next_token == '+'):
        print("R -> + T R")
        lex()
        T()
        R()
     
    elif (next_token== '-'):
        print("R -> - T R")
        lex()
        T()
        R()
     
    else:
        print("R->e")

# T -> F S 
def T():
    global perror
    if(perror):
      return
    print("T -> F S")
    F()
    S()

# S -> * F S | / F S | e 
def S():
    global perror
    if(perror):
         return 0
    if (next_token=='*'):
        print ("S -> * F S")
        lex()
        F()
        S() 
    elif (next_token=='/'): 
        print("S -> / F S")
        lex()
        F()
        S() 
    else:
        print("S -> e") 

# F -> ( E ) | N 
def F():
    global perror
    if (perror):
        return 0
    if (next_token=='(' ):
        print("F->( E )")
        lex()
        E()
        if (next_token == ')' ):
            lex()
  
        else:
            perror = True 
            print("error: unexptected token ", next_token) 
            print("unconsumed_input ", unconsumed_input()) 
            return 

    elif(next_token.isnumeric()):
        print ("F->N")
        N()
  
    else:
        perror = True
        print("error: unexptected token ", next_token) 
        print("unconsumed_input ", unconsumed_input()) 

# N -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
 
def N(): 
    global perror
    if (perror): 
        return
    if(next_token.isnumeric()):
        print ("N->", next_token)
        lex()
    else:
        perror = True
        print("error: unexptected token ", next_token) 
        print("unconsumed_input ", unconsumed_input()) 


 

# Get list of files in the directory

files = listdir("inputs")
while (True):
    
    # Loop through files and index them
    for i,file in enumerate(files):
        print(str(i) + ")", file)
    x = int(input("Enter the index of the file to analyze: "))
    if (x == -1):
        break
    
    # Open files based on the index provided by the user
    file = open("inputs/"+files[x],"r")
    string = "".join(file.readlines())
    file.close()
    
    # Start grammar parsing
    analyze(string)
    os.system("pause")


