---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(hw1_solution)=

# Задание 1. Кубиты, гейты. Решение

[Ссылка на тест](https://ods.ai/tracks/qmlcourse/blocks/de5e69c5-dbca-49d0-bf4e-048f61829fd8).

_Замечания:_
 - _Правильные варианты ответа помечены значком [x]_
 - Часть решений не была набрана в $\LaTeX$, вместо этого приводятся скриншоты рукописей @yorko (надеемся, читаемые)

**1\. Чему равно скалярное произведение $\left\langle a\middle| b\right\rangle$ векторов $\ket{a}$ и $\ket{b}$ (в [bra-ket нотации](https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation)):**

$$\ket{a} = \begin{bmatrix} 2 - i \\ 3 + i  \end{bmatrix} \quad \ket{b} = \begin{bmatrix} i \\ 1 - i \end{bmatrix}$$

- $5$
- $1 + 2i$
- [x] $1 - 2i$
- $3 - i$

**Решение:**

$\left\langle a\middle| b\right\rangle = a^{\intercal^\ast} \cdot b = \begin{bmatrix} 2 + i & 3 - i  \end{bmatrix} \cdot \begin{bmatrix} i \\ 1 - i \end{bmatrix} = (2 + i)i + (3 - i)(1 - i) = 1 - 2i$

<!-- ```{figure} /_static/qcblock/hw1_qcblock_solution/qmlcourse_hw1_q1-4_solution_yorko-0.png
:width: 600px
:name: qmlcourse_hw1_q1-4_solution_yorko-0
``` -->

**2\. Укажите все верные варианты ответа для задачи нахождения собственных значений и собственных векторов оператора Паули  $\hat{\sigma^y} = \begin{bmatrix} 0 & -i\\ i & 0 \end{bmatrix}$:**

- Собственные значения: 0 и 1, собственные вектора: $\begin{bmatrix} 1  \\ 0 \end{bmatrix}$ и $\begin{bmatrix} i  \\ 1 \end{bmatrix}$
- [x]  Собственные значения: 1 и -1, собственные вектора: $\begin{bmatrix} 1  \\ i \end{bmatrix}$ и $\begin{bmatrix} i  \\ 1 \end{bmatrix}$
- Собственные значения: 0 и 1, собственные вектора: $\begin{bmatrix} i  \\ 0 \end{bmatrix}$ и $\begin{bmatrix} 0 \\ i \end{bmatrix}$
- [x]  Собственные значения: -1 и 1, собственные вектора: $\begin{bmatrix} -i  \\ 1 \end{bmatrix}$ и $  \begin{bmatrix} 1  \\ -i \end{bmatrix}$


**Решение:**

```{figure} /_static/qcblock/hw1_qcblock_solution/qmlcourse_hw1_q1-4_solution_yorko-1.png
:width: 600px
:name: qmlcourse_hw1_q1-4_solution_yorko-1
```

**3\. Выберите все верные утверждения:**

- [x] Мат ожидание измерения оператора $\hat{\sigma^y} $ для состояния $\ket{R}$ равно 1  
- [x] Собственные значения оператора Адамара – те же, что у операторов Паули
- [x] Собственные вектора phase-shift гейта $\hat{U_1} (\phi)$ – $\ket{0}$ и $\ket{1}$
- [x] Для $|\alpha|  > |\beta|$ кубит в состоянии $\begin{bmatrix} \alpha  \\ \beta \end{bmatrix}$ при измерении скорее окажется в состоянии $\ket{0}$

**Решение:**

```{figure} /_static/qcblock/hw1_qcblock_solution/qmlcourse_hw1_q1-4_solution_yorko-2.png
:width: 500px
:name: qmlcourse_hw1_q1-4_solution_yorko-2
```

```{figure} /_static/qcblock/hw1_qcblock_solution/qmlcourse_hw1_q1-4_solution_yorko-3.png
:width: 500px
:name: qmlcourse_hw1_q1-4_solution_yorko-3
```

**4\. Выберите все верные утверждения:**
- T-гейт – это то же, что phase-shift гейт $\hat{U}_1 (\phi)$ с параметром $\phi = \pi/2$
- [x] Если вектор состояния $\ket{1}$ повернуть на угол $\frac{\pi}{2}$ с помощью оператора $\hat{RX}(\phi)$, то при измерении по оси $Y$ получится состояние $\ket{R}$
- [x] Любой поворот кубита вокруг любой оси на угол $2\pi k, k \in \mathbb{Z}$ не меняет состояние кубита
- Любой поворот кубита вокруг любой оси на любой угол не меняет вероятностей состояний при измерении кубита

**Решение:**

```{figure} /_static/qcblock/hw1_qcblock_solution/qmlcourse_hw1_q1-4_solution_yorko-4.png
:width: 500px
:name: qmlcourse_hw1_q1-4_solution_yorko-4
```

```{figure} /_static/qcblock/hw1_qcblock_solution/qmlcourse_hw1_q1-4_solution_yorko-5.png
:width: 500px
:name: qmlcourse_hw1_q1-4_solution_yorko-5
```

**5\. Какая из последовательностей гейтов идентична единичному гейту $ \sigma^x $?**

- $ \hat{\sigma^z} \hat{H} \hat{\sigma^z} \hat{H} $
- $ \hat{H} \hat{\sigma^z} \hat{\sigma^z} \hat{H}$
- [x] $ \hat{H} \hat{\sigma^z} \hat{H} $
- $ \hat{\sigma^z} \hat{H} \hat{\sigma^z}$

**Решение:**

```{code-cell} ipython3

import numpy as np

pauli_x = np.array([[0 + 0j, 1 + 0j], [1 + 0j, 0 + 0j]])
pauli_z = np.array([[1 + 0j, 0 + 0j], [0 + 0j, 0j - 1]])

h = 1 / np.sqrt(2) * np.array([
    [1 + 0j, 1 + 0j],
    [1 + 0j, 0j - 1]
])

option_1 = pauli_z @ h @ pauli_z @ h
option_2 = h @ pauli_z @ pauli_z @ h
option_3 = h @ pauli_z @ h
option_4 = pauli_z @ h @ pauli_z

print(np.allclose(option_1, pauli_x),
      np.allclose(option_2, pauli_x),
      np.allclose(option_3, pauli_x),
      np.allclose(option_4, pauli_x))
```

**6 \. Чему равна вероятность получения битовой строки $10$  при измерении в $ \mathbf{Z}$-базисе состояния: $\large (\hat{H} \otimes \hat{I})\ \hat{CNOT}\ (\hat{I} \otimes \hat{RY}(0.7)) \ket{0} \otimes \ket{0})$:**

_Считаем, что по умолчанию углы измеряются в радианах._

- 0.05879
- [x] 0.44121
- 0.66423
- 0.24246

**Решение:**

```{code-cell} ipython3

def ry(state, phi):
    return np.array([
        [np.cos(phi / 2), -np.sin(phi / 2)],
        [np.sin(phi / 2),  np.cos(phi / 2)]
    ]) @ state

cnot = (1 + 0j) * np.array(
    [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
    ]
)

basis = np.array([1 + 0j, 0 + 0j]).reshape((2, 1))
op = np.kron(h, np.eye(2)) @ cnot @ np.kron(np.eye(2), ry(np.eye(2), 0.7))
init_state = np.kron(basis, basis)

final_state = op @ init_state

# Вероятность получения битовой строки 10 равно квадрату третьего элемента
# вектора финального состояния
# (строка 10 – третья в лексикографическом порядке 00, 01, 10, 11).
print(final_state[2].conj() * final_state[2])
```


**7 \. Реализуйте поворот вектора состояния $\ket{0}$ на угол $ \frac{\pi}{2}$  с помощью оператора $\hat{RX}(\phi)$:**
 - на `NumPy`
 - на `PennyLane`

Для этого изучите примеры из лекции: [на Numpy](https://semyonsinchenko.github.io/qmlcourse/_build/html/book/qcblock/gates.html#numpy) и [на PennyLane](https://semyonsinchenko.github.io/qmlcourse/_build/html/book/qcblock/gates.html#id16). Учтите, что в лекции пример с двумя кубитами, а в этом вопросе – проще, с одним.

Найдите [ожидаемые значения при измерении](https://semyonsinchenko.github.io/qmlcourse/_build/html/book/qcblock/qubit.html#id28) кубита по осям $\mathbf{X}$, $\mathbf{Y}$, и $\mathbf{Z}$.

- 0 – по $\mathbf{X}$, 1 – по $\mathbf{Y}$, 0 – по $\mathbf{Z}$
- -1 – по $\mathbf{X}$, 0 – по $\mathbf{Y}$, 0 – по $\mathbf{Z}$
- [x] 0 – по $\mathbf{X}$, -1 – по $\mathbf{Y}$, 0 – по $\mathbf{Z}$
- 0 – по $\mathbf{X}$, 0.70710678 – по $\mathbf{Y}$, 0 – по $\mathbf{Z}$

**Решение:**


На `NumPy`

```{code-cell} ipython3
import numpy as np

def rx(state, phi):
    return np.array([
         [np.cos(phi / 2), -1j * np.sin(phi / 2)],
         [-1j * np.sin(phi / 2),  np.cos(phi / 2)]
    ]) @ state

pauli_y = np.array([[0 + 0j, 0 - 1j], [0 + 1j, 0 + 0j]])

state = np.array([1 + 0j, 0 + 0j]).reshape((2, 1))
op = rx(state, np.deg2rad(90))

# Результаты близки к 0, -1, 0
print(op.conj().T @ pauli_x @ op, op.conj().T @ pauli_y @ op, op.conj().T @ pauli_z @ op)
```

Теперь на `PennyLane`

```{code-cell} ipython3
import pennylane as qml
import pennylane.numpy as np

device = qml.device("default.qubit", 1)

@qml.qnode(device)
def test_x(angle):
    qml.RX(angle, wires=0)
    return qml.expval(qml.PauliX(0))

@qml.qnode(device)
def test_y(angle):
    qml.RX(angle, wires=0)
    return qml.expval(qml.PauliY(0))

@qml.qnode(device)
def test_z(angle):
    qml.RX(angle, wires=0)
    return qml.expval(qml.PauliZ(0))

# Результаты близки к 0, -1, 0
print(test_x(np.deg2rad(90)))
print(test_y(np.deg2rad(90)))
print(test_z(np.deg2rad(90)))
```
