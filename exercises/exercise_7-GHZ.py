import cirq

def create_GHZ_state(qubits):
    # +------------------------+
    # |Type your solution below|
    # +------------------------+

    circuit = cirq.Circuit([cirq.Moment([cirq.H(qubits[0])]),
                            *[cirq.Moment([cirq.CNOT(qubits[0], q)]) for q in qubits[1:]]])

    # +------------------------+
    # |Type your solution above|
    # +------------------------+

    return circuit

if __name__ == "__main__":
    qubits = [cirq.GridQubit(0,i) for i in range(4)]
    construction_circuit = create_GHZ_state(qubits)
    circuit = construction_circuit.copy()
    circuit.append([cirq.measure(q, key = 'qubit{}'.format(i)) for i,q in enumerate(qubits)])
    res = cirq.Simulator().run(circuit, repetitions=50)
    print_circuit = lambda circuit : "  " + (str(circuit).replace('\n','\n  ') if len(circuit) > 0 else "<<This circuit contains no gates.>>")
    print("The circuit you implemented is:")
    print()
    print(print_circuit(construction_circuit))
    print()
    print("We will measure all of the final qubits, so the total circuit becomes:")
    print()
    print(print_circuit(circuit))
    print()
    print("The measurement results should be completely correlated, i.e., all entries in the same column must be the same. Moreover, the distribution of 0's and 1's should be roughly 50/50.")
    print()
    print("  " + (str(res).replace('\n','\n  ') if len(res.measurements) > 0 else "<<There were no measurements.>>"))
    print()
