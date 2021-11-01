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

(qaoa)=

# Quantum Approximate Optimization Algorithm

## Описание лекции

<!-- todo: написать, если нужно -->

## Введение

Алгоритм квантовой приближенной оптимизации -– алгоритм поиска оптимального решения для комбинаторных задач. В частности, алгоритм применяется в расчете рисков инвестиционных портфелей, когда ведется работа с огромным объемом данных и нужно подобрать оптимальную комбинацию многих параметров таким образом, чтобы риск был минимальным.
Фактически данный алгоритм помогает найти оптимум заданной функции с приближённым решением, точность которого зависит от "глубины" слоев, их мы рассмотрим чуть позже.

Схема алгоритма QAOA использует унитарный оператор $U(\beta,\gamma)$, принимающий некоторые параметров $\beta$, $\gamma$ и описывается уже знакомым квантовым состоянием $\ket{\Psi}$. Цель поиска -- найти те самые оптимальные $\beta_opt$ и $\gamma_opt$.

Оператор $U$ состоит из двух частей:

- меняющий фазу $U_{phase}$

  $$
  U(\gamma) = e^{-i{\gamma}H_p}
  $$

- смешивающий кубиты $U_{mixed}$

  $$
  U(\beta) = e^{-i{\beta}H_{mixed}}
  $$

Гамильтониан $U_{phase}$ совершает вращение относительно осей $Z$ или $Y$ с помощью соответствующих матриц Паули:

$$
H_p = Z \ or \ Y \quad axis \ rotation
$$

```{figure} /_static/qaoalock/hamiltonian_u_phase.png
:name: hamiltonian_u_phase

Гамильтониан $U_{phase}$
```

$U_{mixed}$ в классическом случае использует матрицу $X-NOT$.

Операторы применяются к начальному состоянию $\ket{\Psi_0}$ последовательно $р$ раз (или, иначе говоря, используются $p$ слоев):

$$
\ket(\beta,\gamma) = \underbrace{U_\beta U\gamma \ ... \ U_\beta U\gamma}_{\text {p times}}{\ket{\Psi_0}}
$$

Общая схема для $n$ кубитов выглядит следующим образом:

```{figure} /_static/qaoalock/general_scheme_for_n_qubits.png
:name: general_scheme_for_n_qubits

Общая схема для $n$ кубитов
```

Итак, алгоритм состоит со следующих основных этапов:

1. Приготовление начального состояния $\ket{\Psi_0}$ из $n$ кубитов с последующим применением к каждому кубиту матриц Адамара для осуществления суперпозиции всевозможных состояний:

    ```{figure} /_static/qaoalock/the_1t_step_alg.png
    :name: the_1t_step_alg
    ```

3. Применяем оператор вращения фазы

    $$
    H_p = \sum_{i \neq j}^{n-1} e^{-i \gamma Z_i Z_j}
    $$

    например вот так:

    $$
    H_p = (I_0 \oplus Z_1 \oplus I_2 \oplus Z_3)
    $$

    ```{figure} /_static/qaoalock/the_2d_step_alg.png
    :name: the_2d_step_alg
    ```

    Напоминаем, как выглядит данный оператор в матричном виде: $Z = \begin{bmatrix} 1 & 0 \\ 0 & 1\end{bmatrix}$.

3. Применяем смешивающий оператор

    $$
    H_{mixed} = \sum_{i=0}^{n-1} e^{-i \beta X_i}
    $$

    к примеру, так:

    $$
    H_{mixed} = (I \oplus I \oplus X \oplus Z)
    $$

    ```{figure} /_static/qaoalock/the_3d_step_alg.png
    :name: the_3d_step_alg
    ```

    $$
    Z = \begin{bmatrix} 0 & 1 \\ 1 & 0\end{bmatrix}
    $$

В данном алгоритме используется адиабатический метод эволюции состояния $\ket{\Psi_0}$ с переменным гамильтонианом: на каждой итерации параметры $\beta$ и $\gamma$ понемногу изменяются.
Далее производится измерение финального состояния в $Z$-базисе и вычисление $\bra{\Psi(\beta,\gamma)H_{phase}\ket{(\beta,\gamma)}$. Минимум будет соответствовать оптимальным $\beta$ и $\gamma$.


## Quantum Alternating Operator Ansatz

Применение "анзаца" в QAOA заключается в модернизации оператора смешивания $U_{mix}$ и предполагает использование не $X$, а $C-NOT$. На рисунках ниже представлена абстрактная визуализация "смешивания" и обозначение оператора:

```{figure} /_static/qaoalock/ansatz_mixing.png
:name: ansatz_mixing

"Смешивание"
```

```{figure} /_static/qaoalock/ansatz_operator_designation.png
:name: ansatz_operator_designation

Обозначение оператора
```

Пример схемы, реализующий QAOAz:

```{figure} /_static/qaoalock/ansatz_sample.png
:name: ansatz_sample
```
## Что мы узнали из лекции

<!-- todo: дописать -->
