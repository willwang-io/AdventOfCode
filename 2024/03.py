import re

def process_memory(text):
    total = 0
    enabled = True
    instructions = []
    
    for match in re.finditer(r'mul\((\d+),\s*(\d+)\)', text):
        instructions.append(('mul', match.start(), int(match.group(1)), int(match.group(2))))
    
    for match in re.finditer(r'do\(\)', text):
        instructions.append(('do', match.start(), None, None))
    for match in re.finditer(r"don't\(\)", text):
        instructions.append(('dont', match.start(), None, None))
    
    instructions.sort(key=lambda x: x[1])
    
    for inst_type, _, x, y in instructions:
        if inst_type == 'do':
            enabled = True
        elif inst_type == 'dont':
            enabled = False
        elif inst_type == 'mul' and enabled:
            total += x * y
    
    return total

with open("in.txt", "r") as f:
    data = f.read()
    ans = process_memory(data)
    print(ans)