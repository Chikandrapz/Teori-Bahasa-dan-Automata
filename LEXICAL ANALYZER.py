import string

def lexical(loop):
    alphabet_list = list(string.ascii_lowercase)
    state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 
                  'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 
                  'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29']
    transition_table = {}

    # Transition definitions
    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = "error"
            transition_table[(state, "#")] = "error"
            transition_table[(state, " ")] = "error"

    transition_table[("q0", " ")] = "q0"
    transition_table[("q28", "#")] = "accept"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "#")] = "accept"
    transition_table[("q29", " ")] = "q29"

    transition_table[("q0", "i")] = "q1"
    transition_table[("q1", "n")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "i")] = "q1"

    transition_table[("q0", "k")] = "q1"
    transition_table[("q1", "a")] = "q2"
    transition_table[("q2", "t")] = "q3"
    transition_table[("q3", "a")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "k")] = "q1"

    transition_table[("q0", "a")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "a")] = "q28"

    transition_table[("q0", ":")]  = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", ":")] = "q28"

    transition_table[("q0", "p")] = "q17"
    transition_table[("q17", "r")] = "q18"
    transition_table[("q18", "i")] = "q19"
    transition_table[("q19", "n")] = "q20"
    transition_table[("q20", "t")] = "q21"
    transition_table[("q21", "(")] = "q22"
    transition_table[("q22", "k")] = "q23"
    transition_table[("q23", "a")] = "q24"
    transition_table[("q24", "t")] = "q25"
    transition_table[("q25", "a")] = "q26"
    transition_table[("q26", ")")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "p")] = "q17"

    transition_table[("q0", "f")] = "q7"
    transition_table[("q7", "o")] = "q8"
    transition_table[("q8", "r")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "f")] = "q7"
    
    transition_table[("q0", "(")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", "(")] = "q28"
    
    transition_table[("q0", ")")] = "q28"
    transition_table[("q28", " ")] = "q29"
    transition_table[("q29", ")")] = "q28"

    #Lexical Analysis
    idx_char = 0
    state = 'q0'
    current_token = ''
    for current_char in input_string:
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state == 'q28':
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
