(progreview)=

# Обзор фреймворков для квантовых вычислений

В этом обзоре мы кратко пробежимся по существующим сегодня фреймворкам для программирования квантовых компьютеров, а также по тем компьютерам, с которыми они совместимы.

```{note}
Цель этой лекции -- исключительно показать как визуально выглядит тот, или иной фреймворк для программирования квантовых компьютеров. Поэтому не стоит пытаться вникнуть и понять, что именно делает тот, или иной пример приведенного тут кода! Также хочется сразу сказать, что разделение на низкоуровневые и высокоуровневые языки квантового относительно субъективно и эта лекция выражает именно точку зрения ее автора.
```

## Квантовые ассемблеры

### OpenQASM

В нашем курсе мы в основном будем пользоваться относительно высокоуровневые фреймворки. Однако это не значит, что квантовый программист не имеет возможности программировать на низком уровне. Например, компания `IBM` дает доступ к своему квантовому ассемблеру [OpenQASM](https://github.com/QISKit/openqasm) {cite}`qasm2017`, код на котором выглядит примерно так:

```c
/* Measuring the relaxation time of a qubit
 * This example demonstrates the repeated use of fixed delays.
*/
OPENQASM 3.0;
include "stdgates.inc";

duration stride = 1us;            // time resolution of points taken
const int[32] points = 50;              // number of points taken
const int[32] shots = 1000;             // how many shots per point

int[32] counts0;
int[32] counts1 = 0;   // surviving |1> populations of qubits

extern tabulate(int[32], int[32], int[32]);

bit c0;
bit c1;

defcalgrammar "openpulse";

// define a gate calibration for an X gate on any qubit
defcal x $q {
   play drive($q), gaussian(100, 30, 5);
}

for p in [0 : points-1] {
    for i in [1 : shots] {
        // start of a basic block
        reset $0;
        reset $1;
        // excite qubits
        x $0;
        x $1;
        // wait for a fixed time indicated by loop counter
        delay[p * stride] $0;
        // wait for a fixed time indicated by loop counters
        delay[p * durationof({x $1;})];
        // read out qubit states
        c0 = measure $0;
        c1 = measure $1;
        // increment counts memories, if a 1 is seen
        counts0 += int[1](c0);
        counts1 += int[1](c1);
    }
    // log survival probability curve
    tabulate(counts0, shots, p);
    tabulate(counts1, shots, p);
}
```

Пример этого кода [взят](https://github.com/Qiskit/openqasm/blob/master/examples/t1.qasm) из официального репозитория.

### PyQuil

Другим примером относительно низкоуровневого языка квантового программирования является фреймворк [PyQuil](https://github.com/rigetti/pyquil) {cite}`pyquil2017`. Он разработан компанией `Rigetti Computing`, производителем одноименных квантовых компьютеров и включает в себя компилятор и виртуальную машину `QVM`. Вот так выглядит код на этом фреймворке:

```python3
from pyquil import get_qc, Program
from pyquil.gates import CNOT, H, MEASURE

qvm = get_qc('2q-qvm')

p = Program()
p += H(0)
p += CNOT(0, 1)
ro = p.declare('ro', 'BIT', 2)
p += MEASURE(0, ro[0])
p += MEASURE(1, ro[1])
p.wrap_in_numshots_loop(10)

qvm.run(p).readout_data['ro'].tolist()
```

Пример взят из официального репозитория.

## Высокоуровневое программирование

В таких фреймворках программист имеет возможность уже не только напрямую манипулировать кубитами на низком уровне, но также вызывать высокоуровневые функции, например, [квантовое преобразование Фурье](https://quantumai.google/reference/python/cirq/ops/QuantumFourierTransformGate).

### Cirq

Одним из таких фреймворков является `Cirq` от компании `Google`. Код, написанный на нем можно запускать на симуляторах локально или в облаке, а также используя специально разработанные компанией `Google` симуляторы на базе **T**ensor **P**rocessing **U**nits или **TPU** используя `Floq API`. Для целей квантового машинного обучения в связке с `Cirq` можно использовать `Tensorflow Quantum` -- расширение библиотеки для обычного _Deep Leanring_, которое позволяет комбинировать классические и квантовые нейронные сети вместе. Еще в экосистему `Cirq` входит также библиотека для квантовой химии [`OpenFermion`](https://github.com/quantumlib/OpenFermion).


Вот так выглядит код, написанный на `Cirq`:

```python3
import cirq
qubit = cirq.GridQubit(0, 0)

circuit = cirq.Circuit()
circuit.append(cirq.H(qubit))
circuit.append(cirq.measure(qubit))
print(circuit)
```

Еще больше примеров и более детальный обзор этого фреймворка читайте в [нашей статье про `Tensorflow Quantum`](cirq-tfq). Также очень рекомендуем ознакомиться с [блогом](https://quantumai.google/) "квантового" подразделения компании `Google` -- _Google Quantum AI_.

### Q#

`Q#` это полноценный язык квантового программирования от компании `Microsoft`. Этот техногигант также, как и другие, разрабатывает сейчас свои квантовые компьютеры и облачные симуляторы, а также предоставляет облачный доступ к квантовому железу других производителей. Так что программы, написанные на `Q#` можно запускать в облаке [Azure Quantum](https://azure.microsoft.com/en-us/services/quantum/).

В отличии от большинства фреймворков, которые обычно написаны как библиотека для языка `Python`, `Q#` использует `C#` для запуска и в целом имеет синтаксис, больше похожий на `C#` или `Java`:

```c#
namespace QuantumRNG {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Canon;

    @EntryPoint()
    operation GenerateRandomBits() : Result[] {
        use qubits = Qubit[4];
        ApplyToEach(H, qubits);
        return MultiM(qubits);
    }
}
```

Этот пример взят из [официальной документации](https://docs.microsoft.com/en-us/azure/quantum/quickstart-microsoft-qc?view=qsharp-preview&pivots=platform-ionq).

На самом деле `Q#` это не просто язык для программирования квантовых компьютеров, а целая экосистема, в которую кроме самого языка и его стандартной библиотеки также входят:

- Библиотека [Microsoft.Quantum.Chemistry](https://docs.microsoft.com/en-us/azure/quantum/user-guide/libraries/chemistry/?view=qsharp-preview) для квантовой химии
- Библиотека [Microsoft.Quantum.MachineLearning](https://docs.microsoft.com/en-us/azure/quantum/user-guide/libraries/machine-learning/intro?view=qsharp-preview) для квантового машинного обучения

В качестве отличного источника информации про квантовые вычисления с примерами на `Q#`-стеке можно использовать потрясающий репозиторий на `GitHub`, который называется [QuantumKatas](https://github.com/microsoft/QuantumKatas).

### Strawberry-Fields

[`Strawberry-Fields`](https://github.com/XanaduAI/strawberryfields) это библиотека для работы с фотонными квантовыми компьютерами компании `Xanadu`. Эти устройства являются _continuous-variable quantum computers_ и в их основе лежат не бинарные состояния -- кубиты, а состояния с непрерывными значениями. Учитывая сложность этого концепта, а также специфичность решаемых на таких устройствах задач мы мало будем о них говорить, но любопытный читатель может ознакомиться, например, с [этой статьей](https://en.wikipedia.org/wiki/Continuous-variable_quantum_information).

Вот так выглядит код, написанный с использованием этого фреймворка (пример из [официальной документации](https://strawberryfields.readthedocs.io/en/stable/introduction/circuits.html)):

```python3
import strawberryfields as sf
from strawberryfields import ops

# create a 3-mode quantum program
prog = sf.Program(3)

with prog.context as q:
    ops.Sgate(0.54) | q[0]
    ops.Sgate(0.54) | q[1]
    ops.Sgate(0.54) | q[2]
    ops.BSgate(0.43, 0.1) | (q[0], q[2])
    ops.BSgate(0.43, 0.1) | (q[1], q[2])
    ops.MeasureFock() | q
```

Также к `Strawberry-Fields` идет большое число высокоуровневых API для конкретных приложений к задачам реального мира. Например:

- [Вычисление схожести графов](https://strawberryfields.readthedocs.io/en/stable/code/api/strawberryfields.apps.similarity.html)
- [Gaussian Boson Sampling](https://strawberryfields.readthedocs.io/en/stable/code/api/strawberryfields.apps.train.html)
- [Поиск Clique в графах](https://strawberryfields.readthedocs.io/en/stable/code/api/strawberryfields.apps.clique.html)
- [Поиск плотных подграфов](https://strawberryfields.readthedocs.io/en/stable/code/api/strawberryfields.apps.subgraph.html)

И многие другие, с которыми можно ознакомиться на [странице](https://strawberryfields.ai/photonics/applications.html) официальной документации.

### Qiskit

[Qiskit](https://qiskit.org/overview) -- это один из самых популярных в мире фреймворков для квантовых вычислений от компании `IBM`. На самом деле представляет собой даже не фреймворк, а целую экосистему, в которую входят, например:

- Уже [упомянутый нами](../progblock/progreview.html#openqasm) квантовый ассемблер `OpenQASM`
- [Фреймворк](https://github.com/Qiskit/qiskit) для программирования кубитов, написанный на `OpenQASM`
- [API для применения квантовых вычислений в финансах](https://github.com/Qiskit/qiskit-finance)
- [API для применения квантовых вычислений в ML](https://github.com/Qiskit/qiskit-machine-learning)
- [API для применения квантовых вычислений в оптимизации](https://github.com/Qiskit/qiskit-optimization)
- [API для применения квантовых вычислений в квантовой химии](https://github.com/Qiskit/qiskit-nature)
- [Открытый CAD для проектирования квантовых компьютеров (!)](https://github.com/Qiskit/qiskit-metal)

И [многое другое](https://github.com/Qiskit).

Код, написанный на `Qiskit` выглядит так (пример из [официальной документации](https://qiskit.org/documentation/intro_tutorial1.html)):

```python3
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

# Use Aer's qasm_simulator
simulator = QasmSimulator()

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)

# Add a H gate on qubit 0
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])

# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(compiled_circuit)
print("\nTotal count for 00 and 11 are:",counts)

# Draw the circuit
circuit.draw()
```

Код, написанный на `Qiskit` может быть запущен на квантовых компьютерах от компании `IBM.` Для изучения квантовых вычислений с экосистемой `Qsikit` можно рекомендовать [прекрасную онлайн книгу](https://qiskit.org/textbook/what-is-quantum.html). Более подробный обзор библиотеки также [в отдельной лекции нашего курса](qiskit).

### Pennylane

`Pennylane` это относительно высокоуровневая библиотека для квантовых вычислений и квантового машинного обучения от компании `Xanadu`. Вот так выглядит написанный на ней код:

```python3
import pennylane as qml
from pennylane import numpy as np

dev = qml.device('default.qubit', shots=1000, wires=2)

def make_entanglement():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.probs(wires=[0, 1])

circuit = qml.QNode(make_entanglement, dev)
circuit()
```

Эта библиотека может использовать в качестве backend любое из:

- `Cirq`
- `Qiskit`
- `Q#`
- `Strawberry-Fields`
- `PyQuil` (через расширение [Pennylane-Forest](https://github.com/PennyLaneAI/pennylane-forest))

Но для нас самое главное преимущество этой библиотеки -- это огромное количество готовых API для машинного обучения, которые позволяют автоматически считать градиенты и дифференцировать квантовые схемы, или обновлять параметры таких схем градиентным спуском.

В нашем курсе библиотеке `Pennylane` посвящена [целая отдельная лекций](pennylane).

## Заключение

### Что мы будем использовать в курсе?

В рамках нашего курса мы в основном будем пользоваться библиотекой `Pennylane`. Некоторые отдельные лекции будут использовать `Qiskit`, но это скорее в порядке исключения.

### Почему Pennylane?

Но почему `Pennylane`, если самым популярным фреймворком является именно `Qiskit`? Приведем два основных аргумента.

1. Сегодня трудно сказать, какое квантовое железо в итоге победит, а большим преимуществом `Pennylane` является то, что эта библиотека является верхнеуровневой и может использовать различные backend для запуска на квантовых компьютерах разных производителей. Включая `Qsikit` и `IBM`.
2. Наш курс больше про квантовое машинное обучение и именно для этих целей `Pennylane` подходит лучше всего. Там есть рутины и API разных уровней, позволяющих где-то самому писать градиенты квантовых схем и обновлять их параметры, а где-то просто вызывать готовый метод из `API`, чтобы не повторять 10 раз то, что мы уже разбирали в более ранних лекциях.
