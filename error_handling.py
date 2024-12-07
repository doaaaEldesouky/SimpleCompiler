import logging
import traceback
import cProfile
import pdb
from anytree import Node, RenderTree

# إعدادات التسجيل (logging)
logging.basicConfig(filename='compiler_debug.log', level=logging.DEBUG)

# تعريف الجذر والشجرة باستخدام Nodes
S = Node("S")
statement = Node("Statement", parent=S)
assignment = Node("Assignment", parent=statement)
conditional = Node("Conditional", parent=statement)
print_statement = Node("PrintStatement", parent=statement)
loop_statement = Node("LoopStatement", parent=statement)

# بناء الشجرة مع العلاقات بين العقد
assignment_type = Node("Assignment Type", parent=assignment)
loop_for = Node("For Loop", parent=loop_statement)
loop_while = Node("While Loop", parent=loop_statement)
conditional_if = Node("If Statement", parent=conditional)

# إضافة القواعد الأخرى (مثل Type, Expression, وغيرها)
type_int = Node("'int'", parent=assignment_type)
type_float = Node("'float'", parent=assignment_type)
type_string = Node("'string'", parent=assignment_type)

identifier = Node("IDENTIFIER", parent=assignment_type)
expression = Node("Expression", parent=assignment_type)

# بناء الشجرة لقاعدة Conditional
condition = Node("Condition", parent=conditional_if)
identifier_condition = Node("IDENTIFIER", parent=condition)
operator = Node("'>'", parent=condition)
number = Node("NUMBER", parent=condition)

# طباعة الشجرة بشكل هرمي مع إبراز العقد والأفرع لتوضيح شجرة التحليل
print("Parse Tree:")
for pre, fill, node in RenderTree(S):
    print(f"{pre}{node.name}")

# دالة للتحقق من الأخطاء في الأكواد
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

# دالة لتحليل تعبيرات معينة
def parse_expression(expression):
    logging.debug(f"Parsing expression: {expression}")
    try:
        # عملية التحليل هنا
        result = expression  # افتراض أننا نقوم ببعض العمليات هنا
        logging.debug(f"Result: {result}")
        return result
    except Exception as e:
        logging.error(f"Parsing error: {e}")
        logging.error(f"Traceback: {traceback.format_exc()}")
        print(f"Parsing error: {e}")

# دالة لتوليد الكود (Code Generation)
def generate_code(ir_code):
    logging.debug("Starting code generation...")
    try:
        # في هذه الخطوة، يمكن أن نطبع الكود الوسيط لعرضه
        logging.debug(f"Generated Intermediate Code: {ir_code}")
        # هنا سيتم توليد الكود
        final_code = f"Generated Code: {ir_code}"  # افتراض كود مبدئي
        logging.debug(f"Final Generated Code: {final_code}")
        return final_code
    except Exception as e:
        logging.error(f"Error in code generation: {e}")
        logging.error(f"Traceback: {traceback.format_exc()}")
        print(f"Code generation error: {e}")

# دالة لملف السجل (log file)
def log_error(error_message):
    logging.error(f"Error: {error_message}")

# دالة لاختبار التصحيح التفاعلي
def test_debugging():
    pdb.set_trace()  # هذه السطر سيتوقف البرنامج عنده لمتابعة القيم داخل بيئة تفاعلية
    # إجراء عملية بسيطة لمتابعة القيم
    a = 5
    b = 10
    c = a + b
    print(f"The result is: {c}")
    return c

# دالة لتحليل الخطأ
def handle_syntax_error():
    try:
        # هنا يمكن وضع بعض الأكواد التي قد تحتوي على أخطاء لعرضها عبر traceback
        raise SyntaxError("This is a simulated syntax error")
    except SyntaxError as e:
        log_error(f"Syntax error at line {e.lineno}: {e.text}")
        logging.error(f"Traceback: {traceback.format_exc()}")

# تطبيق التحليل وتوليد الكود مع الأخطاء:
tokens = ['int', 'IDENTIFIER', 'string', 'random']  # هنا سيتم إضافة توكن غير صالح (random)
check_for_errors(tokens)

# تحليل تعبيرات وتجربة التوقف التفاعلي
expression = "a + b"
parse_expression(expression)
test_debugging()

# توليد كود واختبار الأخطاء
ir_code = "int x = 5"
generate_code(ir_code)

# اختبار الخطأ البرمجي
handle_syntax_error()

# تحليل الأداء باستخدام cProfile
def profile_code():
    cProfile.run('test_debugging()')

profile_code()
