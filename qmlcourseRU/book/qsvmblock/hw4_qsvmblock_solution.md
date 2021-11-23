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

(hw4_solution)=

# Задание 4. Квантовый SVM. Решение

Авторы – Семен Синченко и Юрий Кашницкий. [Ссылка на тест](https://ods.ai/tracks/qmlcourse/blocks/cef31c12-03fe-422e-87cc-16683db3a921)

_Правильные варианты ответа помечены значком [x]._

**1\. Рассмотрим задачу классификации с двумя классами $\mathbb{Y} = \{-1,1\}$, в которой точки $\{(0, 1), (1, 4), (2, 4) \}$ -- положительные примеры, а точки  $\{(2, 0), (3, 1), (5, 3)\}$ -- отрицательные примеры. C помощью метода опорных векторов найдите линейный классификатор $a(x_1, x_2) = w_1 x_1 + w_2 x_2 + b$, максимизирующий зазор между классами.**

- $a(x_1, x_2) = x_1 + x_2 + 1$
- [x] $a(x_1, x_2) = -1.5 x_1 + x_2 + 1$
- $a(x_1, x_2) = -x_1 + x_2 + 1$
- $a(x_1, x_2) = -1.5 x_1 + x_2 - 1$

**Решение:**

_Задание основано на [этом примере](https://github.com/esokolov/ml-course-hse/blob/master/2016-spring/seminars/sem16-svm.pdf) из лекций Евгения Соколова, на который мы [ссылались](../qsvmblock/classic_svm.html#id10) в лекции по SVM._

Такую "игрушечную" обучающую выборку можно нарисовать на клетчатом листке бумаги или с помощью `matplotlib`. Ниже положительные примеры помечены красными крестиками, а отрицательные -- зелеными кружками.

```{code-cell} ipython3
import matplotlib.pyplot as plt
%config InlineBackend.figure_format = 'retina'
plt.rcParams['figure.figsize'] = (4, 3)

xx = [0, 1, 2, 2, 3, 5]
yy = [1, 4, 4, 0, 1, 3]
labels = list(range(1, 7))

plt.scatter(x=xx[:3], y=yy[:3], marker='P', color='red', s=64)
plt.scatter(x=xx[3:], y=yy[3:], marker='8', color='green', s=64)
plt.axline((0,1), slope=1.5, linestyle='dashed')
plt.axline((2,0), slope=1.5, linestyle='dashed')
for i in range(len(xx)):
    plt.annotate(labels[i], (xx[i] + 0.1, yy[i]))
plt.grid();
```

Выборка линейно-разделимая, поэтому будем решать такую задачу (см. [лекцию](../qsvmblock/classic_svm.html#id6) про SVM):

$$
\begin{equation}
\label{eq:svmSep}
    \left\{
        \begin{aligned}
            & \frac{1}{2} (w_1^2 + w_2^2) \to \min_{w_1, w_2, b} \\
            & y_i \left(
                \langle w, x_i \rangle + b
            \right) \geq 1, \quad i = 1, \dots, 6.
        \end{aligned}
    \right.
\end{equation}
$$

Запишем лагранжиан:

$$\large \mathcal{L}(w_1, w_2, b, \lambda) = \frac{1}{2} (w_1^2 + w_2^2) + \sum_{i=1}^6 \lambda_i (1 - (\langle w, x_i \rangle + b))$$

и условия Куна-Таккера (см. условия 1, 2 и 4 [в лекции](../qsvmblock/classic_svm.html#id10): $w = \sum_{i=1}^6 \lambda_i y_i x_i$, $\sum_{i=1}^6 \lambda_i y_i = 0$, $\lambda_i = 0 \quad \text{или} \quad y_i(\langle w, x_i \rangle + b) = 1$):

$$
    \left\{
        \begin{aligned}
            & w_1 = \lambda_2 + 2 \lambda_3 - 2 \lambda_4 - 3 \lambda_5 - 5 \lambda_6  \\
            & w_2 = \lambda_1 + 4\lambda_2 + 4\lambda_3 - \lambda_4 - \lambda_5 - 3 \lambda_6  \\
            & \lambda_1 + \lambda_2 + \lambda_3 = \lambda_4 + \lambda_5 + \lambda_6 \\
            & \lambda_1 = 0 \quad \text{или} \quad w_2 + b = 1  \\
            & \lambda_2 = 0 \quad \text{или} \quad w_1 + 4w_2 + b = 1 \\
            & \lambda_3 = 0 \quad \text{или} \quad 2 w_1 + 4w_2 + b = 1 \\
            & \lambda_4 = 0 \quad \text{или} \quad -2w_1 -w_2 - b = 1 \\
            & \lambda_5 = 0 \quad \text{или} \quad -3w_1 - w_2 - b = 1 \\
            & \lambda_6 = 0 \quad \text{или} \quad -5w_1 - 3w_2 - b = 1
        \end{aligned}
    \right.
$$

По рисунку видно, что опорные объекты – 1, 3 и 4, поэтому $\lambda_1 > 0, \lambda_3 > 0, \lambda_4 > 0, \lambda_2 = 0, \lambda_5 = 0, \lambda_6 = 0.$

Получаем систему:

$$
    \left\{
        \begin{aligned}
            & w_1 =  2 \lambda_3 - 2 \lambda_4 \\
            & w_2 = \lambda_1 + 4\lambda_3 - \lambda_4   \\
            & \lambda_1  + \lambda_3 = \lambda_4  \\
            & w_2 + b = 1 \\
            & 2 w_1 + 4w_2 + b = 1 \\
            & -2w_1 -w_2 - b = 1
        \end{aligned}
    \right.
$$

Решая систему, получаем $w_1 = -\frac{3}{4}, w_2 = \frac{1}{2}, b = \frac{1}{2}$ и тогда линейный классификатор, максимизирующий зазор между классами:

$$ a(x_1, x_2) = -1.5 x_1 + x_2 + 1$$

```{code-cell} ipython3
plt.scatter(x=xx[:3], y=yy[:3], marker='P', color='red', s=64)
plt.scatter(x=xx[3:], y=yy[3:], marker='8', color='green', s=64)
plt.axline((0,1), slope=1.5, linestyle='dashed')
plt.axline((2,0), slope=1.5, linestyle='dashed')
plt.axline((2/3,0), slope=1.5, linestyle='dashed', c='red')

for i in range(len(xx)):
    plt.annotate(labels[i], (xx[i] + 0.1, yy[i]))
plt.grid();
```

**2\. Какому квантовому ядру (общая схема с $U_1$ как в [этой статье](https://arxiv.org/abs/1906.10467)) соответствует тепловая карта скалярных произведений такого вида:**

![](/_static/qsvmblock/hw4/ZZ8.png)

- $\phi(x) = x, \phi(x_1, x_2) = \pi \cdot x_1\cdot x_2$, измерение $\mathbf{Z} \otimes \mathbf{Y}$
- [x] $\phi(x) = x, \phi(x_1, x_2) = \pi \cdot x_1\cdot x_2$, измерение $\mathbf{Z} \otimes \mathbf{Z}$
- $\phi(x) = x, \phi(x_1, x_2) = \frac{\pi}{3 \cdot \cos(x_1) \cdot \cos(x_2)}$, измерение $\mathbf{Y} \otimes \mathbf{Z}$
- $\phi(x) = x, \phi(x_1, x_2) = \pi \cdot 0.5 \cdot (1 - x_1) \cdot (1 - x_2)$, измерение $\mathbf{Y} \otimes \mathbf{Y}$

**Решение:**
TBA

**3\. Какому квантовому ядру (общая схема с $U_1$ как в [этой статье](https://arxiv.org/abs/1906.10467)) соответствует тепловая карта скалярных произведений такого вида:**

![](/_static/qsvmblock/hw4/YY9.png)

- [x] $\phi(x) = x, \phi(x_1, x_2) = \pi \cdot 0.5 \cdot (1 - x_1) \cdot (1 - x_2)$, измерение $\mathbf{Y} \otimes \mathbf{Y}$
- $\phi(x) = x, \phi(x_1, x_2) = \pi \cdot x_1\cdot x_2$, измерение $\mathbf{Z} \otimes \mathbf{Z}$
- $\phi(x) = x, \phi(x_1, x_2) = \frac{\pi}{3 \cdot \cos(x_1) \cdot \cos(x_2)}$, измерение $\mathbf{Z} \otimes \mathbf{Y}$
- $\phi(x) = x, \phi(x_1, x_2) = \frac{\pi}{3 \cdot \cos(x_1) \cdot \cos(x_2)}$, измерение $\mathbf{Y} \otimes \mathbf{Z}$


**Решение:**
TBA

**4\. Какому квантовому ядру (общая схема с $U_1$ как в [этой статье](https://arxiv.org/abs/1906.10467)) соответствует тепловая карта скалярных произведений такого вида:**

![](/_static/qsvmblock/hw4/ZY11.png)

- $\phi(x) = x, \phi(x_1, x_2) = \pi \cdot x_1\cdot x_2$, измерение $\mathbf{Z} \otimes \mathbf{Y}$
- $\phi(x) = x, \phi(x_1, x_2) = \pi \cdot x_1\cdot x_2$, измерение $\mathbf{Z} \otimes \mathbf{Z}$
- [x] $\phi(x) = x, \phi(x_1, x_2) = \frac{\pi}{3 \cdot \cos(x_1) \cdot \cos(x_2)}$, измерение $\mathbf{Z} \otimes \mathbf{Y}$
- $\phi(x) = x, \phi(x_1, x_2) = \pi \cdot 0.5 \cdot (1 - x_1) \cdot (1 - x_2)$, измерение $\mathbf{Y} \otimes \mathbf{Y}$

**Решение:**
TBA
