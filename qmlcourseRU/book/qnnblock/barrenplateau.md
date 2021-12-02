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

Trainability is the topic of today. What do we know about the optimization of variational circuits that could make them less trainable than, let's say, regular neural networks? This question was studied for the first time by a [team at Google](https://arxiv.org/abs/1803.11173) who introduced the main tool to study this question, namely the **barren plateau phenomenon**. Such phenomenon occurs whenever the gradient of a randomly-initialized parametrized quantum circuit gets exponentially close to $0$ when increasing the number of qubits. The presence of small gradients tends to make the optimization problem extremely difficult for large systems, as it means that the landscape of the function we want to optimize is mostly flat, or *barren*. Finding a good descent direction at each optimization step is therefore a laborious process. The presence or absence of barren plateaus is influenced by many aspects of variational architectures: the [type of ansatz](https://arxiv.org/abs/2011.02966), the [number of layers](https://arxiv.org/abs/2001.00550), the [cost function](https://arxiv.org/abs/2001.00550), the [strength of noise](https://arxiv.org/abs/2007.14384) and [entanglement](https://arxiv.org/abs/2010.15968), the [initialization strategy](https://arxiv.org/abs/1903.05076), etc.

We will explore here those different features of barren plateaus, with the goal of helping you identify if any architecture you're considering might exhibit this phenomenon. Let's start by giving a more precise definition of barren plateaus and go through some simple examples.

## What is a barren plateau?

> **Definition:** a variational circuit on $n$ qubits is said to have a *barren plateau phenomenon* if, when initialized randomly, the gradient of its cost function is concentrated around $0$ with a variance that decreases exponentially with $n$.


Let's unwrap this definition. First of all, the barren plateau is a random phenomenon, meaning that it can only be quantified when considering a random distribution of variational parameters, and will strongly depend on the properties of this distribution. Whether gradients are still small in the middle of the optimization process is harder to prove. Secondly, the presence or absence of a barren plateau depends on both the ansatz and the cost-function. Changing the cost-function or the ansatz used to solve a given problem can therefore serve as a mitigation strategy to avoid barren plateaus. Finally, the barren plateau is an asymptotic phenomenon, and by convention only occurs when the gradient is *exponentially* decaying with the number of qubits. It is something important to notice as a polynomially-vanishing gradient could potentially destroy certain types of quantum advantage without being called barren plateau in the current terminology.

Hands-on code example here.
```{code-cell} ipython3
visualize_barren_plateau()
```

So, why do we care about barren plateaus? Because the properties of the gradients have a large influence on the optimization process. Let's imagine that you are optimizing your cost-function using gradient-descent. Then you need to compute the gradient at each step. If the gradient is exponentially close to zero, we will need an exponential precision to compute it, and that sucks. As we will see later, this issue can also arise when considering gradient-free methods, so the problem is not only about some particular gradient descent algorithms, but really about the landscape of the cost-function.

## When do we have barren plateaus?

### When the circuit distribution is a 2-design

[Insert figure with a big unitary matrix]

"When the what is a what??". Let's unravel those terms, which are crucial to understand the essence of barren plateaus.

#### Haar measure and 2-designs

Let's say you have a certain parametrized quantum circuit.
It can be represented by a unitary matrix $U(\theta)$ depending on some parameters $\theta$.
You then need to specify a distribution to initialize your circuit.
For instance, you could choose to pick your $\theta$s uniformly between $0$ and $2\pi$.
Or have a Gaussian distribution centered around $0$.
In any case, this distribution over the parameters will induce a distribution over unitary matrices:
each time you initialize your circuit, you get a different unitary $U$ that has a certain probability density $p(U)$.
And we're lucky, there is an entire field, called *random matrix theory*, that studies those distribution over matrices, and in particular over unitary matrices.
For example, in random matrix theory, the equivalent of the uniform distribution is called the **Haar measure**.
The Haar measure over the unitary group $\mathcal{U}(n)$ is defined as the unique probability distribution $p_{\text{Haar}}$ such that

\begin{equation}
  \forall U, V \in \mathcal{U}(n), p_{\text{Haar}}(UV)=p_{\text{Haar}}(VU)=p_{\text{Haar}}(U)
\end{equation}

It means that moving around the unitary group does not change the density, or in other words, all unitary matrices have equal probability.
While algorithms exist to sample unitary matrices over the Haar distribution, most quantum circuit initialization schemes are based on parameter initialization and do not directly follow the Haar measure. However, they can often approximate it.

A particular type of approximation of the Haar measure is formed by the so-called **$t$-designs**. A distribution $p$ over the unitary group is a $t$-design if all its moments up to $t$ (expectation, variance, etc.) are equal to those of the Haar measure. More formally, for any polynomial function $f$ of degree $t$, we should have:

$$
  \mathbb{E}_{U \sim p_{\text{Haar}}}[f(U)]=\mathbb{E}_{U \sim p}[f(U)]
$$

Sometimes, you'll also find in the literature the definition of a $t$-design written as

$$
  \forall M, \, \int (U^{\dagger})^{\otimes t} M U^{\otimes t} dp(U) = \int (U^{\dagger})^{\otimes t} M U^{\otimes t} dp_{\text{Haar}}(U)
$$

or

$$
  \forall M, \, \frac{1}{N} \sum_k (U_k^{\dagger})^{\otimes t} M U_k^{\otimes t} = \int (U^{\dagger})^{\otimes t} M U^{\otimes t} dp_{\text{Haar}}(U)
$$

which is just the explicit form of the equation above, when the distribution is respectively continuous or discrete and $M$ is the matrix representing the polynomial we want to take. In particular, $2$-designs are distributions that have the same expectation and variance as the Haar measure, and they appear everywhere in quantum information. For instance, if you construct a circuit by randomly inserting Clifford gates (H, CNOT, S), you'll eventually get a 2-design [TODO: make those statements more precise]

#### 2-designs and barren plateaus

So what's the link between 2-designs and barren plateaus? It happens that whenever your circuit distribution follows a 2-design, you'll get a barren plateau. That statement was proved in the [first paper on barren plateau](https://arxiv.org/abs/1803.11173) and takes the following more precise form:

> **Theorem:** let $U(\theta)$ a parametrized quantum circuit, $U_k=e^{iA\theta_k}$ a particular gate in the circuit, $\rho$ the input density matrix and $E(\theta)=\text{Tr}[HU(\theta)\rho U^\dagger(\theta)]$ the cost function we are trying to optimize. Then, if the unitaries before and after $U_k$ follow a 2-design, we will have as the number of qubits $n \rightarrow \infty$:
>
> $$\mathbb{E}[\partial_k E]=0$$
>
> $$\text{Var}[\partial_k E] \sim - \frac{2}{2^{3n}} \text{Tr}[\rho^2] \text{Tr}[H^2] \text{Tr}[A^2]$$

So in other words, randomly initializing a quantum circuit such that the resulting distribution is 2-design will directly give you exponentially vanishing gradients. The trace terms appearing in the variance usually don't contribute too much to the overall scaling. Indeed, taking VQE as an example, the intial density matrix is usually taken to be $\rho = |0\rangle \langle 0 |$ for which $\text{Tr}[\rho^2]=1$. Gates are usually rotations, in which case $A$ is a pauli matrix fullfilling $\text{Tr}[A^2]=n$. Finally, if $H$ is a sum of local terms (e.g. an Ising Hamiltonian), we can also show that $\text{Tr}[H^2]$ won't have any influence on the scaling.

What is the intuition behind this result? Levy's lemma and concentration of measure

### When the number of layers if high

How do we get 2-designs? By having a large depth.

This statement was made more precise in the cost-function dependent BP paper, in which they studied one particular type of ansatz: the so-called hardware-efficient ansatz (HEA).

Description of the HEA.

Description of the paper's results.


### When the cost function is global

In the previous discussion, we've assumed that the cost function was local.
If the cost function is global, more chance of BP.

Example of global cost function: the fidelity

### When noise is present

Discussion of the noise-induced BP paper

### When hidden and visible layers of QNNs are highly entangled

Specific to a particular QNN architecture as well as QRBM.

## How to mitigate the barren plateau phenomenon?

### Global to local cost function

Example of the fidelity.

### Architectures with a logarithmic number of layers

Example of the QCNN

### Initialization strategies

Paper by UCL team.

## Expressibility vs trainability

## Landscape close to the minimum: narrow gorges

## The maths of barren plateaus

## Resources
