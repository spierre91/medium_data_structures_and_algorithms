from collections import deque

def search_text(lines, pattern, history=5): 
    previous_lines = deque(maxlen=history) 
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('amazon_review.txt') as f:
        for line, previous_lines in search_text(f, 'Python', 5): 
            for pline in previous_lines:
                print(pline, end='') 
            print(line, end='') 
            print('-'*150)
