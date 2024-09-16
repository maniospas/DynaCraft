# DynaCraft

# Data Types

You have to declare datatypes to initialize a variable

```c
int x;
int y = 5;
float z = 4.5;
```

you can also use the keyword var and the compiler will determine the type base on the expression used to initialize the variable

```c
var x = 5; //int

var y = "hello" //string

var z = 5 + "items" //string (string concat)
```

#Blocks
#Blocks as Functions
A block can be called as a function as shown below. self.x : int is used to declare the type of x.
```c

def norm(int x, int y){
                          object self = object();
                          return self.x * self.y;
                      }      
def vector(int x, int y){
                          object self = object();
                          int self.x = x;
                          int self.y = y;
                          int self(self.x,self.y);
                        
                        }

vector a = vector(3,2);
var z = vector.x + vector.y;
#print(z); //this should be 5
#print(norm.a); //this should print 6

```
#Blocks as Code

If a code block is called after the key symbol & then the code inside the block runs as is.

```c
def addition(int x,int y){
                          int x = x + 5;
                          int y = x + 4;
                          #print(y);
                         }


var x = 2;
#print(x); //should print 2

&addition; //should print 11
```

#Shadowing
You can declare a new variable with the same name as a previous one.The second variable overshadows the first, taking any uses of the variable name to itself until either it itself is shadowed or the scope ends.

```c
var x = 5;
#print(x); //5

var x = x +2;
#print(x); //7

sum {
    var x = x+3;
}
#print(sum); //10
#print(x); //7
```
