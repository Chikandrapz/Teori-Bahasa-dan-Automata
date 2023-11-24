import string

def lexical(loop):
    alphabet_list = list(string.ascii_lowercase)
    state_list = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11',
                  'x12', 'x13', 'x14', 'x15', 'x16', 'x17']
    transition_table = {}

    # Transition definitions
    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = "error"
            transition_table[(state, "#")] = "error"
            transition_table[(state, " ")] = "error"

    transition_table[("x0", " ")] = "x0"
    transition_table[("x16", "#")] = "accept"
    transition_table[("x16", " ")] = "x17"
    transition_table[("x17", "#")] = "accept"
    transition_table[("x17", " ")] = "x17"

    transition_table[("x0", "i")] = "x1"
    transition_table[("x1", "n")] = "x16"
    transition_table[("x16", " ")] = "x17"
    transition_table[("x17", "i")] = "x1"

    transition_table[("x0", "k")] = "x1"
    transition_table[("x1", "a")] = "x2"
    transition_table[("x2", "t")] = "x3"
    transition_table[("x3", "a")] = "x16"
    transition_table[("x16", " ")] = "x17"
    transition_table[("x17", "k")] = "x1"

    transition_table[("x0", "a")] = "x16"
    transition_table[("x16", " ")] = "x17"
    transition_table[("x17", "a")] = "x16"

    transition_table[("x0", ":")]  = "x16"
    transition_table[("x16", " ")] = "x17"
    transition_table[("x17", ":")] = "x16"

    transition_table[("x0", "p")] = "x6"
    transition_table[("x6", "r")] = "x7"
    transition_table[("x7", "i")] = "x8"
    transition_table[("x8", "n")] = "x9"
    transition_table[("x9", "t")] = "x10"
    transition_table[("x10", "(")] = "x11"
    transition_table[("x11", "k")] = "x12"
    transition_table[("x12", "a")] = "x13"
    transition_table[("x13", "t")] = "x14"
    transition_table[("x14", "a")] = "x15"
    transition_table[("x15", ")")] = "x16"
    transition_table[("x16", " ")] = "x17"
    transition_table[("x17", "p")] = "x6"

    transition_table[("x0", "f")] = "x4"
    transition_table[("x4", "o")] = "x5"
    transition_table[("x5", "r")] = "x16"
    transition_table[("x16", " ")] = "x17"
    transition_table[("x17", "f")] = "x4"
    
    transition_table[("x0", "(")] = "x16"
    transition_table[("x16", " ")] = "x17"
    transition_table[("x17", "(")] = "x16"
    
    transition_table[("x0", ")")] = "x176"
    transition_table[("x16", " ")] = "x17"
    transition_table[("x17", ")")] = "x16"

    #Lexical Analysis
    idx_char = 0
    state = 'x0'
    current_token = ''
    for current_char in input_string:
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state == 'x16':
            print('CURRENT TOKEN: ', current_token, ', VALID')
            current_token = ''
        if state == 'error':
            print('ERROR')
            break
        idx_char = idx_char + 1

    #Conclusion || state yang di accept
    if state == "accept":
        print('SEMUA TOKEN YANG DIINPUT : ', loop, ', VALID')
    
    return lexical


print("=====================TERMINAL======================")
print("for, in, a, kata, :, print(kata)")
print("===================================================")

loop = input("MASUKKAN INPUT : ",)
input_string = loop.lower()+'#'
lexical(loop)
