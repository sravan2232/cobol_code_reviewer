import re

def parse_cobol_code(code):
    sections = {
        "IDENTIFICATION DIVISION": "",
        "ENVIRONMENT DIVISION": "",
        "DATA DIVISION": "",
        "PROCEDURE DIVISION": "",
        "FILE OPERATIONS": [],
        "PERFORM BLOCKS": [],
        "GOTO USAGE": []
    }

    # Normalize code
    code_lines = code.splitlines()
    normalized_code = "\n".join(line.strip() for line in code_lines if line.strip())

    # Extract divisions
    division_pattern = re.compile(r"(?i)(IDENTIFICATION DIVISION|ENVIRONMENT DIVISION|DATA DIVISION|PROCEDURE DIVISION)(.*?)((?=IDENTIFICATION DIVISION|ENVIRONMENT DIVISION|DATA DIVISION|PROCEDURE DIVISION|$))", re.DOTALL)

    for match in division_pattern.finditer(normalized_code):
        section_name = match.group(1).upper()
        section_body = match.group(2).strip()
        sections[section_name] = section_body

    # Look for file operations
    file_ops = re.findall(r"(?i)\b(OPEN|READ|WRITE|CLOSE)\b\s+[\w-]+", normalized_code)
    sections["FILE OPERATIONS"] = file_ops

    # Look for PERFORM blocks
    perform_blocks = re.findall(r"(?i)\bPERFORM\s+[\w-]+", normalized_code)
    sections["PERFORM BLOCKS"] = perform_blocks

    # Look for GOTO statements
    goto_statements = re.findall(r"(?i)\bGO\s+TO\s+[\w-]+", normalized_code)
    sections["GOTO USAGE"] = goto_statements

    return sections