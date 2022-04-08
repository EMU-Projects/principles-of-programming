import re
import os


# The following are regex rules. They are regular expressions for regular grammars
# The rules are declared in order of precedence. 

# for example ("if", "while", "for") have to come first since they can be considered as identities otherwise
rules = {
    "IF_TOKEN": "^if$",
    "WHILE_TOKEN": "^while$",
    "FOR_TOKEN": "^for$",
    "ID": "^[a-zA-Z]\w*$",
    "INTEGER": "^\-?[0-9]+$",
    "FLOAT": "^\-?[0-9]+\.[0-9]+$",
    "RELOP": "^((>|<|=)?=|(>|<))$",
}

# Symbol table to store non-ERRORED lexemes
symbol_table = []

# A function to check which token a word belongs to
def lex(word):
    # Looping the the rules
    for token,expression in rules.items():
        # We check if the string matches the expression we return the token
        regex = re.compile(expression)
        if regex.match(word):
            return token
        
    # If no string matches any 
    return "ERROR"

# A method to show table by using html tables
def print_table(table):
    html = open("table.html", 'w')
    lines = ["<html>",'<head><link rel="stylesheet" href="style.css"></head>',"<body>"]
    lines.append('<div class="table-wrapper"><table class="fl-table"><tr><th>Lexeme</th><th>Token</th></tr>')
    for row in table:
        token,lexeme = row
        lines.append("<tr>")
        lines.append("<td>"+'"'+lexeme+'"'+"</td>"+ "<td>"+token+"</td>")
        lines.append("</tr>")
    lines.append("</table></div>")
    lines.append("</body></html>")
    html.writelines(lines)
    html.close()
    os.startfile("table.html");
        
def analyze():
    # Reinitialize symbol table in case of changes in input
    symbol_table.clear()
    
    # input.dat contains our words/lexemes
    file = open("input.dat",'r')
    for line in file.readlines():
        for lexeme in line.split(" "):
            # Here we print the token and its lexeme
            token = lex(lexeme)
            print("Token:",token)
            print("Lexeme:",lexeme, end="\n\n")
            if token != "ERROR":
                symbol_table.append([token,lexeme])
    file.close()

i = "0"
while i != "3":
    # Menu display
    print("1.) Call lex \n")
    print("2.) Show symbol table \n")
    print("3.) Exit \n")
    i = input("Enter a digit: ")
    if i == "1":
        analyze()
    elif i == "2":
        print(symbol_table)
        print_table(symbol_table)
    else:
        print("Enter a correct digit this time \n")    

print("GOODBYE!")
