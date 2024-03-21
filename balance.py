from classStack import Stack

def balance(start_list):
    stack_1 = Stack()
    stack_2 = Stack()
    right_el = ')}]'
    left_el = '({['
    for i in start_list:
        stack_1.push(i)
    if stack_1.size() % 2 == 0:
        while stack_1.size() > 1:
            if stack_1.peec() in right_el:
                stack_2.push(stack_1.pop())
            else:
                while stack_2.isEmpty() == False and (stack_1.peec() in left_el):
                    if left_el.index(stack_1.pop()) == right_el.index(stack_2.pop()):
                        result = 'Сбалансированно'
                    else:
                        result = 'Несбалансированно'
                        break
    else:
        result = 'Несбалансированно'
    return result