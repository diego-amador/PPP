
# -----------------------------------------------------------------------------
# parser.py
# A parser for the P++ Language.
# -----------------------------------------------------------------------------
import ply.yacc as yacc
import codeGenerator as generator
import os

#token map
from lexer import tokens



def p_expression_ID(p):
    """expression : START ID ASSIGN Operation COLON Function LPAREN ParameterList RPAREN Location SEMIC END
                 | APPEND ID TO ID SEMIC
                 | START ROTATE ID ASSIGN Operation COLON Function LPAREN ParameterList RPAREN AROUND ID ASSIGN Operation COLON Function LPAREN ParameterList RPAREN SEMIC END
                 | START END
                 | END"""

    if p[1] == 'START':
        if os.path.isfile("PPP.pde"):
            os.remove("PPP.pde")
    if p[2] == 'END':
        p[0] = "grid"
        generator.render(p[0])
        generator.run()
        return

    if p[2] == "rotate":
        p[0] = (p[2], p[9], p[18])
        generator.render(p[0])
        generator.run()
        return

    if p[6] == "sin": 
        p[0] = (p[2], p[3], p[4], p[6], p[8], p[10])
        generator.render(p[0])
        generator.run()
        return
    
       

def p_param_list(p):
    """ParameterList : Parameter AND ParameterList 
                     | Parameter 
                     | empty"""
    if len(p) < 3: p[0] = p[1]      #This covers "Paramater And ParameterList" and "Parameter"
    else: p[0]  = (p[1], p[3])      #This covers "empty"

def p_parameter(p):
    """Parameter : ID ASSIGN DIGIT 
                 | ID ASSIGN String
                 | LINE ASSIGN String """
    generator.updateValue(p[1],p[3])    #Value is updated in the code generator
                    
    p[0] = p[3]     #The value of interest is in index 3

def p_string(p) :
    'String : QUOTE ID QUOTE'
    p[0] = p[2]     #This is used to determine the color

def p_operation(p):
    'Operation : DRAW'
    p[0] = p[1]     #No other function other than draw as of now

def p_function(p):
    """Function : SIN 
                | CIRCLE 
                | GRID 
                | LINE"""
    p[0] = p[1]
   
 
def p_location(p):
    """Location : REGARDING Coordinate
                | empty"""
    if p[1] == '@': p[0] = p[2]     #This covers non DEFAULT coordinates
    else: p[0] = p[1]

def p_coordinate(p):
    """Coordinate : ID 
                  | LPAREN DIGIT COMMA DIGIT RPAREN"""
    if p[1] != '(': p[0] = p[1]     #This covers coordinates represented as ID
    else: p[0] = (p[2], p[4])       #Coordinate as (x, y)


def p_empty(p):
    'empty :'
    p[0] = 'DEFAULT'    #This is the indicator to choose default paramters


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

def translateCode(p):
    print(*p)
    try:
        PPPSource = open(p, 'r')
    except IOError:
        print("Error opening file")
        exit()

    for line in PPPSource:
        try:
            parser.parse(line)
        except IOError:
            print("Error opening file!")
            exit()


fname = 'PPPCode.txt'

with open(fname) as f:
    lines = [line.rstrip('\n') for line in f]
f.close()

ppp = ''
for x in lines:
    if x == 'START':    x = 'START '
    if x == 'END':      x = ' END'
    ppp = ppp + x
print (ppp)
result = parser.parse(ppp)

