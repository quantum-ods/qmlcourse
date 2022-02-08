(intro1)=

# About quantum computers, bitcoin and advantage

Author(s):

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

```{figure} /_static/intro1block/intro1/Moores_Law.png
:name: moores_law

A Moore law illustration; a growth of the number of transistors from 1970s
```

A law that is named a Moore law was formulated by Gordon Moore in the late 60-s. It tell us that the number of transistors by crystal of integral circuit is adding twice every two years. And it have been holding true for the last 60 years.

### Quality evolution of computers

Unfortunately the Moore law holding cannot be endless because there are physical limitations: sooner or later the direct adding twice of the number of transistors could be impossible due tunneling effects. That's why this is said that the modern computers will have a "quality" revolution. Some say about new materials for creating transistors. Another say about new principles of computers. For example about photonic computers where photons are used instead electrons. But one can hear that the next computers revolution will the invention of quantum computers. That is what we will talk about.

### The idea about quantum computers

There are few version who was the first one said about using quantum mechanic's laws for creating the new computer. Like it frequently happens a few scientist independently and at one time came to the same idea. One of them was Richard Phillips Feynman.

```{figure} /_static/intro1block/intro1/Feinman.jpg
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

```{figure} /_static/intro1block/intro1/Shor.png
:name: shor

Piter Shor. The man who set the world on fire with his algorithm.
```

This algorithm will crack the bitcoin and ruin the banking system in the future. But it's not all that simple: evolution of quantum computers threw scientists to creating of _post-quantum_ cryptography that is based on tasks which cannot be effectively solved on both classical and quantum computers.

### Combinatorial and NP-hard problems

Except for difficulties with Moore law there is another problem with classical computers. There are tasks that likely wont be solved effectively on the classical Turing computer. Even on photonic or grafen one. The good example is the knapsack problem. When we have a knapsack of limited volume and a lot of things with different size and cost. And we want to fill our knapsack in such a manner to maximize the total cost of things inside it. The task looks very simple but it is an example of [$NP$-complete problems](https://en.wikipedia.org/wiki/NP-completeness). If we have a big number of different things and a relative big knapsack such problem cannot be solved exactly in reasonable time. Even the finding of the good enough _approximate_ solution of such problem is very hard today!

```{note}
I used a word "likely" because the question about existence of the effective solution of NP-complete problems is one of [the major unsolved problems in computer science](https://en.wikipedia.org/wiki/P_versus_NP_problem). Today we do not know any effective algorithm for it. But we still cannot proof that _there isn't such algorithm_. Highly likely there isn't of course and $P \neq NP$ but no one can proof it. 
```

Так вот, дело в том, что для квантовых компьютеров уже сегодня известны алгоритмы, которые позволяют потенциально эффективно, пусть и _приближенно_ решать такие задачи на квантовом компьютере. Это задача коммивояжера, задача о рюкзаке, задача кластеризации графа и много других задач комбинаторной оптимизации. В нашем курсе будет целый блок, посвященный таким квантовым алгоритмам как _Variational Quantum Eigensolver_ и _Quantum Approximate Optimization Algorithm_.

```{figure} /_static/intro1block/intro1/Salesman.png
:name: salesman

Визуализация решения задачи коммивояжера -- кратчайший путь, чтобы объехать 12 немецких городов -- очень важная задача современной логистики
```

### Симуляция квантовой механики

Это то, ради чего Фейнман предложил создать квантовые компьютеры. Это отдельная большая тема, где много квантовой механики. Ей будет посвящено сразу несколько отдельных лекций нашего курса. Но попробуем объяснить в двух словах, не вдаваясь в детали.

Дело в том, что задачи квантовой механики не получается решать аналитически. Казалось бы, в чем проблема, законы Ньютона уже для трех тел тоже аналитически не решаются, но это не мешает нам летать в космос, ведь такую задачу можно решить _численно_. Но ту приходит вторая проблема, а именно, что явно интегрировать уравнение Шредингера по времени, или, по простому, решать квантовую механику _численно_ тоже вычислительно почти невозможно более чем для двух частиц.

```{figure} /_static/intro1block/intro1/Schrodinger.jpg
:width: 350px
:name: schrodinger

Эрвин Шредингер, 1887-1961, создатель знаменитого уравнения и мема про кота
```

Казалось бы, что нам с этого. Ведь квантовая механика это удел теоретиков. Но вот проблема, квантовая механика лежит в основе квантовой химии, а та, в свою очередь, лежит в основе вообще всей химии и таких ее прикладных направлений, как создание новых лекарств, разработка новых аккумуляторов для автомобилей Tesla и многого другого. И сегодня мы вынуждены использовать лишь очень приближенные решения и концепции, точности которых часто не хватает.

Квантовые компьютеры в этом случае могут сделать реальный прорыв. Ведь в силу своей физической природы, квантовый компьютер идеально подходит для симуляции квантовой механики, а значит и решения столь важных сегодня задач из области разработки лекарств и дизайна новых материалов.

### Машинное обучение и искусственный интеллект

За последние 10-15 лет машинное обучение достигло поистине небывалых высот в своем развитии. Многие задачи, решение которых силами компьютера, раньше казалось невозможным сегодня успешно решаются при помощи машинного обучения. Примеры таких задач это, например, игра в Go, различение пород чихуахуа по фотографии, распознавание лиц в видеопотоке, составление относительно осмысленных текстов и генерация картин в стиле Пикассо из простых фотографий. Но оно все еще очень далеко от возможностей человеческого мозга. Так, наиболее масштабные искусственные нейронные сети, по примерным оценкам, имеют сегодня размер, эквивалентный 15 миллионам нейронов, в то время как человеческий мозг имеет порядка 85 миллиардов! Вызывает вопросы также и скорость обучения современных нейронных сетей. Так, самые большие языковые модели сегодня обучаются неделями на кластерах из тысяч видеокарт, в то время как человек с его относительно скромными вычислительными возможностями учится говорить всего 2-3 года.

И тут тоже на помощь могут прийти квантовые компьютеры. В данном случае, квантовые аналоги нейронных сетей, а также их комбинации с классическими нейронными сетями уже сегодня показывают впечатляющие результаты. Так, есть работы, где показано, что 4 квантовых нейрона по своей выразительности эквивалентны классической искусственной нейронной сети с $\sim 250$ нейронами!

Именно квантовому машинному обучению, а также способам его применения и будет посвящена большая часть нашего курса. Мы постараемся рассмотреть все вопросы по этой теме, начиная от теории того, как можно строить квантовые алгоритмы машинного обучения и заканчивая тем, как их можно запрограммировать на современных языках квантового программирования. Если эта тема вам интересна, то этот курс точно для вас!

## Ну и когда взломают биткоин?

Наверное это один из главных вопросов, которые возникают при чтении подобных статей. И ответим сразу: взломают нескоро, времени еще много, 10 лет точно есть.

```{figure} /_static/intro1block/intro1/Bitcoin.jpg
:width: 400px
:name: bitcoin

Биткоин, как и многие другие электронные средства вынуждены будут перейти на пост-квантовую криптографию
```

### Сколько нужно кубитов под разные задачи?

Наверное сразу стоит оценить тот размер, который квантовый компьютер должен иметь для эффективного решения описанных выше задач. Примерно цифры такие:

- Алгоритм Шора и взлом современной криптографии (включая биткоин): $\sim 20\cdot 10^6$ (20 миллионов) кубит
- Задачи оптимизации: $\sim 100 \cdot 10^3$ (100 тысяч) кубит
- Первые полезные задачи в квантовой химии: $\sim 1\cdot 10^3$ (1 тысяча) кубит
- Квантовое машинное обучение: $\sim 100-500$ кубит

Это кстати одна из причин, почему наш курс посвящен по большей части именно квантовому машинному обучению.

### Логические vs Физические кубиты

Есть еще такая проблема, что вся квантовая механика вероятностная. А еще, что квантовые компьютеры работают в области микромира и очень чувствительны к любым шумам извне. Это ведет к совершенно недопустимому уровню ошибок в вычислениях и их низкой детерминированности. Например, сегодня хорошим уровнем точности для квантовых компьютеров является 99% на одну операцию. Но ведь каждый алгоритм включает в себя сотни или даже тысячи операций! И тогда уровень ошибок становится совсем печальным.

Но есть и хорошие новости. Сегодня существует очень много классных алгоритмов коррекции ошибок, которые позволяют используя несколько физических кубит с высоким уровнем ошибок создать один логический кубит, имеющий очень низкий уровень ошибок. То есть программист будет писать код, который производит операции над одним кубитом, а на физическом уровне это будет операция над несколькими кубитами. В общем вопрос вполне решаемый. Вот только для создания одного качественного логического кубита может потребоваться до тысячи физических кубит! А те оценки, которые мы привели выше, они как раз про логические кубиты, то есть кубиты с очень высокой точностью операций на уровне классических компьютеров.

### Сколько кубит есть сегодня?

Скажем сразу, сегодня уже существуют квантовые компьютеры. Вот только все производители, когда пишут о новом рекорде, имеют в виду чаще всего именно физические кубиты.

```{figure} /_static/intro1block/intro1/quantum_computer.jpg
:width: 350px
:name: qc

Квантовый компьютер компании IBM выглядит примерно так
```

Есть квантовые компьютеры с разной архитектурой. Одни имеют больше кубит, но и более высокий уровень ошибок. Другие имеют низкий уровень ошибок, но их трудно масштабировать. Теме квантового железа в нашем курсе будет посвящен отдельный блок из нескольких лекций. Но если кратко, то можно назвать примерно такие цифры:

- рекорд в относительно легко масштабируемых, но шумных квантовых компьютерах это $\sim 55$ кубит
- рекорд в относительно точных, но медленных и плохо масштабируемых компьютерах это $\sim 20$ кубит
- рекорд в точных и масштабируемых, но очень трудно программируемых компьютерах это $\sim 25$ кубит

```{note}
Тут мы имеем ввиду соответственно:
- сверхпроводящие кубиты, которые сегодня проще всего масштабировать
- ионы в ловушках, которые имеют одну из самых высоких точностей
- фотоны, которые вроде всем хороши, кроме того, что на них программирование это юстировка линз и лазеров на оптическом столе
```

Стоит добавить, что рекорд в точных и масштабируемых, а также программируемых (топологических) кубитах сегодня это ровно 2 кубита. Серьезно, взаимодействие двух логических кубит было опубликовано в `Nature` в этом году.

### Какие планы имеют ведущие игроки на этом рынке?

Казалось бы, с такими масштабами биткоину боятся нечего, да и в целом область выглядит не самой перспективной. Но есть один нюанс. Все крупные игроки на рынке создания квантовых компьютеров (_Google Quantum_, _IBM Quantum_, _IonQ_, _Xanadu_) озвучили планы к 2030-му году иметь порядка одного миллиона физических кубит, что эквивалентно порядка тысячи логических кубит. Для криптографии это еще не страшно, но вот многие полезные задачи уже можно будет попробовать решать. Ну и стоит еще раз посмотреть на график закона Мура для классических компьютеров, которые каждые десять лет показывают примерно такой же прогресс!

## О квантовом превосходстве

Очень часто можно услышать разговоры о том, что достигнуто или опровергнуто квантовое превосходство. Попробуем под конец лекции разобраться, что же это такое и почему это важно (или не важно).

### Понятие квантового превосходства

Само понятие было сформулировано еще в 2012-м году известным физиком теоретиком Джоном Прескиллом.

```{figure} /_static/intro1block/intro1/Preskill.jpg
:width: 350px
:name: preskill

Джон Прескил, который и придумал этот термин. Еще он известен своим знаменитым пари с другим физиком Стивеном Хокингом (которое Хокинг проиграл)
```

Квантовое превосходство это решение на квантовом компьютере задачи, которую нельзя решить на классическом компьютере за разумное время (10 тысяч лет разумным временем не считается). Достижение квантового превосходства это однозначно новый уровень в развитии квантовых вычислений. Но есть один подвох. Дело в том, что речь идет о совершенно любой задаче, независимо от того, насколько она полезна или бесполезна.

Так что когда кто-то заявляет о достижении квантового превосходства, то это важный повод для ученых и разработчиков квантовых компьютеров, но скорее всего это очень малозначимый факт, с точки зрения простого обывателя.

### Хронология событий

Ну и в конце приводим краткую хронологию событий.

- 2019 год, компания _Google_ заявляет о достижении квантового превосходства. Задача выбрана максимально удобная для квантового компьютера и полностью лишенная практического смысла. По словам разработчиков из _Google_ их квантовый компьютер за 4 минуты решил задачу, которую классический суперкомпьютер решал бы 10 тысяч лет. Их квантовый компьютер имел 54 кубита;
- 2019 год, компания _IBM_ заявляет, что _Google_ не учли, что их задачу можно решать на классическом компьютере более оптимально, но без экспериментов;
- 2020 год, компания _Alibaba_ реализует алгоритм _IBM_ на своем суперкомпьютере и решает задачу за $\sim 20$ дней;
- 2021 год, группа китайских ученых оптимизирует классический алгоритм и решает задачу на 60 видеокартах _NVIDIA_ за 7 дней;
- 2021 год, группа других китайских ученых заявляет, что достигла нового превосходства на квантовом компьютере из 56 кубит;

В общем сейчас идет довольно интересный процесс войны меча и щита. Пока одни ученые строят более мощные квантовые компьютеры, другие придумывают более продвинутые алгоритмы их симуляции. Хотя конечно все ученые говорят, что уже где-то на 60-70 кубитах эта история окончательно закончится в пользу квантовых компьютеров.

## А как это вообще выглядит? И сколько стоит?

На сегодня почти все известные технологии создания квантовых компьютеров требуют чего-то из:

- сверхнизкие температуры
- сверхвысокий вакуум
- сверхточная юстировка лазеров на оптическом столе

Или даже всего сразу. Поэтому сегодня почти все квантовые компьютеры продаются через облачные сервисы. Например, относительно недавно ведущий поставщик облачных технологий -- компания _Amazon_ добавила в свой сервис `AWS` новый продукт [Amazon Braket](https://aws.amazon.com/braket/). Этот продукт позволяет взять в аренду самый настоящий компьютер точно также, как мы привыкли брать в аренду процессоры, видеокарты или жесткие диски. Аналогичные продукты сейчас предоставляют и другие крупные игроки на рынке облачных услуг. Хотя это все пока исключительно для целей исследования. Ведь как мы уже поняли, сегодня квантовые компьютеры еще не способны решать реальные задачи. Стоит такое развлечение не очень дорого, например, можно запустить свою квантовую программу на 32-х кубитном компьютере `Aspen-9` всего за $0.3 (per-task).

Некоторые производители идут дальше и предлагают относительно компактные решения. Так, недавно [было представлено 24-х кубитное решение](https://phys.org/news/2021-06-compact-quantum-server-centers.amp?__twitter_impression=true), которое помещается в две стандартных серверных стойки. Но масштабируемость таких устройств вызывает вопросы.

В любом случае, в ближайшие 15-20 лет точно не стоит ждать появление карманного квантового компьютера, или хотя бы квантового сопроцессора в домашнем ПК. Да и в этом нет особого смысла, ведь мало кому дома нужно взламывать биткоин, решать логистическую проблему или разрабатывать высокотемпературный сверхпроводник.

## Заключение

Это вводная лекция, она не даст вам каких-то особых знаний. Скорее, ее цель заинтересовать читателя. Самое интересное будет в основной части курса, где мы будем разбирать квантовые алгоритмы, пытаться симулировать квантовую механику и обучать самые настоящие квантовые нейросети! Ждем вас на курсе!

<p style="page-break-after:always;"></p>
