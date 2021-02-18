import cirq

q0 = cirq.GridQubit(0, 0)
q1 = cirq.GridQubit(0, 1)

circuit = cirq.Circuit.from_ops([q0, q1])

print(circuit)
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=8)
print(result)
