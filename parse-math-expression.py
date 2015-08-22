def evaluate(expression):
    # Strip all whitespace first
    input_string = expression.replace(" ", "")
    # Build a parse tree based on order of operations
    parse_tree = []
    
    for idx in range(len(input_string) + 1):
        last_char = False
        if idx == len(input_string):
            last_char = True
            char = None
        else:
            char = input_string[idx]



        if char == '(' or idx == 0:
            # Add a new frame for each parenthesis
            if idx == 0:
                to_append = int(char)
            else:
                to_append = None
            parse_tree.append({
                'operator' : None,
                'parameter' : to_append
            })
        elif char == ')' or last_char:
            # Compute everything inside the current parenthesis by compressing
            # all of the frames together.
            last_frame = parse_tree.pop()
            while len(parse_tree):
                frame = parse_tree.pop()
                func = frame['operator']
                last_frame = {
                    'operator' : None,
                    'parameter' : func(
                        frame['parameter'],
                        last_frame['parameter'])
                }

            parse_tree.append(last_frame)

        elif char == '+':
            frame = parse_tree[-1]
            frame['operator'] = add
        elif char == '-':
            frame = parse_tree[-1]
            frame['operator'] = subtract
        else:
            frame = parse_tree[-1]
            func = frame['operator']

            if func is None:
                frame['parameter'] = int(char)
            else:
                # Compute the result of the current frame and store it back
                # in the same frame
                result = func(frame['parameter'], int(char))
                frame['operator'] = None
                frame['parameter'] = result

    return parse_tree.pop()['parameter']
    
def add(a, b):
    """Adds two integers"""
    return a + b

def subtract(a, b):
    """Subtracts b from a"""
    return a - b
