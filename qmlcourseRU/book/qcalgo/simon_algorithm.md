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

  $$\large f(x) = f(y) \Leftrightarrow x \oplus y = s$$

То есть, если мы для двух различных строк $x$ и $y$ имеем одинаковое значение $f(x) = f(y)$, то $x \oplus y$ равняется некоторой неизвестной строке $s$. 
Функция $f(x)$ представляет собой чёрный ящик.

Задача состоит в том, чтобы **найти $s$ выполнив при этом как можно меньшее количество вызовов $f(x)$ .**

## Описание алгоритма

```{figure} /_static/qcalgo/simon_algorithm/simon_principal.svg
:name: simon_principal
:width: 400px
```

В принципе, есть небольшие вариации в реализации алгоритма, мы рассмотрим наиболее простую (все необходимые ссылки в конце приведены):

1. Сначала приготовления. Вначале мы приготовим 2 набора квантовых регистров в следующем состоянии:
   
    $$|\psi_0\rangle = |0\rangle|0\rangle$$

2. Применяем матрицы Адамара на первом регистре:

    $$ (H^n \otimes I^n) |\psi_0\rangle = (H^n \otimes I^n) |0\rangle |0\rangle = |\psi_1 \rangle = \frac{1}{\sqrt{2^n}}\sum_{x \in \{ 0, 1\}^n}|x\rangle |0\rangle $$

3. Применяем оператор $U_f$:
    
    $$ 
      U_f(|\psi_1 \rangle) = U_f(\frac{1}{\sqrt{2^n}}\sum_{x \in \{ 0, 1\}^n}|x\rangle |0\rangle) = |\psi_2\rangle = \frac{1}{\sqrt{2^n}}\sum_{x \in \{ 0, 1\}^n}|x\rangle |f(x) \rangle 
    $$

   
4. Снова применяем матрицы Адамара на первом регистре:

    $$ (H^n \otimes I^n) |\psi_2\rangle = |\psi_3\rangle = \frac{1}{2^n} \sum_{x \in \{ 0, 1\}^n}(-1^{\langle x, z\rangle}) \sum_{z \in \{ 0, 1\}^n}|z\rangle |f(x) \rangle $$

    где $\langle x, z\rangle = \bigoplus_{i=0}^{2^n-1} x_i \wedge z_i $. 

    ```{note}
    Для чисел $x = 110111$ и $z = 010101$ получим 

      $\langle x, z\rangle = 1 \wedge 0 \oplus 1 \wedge 1 \oplus 0 \wedge 0 \oplus 1 \wedge 1 \oplus 1 \wedge 0 \oplus 1 \wedge 1 = 1$.

      $(-1)^{1} = -1$
    ```


5. Производим измерение на первом регистре. И здесь возможны 2 варианта исхода:

    1. $ x \oplus y = s = 0^n $

        Вероятность получить первый случай $ x \oplus y = 0^n $ равна:

        $$ \sum_{z \in \{0, 1\}^n}|z\rangle \otimes \frac{1}{2^n} \sum_{x \in \{0, 1\}^n}(-1^{\langle x, z\rangle}) |f(x) \rangle $$

        $$ p_z = \left\| \frac{1}{2^n} \sum_{z \in \{0, 1\}^n} \left((-1)^{\langle z, x\rangle} |f(x)\rangle \right) \right\|^2 = \frac{1}{2^n}$$

        Имеет место **равномерное распределение**.


    2. $ x \oplus y = s \neq 0^n $

        Этот случай гораздо интереснее. Функция $f$ преобразует два различных входных значения $x_1, x_2 \in \{0,1\}^n$ в одно $f(x_1) = f(x_2) = s \in \{0, 1\}^n$ .
        Также, справедливо $x_1 \oplus x_2 = s$, что переписывается в виде $x_1 \oplus s = x_2$ .

        $$ |\psi_3\rangle = \frac{1}{2^n}\sum_{z \in \{0, 1 \}^n}\sum_{x \in \{0, 1 \}^n} \frac{(-1)^{\langle z, x \rangle} (1 + (-1)^{\langle z, s\rangle})}{2} |z\rangle \oplus |f(x)\rangle= \\ 
        
        \frac{1}{2^n}\sum_{z \in \{0, 1 \}^n}|z\rangle \otimes \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{\langle z,  x\rangle} (1 + (-1)^{\langle z, s\rangle})}{2} |f(x)\rangle \\
        $$

        $$ p(z) = \left\| \frac{1}{2^n} \sum_{x \in \{0, 1\}^n} \left((-1)^{\langle x, z\rangle} |f(x)\rangle \right) \right\|^2 =
        \left\| \frac{1}{2^n} \sum_{z \in A} \left(((-1)^{\langle x_1, z\rangle} + (-1)^{\langle x_2, z\rangle})|z\rangle \right) \right\|^2 \\
        = \begin{cases}
            \frac{1}{2^{n-1}}, \text{ если } \langle z, s \rangle = 0 \\
            0, \text{ если }  \langle z, s \rangle = 1
          \end{cases}
        $$

  Выполняем алгоритм $n$ раз. После чего у нас будет система $n$ линейно независимых уравнений.

Теперь приступаем к вычислению строки $s$.


6. Постобработка

Итак, для того, чтобы найти $\vec{s} = (s_0, s_1, s_2, ..., s_{n-1})^T$, нам потребуется $n$ линейно независимых векторов $\vec{z_i}$, для которых выполняется $\langle \vec{z_i}, \vec{s} \rangle = 0$.

После того, как получена система из $n$ линейно независимых уравнений, решение можно найти методом Гауаса.
# Пример

Давайте возьмём n = 3, строка $s = 100$, и функцию $f$, которая соответствует критерию $f(x) = f(y) \Leftrightarrow x \oplus s = y$. 

Обычно функция $f(x)$ задана наперёд. Ну а мы выберем её простейшей: $f(x) = x \oplus s$ .

Давайте посмотрим таблицу истинности всех нужных переменных.

$$\large
\begin{array} {|r|r|r|}
\hline x & x \oplus s & f(x) \\ 
\hline 000 & 100 & 000 \\ 
\hline 001 & 101 & 001 \\ 
\hline 010 & 110 & 010 \\ 
\hline 011 & 111 & 011 \\ 
\hline 100 & 000 & 000 \\ 
\hline 101 & 001 & 001 \\ 
\hline 110 & 010 & 010 \\ 
\hline 111 & 011 & 011 \\ 
\hline  
\end{array}
$$

Сразу же нарисуем схему на Qiskit:

```{code-cell} ipython3
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

# Работаем в пространстве размерности n = 3.
n = 3

# Создаём необходимые регистры
qr1 = QuantumRegister(n, name="q1")
qr2 = QuantumRegister(n, name="q2")
cr1 = ClassicalRegister(n, name="c1")

# Шаг 1. Создаём квантовую схему (инициализация состояния)
qc = QuantumCircuit(qr1, qr2, cr1)

# Шаг 1. Применяем гейт Адамара ко всем кубитам первого регистра
qc.h(range(n))

# Шаг 2. Применяем U_f
qc.cx(qr1[0],qr2[0])

# Шаг 3. Ещё раз применяем гейт адамара к каждому из кубитов
qc.h(range(n))

# Шаг 4. Производим измерение первого регистра
qc.measure(qr1, cr1)

# Рисуем схему
qc.draw()
```


Теперь пройдём по всем шагам алгоритма:

1. Инициализация всех регистров в $0$ состоянии:

    $$|\psi_0\rangle = |000\rangle_{1} |000\rangle_{2}$$

2. Применяем Адамар к первому регистру:
   
    $$ 
    (H^n \otimes I)(|\psi_0\rangle) = |\psi_1\rangle = \frac{1}{\sqrt{8}}(|000\rangle + |001\rangle + |010\rangle + |011\rangle + |100\rangle + |101\rangle + |110\rangle + |111\rangle)_1 |000 \rangle_{2} 
    $$

3. Применяем оракл U_f:

    $$
      U_f(|\psi_1) = |\psi_2\rangle = \\

      \frac{1}{\sqrt{8}} (|000\rangle_{1} |0 \oplus 0, 0, 0 \rangle_{2} \\
      + |001\rangle_{1} |0 \oplus 0, 0, 0 \rangle_{2} \\
      + |010\rangle_{1} |0 \oplus 0, 0, 0 \rangle_{2} \\
      + |011\rangle_{1} |0 \oplus 0, 0, 0 \rangle_{2} \\
      + |100\rangle_{1} |0 \oplus 1, 0, 0 \rangle_{2} \\
      + |101\rangle_{1} |0 \oplus 1, 0, 0 \rangle_{2} \\
      + |110\rangle_{1} |0 \oplus 1, 0, 0 \rangle_{2} \\
      + |111\rangle_{1} |0 \oplus 1, 0, 0 \rangle_{2} )
      
    $$

4. Ещё один раз применяем гейты Адамара на первый регистр:

  $$ 
    (H^n \otimes I)(|\psi_2\rangle) = |\psi_1\rangle = \frac{1}{\sqrt{8}}(|000\rangle + |001\rangle + |010\rangle + |011\rangle + |100\rangle + |101\rangle + |110\rangle + |111\rangle)_1 |000 \rangle_{2} 
  $$


# Приложение

1. Расчёт вероятностей.

    $$ \langle f(x), f(y)\rangle = \langle f(x), f(y) \rangle = 
    \begin{cases}
      1, \text{ если } x = y \text{ или } x = y \oplus s \\
      0, \text{ иначе}
    \end{cases}
    $$

    $$
      \left\| \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{\langle z,x \rangle} (1 + (-1)^{\langle z, s \rangle})}{2} |f(x)\rangle \right\|^2 = \\
      
      = \left\langle \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{\langle z, x \rangle} (1 + (-1)^{\langle z, s \rangle})}{2} |f(x)\rangle, \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{\langle z, x \rangle} (1 + (-1)^{\langle z, s \rangle})}{2} |f(x)\rangle  \right\rangle^2 \\

      = \sum_{x \in \{0, 1 \}^n} \sum_{y \in \{0, 1 \}^n} \frac{(-1)^{\langle z, x \rangle} (1 + (-1)^{\langle z, s \rangle})}{2}\frac{(-1)^{\langle z, y \rangle} (1 + (-1)^{\langle z, s\rangle})}{2}  \langle f(x) , f(y)\rangle \\

      = \sum_{x \in \{0, 1 \}^n} \sum_{y \in \{0, 1 \}^n} \frac{(-1)^{\langle z, (x \oplus y) \rangle} (1 + (-1)^{\langle z, s \rangle})^2}{4}  \langle f(x) , f(y)\rangle \\

      = \sum_{x \in \{0, 1 \}^n} \sum_{y \in \{0, 1 \}^n} \frac{(-1)^{\langle z, s \rangle} (1 + (-1)^{\langle z, s \rangle})^2}{4}  \langle f(x) , f(y)\rangle \\

      = \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{\langle z, s \rangle} (1 + (-1)^{\langle z, s \rangle})^2}{4}  \langle f(x)|f(x)\rangle + \frac{(-1)^{\langle z, s \rangle} (1 + (-1)^{\langle z, s \rangle})^2}{4}  \langle f(x) , f(x + c)\rangle \\

      = \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{\langle z, s \rangle} (1 + (-1)^{\langle z, s \rangle})^2}{2} \\

      = \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{\langle z, s \rangle} (1 + (-1)^{\langle z,  s \rangle})^2}{2}\\

      = \begin{cases}
        2^n, \text{ если } \langle z, s \rangle = 0 \\
        0, \text{ если }  \langle z, s \rangle = 1
      \end{cases}
    $$

    $$
      \sum_{z \in \{0, 1 \}^2} \left\| \sum_{x \in \{0, 1 \}^n} \frac{(-1)^{\langle z, x \rangle} (1 + (-1)^{\langle z, s \rangle})}{2} |f(x)\rangle \right\|^2 = 2^{n-1} 2 ^{n} = 2^{2n-1}
    $$

    $$
      p(z) = \begin{cases}
        \frac{1}{2^{n-1}}, \text{ если } \langle z, s \rangle = 0 \\
        0, \text{ если }  \langle z, s \rangle = 1
      \end{cases}
    $$


# Ссылки

[Simon Algorithm](https://leimao.github.io/blog/Simon-Algorithm/)

[Simon's problem](https://en.wikipedia.org/wiki/Simon%27s_problem)

[Qiskit Simon algorithm](https://qiskit.org/textbook/ch-algorithms/simon.html)