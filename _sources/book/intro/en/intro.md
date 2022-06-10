(intro_en)=

# About quantum computers, bitcoin, and superiority

 Author(s):

 - [Sinchenko Semyon](https://github.com/SemyonSinchenko)

Translation:

 - [Sinchenko Semyon](https://github.com/SemyonSinchenko)

 ## About the lecture

 The lecture hasn't any learning meaning but tries to answer questions that can have anyone who faces the topic about quantum computing for a first time:

 - what the computing is this?
 - why we need all this stuff?
 - when one will crack bitcoin?
 - what the advantage is said all around?

 ## What the computing is this?

 ### Quantity evolution of computers

 Classical computers which are based on Turing, Von Neumann and Shockley ideas are an organic part of our live. We all used to have an every year growing computational power of such computers. And today's cheap laptop have a power that supercomputers had 15 years ago.

 ```{figure} /_static/intro/en/Moores_Law.png
 :name: moores_law

 A Moore law illustration; a growth of the number of transistors from 1970s
 ```

 A law that is named a Moore law was formulated by Gordon Moore in the late 60-s. It tell us that the number of transistors by crystal of integral circuit is adding twice every two years. And it have been holding true for the last 60 years.

 ### Quality evolution of computers

 Unfortunately the Moore law holding cannot be endless because there are physical limitations: sooner or later the direct adding twice of the number of transistors could be impossible due tunneling effects. That's why this is said that the modern computers will have a "quality" revolution. Some say about new materials for creating transistors. Another say about new principles of computers. For example about photonic computers where photons are used instead electrons. But one can hear that the next computers revolution will the invention of quantum computers. That is what we will talk about.

 ### The idea about quantum computers

 There are few version who was the first one said about using quantum mechanic's laws for creating the new computer. Like it frequently happens a few scientist independently and at one time came to the same idea. One of them was Richard Phillips Feynman.

 ```{figure} /_static/intro/en/Feinman.jpg
 :name: feinman

 Richard Phillips Feynman, 1918-1988
 ```

 In 1981 when there was a very active development of the both classical computers and computational quantum mechanics he said that for solving quantum mechanical problems we should have a quantum computer.

 ### What the computer is this?

 It is very complicated question and all the first half of our course will try to answer it. It is strange if such a complex question that is discussed in few lectures with hard math could be explained in a few words. It will be wrong to say that classical computers are based on the classical physic's laws and quantum computers are based on laws of quantum physics because one couldn't explain the principles of modern transistors without such quantum things like the Fermi level and other stuff. Also it will be wrong to say that classical computers operate with $0$ and $1$ but quantum have all states from $0$ to $1$ because there is the probability Turing machine that works with probabilistic bit that can have all the states from $0$ to $1$. Especially we do not want to rush with a lot of complex and unclear terms like a quantum superposition, qubits or quantum entanglement because such a terms mean nothing for anyone who is not in the loop. At first let agree that _quantum computers_ are not only based on new technology like photonic or grafen computers but uses a whole new principles of computation and information representation different from what Turing was invented

 ## Why do we need it?

 ### Factorization problem

 It seems to me that specifically the invention of the Shor algorithm for effective solving of the factorization problem was the most important step for popularization of quantum computing. After that a lot of specialists and scientists rushed to this field, military forces and corporation pushed a fantastic sum of money to the field, reporters started to talking about the future fail of the bank system and the whole world. Probably the Shor algorithm is the most hype quantum algorithm.

 The reason is that the biggest part of modern cryptography is based on the one simple assuming that there is no polynomial algorithm for the factorization task. In other words if we have a number that is the result of two big prime numbers product we can try to find that prime numbers until the death of the universe. But it is true only for the classical computer. A quantum computer has the effective polynomial algorithm invented by Piter Shor in 1994. And this algorithm can solve the factorization problem in relative short time.

 ```{figure} /_static/intro/en/Shor.png
 :name: shor

 Piter Shor. The man who set the world on fire with his algorithm.
 ```

 This algorithm will crack the bitcoin and ruin the banking system in the future. But it's not all that simple: evolution of quantum computers threw scientists to creating of _post-quantum_ cryptography that is based on tasks which cannot be effectively solved on both classical and quantum computers.

 ### Combinatorial and NP-hard problems

 Except for difficulties with Moore law there is another problem with classical computers. There are tasks that likely wont be solved effectively on the classical Turing computer. Even on photonic or grafen one. The good example is the knapsack problem. When we have a knapsack of limited volume and a lot of things with different size and cost. And we want to fill our knapsack in such a manner to maximize the total cost of things inside it. The task looks very simple but it is an example of [$NP$-complete problems](https://en.wikipedia.org/wiki/NP-completeness). If we have a big number of different things and a relative big knapsack such problem cannot be solved exactly in reasonable time. Even the finding of the good enough _approximate_ solution of such problem is very hard today!

 ```{note}
 I used a word "likely" because the question about existence of the effective solution of NP-complete problems is one of [the major unsolved problems in computer science](https://en.wikipedia.org/wiki/P_versus_NP_problem). Today we do not know any effective algorithm for it. But we still cannot proof that _there isn't such algorithm_. Highly likely there isn't of course and $P \neq NP$ but no one can proof it.
 ```
