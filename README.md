# QHRF-CIRQ-QASM-001

## 🔭 Overview

This repository bridges **Qiskit → OpenQASM 2.0 → Cirq** using a gate rewrite strategy to support non-native gates (`u`, `sx`, `rzz`, etc.) and includes a placeholder for a **Quantum Harmonic Resonance Framework (QHRF)** optimizer pass. It was built for the UnitaryHack 2025 bounty: [Support more OpenQASM 2.0 gates from qelib1.inc](https://github.com/quantumlib/Cirq/issues/7072).

---

## 🚀 Setup Instructions

### 1. Clone and Activate Environment

```bash
git clone https://github.com/xs-es/qhrf_cirq_qasm
cd qhrf_cirq_qasm
python -m venv .venv
source .venv/bin/activate  # or .\.venv\Scripts\activate on Windows
```

### 2. Install Dependencies

```bash
pip install qiskit cirq numpy
```

### 3. Run the Pipeline

```bash
python test_pipeline.py
```

---

## 🥪 Details

This script:

* Builds a Qiskit circuit with gates not natively supported by Cirq
* Converts the circuit to OpenQASM 2.0
* Rewrites QASM to eliminate unsupported operations (e.g., `u`, `barrier`, `rzz`)
* Imports it into Cirq using `circuit_from_qasm`
* Passes the circuit through a stub QHRF optimizer
* Simulates and measures the result in Cirq

---

## 🆕️ Newly Supported Gates

This project implements parsing support for the following QASM gates:

| Gate    | Cirq Mapping                   |
| ------- | ------------------------------ |
| `rzz`   | `cirq.ZZPowGate`               |
| `rxx`   | `cirq.XXPowGate`               |
| `ryy`   | `cirq.YYPowGate`               |
| `crx`   | `cirq.ControlledGate(cirq.rx)` |
| `cry`   | `cirq.ControlledGate(cirq.ry)` |
| `iswap` | `cirq.ISwapPowGate`            |

> These are rewritten in a QASM-compatible format and imported cleanly via `circuit_from_qasm`.

---

## 📂 Project Structure

```
qhrf_cirq_qasm/
├── test_pipeline.py     # Main Qiskit → Cirq → QHRF workflow
├── qhrf_opt.py          # QHRF optimizer stub (placeholder)
├── README.md            # Documentation (this file)
├── LICENSE              # Apache 2.0 License
```

---

## 🧠 Metadata

* 🥪 Experiment ID: `QHRF-CIRQ-QASM-001`
* 👤 Author: Zachary L. Musselwhite
* 📧 Email: [Xses.Science@gmail.com](mailto:Xses.Science@gmail.com)
* 🧠 QHRF Inventions: [See full list](https://chat.openai.com/share/77e3532d-071f-4560-b6de-22b331dca631)

---

## 📜 License

This project is licensed under the **Apache 2.0 License**.
See [`LICENSE`](./LICENSE) for details.

---

## 🙌 Contribution

This project was submitted for UnitaryHack 2025.
Feel free to fork and build QHRF-aware quantum compilation tools on top of this pipeline.
