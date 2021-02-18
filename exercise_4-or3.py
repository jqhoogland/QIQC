import cirq

def or3(cq1, cq2, cq3, tq):
    # +------------------------+
    # |Type your solution below|
    # +------------------------+
    qs = [cq1, cq2, cq3, tq]
    ccx = lambda c1, c2, t: cirq.Moment([cirq.TOFFOLI(qs[c1], qs[c2], qs[t])])
    cx = lambda c, t: cirq.Moment([cirq.CNOT(qs[c], qs[t])])
    x = lambda t: cirq.Moment([cirq.X(qs[x])])
    xs = lambda ts: cirq.Moment([cirq.X(qs[i]) for i in ts])

    circuit = cirq.Circuit([ xs([1, 2]),
                             ccx(0, 1, 2),
                             cx(2, 3),
                             ccx(0, 1, 2),
                             xs([1, 2])])

    # +------------------------+
    # |Type your solution above|
    # +------------------------+

    return circuit

if __name__ == "__main__":
    cq1 = cirq.GridQubit(0,0)
    cq2 = cirq.GridQubit(0,1)
    cq3 = cirq.GridQubit(0,2)
    tq = cirq.GridQubit(0,3)
    circuit = cirq.Circuit()
    or3_circuit = or3(cq1, cq2, cq3, tq)
    circuit.append([cirq.X(cq1), cirq.X(cq3)])
    circuit.append(or3_circuit.all_operations())
    circuit.append([cirq.measure(cq1, key = 'x1'), cirq.measure(cq2, key = 'x2'), cirq.measure(cq3, key = 'x3'), cirq.measure(tq, key = 'x4')])
    res = cirq.Simulator().run(circuit, repetitions = 20)
    print_circuit = lambda circuit : "  " + (str(circuit).replace('\n','\n  ') if len(circuit) > 0 else "<<This circuit contains no gates.>>")
    print("We are testing your circuit on the input x1 = 1, x2 = 0, x3 = 1.")
    print("Your circuit looks like this:")
    print()
    print(print_circuit(or3_circuit))
    print()
    print("The complete circuit looks like this:")
    print()
    print(print_circuit(circuit))
    print()
    print("If you implemented the or3 circuit correctly, we should obtain the following measurement outcomes:")
    print()
    print("  x1={}".format('1'*20))
    print("  x2={}".format('0'*20))
    print("  x3={}".format('1'*20))
    print("  x4={}".format('1'*20))
    print()
    print("The actual outcome is:")
    print()
    print("  " + (str(res).replace('\n','\n  ') if len(res.measurements) > 0 else "<<There were no measurements.>>"))
    print()
