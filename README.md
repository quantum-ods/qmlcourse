<img src="./qmlcourseRU/logo.svg" align="left"></img>

# QMLCourse

<p align="left">
  <a href="https://github.com/SemyonSinchenko/qmlcourse/blob/master/LICENSE">
    <img alt="shield_license" src="https://img.shields.io/badge/license-CC--BY--4.0-brightgreen">
  </a>
  <a href="https://github.com/SemyonSinchenko/qmlcourse/discussions">
    <img alt="shield_discussions" src="https://img.shields.io/github/discussions/SemyonSinchenko/qmlcourse">
  </a>
  <a href="https://github.com/SemyonSinchenko/qmlcourse/actions/workflows/pre-commit-deploy-book.yml">
    <img alt="pre_commit_deploy_book" src="https://github.com/SemyonSinchenko/qmlcourse/actions/workflows/pre-commit-deploy-book.yml/badge.svg">
  </a>
  <a href="https://semyonsinchenko.github.io/qmlcourse/_build/html/book/index.html">
    <img alt="shield_website_jb" src="https://img.shields.io/website?up_color=orange&up_message=nightly-build&url=https%3A%2F%2Fsemyonsinchenko.github.io%2Fqmlcourse%2F_build%2Fhtml%2Fbook%2Findex.html">
  </a>
  <a href="https://ods.ai/tracks/qmlcourse">
    <img alt="shield_website_ods" src="https://img.shields.io/website?up_color=critical&up_message=ods.ai%20course&url=https%3A%2F%2Fsemyonsinchenko.github.io%2Fqmlcourse%2F_build%2Fhtml%2Fbook%2Findex.html">
  </a>
</p>

</br>

## About

| Note: the course is under active development and, for now, is Russian-only! |
| --------------------------------------------------------------------------- |


This is the main repository of the course.

1. [Contributing Guide](#contributing-guide)
2. [Discussions](#discussions)
3. [Course Program](#course-program)
4. [Team](#team)
5. [Join ODS](#join-ods)
6. [Similar Projects](#similar-projects)
7. [Bibtex Citations](#bibtex)
8. [Legal Issues](#legal-issues)

## Contributing Guide

[Contributing Guide](./CONTRIBUTING.md)

## Discussions

Some ideas, suggestions, remarks, etc. you can write on a separate page [here](https://github.com/SemyonSinchenko/qmlcourse/discussions).

## Course Program

![](./qmlcourseRU/_static/index/program.png)

### How to read the schema?

- **BLUE** &mdash; introductory blocks covering prerequisites for the rest of the course;
- **GREEN** &mdash; the main flow of the course with simple introductory lectures on QC and QML;
- **YELLOW** &mdash; highly recommended facultative lectures which explain additional topics about QML and QC;
- **RED** &mdash; advanced-level lectures that deeply explain the math and the principles underlying QML.
- **WHITE** &mdash; career in quantum computations and quantum QML

## Team

There is a not full list of core members. The first is the nickname in the ODS slack and the second is the GitHub account.

### Contributor roles

Here we list all team members according to their contributor roles. Refer to [CONTRIBUTING.md](https://github.com/SemyonSinchenko/qmlcourse.ai/blob/master/CONTRIBUTING.md) for the definition of all contributor roles.

### Benevolent Dictator

Semyon Sinchenko, @sem ([GitHub](https://github.com/SemyonSinchenko))

### Core reviewers

- @evgeniyzh ([GitHub](https://github.com/Randl))
- @gamlo ([GitHub](https://github.com/ooovector))
- @Sergei Shirkin ([GitHub](https://github.com/SergeiShirkin))

To be extended based on the actual commitment and qualification of all contributors.

### Reviewers

By default that's everyone who is invited to the #org_qml_course Slack channel.

### Authors

Content generators, to be agreed with Benevolent Dictator. See [Issues](https://github.com/SemyonSinchenko/qmlcourse.ai/issues) to pick up one of the open tasks and for updates; this list is not intended to be always up-to-date.

Also, all authors for some updates are participants special channel into community ods.ai, join filling the form and write your nickname to orgs to add you to the channel.

- @stm ([GitHub](https://github.com/stalkermustang)): Python
- @maruschin ([GitHub](https://github.com/maruschin)): Python
- @sharthZ23 ([GitHub](https://github.com/sharthZ23)): Python, NumPy
- @alex.ozerin ([GitHub](https://github.com/m12sl)): NumPy, math
- @yorko ([GitHub](https://github.com/Yorko)): ML intro, advanced SVM
- @nkarelin ([GitHub](https://github.com/karelin)): quantum entropy and mixed states
- @gamlo ([GitHub](https://github.com/ooovector)): hardware
- @Sergei Shirkin ([GitHub](https://github.com/SergeiShirkin)): PennyLane, Deutsch, Grover
- @sem ([GitHub](https://github.com/SemyonSinchenko)): multiple lectures
- @zimka ([GitHub](https://github.com/zimka)): quantum chemistry
- @Aleksandr Berezutskii ([GitHub](https://github.com/meandmytram)): D-Wave, Barren plateau

### Editors

- @nmarkova ([GitHub](https://github.com/nsmarkova))

### Orgs

- @yorko ([GitHub](https://github.com/Yorko))
- @vtrohimenko ([GitHub](https://github.com/vtrokhymenko))

### DevOps

- @Korzhov Dmitry ([GitHub](https://github.com/dkorzhov))

## Join ODS

To join the ODS-community slack you need to fill the form [here](https://ods.ai/join-community). After filling the form contact us via [email](mailto:qmlcourse.ods@gmail.com) and send the ODS registration email and date of the registration. After that, we add you to the closed channel in the ODS Slack.

## Similar projects

- [QuantumAlgorithms.org](https://github.com/Scinawa/quantumalgorithms.org) [ENG]: lecture notes for students about quantum algorithms and quantum machine learning. Compared to this project our lectures are more practice and programming-oriented. In our course, there are more entry-level and sci-pop lectures but in QuantumAlgorithms.org there are more hard math and strong proofs of theorems. Also, we pay less attention to fully-quantum algorithms and ML but pay more attention to the variational and hybrid quantum-classical things.
- [Qiskit-textbook](https://github.com/qiskit-community/qiskit-textbook) [ENG]: a textbook about learning quantum computing with qiskit. Compared to this project our course is more about ML, not the quantum protocols and algorithms. Also, we use `PennyLane` as the main quantum framework because it could be used with different backends including `Qiskit` and `CirQ`.

## Bibtex

```bibtex
@misc{qmlcourse2021,
  author = {Sinchenko SA et al.},
  title = {QMLCourse},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/SemyonSinchenko/qmlcourse.ai}},
}
```

## Legal Issues

You can communicate with course orgs via [email](mailto:qmlcourse.ods@gmail.com). Please email us first if you found an intellectual property rights violation in the course materials or if you want to use the course materials, not under the CC-BY-4.0 License.
