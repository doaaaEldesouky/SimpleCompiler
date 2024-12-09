import logging
import traceback
import cProfile
import pdb
from anytree import Node, RenderTree

# Logging settings
logging.basicConfig(filename='compiler_debug.log', level=logging.DEBUG)

# Define the root and tree structure using Nodes
S = Node("S")
statement = Node("Statement", parent=S)
assignment = Node("Assignment", parent=statement)
conditional = Node("Conditional", parent=statement)
print_statement = Node("PrintStatement", parent=statement)
loop_statement = Node("LoopStatement", parent=statement)

# Build the tree with relationships
assignment_type = Node("Assignment Type", parent=assignment)
loop_for = Node("For Loop", parent=loop_statement)
loop_while = Node("While Loop", parent=loop_statement)
conditional_if = Node("If Statement", parent=conditional)

# Add other rules (e.g., Type, Expression, etc.)
type_int = Node("'int'", parent=assignment_type)
type_float = Node("'float'", parent=assignment_type)
type_string = Node("'string'", parent=assignment_type)

identifier = Node("IDENTIFIER", parent=assignment_type)
expression = Node("Expression", parent=assignment_type)

# Build the tree for the Conditional rule
condition = Node("Condition", parent=conditional_if)
identifier_condition = Node("IDENTIFIER", parent=condition)
operator = Node("'>'", parent=condition)
number = Node("NUMBER", parent=condition)

# Print the parse tree hierarchically
print("Parse Tree:")
for pre, fill, node in RenderTree(S):
    print(f"{pre}{node.name}")

# Function to check for errors in tokens
def check_for_errors(tokens):
    try:
        if not tokens:
            raise ValueError("Token list is empty")
        for token in tokens:
            if token not in ['int', 'float', 'string', 'IDENTIFIER', 'NUMBER']:
                raise ValueError(f"Invalid token: {token}")
        logging.info("Tokens are valid")
    except ValueError as e:
        logging.error(f"Error: {e}")
        logging.error(f"Traceback: {traceback.format_exc()}")
        print(f"Error: {e}")

# Function to parse specific expressions
def parse_expression(expression):
    logging.debug(f"Parsing expression: {expression}")
    try:
        # Perform the parsing operation
        result = expression  # Assume some operations are done here
        logging.debug(f"Result: {result}")
        return result
    except Exception as e:
        logging.error(f"Parsing error: {e}")
        logging.error(f"Traceback: {traceback.format_exc()}")
        print(f"Parsing error: {e}")

# Function for code generation
def generate_code(ir_code):
    logging.debug("Starting code generation...")
    try:
        # Log intermediate code for visibility
        logging.debug(f"Generated Intermediate Code: {ir_code}")
        # Generate the final code
        final_code = f"Generated Code: {ir_code}"  # Assume preliminary code
        logging.debug(f"Final Generated Code: {final_code}")
        return final_code
    except Exception as e:
        logging.error(f"Error in code generation: {e}")
        logging.error(f"Traceback: {traceback.format_exc()}")
        print(f"Code generation error: {e}")

# Function to log an error message
def log_error(error_message):
    logging.error(f"Error: {error_message}")

# Function to test interactive debugging
def test_debugging():
    pdb.set_trace()  # The program will stop here for interactive value inspection
    # Perform a simple operation to follow values
    a = 5
    b = 10
    c = a + b
    print(f"The result is: {c}")
    return c

# Function to handle syntax errors
def handle_syntax_error():
    try:
        # Place some code that might have errors for traceback demonstration
        raise SyntaxError("This is a simulated syntax error")
    except SyntaxError as e:
        log_error(f"Syntax error at line {e.lineno}: {e.text}")
        logging.error(f"Traceback: {traceback.format_exc()}")

# Apply analysis and code generation with error handling
tokens = ['int', 'IDENTIFIER', 'string', 'random']  # Includes an invalid token (random)
check_for_errors(tokens)

# Parse expressions and test interactive debugging
expression = "a + b"
parse_expression(expression)
test_debugging()

# Generate code and test errors
ir_code = "int x = 5"
generate_code(ir_code)

# Test programmatic error handling
handle_syntax_error()

# Analyze performance using cProfile
def profile_code():
    cProfile.run('test_debugging()')

profile_code()
