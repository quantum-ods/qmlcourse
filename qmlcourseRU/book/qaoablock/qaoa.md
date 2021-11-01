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

Алгоритм квантовой приближенной оптимизации -– алгоритм для комбинаторных задач. Он использует унитарный оператор $U(\beta,\gamma)$, зависящий от некоторых параметров $(\beta,\gamma)$ как и итоговое квантовое состояние $\ket{\Psi}$. Цель -- найти оптимальные $\beta_opt$ и $\gamma_opt$.
Оператор $U$ состоит из двух частей:
- меняющий фазу $U_phase$

$$
U(\gamma) = \e^{-i\gammaH_p}
$$

- смешивающий кубиты $U_mix$

$$
U(\beta) = e^{-u\betaH_M}
$$

## Что мы узнали из лекции

<!-- todo: дописать -->
