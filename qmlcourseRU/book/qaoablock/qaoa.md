(qaoa)=

# Quantum Approximate Optimization Algorithm

## Описание лекции

<!-- todo: написать, если нужно -->

## Введение

Алгоритм квантовой приближенной оптимизации (`Quantum Approximate Optimization Algorithm (QAOA)`) -- алгоритм поиска оптимального решения для комбинаторных задач оптимизации. В частности, алгоритм может [применяться](https://medium.com/mdr-inc/portfolio-optimization-with-minimum-risk-using-qaoa-e29e1d66c194) для расчета рисков инвестиционных портфелей, когда ведется работа с больгим объемом данных и нужно подобрать оптимальную комбинацию многих параметров таким образом, чтобы риск был минимальным. Фактически `QAOA` помогает найти минимум функции, заданной на дискретном множестве. Точность решения зависит от "глубины" алгортма -- количества слоев, их мы рассмотрим чуть позже.

`QAOA` использует унитарный оператор $U(\beta,\gamma)$, принимающий на вход вещественные параметры $\beta$, $\gamma$, и описывается уже знакомым квантовым состоянием $\ket{\Psi}$. Цель поиска -- найти те самые оптимальные $\beta_{\text{opt}}$ и $\gamma_{\text{opt}}$.

Оператор $U$ состоит из двух частей:

- меняющий фазу $U_{\text{phase}}$

    $$
    U_{\text{phase}}(\gamma) = e^{-i{\gamma}H_{\text{phase}}}
    $$

- смешивающий кубиты $U_{\text{mixer}}$

    $$
    U_{\text{mixer}}(\beta) = e^{-i{\beta}H_{\text{mixer}}}
    $$

Оператор $U_{\text{phase}}$ совершает вращение относительно осей $Z$ или $Y$ с помощью соответствующих матриц Паули:

$$
H_{\text{phase}} = Z \ or \ Y \ \text{axis rotation}
$$

```{figure} /_static/qaoablock/hamiltonian_u_phase.png
:name: hamiltonian_u_phase
:width: 444px

Оператор $U_{\text{phase}}$
```

$U_{\text{mixed}}$ в классическом случае использует матрицу $XNOT$.

Операторы применяются к начальному состоянию $\ket{\Psi_0}$ последовательно $р$ раз (или, иначе говоря, используются $p$ слоев):

$$
\ket(\beta,\gamma) = \underbrace{U_{\text{mixer}}(\beta) U_{\text{phase}}(\gamma) \ ... \ U_{\text{mixer}}(\beta) U_{\text{phase}}(\gamma)}_{\text {p times}}{\ket{\Psi_0}}
$$

Общая схема для $n$ кубитов выглядит следующим образом:

```{figure} /_static/qaoablock/general_scheme_for_n_qubits.png
:name: general_scheme_for_n_qubits

Общая схема для $n$ кубитов
```

Итак, алгоритм состоит со следующих основных этапов:

1. Приготовление начального состояния $\ket{\Psi_0}$ из $n$ кубитов с последующим применением к каждому кубиту матриц Адамара для осуществления суперпозиции всевозможных состояний:

    ```{figure} /_static/qaoablock/the_1t_step_alg.png
    :name: the_1t_step_alg
    :width: 222px
    ```

2. Применяем оператор вращения фазы

    $$
    U_{\text{phase}} = \sum_{i \neq j}^{n-1} e^{-i \gamma Z_i Z_j}
    $$

    например вот так:

    $$
    H_p = (I_0 \otimes Z_1 \otimes I_2 \otimes Z_3)
    $$

    ```{figure} /_static/qaoablock/the_2d_step_alg.png
    :name: the_2d_step_alg
    :width: 444px
    ```

    Напоминаем, как выглядит данный оператор в матричном виде: $Z = \begin{bmatrix} 1 & 0 \\ 0 & 1\end{bmatrix}$.

3. Применяем смешивающий оператор

    $$
    U_{\text{mixer}} = \sum_{i=0}^{n-1} e^{-i \beta X_i}
    $$

    к примеру, так:

    $$
    U_{\text{mixer}} = (I \otimes I \otimes X \otimes Z)
    $$

    ```{figure} /_static/qaoablock/the_3d_step_alg.png
    :name: the_3d_step_alg
    :width: 444px
    ```

    $$
    Z = \begin{bmatrix} 0 & 1 \\ 1 & 0\end{bmatrix}
    $$

В данном алгоритме используется адиабатический метод эволюции состояния $\ket{\Psi_0}$ с переменным гамильтонианом: на каждой итерации параметры $\beta$ и $\gamma$ понемногу изменяются.
Далее производится измерение финального состояния в $Z$-базисе и вычисление $\bra{\Psi(\beta,\gamma)}H_{phase}\ket{\Psi(\beta,\gamma)}$. Минимум будет соответствовать оптимальным $\beta$ и $\gamma$.


## Quantum Alternating Operator Ansatz

Применение "анзаца" в QAOA заключается в модернизации оператора смешивания $U_{mix}$ и предполагает использование не $X$, а $CNOT$. На рисунках ниже представлена абстрактная визуализация "смешивания" и обозначение оператора:

```{figure} /_static/qaoablock/ansatz_mixing.png
:name: ansatz_mixing
:width: 444px

"Смешивание"
```

```{figure} /_static/qaoablock/ansatz_operator_designation.png
:name: ansatz_operator_designation

Обозначение оператора
```

Пример схемы, реализующий QAOAz:

```{figure} /_static/qaoablock/ansatz_sample.png
:name: ansatz_sample
:width: 444px
```
## Что мы узнали из лекции

<!-- todo: дописать -->
