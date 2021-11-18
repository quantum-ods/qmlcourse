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
 - _Правильные варианты ответа помечены значком [x]._

**1\. Чему равно скалярное произведение $\left\langle a\middle| b\right\rangle$ векторов $\ket{a}$ и $\ket{b}$ (в [bra-ket нотации](https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation))?**

$$\ket{a} = \begin{bmatrix} 2 - i \\ 3 + i  \end{bmatrix}, \quad \ket{b} = \begin{bmatrix} i \\ 1 - i \end{bmatrix}$$

- $5$;
- $1 + 2i$;
- [x] $1 - 2i$;
- $3 - i$.

**Решение:**

$\left\langle a\middle| b\right\rangle = a^{T^\ast} \cdot b = \begin{bmatrix} 2 + i & 3 - i \end{bmatrix} \cdot \begin{bmatrix} i \\ 1 - i \end{bmatrix} = (2 + i)i + (3 - i)(1 - i) = 1 - 2i$

**Решение на `NumPy`:**

```{code-cell} ipython3
import numpy as np

a = np.array([2 - 1j, 3 + 1j]).T
b = np.array([1j, 1 - 1j])

print(f"Answer: {a.conj().T @ b}")
# or
print(f"Answer: {np.vdot(a, b)}")
```

**2\. Укажите все верные варианты ответа для задачи нахождения собственных значений и собственных векторов оператора Паули  $\hat{\sigma^y} = \begin{bmatrix} 0 & -i\\ i & 0 \end{bmatrix}$:**

- Собственные значения: 0 и 1, собственные вектора: $\begin{bmatrix} 1  \\ 0 \end{bmatrix}$ и $\begin{bmatrix} i  \\ 1 \end{bmatrix}$;
- [x]  Собственные значения: 1 и -1, собственные вектора: $\begin{bmatrix} 1  \\ i \end{bmatrix}$ и $\begin{bmatrix} i  \\ 1 \end{bmatrix}$;
- Собственные значения: 0 и 1, собственные вектора: $\begin{bmatrix} i  \\ 0 \end{bmatrix}$ и $\begin{bmatrix} 0 \\ i \end{bmatrix}$;
- [x]  Собственные значения: 1 и -1, собственные вектора: $\begin{bmatrix} -i  \\ 1 \end{bmatrix}$ и $\begin{bmatrix} 1  \\ -i \end{bmatrix}$.


**Решение:**

Собственные вектора и значения: $\begin{vmatrix} \hat{\sigma^y} - \lambda_k E \end{vmatrix} = 0$ и $\hat{\sigma^y} u_k = \lambda_k u_k$

$\begin{vmatrix} -\lambda & -i \\ i & -\lambda \end{vmatrix} = 0 \quad \Leftrightarrow \quad \lambda^2 - 1 = 0 \quad \Leftrightarrow \quad \lambda = \pm 1$

Для $\lambda_1 = 1: \begin{bmatrix} -1 & -i \\ i & -1 \end{bmatrix} \cdot u_1 = 0 \quad \Leftrightarrow \quad u_1 = \begin{bmatrix} 1 \\ i \end{bmatrix}$

Для $\lambda_2 = -1: \begin{bmatrix} 1 & -i \\ i & 1 \end{bmatrix} \cdot u_2 = 0 \quad \Leftrightarrow \quad u_2 = \begin{bmatrix} i \\ 1 \end{bmatrix}$

Вариант $\begin{bmatrix} -i \\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\ -i \end{bmatrix}$ тоже верный, т.к. отличается от представленного только умножением на константу $-i$.

**Решение на `NumPy`:**

```{code-cell} ipython3
import numpy as np

pauli_y = np.array([[0 + 0j, 0 - 1j], [0 + 1j, 0 + 0j]])
eigenvalues, eigenvectors = np.linalg.eig(pauli_y)
print(f"eigenvalues={eigenvalues}")
print(f"eigenvectors={eigenvectors}")

print("А – False, 0 – не собственное значение.")

# b - Проверим, что собственные вектора отличаются на константу:
a1 = eigenvectors[0] / np.array([1, 1j]) # поделим вектора покоординатно
check1 = np.allclose(a1[0],a1[1]) # проверим, что коэффициент пропорциональности - один
print(check1)

# то же самое для второго вектора
a2 = eigenvectors[1] / np.array([1j, 1])
check2 = np.allclose(a2[0], a2[1])
print(check2)
print(f"B – {check1 and check2}")

# C
print("C – False, ноль – не собственное значение.")

# D проверим так же, как и для b), только учтем, что собственные значения переставлены:
a1 = eigenvectors[1] / np.array([-1j, 1])
a2 = eigenvectors[0] / np.array([1, -1j])
print(np.allclose(a1[0], a1[1]))
print(np.allclose(a2[0], a2[1]))
print("D – False, можно заметить, что переставили собственные значения, а собственные вектора умножили на i по сравнению с вариантом B, но не переставили.")
```

**3\. Выберите все верные утверждения:**

- [x] Матожидание измерения оператора $\hat{\sigma^y}$ для состояния $\ket{R}$ равно $1$;
- [x] Собственные значения оператора Адамара – те же, что у операторов Паули;
- [x] Собственные вектора phase-shift гейта $\hat{U_1} (\phi)$ – $\ket{0}$ и $\ket{1}$;
- [x] Для $|\alpha|  > |\beta|$ кубит в состоянии $\begin{bmatrix} \alpha  \\ \beta \end{bmatrix}$ при измерении скорее окажется в состоянии $\ket{0}$.

**Решение:**

1\. $\hat{\sigma^y} = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}$, $\ket{R} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ i \end{bmatrix}$

Матожидание измерения оператора:

$\mathbf{E}(\hat{\sigma^y}) = \left\langle R\middle| \hat{\sigma^y} \middle| R\right\rangle = R^{T^\ast} \cdot \hat{\sigma^y} \cdot R = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & -i \end{bmatrix} \cdot \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix} \cdot \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ i \end{bmatrix} = \frac{1}{2} \begin{bmatrix} 1 & -i \end{bmatrix} \cdot \begin{bmatrix} 1 \\ i \end{bmatrix} = 1$

$\underline{Утверждение \ верно}$

2\. $\hat{H} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$

Собственные значения: $\begin{vmatrix} \hat{H} - \lambda E \end{vmatrix} = 0 \quad \Leftrightarrow \quad \frac{1}{\sqrt{2}} \begin{vmatrix} 1 - \sqrt{2} \lambda & 1 \\ 1 & -1 - \sqrt{2} \lambda \end{vmatrix} = 0 \quad \Leftrightarrow \quad (\sqrt{2} \lambda - 1)(\sqrt{2} \lambda + 1) - 1 = 0 \quad \Leftrightarrow \quad \lambda = \pm 1$

Собственные значения такие же, что у операторов Паули.

$\underline{Утверждение \ верно}$

3\. $\hat{u}_1(\phi) = \begin{bmatrix} 1 & 0 \\ 0 & e^{i \phi} \end{bmatrix}$

Собственные значения: $\begin{vmatrix} 1 - \lambda & 0 \\ 0 & e^{i \phi} - \lambda \end{vmatrix} = 0$

$\lambda_1 = 1 \quad \Rightarrow \quad \begin{vmatrix} 0 & 0 \\ 0 & e^{i \phi} - 1 \end{vmatrix} u_1 = 0 \quad \Rightarrow \quad u_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$

$\lambda_2 = e^{i \phi} \quad \Rightarrow \quad \begin{vmatrix} 1 - e^{i \phi} & 0 \\ 0 & 0 \end{vmatrix} u_2 = 0 \quad \Rightarrow \quad u_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$

$\underline{Утверждение \ верно}$

4\. $\ket{\Psi} = \begin{bmatrix} \alpha \\ \beta \end{bmatrix}$

Измерение по оси $\mathbf{Z}$ делается оператором $\hat{\sigma^z} = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$.

Матожидание при измерении:

$\mathbf{E}(\hat{\sigma^z}) = \left\langle \Psi \middle| \hat{\sigma^z} \middle| \Psi \right\rangle = \begin{bmatrix} \alpha^* & \beta^* \end{bmatrix} \cdot \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \cdot \begin{bmatrix} \alpha \\ \beta \end{bmatrix} = \begin{bmatrix} \alpha^* & \beta^* \end{bmatrix} \cdot \begin{bmatrix} \alpha \\ -\beta \end{bmatrix} = \alpha \alpha^* - \beta \beta^* = {|\alpha|}^2 - {|\beta|}^2$

При $|\alpha| > |\beta|$ видно, что $\mathbf{E}(\hat{\sigma^z}) > 0$, значит состояние $\ket{0}$ более вероятно, чем $\ket{1}$. Заметим, что $\ket{1}$ соответствует значению $-1$ по оси $Z$, а $\ket{0}$ -- значению 1.

$\underline{Утверждение \ верно}$

**4\. Выберите все верные утверждения:**
- T-гейт – это то же, что phase-shift гейт $\hat{U}_1 (\phi)$ с параметром $\phi = \pi/2$;
- [x] Если вектор состояния $\ket{1}$ повернуть на угол $\frac{\pi}{2}$ с помощью оператора $\hat{RX}(\phi)$, то при измерении по оси $\mathbf{Y}$ получится состояние $\ket{R}$;
- [x] Любой поворот кубита вокруг любой оси на угол $2\pi k, k \in \mathbb{Z}$ не меняет состояние кубита;
- Любой поворот кубита вокруг любой оси на любой угол не меняет вероятностей состояний при измерении кубита.

**Решение:**

1\. $\hat{T} = \begin{bmatrix} 1 & 0 \\ 0 & \frac{1+i}{\sqrt{2}} \end{bmatrix},\
\hat{u_1}(\phi) = \begin{bmatrix} 1 & 0 \\ 0 & e^{i \phi} \end{bmatrix},\
\hat{u_1}(\frac{\pi}{2}) = \begin{bmatrix} 1 & 0 \\ 0 & e^{i \frac{\pi}{2}} \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & i \end{bmatrix} \neq \hat{T}$

$\underline{Утверждение \ неверно}$

2\. $\ket{\Psi} = \hat{RX}(\frac{\pi}{2}) \cdot \ket{1} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & -i \\ -i & 1 \end{bmatrix} \cdot \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} -i \\ 1 \end{bmatrix}$

Изменение по оси $\mathbf{Y}$ делается оператором Паули $\hat{\sigma^y}$.

Матожидание: $\left\langle \Psi \middle| \hat{\sigma^y} \middle| \Psi \right\rangle =\frac{1}{\sqrt{2}} \begin{bmatrix} i & 1 \end{bmatrix} \cdot \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix} \cdot \frac{1}{\sqrt{2}} \begin{bmatrix} -i \\ 1 \end{bmatrix} = \frac{1}{2} \begin{bmatrix} i & 1 \end{bmatrix} \cdot \begin{bmatrix} -i \\ 1 \end{bmatrix} = 1$

То есть финальное состояние -- $\ket{R}$.

$\underline{Утверждение \ верно}$

3\. При $\phi = 2 \pi k, k \in \mathbb{Z}$ все операторы поворота равны:

$\hat{RX}(2 \pi k) = \hat{RY}(2 \pi k) = \hat{RZ}(2 \pi k) = \begin{bmatrix} \cos \pi k & 0 \\ 0 & \cos \pi k \end{bmatrix} = (-1)^kE,$ с точностью до коэффициента $-1$ (
то есть до "глобальной фазы", [см. пояснение в лекции](https://semyonsinchenko.github.io/qmlcourse/_build/html/book/qcblock/qubit.html#id27)) состояние кубита при таком повороте не поменяется.

$\underline{Утверждение \ верно}$

4\. $\underline{Утверждение \ неверно}$.

В качестве контрпримера возьмем поворот кубита из $\ket{0}$ вокруг оси $\mathbf{X}$ и измерение по $\mathbf{Z}$.

$\ket{\Psi} = \hat{RX}(\phi) \cdot \ket{0} = \begin{bmatrix} \cos \frac{\phi}{2} & -i \sin \frac{\phi}{2} \\ -i \sin \frac{\phi}{2} & \cos \frac{\phi}{2} \end{bmatrix} \cdot \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} \cos \frac{\phi}{2} \\ -i \sin \frac{\phi}{2} \end{bmatrix}$

Матожидание при измерении по $\mathbf{Z}$:

$\left\langle \Psi \middle| \hat{\sigma^z} \middle| \Psi \right\rangle = \begin{bmatrix} \cos \frac{\phi}{2} & -i \sin \frac{\phi}{2} \end{bmatrix} \cdot \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \cdot \begin{bmatrix} \cos \frac{\phi}{2} \\ -i \sin \frac{\phi}{2} \end{bmatrix} = \begin{bmatrix} \cos \frac{\phi}{2} & -i \sin \frac{\phi}{2} \end{bmatrix} \cdot \begin{bmatrix} \cos \frac{\phi}{2} \\ -i \sin \frac{\phi}{2} \end{bmatrix} = \cos^2\frac{\phi}{2} - \sin^2\frac{\phi}{2} = \cos \phi$

В зависимости от $\phi$ будут получаться разные состояния.

**5\. Какая из последовательностей гейтов идентична единичному гейту $\sigma^x$?**

- $\hat{\sigma^z} \hat{H} \hat{\sigma^z} \hat{H}$ ;
- $\hat{H} \hat{\sigma^z} \hat{\sigma^z} \hat{H}$ ;
- [x] $\hat{H} \hat{\sigma^z} \hat{H}$ ;
- $\hat{\sigma^z} \hat{H} \hat{\sigma^z}$ .

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

**6 \. Чему равна вероятность получения битовой строки $10$  при измерении в $\mathbf{Z}$-базисе состояния: $\large (\hat{H} \otimes \hat{I})\ \hat{CNOT}\ (\hat{I} \otimes \hat{RY}(0.7)) \ket{0} \otimes \ket{0})$?**

_Считаем, что по умолчанию углы измеряются в радианах._

- 0.05879 ;
- [x] 0.44121 ;
- 0.66423 ;
- 0.24246 .

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


**7 \. Реализуйте поворот вектора состояния $\ket{0}$ на угол $\frac{\pi}{2}$  с помощью оператора $\hat{RX}(\phi)$:**
 - на `NumPy`;
 - на `PennyLane`.

Для этого изучите примеры из лекции: [на Numpy](https://semyonsinchenko.github.io/qmlcourse/_build/html/book/qcblock/gates.html#numpy) и [на PennyLane](https://semyonsinchenko.github.io/qmlcourse/_build/html/book/qcblock/gates.html#id16). Учтите, что в лекции пример с двумя кубитами, а в этом вопросе – проще, с одним.

Найдите [ожидаемые значения при измерении](https://semyonsinchenko.github.io/qmlcourse/_build/html/book/qcblock/qubit.html#id28) кубита по осям $\mathbf{X}$, $\mathbf{Y}$, и $\mathbf{Z}$.

- 0 – по $\mathbf{X}$, 1 – по $\mathbf{Y}$, 0 – по $\mathbf{Z}$ ;
- -1 – по $\mathbf{X}$, 0 – по $\mathbf{Y}$, 0 – по $\mathbf{Z}$ ;
- [x] 0 – по $\mathbf{X}$, -1 – по $\mathbf{Y}$, 0 – по $\mathbf{Z}$ ;
- 0 – по $\mathbf{X}$, 0.70710678 – по $\mathbf{Y}$, 0 – по $\mathbf{Z}$ .

**Решение:**

На `NumPy`:

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

Теперь на `PennyLane`:

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
