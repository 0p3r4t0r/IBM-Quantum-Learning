# Custom code to safely load token
from dotenv import dotenv_values

env = dotenv_values(".env")
token = env["IBM_QUANTUM_PLATFORM_API_KEY"]


# Example from: https://docs.quantum.ibm.com/guides/setup-channel
 
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

# Create empty circuit
example_circuit = QuantumCircuit(2)
example_circuit.measure_all()

service = QiskitRuntimeService(channel="ibm_quantum", token=token)
backend = service.least_busy(operational=True, simulator=False)

sampler = Sampler(backend)
job = sampler.run([example_circuit])
print(f"job id: {job.job_id()}")
result = job.result()
print(result)