---
title: "verilator"
description: "Open-source compiler/simulator for syntehsizable Verilog or SystemVerilog"
authors:
  - "Wilson Snyder"
links:
  web: https://www.veripool.org/wiki/verilator
  gh: verilator/verilator
categories: [
  "Tools",
  "Tools:Simulators"
]
tags: [
  "analiser",
  "compiler",
  "simulator",
  "verilog",
  "systemverilog",
]
licenses: [
  "LGPL-3.0-only",
  "Artistic-2.0"
]
active:
  from: 2003
talk: 110
---

Verilator is "the fastest free Verilog HDL simulator". From a verification
perspective it supports *line coverage*, *signal toggle coverage* and limited
specification of *functional coverage* using SystemVerilog Assertions.
It also allows one to write testbenches in C++ or SystemC.

<!--more-->

- Written In: C++
- Write testbenches in: C++/SystemC
- Supports: Design simuation, *Coverage collection from simulations*.
