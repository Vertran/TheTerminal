memory = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13"
]

def read_memory(start_pos, len):
    lines =''
    pos = 0
    for line in memory:
        pos += 1
        if pos > start_pos and pos < (start_pos + len):
            lines += line
            lines += '\n'
    return lines

def write_memory