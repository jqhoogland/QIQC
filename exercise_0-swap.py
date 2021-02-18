import cirq

def swap(qubit1, qubit2):
    circuit = cirq.Circuit()

    # +------------------------+
    # |Type your solution below|
    # +------------------------+

    circuit.append(cirq.CNOT(qubit1, qubit2))
    circuit.append(cirq.CNOT(qubit2, qubit1))
    circuit.append(cirq.CNOT(qubit1, qubit2))

    # +------------------------+
    # |Type your solution above|
    # +------------------------+

    return circuit

if __name__ == "__main__":
    qubit1 = cirq.GridQubit(0,0)
    qubit2 = cirq.GridQubit(0,1)
    swap_circuit = swap(qubit1, qubit2)
    circuit = cirq.Circuit()
    circuit.append(cirq.X(qubit2))
    circuit.append(swap_circuit.all_operations())
    circuit.append([cirq.measure(qubit1, key = 'a'), cirq.measure(qubit2, key = 'b')])
    res = cirq.Simulator().run(circuit, repetitions = 20)
    print("The current circuit you implemented is:")
    print()
    print("  " + (str(swap_circuit).replace('\n','\n  ') if len(swap_circuit) > 0 else "<<This circuit contains no gates.>>"))
    print()
    print("The input to the swap circuit was a = 0 and b = 1.")
    print("If the swap circuit is correctly implemented, we should obtain the following measurement outcomes:")
    print()
    print("  a={}".format('1'*20))
    print("  b={}".format('0'*20))
    print()
    print("The actual outcome is:")
    print()
    print("  " + str(res).replace('\n','\n  '))
    print()
