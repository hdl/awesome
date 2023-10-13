---
title: "SystemRDL Compiler"
description: "SystemRDL language compiler front-end"
authors:
  - Alex Mykyta
links:
  gh: "SystemRDL/systemrdl-compiler"
  docs: "https://systemrdl-compiler.readthedocs.io"
tags:
  - SystemRDL
  - language-model
  - parser
  - compiler
  - code-generator
  - Python
  - configuration-register
  - csr
categories:
  - "Tools:CSR Automation"
licenses:
  - MIT
active:
  from: 2017
talk: 241
---

SystemRDL is a domain specific language used to describe control/status
registers (CSR) that define a hardware/software boundary for hardware
peripherals. By describing the structure of a CSR in SystemRDL, one can create a single source of truth specification for CSR automation and code generation.

The `systemrdl-compiler` project implements a generic compiler front-end for
Accellera's [SystemRDL 2.0](http://accellera.org/downloads/standards/systemrdl)
register description language. The goal of this project is to provide a free and
open compiler that lowers the barrier to entry to using an industry standard
register description language.

By providing an elaborated register model that is easy to traverse and query,
it should be far easier to write custom register space view generators.
