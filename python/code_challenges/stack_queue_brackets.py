from data_structures.stack import Stack


def multi_bracket_validation(str):

    opened = Stack()
    brackets = {'{': 'open',
                '(': 'open',
                '[': 'open',
                '}': 'close',
                ')': 'close',
                ']': 'close'
                }

    match = {'{': '}', '(': ')', '[': ']'}

    for char in str:
        if char in brackets.keys():
            if brackets[char] == 'open':
                opened.push(char)

            else:
                # if our char is a closing bracket/ any other character and opened stack is empty return False
                if opened.is_empty():
                    return False
                # if our char is a closing bracket and matches any of the value of match pairs, pop opened stack
                if char == match[opened.peek()]:
                    opened.pop()
                # if our character is anything other than closing bracket
                else:
                    return False
    # if opened stack is not empty return false since that means we didn't get matching pairs
    if not opened.is_empty():
        return False

    return True



