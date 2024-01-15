operators = set(['+', '*'])
precedence = {'+': 1, '*': 2}

def infix_to_postfix(infix):
    postfix = ''
    stack = []

    for character in infix:
        if character not in operators:
            postfix += character
        else:
            while stack and precedence[character] <= precedence[stack[-1]]:
                postfix += stack.pop()
            stack.append(character)
    
    while stack:
        postfix += stack.pop()

    return postfix

infix = 'a*b+c'
 
print(f'infix notation: {infix}')
print(f'postfix notation: {infix_to_postfix(infix)}')