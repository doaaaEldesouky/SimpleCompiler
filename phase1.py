import re
from collections import defaultdict
import tkinter as tk
from tkinter import Scrollbar, Text

# قراءة الكود المصدر من الملف
with open('source_code.txt', 'r') as file:
    source_code = file.read()

# نمط التوكنات
tokens_pattern = r'\b\w+\b|[^\w\s]'
lexemes = re.findall(tokens_pattern, source_code)

# تصنيف التوكنات
def classify_lexeme(lexeme):
    keywords = {"for", "while", "if", "else", "print", "int", "float", "string"}
    if lexeme.isdigit():
        return "NUMBER"
    elif lexeme in keywords:
        return "KEYWORD"
    elif lexeme.isidentifier():
        return "IDENTIFIER"
    elif lexeme in ("(", ")", "{", "}", ";"):
        return "SYMBOL"  # تصنيف ; كـ SYMBOL
    else:
        return "OPERATOR"

# تخزين التوكنات والعد
token_list = []
token_count = defaultdict(int)

# تصنيف التوكنات
for lexeme in lexemes:
    token = classify_lexeme(lexeme)
    token_list.append((lexeme, token))
    token_count[token] += 1

# القواعد النحوية
grammar_rules = {
    "S": ["Statement"],
    "Statement": [
        "Assignment", 
        "Conditional", 
        "PrintStatement", 
        "LoopStatement", 
        "Block"
    ],
    "Assignment": [
        "Type IDENTIFIER '=' Expression ';'"
    ],
    "LoopStatement": [
        "'for' '(' Assignment Expression ';' Expression ')' Block",
        "'while' '(' Expression ')' Block"
    ],
    "Type": [
        "'int'", 
        "'float'", 
        "'string'"
    ],
    "IDENTIFIER": [
        "[a-zA-Z_][a-zA-Z0-9_]*"
    ],
    "Expression": [
        "Expression '+' Term",
        "Expression '-' Term",
        "Term"
    ],
    "Term": [
        "Term '*' Factor",
        "Term '/' Factor",
        "Factor"
    ],
    "Factor": [
        "NUMBER", 
        "IDENTIFIER", 
        "'(' Expression ')'"
    ],
    "Value": [
        "NUMBER", 
        "IDENTIFIER"
    ],
    "Conditional": [
        "'if' '(' Condition ')' Block"
    ],
    "Condition": [
        "IDENTIFIER '>' Expression",
        "IDENTIFIER '<' Expression",
        "IDENTIFIER '==' Expression",
        "IDENTIFIER '>=' Expression",
        "IDENTIFIER '<=' Expression",
        "IDENTIFIER '!=' Expression"
    ],
    "PrintStatement": [
        "'print' '(' IDENTIFIER ')' ';'"
    ],
    "Block": [
        "'{' (Statement)* '}'"
    ],
    "NUMBER": [
        "DIGIT+", 
        "DIGIT+ '.' DIGIT+"
    ],
    "DIGIT": [
        "'0'", "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "'7'", "'8'", "'9'"
    ]
}

# دالة لعرض الجداول باستخدام Tkinter
def display_table(title, headers, data):
    window = tk.Tk()
    window.title(title)
    
    text_box = Text(window, width=80, height=20)
    text_box.pack(pady=20)

    # كتابة العنوان
    text_box.insert(tk.END, f"{title}:\n")
    
    # كتابة رؤوس الأعمدة
    text_box.insert(tk.END, " | ".join(headers) + "\n")
    
    # كتابة البيانات
    for row in data:
        text_box.insert(tk.END, " | ".join(str(cell) for cell in row) + "\n")
    
    # تمكين التمرير العمودي
    scrollbar = Scrollbar(window, command=text_box.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_box.config(yscrollcommand=scrollbar.set)
    
    window.mainloop()

# عرض التوكنات
display_table("LEXEME AND TOKEN", ["LEXEME", "TOKEN"], token_list)

# عرض عدد التوكنات
def display_token_count():
    window = tk.Tk()
    window.title("Token Counts")

    text_box = Text(window, width=40, height=10)
    text_box.pack(pady=20)

    text_box.insert(tk.END, "Token Counts:\n")
    for token, count in token_count.items():
        text_box.insert(tk.END, f"{token}: {count}\n")

    window.mainloop()

display_token_count()

# دالة لعرض القواعد النحوية باستخدام Tkinter
def display_grammar_rules():
    window = tk.Tk()
    window.title("Grammar.txt")

    text_box = Text(window, width=80, height=20)
    text_box.pack(pady=20)

    text_box.insert(tk.END, "Grammar Rules:\n")
    for rule, components in grammar_rules.items():
        text_box.insert(tk.END, f"{rule}: {', '.join(components)}\n")
    
    window.mainloop()

display_grammar_rules()
