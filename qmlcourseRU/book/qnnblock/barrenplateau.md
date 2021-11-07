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

# The barren plateau phenomenon

## Description of the lecture

In this lecture, we will learn about the barren plateau phenomenon. It is a common pittfall of many VQC architectures, for which an exponentially vanishing gradient hinders the optimization process. In particular, we will try to answer the following questions:
* What is the barren plateau phenomenon?
* Under which conditions can barren plateaus occur? 
* What strategies can we adopt to avoid them?

## Introduction

Variational algorithms have emerged as a central class of quantum algorithms for NISQ devices. They can be used to solve a large variety of problems, from finding the ground-state of a Hamiltonian in quantum chemistry, material science or combinatorial optimization to solving machine learning problems with quantum neural networks. However, the elephant in the room is that we basically don't know if they can solve problems that classical computers couldn't solve as efficiently. Indeed, variational algorithms can be victim of two kinds of issues:

- **Low-expressiveness**: the variational circuit cannot efficiently represent the states or functions of interest. For instance, a ansatz for VQE might need an exponential number of gates/layers to be able to approximate the ground state of interesting Hamiltonians (i.e. Hamiltonians that cannot be efficiently simulated with classical tensor network or Monte Carlo techniques).
- **Bad trainability**: it takes an exponential time (or an exponential precision in the measurement process) to find the correct parameters of the variational ansatz.

Trainability is the topic of today. What do we know about the optimization of variational circuits that could make them less trainable than, let's say, regular neural networks? This question was studied for the first time by a [team at Google](https://arxiv.org/abs/1803.11173) who introduced the main tool to study this question, namely the **barren plateau phenomenon**. So what's a barren plateau?

> **Definition:** a variational circuit on $n$ qubits is said to have a *barren plateau phenomenon* if, when initialized randomly, the gradient of its cost function is concentrated around 0 with a variance that decreases exponentially with $n$.


Let's unwrap this definition. First of all, the barren plateau is a random phenomenon, meaning that it can only be quantified when considering a random distribution of variational parameters, and will strongly depend on the properties of this distribution. Whether a barren plateau phenomenon is still present in the middle of the optimization process is still an open question. Secondly, the presence or absence of a barren plateau depends on both the ansatz and the cost-function. Changing the cost-function or the ansatz used to solve a given problem can therefore serve as a mitigation strategy to avoid barren plateaus. Finally, the barren plateau is an asymptotic phenomenon, and by convention only occurs when the gradient is *exponentially* decaying with the number of qubits. It is something important to notice as a polynomially-vanishing gradient could potentially destroy certain types of quantum advantage without being called barren plateau in the current terminology.

Hands-on code example here.
```{code-cell} ipython3
visualize_barren_plateau()
```

So, why do we care about barren plateau? Because the properties of the gradients have a large influence on the optimization process. Let's imagine that you are optimizing your cost-function using gradient-descent. Then you need to compute the gradient at each step. If the gradient is exponentially close to zero, we will need an exponential precision to compute it, and that sucks. As we will see later, this issue can also arise when considering gradient-free methods, so the problem is not only about some particular gradient descent algorithms, but really about the landscape of the cost-function.

## When do we have barren plateaus?

## How to avoid barren plateaus?

## Expressibility vs trainability
