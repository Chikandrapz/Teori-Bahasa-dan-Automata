def parser(loop):
    tokens = loop.lower().split()
    tokens.append('EOS')

    non_terminals = ['statement', 'newVar','variable', 'print_statement', 'simbol']
    terminals = ['for', 'kata', 'in', 'a', ':', 'print(kata)', '(', ')', 'EOS']

    parse_table = {}

    parse_table[('statement', 'for')] = ['for', 'newVar', 'in', 'variable', ':','print_statement']
    parse_table[('statement', 'kata')] = ['newVar']
    parse_table[('statement', 'in')] = ['error']
    parse_table[('statement', 'a')] = ['variable']
    parse_table[('statement', ':')] = [':']
    parse_table[('statement', 'print(kata)')] = ['print_statement']
    parse_table[('statement', '(')] = ['error']
    parse_table[('statement', ')')] = ['error']

    parse_table[('newVar', 'for')] = ['error']
    parse_table[('newVar', 'kata')] = ['kata']
    parse_table[('newVar', 'in')] = ['error']
    parse_table[('newVar', 'a')] = ['error']
    parse_table[('newVar', ':')] = ['error']
    parse_table[('newVar', 'print(kata)')] = ['error']
    parse_table[('newVar', '(')] = ['error']
    parse_table[('newVar', ')')] = ['error']


    parse_table[('variable', 'for')] = ['error']
    parse_table[('variable', 'kata')] = ['error']
    parse_table[('variable', 'in')] = ['error']
    parse_table[('variable', 'a')] = ['a']
    parse_table[('variable', ':')] = ['error']
    parse_table[('variable', 'print(kata)')] = ['error']
    parse_table[('variable', '(')] = ['error']
    parse_table[('variable', ')')] = ['error']

    parse_table[('print_statement', 'for')] = ['error']
    parse_table[('print_statement', 'kata')] = ['error']
    parse_table[('print_statement', 'in')] = ['error']
    parse_table[('print_statement', 'a')] = ['error']
    parse_table[('print_statement', ':')] = [':']
    parse_table[('print_statement', 'print(kata)')] = ['print(kata)']
    parse_table[('print_statement', '(')] = ['error']
    parse_table[('print_statement', ')')] = ['error']

    parse_table[('simbol', 'for')] = ['error']
    parse_table[('simbol', 'kata')] = ['error']
    parse_table[('simbol', 'in')] = ['error']
    parse_table[('simbol', 'a')] = ['error']
    parse_table[('simbol', ':')] = ['error']
    parse_table[('simbol', 'print(kata)')] = ['print_statement']
    parse_table[('simbol', '(')] = ['(']
    parse_table[('simbol', ')')] = [')']

    stack = ['#', 'statement']
    index_token = 0
    symbol = tokens[index_token]

    while len(stack) > 0:
        top = stack[len(stack) - 1]
        print('TOP    =', top)
        print('SYMBOL =', symbol)
        if top in terminals:
            print('TOP ADALAH SYMBOL TERMINAL')
            if top == symbol:
                stack.pop()
                index_token += 1
                symbol = tokens[index_token]
                if symbol == "EOS":
                    stack.pop()
                    print('ISI STACK:', stack)
            else:
                print('ERROR')
                break
        elif top in non_terminals:
            print('TOP ADALAH SYMBOL NON-TERMINAL')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbol_to_be_pushed = parse_table[(top, symbol)]
                for i in range(len(symbol_to_be_pushed)-1, -1, -1):
                    stack.append(symbol_to_be_pushed[i])
            else:
                print('ERROR')
                break
        else:
            print('ERROR')
            break
        print('ISI STACK:', stack)
        print()
    print()
    
    if symbol == 'EOS' and len(stack) == 0:
        print('Inputan String "', loop, '" Diterima, Sesuai Grammar')
    else:
        print('ERROR, Inputan String:', '"', loop, '"', ', Tidak Diterima, Tidak Sesuai Grammar')

    return parser

# Main Program Parser
print("============= TERMINAL =============")
print("statement : for, in, :")
print("newVar : kata")
print("variable  : a")
print("print_statement  : print(kata)")
print("simbol    : (, )")
print("==================================== \n")
loop = input("MASUKKAN INPUT: ")
input_string = loop.lower() + '#'
parser(loop)



