from collections import deque
def search(lines,pattern,history = 3):
    previous_lines = deque(mazlen = history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)
