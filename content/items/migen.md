---
title: migen/nMigen
description: A Python toolbox for building complex digital hardware
authors:
  - "M-Labs Limited"
  - "whitequark"
links:
  gh: m-labs/migen
  web: https://m-labs.hk/migen
categories: [
  "Languages",
  "Frameworks"
]
tags: [
  "HDL",
  "FHDL",
  "Python",
  "RTL"
]
active:
  from: 2011
licenses: [
  "BSD-2-Clause"
]
talk: 19
---

*"Despite being faster than schematics entry, hardware design with Verilog and VHDL remains tedious and inefficient for several reasons. The event-driven model introduces issues and manual coding that are unnecessary for synchronous circuits \[...\]. To address those issues, we have developed the Migen FHDL, a library that replaces the event-driven paradigm with the notions of combinatorial and synchronous statements, has arithmetic rules that make integers always behave like mathematical integers, and most importantly allows the design's logic to be constructed by a Python program."*

*"nMigen is based on Migen \[...\]. Although Migen works very well in production, its design could be improved in many fundamental ways, and nMigen reimplements Migen concepts from scratch to do so. nMigen also provides an extensive compatibility layer that makes it possible to build and simulate most Migen designs unmodified, as well as integrate modules written for Migen and nMigen."*

nMigen is *"A refreshed Python toolbox for building complex digital hardware"*, which first commit dates at late 2018.

References:

- [litex]({{< ref "/items/litex" >}} "LiteX")
- [nmigen/nmigen](https://github.com/nmigen/nmigen)
  - [nmigen.info/nmigen](https://nmigen.info/nmigen/)
- [m-labs/nmigen](https://github.com/m-labs/nmigen)
  - [nmigen.org/](https://nmigen.org/)
