---
title: PipelineC
description: Open source C-like hardware description language with high-level-synthesis-like automatic pipelining and several other real life design inspired features.
authors:
  - Julian Kemmerer
links:
  gh: JulianKemmerer/PipelineC
categories: [
  "Languages",
  "Frameworks"
]
tags: [
  "C",
  "HDL",
  "RTL",
  "VHDL",
  "Python"
]
active:
  from: 2018
licenses: [
  "GPL-3.0"
]
talk: 228
---

*"Fundamental design elements are state machines/stateful elements(registers, rams, etc), auto-pipelined stateless pure functions, and interconnects (wires, cdc, async fifos, etc).*

*By isolating complex logic into autopipelineable functions, and only writing literal clock by clock hardware description when absolutely necessary, PipelineC designs do not need to be rewritten for each new target device / operating frequency.*
*The hope is to build shared, high performance, device agnostic, hardware designs described in a familiar and powerfully composable C language look.*

*For software folks PipelineC should feel like solving a programming puzzle in C where the rules of the puzzle hide/imply hardware concepts. For hardware folks I want PipelineC to be a better hardware description language."*
