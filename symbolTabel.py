import re

# Generate cross-reference symbol table
def generate_cross_reference_table(code):
    symbol_table = []
    line_number = 1
    current_address = 0  # Start from 0
    counter = 1
    data_type_sizes = {
        "int": 2,     # int is 2 bytes
        "char": 1,    # char is 1 byte
        "float": 1,   # float is 1 byte
        "string": 1   # string is 1 byte per character
    }

    for line in code.splitlines():
        match = re.match(r"^\s*(?P<data_type>\w+)\s+(?P<variable_def>.+);$", line)
        if match:
            data_type = match.group("data_type")
            variable_def = match.group("variable_def")

            # Handle multiple variables in one line
            for var in variable_def.split(","):
                var_match = re.match(r"(?P<variable_name>\w+)(\[(?P<dim1>\d+)\](\[(?P<dim2>\d+)\])?)?", var.strip())
                if var_match:
                    variable_name = var_match.group("variable_name")
                    dim1 = int(var_match.group("dim1")) if var_match.group("dim1") else 1
                    dim2 = int(var_match.group("dim2")) if var_match.group("dim2") else 1

                    # Calculate size
                    size = data_type_sizes.get(data_type, 0) * dim1 * dim2

                    # Add entry to the symbol table
                    symbol_table.append({
                        "Counter": counter,
                        "Variable Name": variable_name,
                        "Object Address": current_address,
                        "Type": data_type,
                        "Dim": (dim1, dim2) if dim1 > 1 or dim2 > 1 else 0,
                        "Line Declared": line_number,
                        "Line Reference": set()
                    })
                    counter += 1
                    current_address += size  # Increment address

        # Update line references
        for variable in re.findall(r"\b\w+\b", line):
            for entry in symbol_table:
                if entry["Variable Name"] == variable:
                    if line_number != entry["Line Declared"]:
                        entry["Line Reference"].add(line_number)
                    break

        line_number += 1

    return symbol_table

# Example C code
c_code = """\
int i, j[5];
char C, index[5][6], block[5];
float f;
i = 0;
i = i + k;
f = f + i;
C = 'x';
block[4] = C;
"""

# Generate the symbol table
symbol_table = generate_cross_reference_table(c_code)

# Print the table in a format similar to the image
header = f"{'Counter':<10}{'Variable Name':<15}{'Object Address':<15}{'Type':<10}{'Dim':<10}{'Line Declared':<15}{'Line Reference':<15}"
separator = "-" * 90

print(separator)
print(header)
print(separator)
for entry in symbol_table:
    dim = f"{entry['Dim'][0]}x{entry['Dim'][1]}" if isinstance(entry["Dim"], tuple) else entry["Dim"]
    line_ref = ", ".join(map(str, sorted(entry["Line Reference"]))) if entry["Line Reference"] else "-"
    print(f"{entry['Counter']:<10}{entry['Variable Name']:<15}{entry['Object Address']:<15}{entry['Type']:<10}{dim:<10}{entry['Line Declared']:<15}{line_ref:<15}")
print(separator)
