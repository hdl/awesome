---
title: "Icarus Verilog (iverilog)"
description: "Verilog simulation and synthesis tool"
authors:
  - "Stephen Williams"
links:
  web: http://iverilog.icarus.com
  gh: steveicarus/iverilog
categories: [
  "Tools",
  "Tools:Simulators",
  "Tools:Synthesizers"
]
tags: [
  "simulator",
  "synthesis",
  "verilog",
]
licenses: [
  "GPL-2.0-only"
]
active:
  from: 1998
talk: 15
---

Icarus Verilog is a Verilog simulation and synthesis tool. It operates as a compiler, compiling source code written in Verilog (IEEE-1364) into some target format. For batch simulation, the compiler can generate an intermediate form called vvp assembly. This intermediate form is executed by the `vvp` command. For synthesis, the compiler generates netlists in the desired format. 
