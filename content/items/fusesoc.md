---
title: fusesoc
description: Package manager and build abstraction tool for FPGA/ASIC development
authors:
  - Olof Kindgren
links:
  gh: rolofk/fusesoc
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
  from: 2014
licenses: [
  "BSD-2-Clause"
]
talk: 64
---

FuseSoC is an award-winning package manager and a set of build tools for HDL (Hardware Description Language) code.

Its main purpose is to increase reuse of IP (Intellectual Property) cores and be an aid for creating, building and simulating SoC solutions.

FuseSoC makes it easier to

* reuse existing cores
* create compile-time or run-time configurations
* run regression tests against multiple simulators
* Port designs to new targets
* let other projects use your code
* set up continuous integration


References:

- [fusesoc-cores](https://github.com/fusesoc/fusesoc-cores): FuseSoC standard core library 
- [tiny-cores](https://github.com/fusesoc/tiny-cores): Collection of assorted small cores
- [edalize]({{< ref "/items/edalize" >}} "edalize") was part of FuseSoC
- FuseSoc is the continuation of [ORPSoC](https://github.com/scutwengxinqian/orpsoc)
