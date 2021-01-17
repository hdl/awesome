---
title: pyVHDLModel
description: An abstract language model of VHDL written in Python
authors:
  - Patrick Lehmann
links:
  gh: vhdl/pyVHDLModel
  docs: https://vhdl.github.io/pyVHDLModel
tags: [
  "abstract",
  "dom",
  "language-model",
  "python",
  "vhdl",
]
talk: 57
---

# Main Goals
This Python package provides a unified abstract language model for VHDL. Projects
reading from source files can derive own classes and implement additional logic
to create a concrete language model for their tools.

Projects consuming pre-processed VHDL data (parsed, analyzed or elaborated) can
build higher level features and services on such a model, while supporting
multiple frontends.

## Use Cases
* High-level API for [GHDL's]({{< ref "/items/ghdl" >}} "GHDL") libghdl offered as Python package `pyGHDL.dom`.
* Code Document-Object-Model (Code-DOM) in [pyVHDLParser]({{< ref "/items/pyvhdlparser" >}} "pyVHDLParser").
