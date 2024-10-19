from lark import Lark, Tree
from lark.tree import pydot__tree_to_png
from IPython.display import Image, display

# Define the grammar
grammar = """
start: statement* COMMENT*

statement: semicolonstatements
         | for_statement
         | methoddecl
         | if_statement
         | while_statement
         
         

semicolonstatements: basicstatement ";"

basicstatement: listget
              | returns
              | assignment
              | reassignment
              | vardecl
              | method
              | listadd
              | listdecl
              | listremove
              
returns : "return" (assignment | reassignment | expression)

assignment: vartype assignable "=" expression 

reassignment:  assignable "=" expression

methoddecl: "def" NAME methodparams codeblock -> method_decl

if_statement: "if" methodcall":" codeblock
            | "if" methodcall":" codeblock "else"":" codeblock
            | "if" comparison_operators":" codeblock 
            | "if" comparison_operators":" codeblock "else"":" codeblock

while_statement:"while" comparison_operators":" codeblock

for_statement: "for" "key" "in" assignable ":" codeblock

methodparams : "(" ")"
             | "(" param_list ")"

vardecl: vartype NAME  -> var_decl

listdecl: "map" "[" vartype "," vartype "]" assignable "=" "map" "[" vartype "," vartype "]" "(" ")"
        

listadd : assignable  "[" simpleexpression "]"("[" simpleexpression "]")* "=" simpleexpression
        | assignable  "[" simpleexpression "]"("[" simpleexpression "]")* "=" "map" "[" vartype "," vartype "]"

listget : assignable "[" simpleexpression "]" ("[" simpleexpression "]")*


listremove : "del" assignable  "[" simpleexpression "]"("[" simpleexpression "]")* 

param_list : paramdecl("," paramdecl)*

paramdecl : vartype NAME
          | "self"

vartype : "string" -> string
        | "int"  -> int
        | "float" -> float
        | "bool" -> bool
        | "object" -> object
        | "var" -> var
        | NAME -> derived
        | "map" "[" vartype "," vartype "]"

codeblock : "{}"
          | "{" (semicolonstatements | listget | listadd | if_statement | for_statement | while_statement)+ "}"


method : methodcall  | blockexec 

methodcall :  simpleexpression "(" (STRING| NAME | NUMBER | methodcall | listget | comparison_operators)? ("," (STRING | NAME | NUMBER | methodcall | listget | comparison_operators))* ")"


blockexec : "<"NAME">"

expression : listget |simpleexpression | operators

simpleexpression: methodcall
          | BOOLEAN
          | NUMBER
          | blockexec 
          | assignable
          | simpleexpression "(" operators ")"
          | STRING


assignable: NAME
          | simpleexpression"."NAME

operators : expression "+" expression   -> add
          | expression "-" expression   -> sub
          | expression "*" expression   -> mul
          | expression "/" expression   -> div
          | expression "^" expression   -> pow
          
comparison_operators : expression "==" expression -> equal
                     | expression ">=" expression -> bigger_equal_than
                     | expression ">" expression -> bigger_than
                     | expression "<=" expression ->  smaller_equal_than
                     | expression "<" expression ->  smaller_than
                     | expression "!=" expression -> not_equal


BOOLEAN.10: "true" | "false"  

NAME: /([a-zA-Z_][a-zA-Z0-9_]*|[a-zA-Z_][a-zA-Z0-9_]*)/
NUMBER : /-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?/
STRING: /"(([^"])|(\\["\\bfnrt]))*"/

COMMENT: "//" /.*/

%ignore " "
%ignore COMMENT
"""

# Create the parser
parser = Lark(grammar, start='start', parser='lalr')


#returns : "return" (assignment | reassignment | expression)