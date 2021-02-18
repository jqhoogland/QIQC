import collections, argparse
import numpy as np
import cirq
from matplotlib import pyplot as plt
from matplotlib import animation
from tqdm import tqdm

class Step(cirq.Gate):
    def __init__(self, num_qubits):
        super(Step, self)
        self._num_qubits = num_qubits

    def num_qubits(self):
        return  self._num_qubits

    def _unitary_(self):
        # ups = np.array([[1, 1], [1, 1]])
        # downs = np.array([[1, -1], [-1, 1]])

        ups = np.array([[1, 0], [0, 0]])
        downs = np.array([[0, 0], [0, 1]])

        n_states = 2 ** (self._num_qubits -1)
        plus_one = np.eye(n_states, k=1)
        plus_one[n_states - 1, 0] = 1

        minus_one = np.eye(n_states, k=-1)
        minus_one[0, n_states - 1] = 1

        # print("ups\n{}\n downs\n{}\n plus one\n{}\n  minus one\n{}\n ".format(ups, downs, plus_one, minus_one))

        res = (np.kron(ups, plus_one) + np.kron(downs, minus_one)) / 2
        # print(res)
        return res


class Walk(cirq.Gate):
    def __init__(self, num_qubits):
        super(Walk, self)
        self._num_qubits = num_qubits

    def __repr__(self):
        return "Walk"

    def num_qubits(self):
        return  self._num_qubits

    def _decompose_(self, qubits):
        yield cirq.H(qubits[0])
        yield Step(self._num_qubits).on(*qubits)

 def quantum_walk(step_qubit, register_qubits, n_steps, start_in_plus=True, start_in_both_parities=False):
    circuit = cirq.Circuit()

    if start_in_plus:
        circuit.append(cirq.H(step_qubit))
        circuit.append(cirq.S(step_qubit))

    if start_in_both_parities:
        circuit.append(cirq.H(register_qubits[-1]))

    num_register = len(register_qubits)
    num_qubits = num_register + 1

    for i in range(n_steps):
        circuit.append(Walk(num_qubits).on(step_qubit, *register_qubits))

    for q in register_qubits:
        circuit.append(cirq.measure(q))

    return circuit

def measurements_to_decimal(vals, n_measurements):
    results = []
    qubits = sorted(vals.keys())
    for i in range(n_measurements):
        bitstring = ""

        for q in qubits:
            bitstring += str(int(vals[q][i][0]))

        results.append(int(bitstring, 2))

    return results

def measurements_to_freq(vals, n_measurements):
    decimal_measurements = measurements_to_decimal(vals, n_measurements)
    return dict(zip(*np.unique(decimal_measurements, return_counts=True)))


def draw_freq_plot(vals, n_measurements):
    freq_dict = measurements_to_freq(vals, n_measurements)

    plt.bar(freq_dict.keys(), freq_dict.values())
    plt.show()

def animate(data):
    fig = plt.figure()

    def update_hist(i, data):
        plt.cla()
        plt.hist(data[i], bins=64, range=(0, 64))

    anim = animation.FuncAnimation(fig, update_hist, fargs=(data, ),
                                   frames=len(data), interval=100)
    #plt.show()
    FFwriter=animation.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
    anim.save("quantum_walk.mp4", writer = FFwriter)


parser = argparse.Parser()

parser.add()

if __name__ == "__main__":
    n_register = 6
    n_steps = 1000
    n_measurements = 1000
    control = cirq.GridQubit(0,0)
    register_qubits = [cirq.GridQubit(0,i) for i in range(1, n_register + 1)]

    freqs = []

    for i in tqdm(range(0, n_steps, 1)):
        circuit = quantum_walk(control, register_qubits, i, start_in_both_parities=False)
        res = cirq.Simulator().run(circuit, repetitions = n_measurements)

        # print(("1) The current circuit you implemented is:\n{} \n " +
        #        "We measured the results:\n{}")
        #       .format(str(circuit).replace('\n','\n  '),
        #               res))

        freqs.append(measurements_to_decimal(res.measurements, n_measurements))

    animate(freqs)
