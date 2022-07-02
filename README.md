<img src="./qmlcourse/logo.svg" align="left" width="178" height="178"></img>

# QMLCourse

<a href="https://quantum-ods.github.io/qmlcourse/" target="_blank">
    <img alt="shield_website_jb" src="https://img.shields.io/website?style=for-the-badge&up_color=blueviolet&up_message=nightly-build&url=https%3A%2F%2Fquantum-ods.github.io%2Fqmlcourse%2Fbook%2Findex.html">
</a>
<a href="https://ods.ai/tracks/qmlcourse" target="_blank">
    <img alt="shield_website_ods" src="https://img.shields.io/website?style=for-the-badge&up_color=critical&up_message=ods.ai&url=https%3A%2F%2Fods.ai%2Ftracks%2Fqmlcourse">
<a href="https://github.com/quantum-ods/qmlcourse/blob/master/LICENSE">
    <img alt="shield_license" src="https://img.shields.io/github/license/quantum-ods/qmlcourse?style=for-the-badge">
</a>
</a>

<p align="left">
  <a href="https://github.com/quantum-ods/qmlcourse/actions/workflows/pre-commit.yml">
    <img alt="pre_commit" src="https://github.com/quantum-ods/qmlcourse/actions/workflows/pre-commit.yml/badge.svg">
  </a>
  <a href="https://github.com/quantum-ods/qmlcourse/actions/workflows/deploy-book-master.yml">
    <img alt="deploy_book" src="https://github.com/quantum-ods/qmlcourse/actions/workflows/deploy-book-master.yml/badge.svg">
  </a>
  <a href="https://qmlc-web-page-stage.netlify.app/">
    <img alt="netlify_status" src="https://api.netlify.com/api/v1/badges/ff3a4d3f-49a9-47db-9335-364525652b89/deploy-status">
  </a>
</p>
</br>

> **Note**
> * Russian-only
> * English version translation help tube, visit [issue #399](https://github.com/quantum-ods/qmlcourse/issues/399) & [CONTRIBUTING.md](./CONTRIBUTING.md)

## Contributing

Refer to [Contributing Guide](./CONTRIBUTING.md) for the definition of all contributor roles.

### Discussions & Issues

Some ideas, suggestions, remarks, etc. you can write on the [discussions](https://github.com/quantum-ods/qmlcourse/discussions) page. Also, we have [issues](https://github.com/quantum-ods/qmlcourse/issues).

## Course Program

![](./qmlcourse/_static/index/program.png)

### How to read the schema?

- **BLUE** &mdash; introductory blocks covering prerequisites for the rest of the course;
- **GREEN** &mdash; the main flow of the course with simple introductory lectures on QC and QML;
- **YELLOW** &mdash; highly recommended facultative lectures which explain additional topics about QML and QC;
- **RED** &mdash; advanced-level lectures that deeply explain the math and the principles underlying QML.
- **WHITE** &mdash; career in quantum computations and quantum QML

## Build the book

Building the PDF-version of the book is very time-expensive and could not be automated via GutHub actions. If you want the PDF-version of the book you should run the following commands:

`xelatex` (Linux):

  ```
  git clone https://github.com/quantum-ods/qmlcourse.git
  cd qmlcourse/
  git checkout web-page-master
  cd latex/
  ```

  ```
  sudo apt-get install texlive-latex-recommended texlive-latex-extra \
                       texlive-fonts-recommended texlive-fonts-extra \
                       texlive-xetex latexmk
  ```

  ```
  xelatex -interaction nonstopmode qmlcourse.tex
  ```

## Team

The main authors, reviewers, editors, DevOps you can find [here](https://quantum-ods.github.io/qmlcourse/book/authors.html).

Content generators, to be agreed with [@SemyonSinchenko](https://github.com/SemyonSinchenko). See [Issues](https://github.com/quantum-ods/qmlcourse/issues) to pick up one of the open tasks and for updates; this list is not intended to be always up-to-date.

Also, all authors for some updates are participants special channel into community [ods.ai](https://ods.ai), join filling the form and write your nickname to orgs to add you to the channel.

## Join ODS

To join the ODS-community slack you need to fill the form [here](https://ods.ai/join-community). After filling the form contact us via [email](mailto:qmlcourse.ods@gmail.com) and send the ODS registration email and date of the registration. After that, we add you to the closed channel in the ODS Slack.

## Similar Projects

- [QuantumAlgorithms.org](https://github.com/Scinawa/quantumalgorithms.org) [ENG]: lecture notes for students about quantum algorithms and quantum machine learning. Compared to this project our lectures are more practice and programming-oriented. In our course, there are more entry-level and sci-pop lectures but in QuantumAlgorithms.org there are more hard math and strong proofs of theorems. Also, we pay less attention to fully-quantum algorithms and ML but pay more attention to the variational and hybrid quantum-classical things.
- [Qiskit-textbook](https://github.com/qiskit-community/qiskit-textbook) [ENG]: a textbook about learning quantum computing with qiskit. Compared to this project our course is more about ML, not the quantum protocols and algorithms. Also, we use `PennyLane` as the main quantum framework because it could be used with different backends including `Qiskit` and `CirQ`.
- [CERN Introductory Course](https://home.cern/news/announcement/computing/online-introductory-lectures-quantum-computing-6-november) [ENG]: A series of weekly lectures on the basics of quantum computing. The talks focus on the practical aspects of quantum computing and are organised by CERN openlab and the CERN Quantum Technology Initiative. They are given by Elias Fernandez-Combarro Alvarez, an associate professor in the Computer Science Department at the University of Oviedo in Spain since 2009 and a cooperation associate at CERN since earlier this year. Compared to that lectures our course is more practice and programming oriented. Also our course is open source and maintained by community compared to the CERN course which is maintained by the author Dr. Alvarez.
- [CERN Introductory Course (adopted version in russian)](https://russol.info/quantum) [RU]: The same as above but in russian and better adopted for entry-level poeple. Lectures are splitted to short parts and notes are commented and illustrated.

## Legal Issues

You can communicate with course orgs via [email](mailto:qmlcourse.ods@gmail.com). Please email us first if you found an intellectual property rights violation in the course materials or if you want to use the course materials, not under the CC-BY-4.0 License.
