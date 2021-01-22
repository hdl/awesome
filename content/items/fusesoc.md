---
title: fusesoc
description: Package manager and build abstraction tool for FPGA/ASIC development
authors:
  - Olof Kindgren
links:
  gh: olofk/fusesoc
  docs: https://fusesoc.readthedocs.io/en/latest
categories: [
  "Cores:Collection",
  "Tools",
  "Tools:Package Managers"
]
tags: [
  "vhdl",
  "verilog",
  "eda",
  "hdl",
  "rtl",
  "synthesis",
  "FPGA",
  "simulation",
  "Xilinx",
  "Altera"
]
active:
  from: 2011
licenses: [
  "BSD-2-Clause"
]
talk: 64
---

FuseSoC is a package manager and a set of build tools for HDL code.
Its main purpose is to increase reuse of IP cores and be an aid for creating, building and simulating SoC solutions.
FuseSoC provides utilities for:

* reusing existing cores
* creating compile-time or run-time configurations
* running regression tests against multiple simulators
* porting designs to new targets
* leting other projects use your code

References:

- [fusesoc-cores](https://github.com/fusesoc/fusesoc-cores): FuseSoC standard core library 
- [tiny-cores](https://github.com/fusesoc/tiny-cores): Collection of assorted small cores
- [edalize]({{< ref "/items/edalize" >}} "edalize") was part of FuseSoC
- FuseSoc is the continuation of [ORPSoC](https://github.com/scutwengxinqian/orpsoc)
