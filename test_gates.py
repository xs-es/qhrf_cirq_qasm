import math
from qiskit import QuantumCircuit
from qiskit.qasm2 import dumps
from qhrf_opt import qhrf_optimize
from cirq.contrib.qasm_import import circuit_from_qasm
import cirq

def rewrite_qasm(qasm: str) -> str:
    from re import sub

    lines = qasm.splitlines()
    new_lines = []
    for line in lines:
        if any(gate in line for gate in ["rzz", "barrier"]):
            continue  # Remove unsupported lines entirely
        line = line.replace("u3", "u")
        line = line.replace("sx", "u2(0,pi)")
        # Replace crx and cry with comments (or define these later as decompositions)
        if "crx" in line or "cry" in line:
            new_lines.append(f"// {line}  <-- unsupported gate removed")
            continue
        # Replace iswap with comment as well
        if "iswap" in line:
            new_lines.append(f"// {line}  <-- unsupported gate removed")
            continue
        new_lines.append(line)
    return "\n".join(new_lines)



qc = QuantumCircuit(2)
qc.rx(math.pi/2, 0)
qc.ry(math.pi/2, 1)
qc.rzz(math.pi, 0, 1)
qc.sx(0)
qc.crx(math.pi/3, 0, 1)
qc.cry(math.pi/5, 1, 0)
qc.iswap(0, 1)
qc.measure_all()

qasm_code = dumps(qc)
patched_qasm = rewrite_qasm(qasm_code)
cirq_circuit = circuit_from_qasm(patched_qasm)
qhrf_circuit = qhrf_optimize(cirq_circuit)

print("QHRF Optimized Circuit:\n", qhrf_circuit)

sim = cirq.Simulator()
result = sim.run(qhrf_circuit, repetitions=100)
print("\nMeasurement Results:")
print(result)
