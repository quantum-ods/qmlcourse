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

(simon_algorithm)=

# Алгоритм Саймона


## Задача Саймона
Давайте начнём с того, что алгоритм Саймона решает задачу Саймона. Да, вот такой замечательный учёный - нашёл проблему, решил проблему.

По своей природе задача Саймона является разновидностью задачи о скрытой абелевой подгруппе. {cite}`lomont2004hidden`


Пусть задана функция $f: \{0, 1\}^n \rightarrow \{0, 1\}^n$ и **неизвестная** строка $s \in  \{0, 1\}^n$, для всех $x, y \in \{0, 1\}^n$ выполняется:

  $$\large f(x) = f(y) \Leftrightarrow x \oplus y \in \{0^n, s\}$$

То есть, если мы для двух различных строк $x$ и $y$ имеем одинаковое значение $f(x) = f(y)$, то $x \oplus y$ будет равняться либо нулевой строке либо неизвестной строке $s$. 
Функция $f(x)$ представляет собой чёрный ящик.

Задача состоит в том, чтобы **найти $s$ выполнив при этом как можно меньшее количество вызовов $f(x)$ .**

## Описание алгоритма

```{figure} /_static/qcblock/simon_algorithm/simon_principal.svg
:name: simon_principal
:width: 400px
```

1. Сначала приготовления. Вначале мы приготовим 2 набора квантовых регистров в следующем состоянии:
   
    $$|\psi_0\rangle = |0\rangle|0\rangle$$

2. Применяем матрицы Адамара на первом регистре:

    $$ (H^n \otimes I^n) |\psi_0\rangle = (H^n \otimes I^n) |0\rangle |0\rangle = |\psi_1 \rangle = \frac{1}{\sqrt{2^n}}\sum_{k=0}^{2^n-1}|k\rangle |0\rangle $$

3. Применяем оператор $U_f$:
    
    $$ U_f(|\psi_1 \rangle) = U_f(\frac{1}{\sqrt{2^n}}\sum_{k=0}^{2^n-1}|k\rangle |0\rangle) = |\psi_2\rangle = \frac{1}{\sqrt{2^n}}\sum_{k=0}^{2^n-1}|k\rangle |f(k) \rangle $$

4. Снова применяем матрицы Адамара на первом регистре:

    $$ (H^n \otimes I^n) |\psi_2\rangle = |\psi_3\rangle = \frac{1}{2^n} \sum_{k=0}^{2^n-1}(-1^{k \cdot z}) \sum_{z=0}^{2^n-1}|z\rangle |f(k) \rangle $$

    где $k \cdot z = \sum_{i=0}^{2^n-1} k_i \wedge z_i $. 

    ```{note}
    Для чисел $k = 110111$ и $z = 010101$ получим 

      $ k \cdot z = 1 \wedge 0 + 1 \wedge 1 + 0 \wedge 0 + 1 \wedge 1 + 1 \wedge 0 + 1 \wedge 1 = 3$.

      (-1)^3 = -1
    ```


5. Производим измерение на первом регистре. И здесь возможны 2 варианта исхода:

    1. $ x \oplus y = 0^n $

    2. $ x \oplus y = s, \text{ при этом } s \neq 0^n $

    Т.е. во втором случае мы сможем получить значение искомой строки $s$.

    Здесь мы рассмотрим оба случая отдельно.

    Вероятность получить первый случай $ x \oplus y = 0^n $ равна:

    $$ \sum_{z \in \{0, 1\}^n}|z\rangle \otimes \frac{1}{2^n} \sum_{k \in \{0, 1\}^n}(-1^{k \cdot z}) |f(k) \rangle $$

    $$ p_z = \left\| \frac{1}{2^n} \sum_{z \in \{0, 1\}^n} \left((-1)^{z \cdot k } |f(k)\rangle \right) \right\|^2 = \frac{1}{2^n}$$

    Имеет место **равномерное распределение**.

    Гораздо интереснее случай $ x \oplus y = s $, $ s \neq 0^n$. В данном случае функция $f$ преобразует два различных входных значения $x_1, x_2 \in \{0,1\}^n$ в одно $f(x_1) = f(x_2) = s \in \{0, 1\}^n$ .
    Также в данном случае справедливо $x_1 \oplus x_2 = s$, что переписывается в виде $x_1 \oplus s = x_2$ .

    $$ p_y = \left\| \frac{1}{2^n} \sum_{x \in \{0, 1\}^n} \left((-1)^{x \cdot y } |f(x)\rangle \right) \right\|^2 =
     \left\| \frac{1}{2^n} \sum_{z \in A} \left(((-1)^{x_1 \cdot y } (-1)^{x_2 \cdot y })|z\rangle \right) \right\|^2$$

    $$ |\psi_3\rangle = \frac{1}{2^n}\sum_{z \in \{0, 1 \}^n}\sum_{x \in \{0, 1 \}^n} \frac{(-1)^{z \cdot x} (1 + (-1)^{z \cdot s})}{2} |z\rangle \oplus |f(x)\rangle= \\ 
    
    \frac{1}{2^n}\sum_{z \in \{0, 1 \}^n}|z\rangle \otimes \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{z \cdot x} (1 + (-1)^{z \cdot s})}{2} |f(x)\rangle \\
    $$

    Здесь необходимо пояснить и расписать.

    $$\langle f(x),f(y)\rangle = 
    \begin{cases}
      1, \text{ если } x = y \text{ или } x = y \oplus s \\
      0, \text{ иначе}
    \end{cases}
    $$

    $$
      \left\| \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{z \cdot x} (1 + (-1)^{z \cdot s})}{2} |f(x)\rangle \right\|^2 = \\
      
      = \left\langle \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{z \cdot x} (1 + (-1)^{z \cdot s})}{2} |f(x)\rangle, \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{z \cdot x} (1 + (-1)^{z \cdot s})}{2} |f(x)\rangle  \right\rangle^2 \\

      = \sum_{x \in \{0, 1 \}^n} \sum_{y \in \{0, 1 \}^n} \frac{(-1)^{z \cdot x} (1 + (-1)^{z \cdot s})}{2}\frac{(-1)^{z \cdot y} (1 + (-1)^{z \cdot s})}{2}  \langle f(x)|f(y)\rangle \\

      = \sum_{x \in \{0, 1 \}^n} \sum_{y \in \{0, 1 \}^n} \frac{(-1)^{z \cdot (x \oplus y)} (1 + (-1)^{z \cdot s})^2}{4}  \langle f(x)|f(y)\rangle \\

      = \sum_{x \in \{0, 1 \}^n} \sum_{y \in \{0, 1 \}^n} \frac{(-1)^{z \cdot s} (1 + (-1)^{z \cdot s})^2}{4}  \langle f(x)|f(y)\rangle \\

      = \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{z \cdot s} (1 + (-1)^{z \cdot s})^2}{4}  \langle f(x)|f(x)\rangle + \frac{(-1)^{z \cdot s} (1 + (-1)^{z \cdot s})^2}{4}  \langle f(x)|f(x + c)\rangle \\

      = \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{z \cdot s} (1 + (-1)^{z \cdot s})^2}{2} \\

      = \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{z \cdot s} (1 + (-1)^{z \cdot s})^2}{2}\\

      = \begin{cases}
        2^n, \text{ если } z \cdot s = 0 \\
        0, \text{ если }  z \cdot s = 1
      \end{cases}
    $$

    $$
      \sum_{z \in \{0, 1 \}^2} \left\| \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{z \cdot x} (1 + (-1)^{z \cdot s})}{2} |f(x)\rangle \right\|^2 = 2^{n-1} 2 ^{n} = 2^{2n-1}
    $$

    $$
      p(z) = \begin{cases}
        \frac{1}{2^{n-1}}, \text{ если } z \cdot s = 0 \\
        0, \text{ если }  z \cdot s = 1
      \end{cases}
    $$

    Пусть мы замеряем первый регистр $k$ раз и получаем $z_0, z_1, z_2, ..., z_{k-1}$. Теперь мы знаем, что $z_i \cdot s = 0$ для всех $i \in [0, k-1]$.

    Теперь приступаем к вычислению строки $s$.

## Постобработка

Итак, для того, чтобы найти $\vec{s} = (s_0, s_1, s_2, ..., s_{n-1})^T$, нам потребуется $n$ линейно независимых векторов $\vec{z_i}$, для которых выполняется $\vec{z_i} \cdot \vec{s} = 0$.

Пусть заданы **бинарные векторы** $\vec{z_0}, \vec{z_1}, ..., \vec{z_{n-1}}$ и булевы значения $b_0, b_1, ..., b_{n-1}$. Тогда множество векторов $\{\vec{z_i} \} i \in \{0, ..., n-1\}$  **линейно независимо**
, если:

$$
  (b_0 \wedge \vec{z_0}) \oplus (b_1 \wedge \vec{z_1}) \oplus (b_2 \wedge \vec{z_2}) \oplus ... \oplus (b_{n-1} \wedge \vec{z_{n-1}}) = \vec{0}
$$

имеет только тривиальные решения $b_0 = b_1 = ... = b_{n-1} = 0$. Иначе, векторы $\vec{z_i}, i \in \{0, ..., n-1\}$ **линейно зависимы**.

Отсюда следует $\vec{ z_{i} } \neq \vec{0}, i \in [0, ..., n-1] $ .

Пусть $z_0, z_1, ..., z_{n-1}$ линейно зависимы, тогда, хотя бы $1$ из $n$ линейных уравнений $\vec{z_0} \cdot \vec{s} = 0, \vec{z_1} \cdot \vec{s} = 0, ..., \vec{z_{n-1}} \cdot \vec{s} = 0$, могут быть сокращены.

$$
  0 = \vec{0} \cdot \vec{s}
  = (b_0 \wedge \vec{z_0}) \oplus (b_1 \wedge \vec{z_1}) \oplus (b_2 \wedge \vec{z_2}) \oplus ... \oplus (b_{n-1} \wedge \vec{z_{n-1}}) \cdot \vec{s} \\

  = (b_0 \wedge \vec{z_0}) \cdot \vec{s} \oplus (b_1 \wedge \vec{z_1}) \cdot \vec{s} \oplus (b_2 \wedge \vec{z_2}) \cdot \vec{s} \oplus ... \oplus (b_{n-1} \wedge \vec{z_{n-1}}) \cdot \vec{s} \\

  = b_0 \wedge (\vec{z_0} \cdot \vec{s}) \oplus b_1 \wedge (\vec{z_1} \cdot \vec{s}) \oplus b_2 \wedge (\vec{z_2} \cdot \vec{s}) \oplus ... \oplus b_{n-1} \wedge (\vec{z_{n-1}} \cdot \vec{s}) \\

$$

Также, из-за того, что $z_0, z_1, ..., z_{n-1}$ линейно зависимы, можно утверждать, что $b_i \neq 0 (b_i = 1)$:

$$
  \vec{z_i} \cdot \vec{s} = b_i \wedge \vec{z_i} \cdot \vec{s} = (b_i \wedge (\vec{z_i} \cdot \vec{s})) \oplus 0 \\
  = (b_i \wedge (\vec{z_i} \cdot \vec{s})) \oplus (b_0 \wedge (\vec{z_0} \cdot \vec{s})) \oplus
  (b_1 \wedge (\vec{z_1} \cdot \vec{s})) \oplus (b_2 \wedge (\vec{z_2} \cdot \vec{s})) \oplus ... \oplus (b_{n-1} \wedge (\vec{z_{n-1}} \cdot \vec{s}))  \\

  = (b_i \wedge (\vec{z_i} \cdot \vec{s})) \oplus (b_i \wedge (\vec{z_i} \cdot \vec{s})) \oplus \bigoplus_{j \neq i}(b_j \wedge (\vec{z_j} \cdot \vec{s})) \\

  = 0 \oplus  \bigoplus_{j \neq i}(b_j \wedge (\vec{z_j} \cdot \vec{s})) \\

  =\bigoplus_{j \neq i}(b_j \wedge (\vec{z_j} \cdot \vec{s})) \\

  =\bigoplus_{j \neq i}(b_j \wedge 0) \\

  = \bigoplus_{j \neq i} 0 \\

  = 0\\

$$

Т.е. мы сократили $(\vec{z_i} \cdot s)$.

# Пример



## Ссылки

[Simon Algorithm](https://leimao.github.io/blog/Simon-Algorithm/)

[Simon's problem](https://en.wikipedia.org/wiki/Simon%27s_problem)