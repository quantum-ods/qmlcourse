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

(numpy)=
# Numpy

Широко используемая библиотека для вычислений с многомерными массивами. API большей частью вдохновлен MATLAB (великая и ужасная среда, язык и IDE для матричных вычислений), а теперь сам является примером для подражания API различных вычислительных пакетов.
Более последовательный гайд стоит посмотреть на [сайте библиотеки](https://numpy.org/devdocs/user)


## Массивы

```{code-cell} ipython3
import numpy as np

a = np.array([1, 2, 3]) # создадим вектор
print(f"{a = }")

b = np.zeros((2, 2))
print(f"{b = }")

c = np.eye(3)
print(f"{c = }")

q = np.random.random((1, 100))
print(f"{q = }")
```


## Math ops
Для удобства использования np.ndarray определены арифметические операторы, так чтобы соответствовать ожиданиям:

```{code-cell} ipython3
a = np.array([1, 2, 3])
b = np.array([-1, 3, 4])

diff = a - b
print(f"{diff = }")

mult = a * b
print(f"{mult = }")

scalar_mult = a @ b
print(f"{scalar_mult = }")
```


## Indexing, slicing and sugar

Numpy поддерживает кажется все разумные варианты индексации:

```{code-cell} ipython3
a = np.arange(16).reshape(4, 4)
print(f"{a = }")

# просто по индексам
print(f"a_{0,1}: {a[0, 1] = }, {a[0][1] = }")

# по слайсам
print("a_{1,1..3}", a[0, 1:3])
print(f"a_{2}: {a[2] = }, {a[2, :] = }, {a[2, ...] = }")

# по маске
mask = (a % 3 == 0)
print(f"{mask = }")
print(f"{a[mask] = }")

first_rows = np.array([True, True, False, False])
print(f"{a[first_rows] = }")
```

Для работы с размерностями часто используются еще три конструкции: `None`, `...` (ellipsis, многоточие) и `:` (двоеточие).

```{code-cell} ipython3
a = np.arange(16).reshape(4, 4)
print(f"{a = }")

# None добавляет ось размерности 1
print(f"{a[None].shape = }")
print(f"{a[:, :, None].shape = }")

# : превращается в slice (None), берет все элементы вдоль размерности
print(f"{a[2, :] = "})
print(f"a[2, 0:None] = }")

# ... ellipsis, превращается в необходимое число двоеточий :,:,:
print(f"{a[...] = }")

# также ... удобен когда мы не знаем настоящий шейп массива или нужно не трогать несколько подряд идущих размерностей
z = np.arange(27).reshape(3, 3, 3)
print(f"{z[0, ..., 1] = }, {z[0, :, 1] = }")
```

В целом, в numpy очень здорово реализованы методы `__getitem__`/`__setitem__`.

```{code-cell} ipython3
a = np.array([1, 2, 3])
element = a[2]
print(f"{element = }")

a[2] = 5
print(f"{a = }")
```

Кроме того, мы можем делать индексацию по заданному условию с помощью `np.where`

```{code-cell} ipython3
# создадим вектор
a = np.array([2, 4, 6, 8])

selection = np.where(a < 5)
print(f"{selection = }")

# дополнительно мы можем передать два значения или вектора, при выполнении условия выбираются элементы из первого значения/вектора, при невыполнении - из второго
a2 = np.where(a < 5, 2, a * 2)
print(f"{a2 = }")

# np.where работает и с многомерными массивами
b = np.array([[8, 8, 2, 6], [0, 5, 3, 4]])
b_mult = np.where(b < 4, b, 1)
print(f"{b_mult = }")
```


## Broadcasting

Что происходит, если мы хотим арифметику с массивами разных размеров?

```{code-cell} ipython3
a = np.array([1, 2, 3])
k = 2
broad = a * k
print(f"{broad = }")
```

С точки зрения математики, ничего интересного тут не происходит: мы подразумевали умножение всего вектора на скаляр. Однако матричные операции в numpy справляются и с менее очевидными случаями, например при сложении или вычитании вектора и скаляра:

```{code-cell} ipython3
a = np.array([1, 2, 3])
k = 2
broad = a - k
print(f"{broad = }")
```

В numpy приняты следующие правила работы с массивами разного размера:

1. Размерности сравниваются справа налево
2. Два массива совместимы в размерности, если она одинаковая, либо у одного из массивов единичная.
3. Вдоль отсутствующих размерностей происходит расширение повторением (`np.repeat`).

![.](https://i.stack.imgur.com/JcKv1.png)

```{admonition} Link to the source
https://mathematica.stackexchange.com/questions/99171/how-to-implement-the-general-array-broadcasting-method-from-numpy
```

Be aware, автоматический броадкастинг легко приводит к ошибкам, так что лучше делать его самостоятельно в явной форме.


## floating point things

Отдельно стоит поговорить про числа с плавающей точкой.
Число с плавающей запятой (или число с плавающей точкой) — экспоненциальная форма представления вещественных (действительных) чисел, в которой число хранится в виде мантиссы и порядка (показателя степени). При этом число с плавающей запятой имеет фиксированную относительную точность и изменяющуюся абсолютную.
В результате одно и то же значение может выглядеть по-разному, если хранить его с разной точностью.

```{code-cell} ipython3
f16 = np.float16("0.1")
f32 = np.float32(f16)
f64 = np.float64(f32)
print(f"{f16 = }, {f32 = }, {f64 = }")
print(f"{f16 == f32 == f64 = }")

f16 = np.float16("0.1")
f32 = np.float32("0.1")
f64 = np.float64("0.1")
print(f"{f16 = }, {f32 = }, {f64 = }")
print(f16 == f32 == f64)
```

Из-за этого для сравнения массивов с типом float используют `np.allclose`.

```{code-cell} ipython3
print(f"{np.allclose([1e10,1e-7], [1.00001e10,1e-8]) = }")
print(f"{np.allclose([1e10,1e-8], [1.00001e10,1e-9]) = }")
```


## numpy & linalg fun

[Не знаю, что имеется ввиду под "Матричные трюки"]

["вычисление попарных расстояний" - вроде обычно используется scipy/sklearn?]

### Решение системы линейных уравнений

Numpy позволяет решить систему линейных уравнений.

```{code-cell} ipython3
a = np.array([[7, 4], [9, 8]])
b = np.array([5, 3])
solution = np.linalg.solve(a, b)
print(f"{solution = }")
```

### Обращение матриц.

Numpy даёт возможность выполнить операцию обращения матриц.

```{code-cell} ipython3
a = np.array([[1., 2.], [3., 4.]])
inv = np.linalg.inv(a)
print(f"{inv = }")
```

### Собственные вектора и числа

Вычисление собственных векторов и чисел.

```{code-cell} ipython3
print(np.linalg.eig(np.diag((1, 2, 3))))
```


## Что мы узнали

- основы работы с numpy
- индексацию в массивах
- broadcasting
- floating point things
- numpy fun
