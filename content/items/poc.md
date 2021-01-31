---
title: "Pile of Cores Library (PoC)"
description: "A library of free, open-source and platform independent IP cores"
authors: []
links:
  gh: VLSI-EDA/PoC
  docs: https://poc-library.readthedocs.io/en/latest
categories: [
  "Cores",
  "Cores:Library"
]
tags: [
  "library",
  "ip-core",
  "vhdl",
]
active:
  from: 2014
licenses: [
  "Apache-2.0"
]
talk: 26
---

PoC - “Pile of Cores” provides implementations for often required hardware
functions such as Arithmetic Units, Caches, Clock-Domain-Crossing Circuits,
FIFOs, RAM wrappers, and I/O Controllers. The hardware modules are typically
provided as VHDL or Verilog source code, so it can be easily re-used in a
variety of hardware designs.

All hardware modules use a common set of VHDL packages to share new VHDL types,
sub-programs and constants. Additionally, a set of simulation helper packages
eases the writing of testbenches. Because PoC hosts a huge amount of IP cores,
all cores are grouped into sub-namespaces to build a better hierarchy.

Various simulation and synthesis tool chains are supported to interoperate with
PoC. To generalize all supported free and commercial vendor tool chains, PoC is
shipped with a Python based infrastructure to offer a command line based
frontend.

References:

- [pyIPCMI]({{< ref "/items/pyipcmi" >}} "pyIPCMI")
