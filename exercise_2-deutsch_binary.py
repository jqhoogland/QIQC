import cirq

def deutsch(oracle, qubit1, qubit2):
    circuit = cirq.Circuit()

    # +------------------------+
    # |Type your solution below|
    # +------------------------+

    qs = [qubit1, qubit2]
    H = lambda i: cirq.H(qs[i])
    X = lambda i: cirq.X(qs[i])

    circuit.append(X(1))
    circuit.append([H(i) for i in [0, 1]])
    circuit.append(oracle.all_operations())
    circuit.append(H(0))
    circuit.append([cirq.measure(qubit1, key="d")])

    # +------------------------+
    # |Type your solution above|
    # +------------------------+

    return circuit

if __name__ == "__main__":
    qubit1 = cirq.GridQubit(0,0)
    qubit2 = cirq.GridQubit(0,1)
    oracle = cirq.Circuit()
    oracle.append(cirq.CNOT(qubit1, qubit2))  # This implements the function f(x) = x. Comment if you want to test with the function f(x) = 0 instead.
    circuit = deutsch(oracle, qubit1, qubit2)
    res = cirq.Simulator().run(circuit, repetitions = 20)
    print_circuit = lambda circuit : "  " + (str(circuit).replace('\n','\n  ') if len(circuit) > 0 else "<<This circuit contains no gates.>>")
    print("We are testing your circuit on the function f(x) = x.")
    print("The oracle looks like this:")
    print()
    print(print_circuit(oracle))
    print()
    print("The current circuit you implemented is:")
    print()
    print(print_circuit(circuit))
    print()
    print("If you implemented Deutsch's algorithm correctly, we should obtain the following measurement outcomes:")
    print()
    print("  d={}".format('1'*20))
    print()
    print("The actual outcome is:")
    print()
    print("  " + (str(res).replace('\n','\n  ') if len(res.measurements) > 0 else "<<There were no measurements.>>"))
    print()
