import re

# Unordered Symbol Table
def generate_symbol_table(code):
    symbol_table = []
    line_number = 1
    current_address = 0  
    counter = 0

    for line in code.splitlines():
        # مطابقة تعريف المتغير
        match = re.match(r"^\s*(?P<data_type>\w+)\s+(?P<variable_name>\w+)\s*=\s*(?P<value>.+);$", line)
        if match:
            data_type = match.group("data_type")
            variable_name = match.group("variable_name")

            # إدخال في جدول الرموز
            symbol_table.append({
                "Counter": counter,
                "Variable Name": variable_name,
                "Address": current_address,
                "Data Type": data_type,
                "No. of Dimensions": 0,
                "Line Declaration": line_number,
                "Reference Line": set(),  # مجموعة فارغة
            })
            counter += 1
            current_address += 2  # تحديث العنوان

        # تحديث مراجع الرموز في الأسطر
        for variable in re.findall(r"\b\w+\b", line):
            for entry in symbol_table:
                if entry["Variable Name"] == variable:
                    if line_number != entry["Line Declaration"]:  # ليس خط التعريف
                        entry["Reference Line"].add(line_number)
                    break

        line_number += 1

    return symbol_table

# Ordered Symbol Table
def generate_symbol_table_ordered(code):
    symbol_table = generate_symbol_table(code)

    # ترتيب الجدول أبجدياً حسب اسم المتغير
    symbol_table.sort(key=lambda x: x["Variable Name"])

    # تحديث القيم بعد الترتيب
    counter = 0
    for entry in symbol_table:
        entry["Counter"] = counter
        entry["Address"] = counter * 2  # تحديث العنوان
        counter += 1

    return symbol_table


# قراءة الكود من الملف
file_path = "C:/Users/Computec/Desktop/compiler pro/source_code.txt"
with open(file_path, 'r') as file:
    code = file.read()

# إنشاء الجدول غير المرتب
symbol_table = generate_symbol_table(code)

# طباعة الجدول غير المرتب
header = f"{'Counter':<8}{'VariableName':<15}{'Address':<10}{'Data Type':<15}{'No.of Dimensions':<20}{'LineDeclaration':<20}{'ReferenceLine':<25}"
separator_length = 100  # You can adjust this value as needed
separator = "-" * separator_length


print("\nUnordered Symbol Table:\n")
print(separator)
print(header)
print(separator)
for entry in symbol_table:
    print(f"{entry['Counter']:<8}{entry['Variable Name']:<15}{entry['Address']:<10}{entry['Data Type']:<15}{entry['No. of Dimensions']:<20}{entry['Line Declaration']:<20}{str(entry['Reference Line']).replace('set()', '{}'):<25}")
print(separator)

# إنشاء الجدول المرتب
symbol_table_ordered = generate_symbol_table_ordered(code)

# طباعة الجدول المرتب
print("\nOrdered Symbol Table:\n")
print(separator)
print(header)
print(separator)
for entry in symbol_table_ordered:
    print(f"{entry['Counter']:<8}{entry['Variable Name']:<15}{entry['Address']:<10}{entry['Data Type']:<15}{entry['No. of Dimensions']:<20}{entry['Line Declaration']:<20}{str(entry['Reference Line']).replace('set()', '{}'):<25}")
print(separator)
