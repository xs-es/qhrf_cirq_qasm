import math
from qiskit import QuantumCircuit
from qiskit.qasm2 import dumps
from qhrf_opt import qhrf_optimize
from cirq.contrib.qasm_import import circuit_from_qasm
import cirq

def rewrite_qasm(qasm_str: str) -> str:
    qasm_str = qasm_str.replace("rzz", "// rzz removed for manual handling")
    qasm_str = qasm_str.replace("sx", "u2(0,pi)")  # map sx → u2
    # Remove any lines with 'barrier'
    qasm_str = "\n".join(
        line for line in qasm_str.splitlines()
        if not line.strip().startswith("barrier")
    )
    return qasm_str


# Step 1: Build the Qiskit circuit
qc = QuantumCircuit(2)

# Replace u() with rz-ry-rz decomposition
theta, phi, lam = math.pi / 2, math.pi / 2, math.pi / 2
qc.rz(phi, 0)
qc.ry(theta, 0)
qc.rz(lam, 0)

qc.sx(1)  # will be rewritten to u2(0, pi)
qc.measure_all()

# Step 2: Export to QASM using Qiskit 1.x-compatible API
qasm_code = dumps(qc)

# Step 3: Rewrite unsupported gates
patched_qasm = rewrite_qasm(qasm_code)

# Step 4: Import into Cirq
cirq_circuit = circuit_from_qasm(patched_qasm)

# Step 5: QHRF optimizer (placeholder)
qhrf_circuit = qhrf_optimize(cirq_circuit)

# Step 6: Simulate
simulator = cirq.Simulator()
result = simulator.run(qhrf_circuit, repetitions=1000)

# Output
print("Optimized Circuit:\n", qhrf_circuit)
print("\nMeasurement Results:\n", result)
