#výraz - postfix - výpočítať
#DUDO.GVPT.SK - spracovanie číselného výrazu

class Stack(list):
    def __init__(self):
        super().__init__()

    def __setitem__(self, key, value): #pri výnimke
        raise("Nope, toto nejde.")

    def __getitem__(self, item): #pri výnimke (druhý spôsob)
        raise("Nope, toto nejde.")

    def isEmpty(self):
        if len(self) > 0:
            return False
        else:
            return True

    def push(self, value):
        super().append(value)

    def pop(self):
        return super(Stack, self).pop(-1)


stack = Stack()

def infix_to_postfix(input:str):
    priority = {"*":3, "/":3, "+":2, "-":2, "(":1, ")":1}
    output = []
    global stack
    input = input.split(" ")
    for character in input:
        if character == "(":
            stack.push(character)
        elif character == ")":
            p = stack.pop()
            stack.push(p)
            while p != "(":
                if p in "*/-+()":
                    output.append(p)
                    stack.pop()
                    p = stack.pop()
                    stack.push(p)
            stack.pop()
        elif character in "*/-+":
            for i in stack:
                if priority[i] == "2":
                    stack.remove(i)
                    output.append(i)
            stack.push(character)
        else:
            output.append(character)
    while stack.isEmpty() == False:
        output.append(stack.pop())
    return output

print(*infix_to_postfix("( A + B ) * C"))           # -> A B + C *
print(*infix_to_postfix("A + B * C"))               # -> A B C * +
print(*infix_to_postfix("( A + B ) * ( C + D )"))   # -> A B + C D + *

#ak tam niečo nedáva zmysel, tak je to tým, že som chýbala, keď ste robili s class - ale doberám si to :D
