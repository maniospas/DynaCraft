import logging

# Create a logger
logger = logging.getLogger(__name__)

# Define your flags
#FLAG_PRINT_ALL = False
FLAG_PRINT_RETURNS = False
FLAG_PRINT_DEBUG = False
FLAG_PRINT_INFO = False
FLAG_PRINT_EXPRESSION_TREE = False

# Define a custom function to print debug messages if the flag is set
def print_return(message,*args):
    if FLAG_PRINT_RETURNS:
        print("[RETURNS] " + message, *args)


# Define a custom function to print info messages if the flag is set
def print_debug(message, *args):
    if FLAG_PRINT_DEBUG:
        print("[DEBUG] " + message, *args)

# Define a custom function to print info messages if the flag is set
def print_info(message, *args):
    if FLAG_PRINT_DEBUG:
        print("[INFO] " + message, *args)

def print_expression_tree(message, *args):
    if FLAG_PRINT_EXPRESSION_TREE:
        print("[EXPRESSION TREE] " + message, *args)



