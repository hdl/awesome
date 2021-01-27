---
title: "VUnit"
description: "Open source unit testing framework for VHDL/SystemVerilog"
authors:
  - Lars Asplund
  - Olof Kraigher
links:
  gh: VUnit/vunit
  web: http://vunit.github.io
categories: [
  "Frameworks",
  "Frameworks:Verification"
]
tags: [
  "framework",
  "testing",
  "verification",
  "vhdl",
  "systemverilog",
]
active:
  from: 2014
licenses: [
  "MPL-2.0"
]
talk: 38
---

*"VUnit is an open source unit testing framework for VHDL/SystemVerilog \[...\]  It features the functionality needed to realize continuous and automated testing of your HDL code. VUnit doesn’t replace but rather complements traditional testing methodologies by supporting a “test early and often” approach through automation."*

<!--more-->

VUnit includes:

- A library and test configuration API (Python).
- A simulator interfacing module (API), and a test management plumbing written in Python and HDL (VHDL and System Verilog).
- Multiple optional HDL libraries providing utilities for verification (checks, communication, VCs/BFMs, etc.).
- A customizable CLI for integration into ad-hoc workflows and CI services.

[OSVVM]({{< ref "/items/osvvm" >}} "OSVVM") and [JSON-for-VHDL]({{< ref "/items/json-for-vhdl" >}} "JSON-for-VHDL") are submodules of VUnit. The former provides randomization features, and the latter allows passing arbitrarily complex generics from Python to the HDL testbenches.

- Written In: Python/VHDL/System Verilog
- Write Testbenches In: VHDL/System Verilog
