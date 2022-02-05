---
title: "Electronic Design Automation Abstraction (EDA²)"
description: "Conceptual model for characterising the abstraction layers in Electronic Design Automation (EDA) projects based on Hardware Description Languages (HDLs)"
authors: []
links:
  gh: edaa-org
  web: https://edaa-org.github.io/
tags: [
  "verification",
  "vhdl",
  "verilog",
  "systemverilog",
  "CLI",
  "workflow",
  "data-model",
  "project",
  "configuration"
]
categories: [
  "Frameworks"
]
talk: 227
---

*"Electronic Design Automation Abstraction (EDA²) is a conceptual model for characterising the abstraction layers in Electronic Design Automation (EDA) projects based on Hardware Description Languages (HDLs). Its goal is the interoperability of diverse tools and languages, through documented interfaces.*

*EDA² aims to provide reference Python implementations and schemas of commonly needed software layers for (open source) EDA tooling/frameworks to reduce code duplication and reinventions of existing algorithms and data structures. Each layer solves the problems at a different abstraction level, hence, they are organised as an stack."*

<!--more-->

![](https://edaa-org.github.io/_images/model.png)

*"Although all the resources provided through EDA² can be used together, that is not a requirement. Third parties are expected to (re)use only the subset of layers that allows them to reduce the maintenance burden of their codebase, while preserving the functionality and UX expected by their user base. In fact, pyEDAA modules are based on Object Oriented Programming (OOP) patterns, to allow enhancements through inheritance and overriding.*

*See [Conceptual Model](https://edaa-org.github.io/ConceptualModel.html) and [Frequently Asked Questions (FAQ)](https://edaa-org.github.io/FAQ.html)."*
