import cirq
import numpy as np
from cirq.contrib.qasm_import import QasmParser

def register_custom_gates():
    def u3(args, qubits):
        theta, phi, lam = args
        q = qubits[0]
        u = cirq.unitary(cirq.rz(lam)) @ cirq.unitary(cirq.ry(theta)) @ cirq.unitary(cirq.rz(phi))
        return [cirq.MatrixGate(u)(q)]

    def rzz(args, qubits):
        theta = args[0]
        q0, q1 = qubits
        return [cirq.ZZPowGate(exponent=theta / np.pi)(q0, q1)]

    def sx(args, qubits):
        return [cirq.X(qubits[0]) ** 0.5]

    # Monkey-patch Cirq's QasmParser
    QasmParser.gate_parsers.update({
        'u3': u3,
        'rzz': rzz,
        'sx': sx
    })
