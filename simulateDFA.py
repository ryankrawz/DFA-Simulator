# Deterministic Finite Automaton Simulator
# Ryan Krawczyk


# Machine = (Q, Sigma, delta, q0, F)
# Receives machine elements and input string as lists
# Generates state trajectory and acceptance/rejection
def simDFA(m, s):
    Q = m[0]
    Sigma = m[1]
    delta = m[2]
    q0 = m[3]
    F = m[4]

    current = q0
    print("\nStart state: " + str(current) + "\n")
    for i in s:
        try:
            current = delta[Q.index(current)][Sigma.index(i)]
            print("Reading " + str(i) + ", transitioning to state " + str(current))
        except:
            print("EXCEPTION: machine alphabet does not contain " + str(i))
            break

    if current in F:    output = "\n" + str(s) + " is accepted\n"
    else:               output = "\n" + str(s) + " is rejected\n"
    print(output)
