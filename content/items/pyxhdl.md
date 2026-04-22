---
title: PyXHDL - Python Frontend For VHDL And Verilog
description: Use the power of the Python ecosystem to model hardware and generate directly SystemVerilog (>= 2012) and VHDL (>= 2008) source code.
authors:
  - Davide Libenzi
links:
  gh: davidel/pyxhdl
  docs: https://github.com/davidel/pyxhdl/blob/main/README.md
categories: [
  "Languages",
  "Frameworks",
  "Tools"
]
tags: [
  "HDL",
  "Python",
  "RTL",
  "Verilog",
  "SystemVerilog",
  "VHDL",
  "FPGA",
  "ASIC"
]
active:
  from: 2023
licenses: [
  "Apache-2"
]
talk: 151
---

PyXHDL allows to write HDL code in Python, generating VHDL (>= 2008) and Verilog (SystemVerilog >= 2012) code to be used for synthesis and simulation.

PyXHDL does not try to create an IR to be lowered, but instead interprets Python AST code and maps that directly into the selected HDL backend code. The optimizations are left to the OEM HDL compiler used to syntesize the design.

The main advantage of PyXHDL is that you can write functions and modules/entities wihtout explicit parametrization. The function calls, and the modules/entities instantiations automatically capture the call/instantiation site types, similarly to what C++ template programming allows.

Even though user HDL code in Python can use loops and functions, by default everything will be unrolled in the final VHDL/Verilog code (this is what the synthesis will do anyway, since there are no loops or function calls in HW).
