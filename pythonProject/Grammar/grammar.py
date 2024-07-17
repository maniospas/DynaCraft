from lark import Lark, Tree
from lark.tree import pydot__tree_to_png
from IPython.display import Image, display

# Define the grammar
grammar = """
start: statement*

statement: semicolonstatements
         | methoddecl
         | if_statement
         | while_statement
         

semicolonstatements: basicstatement ";"

basicstatement: returns
              | assignment
              | reassignment
              | vardecl
              | method

returns : "return" (assignment | reassignment | expression)

assignment: vartype assignable "=" expression 

reassignment:  assignable "=" expression

methoddecl: "def" NAME methodparams codeblock -> method_decl

if_statement:"if" methodcall codeblock "else" codeblock
            | "if" comparison_operators":" codeblock "else" codeblock

while_statement:"while" comparison_operators":" codeblock

methodparams : "(" ")"
             | "(" paramdecl ")"

vardecl: vartype NAME  -> var_decl

paramdecl : vartype NAME
          | "self"
          | paramdecl"," paramdecl


vartype : "string" -> string
        | "int"  -> int
        | "float" -> float
        | "object" -> object
        | "var" -> var
        | NAME -> derived

codeblock : "{}"
          | "{" (semicolonstatements | if_statement | while_statement)+ "}"


method : methodcall  | blockexec 

methodcall : simpleexpression "(" (NAME | NUMBER | methodcall)? ("," (NAME | NUMBER | methodcall))* ")"


blockexec : "<"NAME">"

expression : simpleexpression | operators

simpleexpression: methodcall
          | NUMBER
          | blockexec 
          | assignable
          | simpleexpression "(" operators ")"


assignable: NAME
          | simpleexpression"."NAME

operators : expression "+" expression   -> add
          | expression "-" expression   -> sub
          | expression "*" expression   -> mul
          | expression "/" expression   -> div
          
comparison_operators : expression "==" expression -> equal
                     | expression ">=" expression -> bigger_than
                     | expression "<=" expression ->  smaller_than
                     | expression "!=" expression -> not_equal

NAME: /([a-zA-Z_][a-zA-Z0-9_]*|[a-zA-Z_][a-zA-Z0-9_]*)/
NUMBER : /-?\\d+(\\.\\d+)?([eE][+-]?\\d+)?/
STRING : /".*?(?<!\\)"/

%ignore " "
"""

# Create the parser
parser = Lark(grammar, start='start', parser='lalr')
#returns : "return" (assignment | reassignment | expression)