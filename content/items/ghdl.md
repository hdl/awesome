---
title: "GHDL"
description: "Open-source analyzer, compiler, simulator and synthesizer for VHDL"
authors:
  - "Tristan Gingold"
links:
  gh: ghdl/ghdl
  docs: https://ghdl.github.io/ghdl
categories: [
  "Tools",
  "Tools:Simulators",
  "Tools:Synthesizers"
]
tags: [
  "analiser",
  "compiler",
  "simulator",
  "synthesis",
  "parser",
  "VHDL",
]
licenses: [
  "GPL-2.0-or-later"
]
active:
  from: 2002
talk: 100
---

Open-source analyzer, compiler, simulator and (experimental) synthesizer for VHDL, a Hardware Description Language (HDL). GHDL is not an interpreter: it allows you to analyse and elaborate sources to generate machine code from your design. Native program execution is the only way for high speed simulation.

Full support for the 1987, 1993, 2002 versions of the IEEE 1076 VHDL standard, and partial for the latest 2008 revision. Partial support of PSL. Can write waveforms to a GHW, VCD or FST file. Combined with a GUI-based waveform viewer and a good text editor, GHDL is a very powerful tool for writing, testing and simulating your code.

References:

- [ghdl-yosys-plugin]({{< ref "/items/ghdl-yosys-plugin" >}} "ghdl-yosys-plugin")
- [ghdl/ghdl-cosim](https://github.com/ghdl/ghdl-cosim)
- [ghdl/ghdl-language-server](https://github.com/ghdl/ghdl-language-server)
- [ghdl/setup-ghdl-ci](https://github.com/ghdl/setup-ghdl-ci)
- [ghdl/docker](https://github.com/ghdl/docker)
- [ghdl/extended-tests](https://github.com/ghdl/extended-tests)
