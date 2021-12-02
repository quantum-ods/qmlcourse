(np2ising)=

# Формулировка задач оптимизации в терминах модели Изинга

Мы не зря так глубоко изучали [модель Изинга](ising) и [анализировали](advising) ее решения -- сегодня мы увидим, как в терминах этой модели можно сформулировать большинство важных задач [комбинаторной оптимизации](copt).

(qubo-matrix)=
## QUBO матрица

Но сначала мы кратко обсудим так называемую _QUBO_ матрицу {cite}`glover2019tutorial` -- это еще один способ записать задачу модель Изинга и дальше по курсу мы иногда будем этим пользоваться.

_QUBO_ -- это сокращение от _Quadratic Unconstrainde Binary Optimization_, или, если переводить, то это _задачи квадратичной оптимизации без ограничений_. То есть это такие задачи для которых нет отдельных ограничений, например равенств или неравенств, а функция стоимости включает представима в виде многочлена второй степени от входных переменных. А решением такой задачи является бинарный вектор $X = \{x_1, x_2, ..., x_n\}$ такой, что $x_1, ..., x_n \in \{0, 1\}$. В этом случае функцию стоимости $C$ можно записать в виде:

$$
C = a_1 x_1^2 + a_2 x_2^2 + ... + a_n x_n^2 + b_1 x_1 + ... + b_n x_n + c_{1, 2} x_1 x_2 + c_{1, 3} x_1 x_3 + ... + c_{n, n - 1} x_n x_{n -1}
$$

Но так как наши переменные бинарные, то разницы между $x_i^2$ и $x_i$ нет -- дальше мы будем использовать $a_i$ как единственные коэффициенты считая, что $b_i$ уже так включены туда. И в этом случае можно представить функцию стоимости как матрицу размера $|X| \times |X|$, на диагонали которой стоят коэффициенты $a_1, ..., a_n$, а вне диагонали стоят коэффициенты, с которыми в стоимость входят пары элементов:

$$
Q = \begin{pmatrix}a_1 & c_{1, 2} & ... & c_{1, n} \\
... & ... & ... & ...\\
c_{n, 1} & ... & ... & a_{n}
\end{pmatrix}
$$

А сама оптимизационная задача в этом случае формулируется следующим образом:

$$
\arg\min_{X} {X^T Q X}
$$

```{note}
Тут мы рассматриваем именно минимизацию функции стоимости. Но если исходная задача формулировалась в терминах максимизации чего-то, например, как задача о рюкзаке или максимальном разрезе в графе, то очевидно, что просто домножив стоимость на -1 мы перейдем от максимизации к минимизации. Далее для нас это будет важно, так как мы будем рассматривать нашу задачу как поиск _основного состояния_ квантомеханической системы, а такое состояние это по определению состояние именно с _минимальной_ энергией.
```

## QUBO как квантовый гамильтониан

Если вспомнить, как [выглядит](../problemsblock/advising.html#id2) модель Изинга, то легко заметить, что там у нас как и в _QUBO_-проблемах есть лишь члены первой и второй степени. Вот только [спиновые операторы (матрицы Паули) имеют собственные значения](../qcblock/qubit.html#hat-sigma-z) $\pm 1$, а не $\{0, 1\}$, которые фигурируют в _QUBO_. Это проблема, так как квадраты этих значений не равны им самим. Но это легко можно исправить введя "бинарный" оператор $\hat{x}$:

$$
\hat{x} = \frac{1 + \hat{\sigma}^z}{2} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}
$$

Введя "промежуточные" переменные $sz_i$ которые связаны с $x_i$ через это выражение ($x_i = \frac{1 + sz}{2}$ мы всегда можем свести выражение для $C$ к следующему виду:

$$
C = \sum_{i, j \in \{1, ..., |X|\}} J_{i, j} sz_i sz_j + \sum_{i \in {\{1, ..., |X|\}}} h_i sz_i
$$

А это уже почти наша модель Изинга! Заменяем $sz$ на операторы $\sigma^z$ и получаем гамильтониан системы. Причем такой, что минимум его энергии будет совпадать с минимальным значением функции стоимости $C$:

$$
\begin{align*}
& \hat{H} = \sum_{i, j \in \{1, ..., |X|\}} J_{i, j} \sigma^z_i \sigma^z_j + \sum_{i \in {\{1, ..., |X|\}}} h_i \sigma^z_i \\
& \braket{\Psi | \hat{H} | \Psi} = \min {X^T Q X} = \min {C} \quad \text{если }\Psi\text{ - это основное состояние системы}
\end{align*}
$$

Причем в силу того, что у нас в выражении для $\hat{H}$ фигурируют лишь $\sigma^z$, то основное состояние нашего гамильтониана является "классическим", то есть все спины "ориентированы" либо вверх, либо вниз, но не находятся в суперпозиции. Другими словами, наш гамильтониан диагонализируется в $\mathbf{Z}$-базисе.

## Поиск основного состояния

Как мы увидели, задачи, сформулированные в терминах _QUBO_ можно свести к задаче нахождения основного состояния квантовой системы, которая описывается некоторым оператором. Но что это вообще значит? И что это за гамильтониан такой, о котором мы все время говорим? Вообще говоря, гамильтониан это оператор энергии:

$$
\hat{H} = \hat{T} + \hat{U},
$$

где $T$ -- это кинетическая энергия системы, а $U$ -- потенциальная энергия. Именно этот оператор определяет квантовую динамику в уравнении Шредингера. То есть это оператор, зная который (а также начальное состояние системы) можно посчитать волновую функцию системы ($\ket{\Psi}(t)$) в любой момент времени в будущем. Правда это лишь в теории, так как сложность интегрирования уравнения Шредингера очень быстро растет с ростом размера системы. Мы немного касались этой темы в [лекции про виды квантового машинного обучения](../qmlkindsblock/qmlkinds.html#id3), когда рассматривали, как нейросети помогают решать это самое уравнение.

Мы еще коснемся этой темы в следующих лекциях, но пока нам достаточно понимания о том, что гамильтониан полностью описывает квантовую систему. С другой стороны, одновременно, зная гамильтониан мы всегда можем построить "в железе" квантовую систему, которую он описывает. Например, конфигурируя магнитные поля и двухчастичные обменные взаимодействия.

Таким образом, решение проблемы _QUBO_ сводится к поиску $\ket{\Psi}_{GS}$ -- волновой функции, отвечающей основному состоянию:

$$
\arg\min_{\ket{\Psi}} {\hat{H}}
$$

А финальное решение получается просто как наиболее вероятная конфигурация спинов в состоянии $\ket{\Psi}_{GS}$. Ну и останется лишь перейти от полученных собственных значений операторов $\sigma^z_i$ к собственным значениям операторов $\hat{x}_i$.

```{note}
Кстати справедлив и обратный переход, то есть решив проблему QUBO каким нибудь из [классических алгоритмов](problemsblock/copt.html#id9) для решения комбинаторных задач мы автоматически получим конфигурацию основного состояния соответствуеющей физической системы! Этот подход впервые был предложен аж в 1988-м году в работе {cite}`barahona1988application`. Таким образом, мы приходим к пониманию о **тесной связи задач квантовой физики и комбинаторной оптимизации**. Именно на этом и строятся огоромное число перспективных квантовых алгоритмов для решения задач реального мира. Особенно в _NISQ_ эпоху!
```

Важным преимуществом квантового представления _QUBO_-задач заключается в том, что наш мир устроен таким образом, что любая квантовая система всегда стремится в состояние с минимальной энергией, то есть основное. На этом построен даже целый класс квантовых аннилеров. Но и для вариационных квантовых алгоритмов это также дает свои преимущества.

## Статья Ising formulations of many NP problems

Основным источником информации для нас будет статья _Ising formulations of many NP problems_ {cite}`combinatorics2ising`, вышедшая в 2014-м году. В данной лекции мы рассмотрим лишь часть примеров из этой работы, хотя наше рассмотрение будет чуть более подробным. В целом эта статья может быть использована как прекрасный справочник.

## Задача о максимальном разрезе в графе (повторение)

Мы уже рассматривали эту задачу в [лекции о модели Изинга](ising) и в [лекции про задачи комбинаторно оптимизации](copt), но теперь повторим еще раз. Итак, у нас есть граф на множестве вершин $V$, связанных множеством ребер $E$. Каждое ребро соединияет вершины $u,v$. Для простоты будем рассматривать случай ненаправленного графа. Каждое ребро имеет вес $w$. Наша цель -- разбить множество вершин $V$ на два непересекающихся сообщества $V_1, V_2$ таким образом, чтобы суммарный вес ребер, соединяющих вершины из разных сообществ был максимален:

$$
\arg\max{V_1, V_2} {\sum_{u,v,w \in E} w (\mathbf{1}(u \in V_1, v \in V_2) + \mathbf{1}(u \in V_2, v \in V_1))}
$$

```{figure} /_static/problemsblock/ising/Max-cut.png
:width: 400px
:name: MaxCut

Иллюстрация задачи о максимальном разрезе в графе
```

Эта задача уже является задачей без ограничений и может быть сразу сформулирована в терминах _QUBO_ и модели Изинга.

### _QUBO_ матрица

_QUBO_ матрица для этой задачи иметь размер $|V| \times |V|$, а вектор решения $X$ это, соответственно, будет бинарный вектор длины $|V|$. Для простоты обозначим сообщество $V_1$ как вершины, для которых $x_i = 0$, а $V_2$ это будут вершины с $x_i = 1$. Ну и еще мы хотим решать задачу минимизации вместо задачи максимизации. Запишем новую целевую функцию:

$$
C = -\sum_{i,j \in \{1, .., |V|\}} w_{i,j} (x_i + x_j - 2 x_i x_j)
$$

Чтобы записать _QUBO_ матрицу нам будет удобнее работать с матрицей смежности графа, а не списком его ребер. Матрица смежности $A$ (_adjacency matrix_) это матрица размера $|V| \times |V|$, элементы которой это веса $w_{i, j}$, если в графе есть ребро между вершинами $i$ и $j$ и $0$ если ребра нет. Тогда наша _QUBO_ будет иметь следующий вид:

$$
QUBO = \begin{pmatrix}
\sum_{j = 0}^{|V| - 1} A_{0,j} & -2 A_{0, 1} & ... & -2 A_{0, |V|} \\
... & ... & ... & ... \\
-2 A_{|V|, 0} & ... & ... & \sum_{j = 0}^{|V| - 1} A{|V|, j}
\end{pmatrix}
$$

### Гамильтониан Изинга

В случае этой задачи можно сказать, что она изначально имеет вид модели Изинга. И действительно, наиболее вероятная конфигурация спинов для основного состояния системы с гамильтонианом такого вида:

$$
\hat{H} = \sum_{i,j \in \{1, ..., |V|\}} (1 - \sigma^z_i \sigma^z_j)
$$

будет в точности соответствовать решению задачи о максимальном разрезе. Ну а численное значение энергии будет отличаться ровно на величину $|E|$, то есть на число ребер, так как величина $(1 - \sigma^z_i \sigma^z_j$)$ будет равна нулю, если вершины в разных сообществах или единице, если они находятся в одном.

## Задача коммивояжера

Задача коммивояжера обсуждалась нами в [лекции по комбинаторной оптимизации](../problemsblock/copt.html#id7), где мы уже получили выражения для представления данной задачи в виде "без ограничений". Напомним, что нам удалось добиться этого "внеся" ограничения в выражения для целевой функции в виде штрафа за отклонение от ограничений. Ну и мы также добавили соответствующие коэффициенты. Полученное в той лекции выражение имеет вид:

$$
C = A (1 - \sum_i x_{i,p})^2 + A (1 - \sum_p x_{i,p})^2 + A \sum_{u,v \notin E} x_{u,p} x_{v,p+1} + B \sum_{u,v,w \in E} w x_{u,p} x_{v,p+1}
$$

Для нас удобно, что это уже задача минимизации. В данном случае, _QUBO_-матрица получается при помощи явного раскрытия скобок в выраженнии для стоимости. Можно заметить, что в этом случае мы получаем также элементы 0-й степени, но формат _QUBO_-матрицы такого не предусматривает. Но во-первых, в данном случае мы легко можем определить разницу между $X^T Q X$ и минимумом $C$, а во-вторых для нас это не столь важно -- нам нужно решение, а значение энергии/функции стоимости получается без каких-либо проблем за полиномиальное время.

```{note}
Это довольно важное замечание, так как часто можно найти относительно простое представлениие задачи в виде _QUBO_, а вот учет всех констант может сильно усложнить ее вид. Более того, как мы увидим далее, не все представления _QUBO_ одинаково эффективны, особенно когда мы переходим к решению на квантовом компьютере: для каких-то видов _QUBO_ у нас будет одна величина энергетической щели между основным и возбужденным состоянием в процессе решения, а для других _QUBO_-представлений той же задачи оно уже может стать больще!
```

## Задача о выделении сообществ в графе

## Заключение

Из этой лекции мы узнали, что такое _QUBO_ матрица, а также как от такой формулировки оптимизационных задач можно перейти к задаче поиска основного состояния кванто-механической системы. В будущих лекциях мы познакомимся уже непосредственно с тремя основными методами решения этой задачи:

1. Квантовый отжиг. В этом случае мы реализуем нашу модель Изинга буквально в железе. Это сразу дает нам ряд ограничений и особенностей, но с другой стороны мы получаем возможность хорошо масштабировать нашу систему. И действительно, сегодня компьютеры фирмы D-Wave имеют порядка нескольких тысяч кубитов. Многие специалисты считают, что до появления универсальных квантовых компьютеров, именно аналоговые машины D-Wave, решающие задачу Изинга станут основным коммерческим инструментов в квантовых вычислениях.
2. Вариационные-градиентные методы. В этом подходе мы пытаемся закодировать волновую функцию основного состояния системы при помощи [вариационной квантовой схемы](vqc), а дальше найти такие параметры, которые минимизируют результат измерения нашего гамильтониана в таком состоянии. Этот метод называется **V**ariational **Q**uantum **E**igensolver.
3. Третий пополярный подход соединяет идеи первых двух: в этом случае мы также делаем квантовый отжиг, но для этого не строим целевую систему в железе, а производим симуляцию квантовой динамики на кубитах при помощи специальных приближений из области квантовой механики. А параметры "отжига" мы, как и в **VQE** подбираем при помощи градиентных методов. Такой подход носит название **Q**uantum **A**pproximate **O**ptimization **A**lgorithm.

Именно этим темам будет посявщена бОльшая часть из оставшихся лекций.