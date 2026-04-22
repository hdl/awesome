---
title: "PeakRDL"
description: "Control & Status register (CSR) automation toolchain"
authors:
  - Alex Mykyta
links:
  gh: "SystemRDL/PeakRDL"
  docs: "https://peakrdl.readthedocs.io"
tags:
  - SystemRDL
  - code-generator
  - Python
  - configuration-register
  - csr
  - verilog
  - systemverilog
  - documentation
  - UVM-reg
  - RTL
  - abstract
categories:
  - "Tools:CSR Automation"
licenses:
  - GPL-3.0
active:
  from: 2018
talk: 241
---

PeakRDL is a free and open-source control & status register (CSR) automation
toolchain. This project provides a command-line tool that unifies many aspects of register automation centered around the SystemRDL register description language.

This tool can:

* Process SystemRDL 2.0 register descriptions.
* Import & export IP-XACT XML.
* Generate synthesizable SystemVerilog RTL register blocks using APB, AXI4-Lite, Avalon, and other interfaces.
* Create rich and dynamic HTML documentation.
* Build a UVM register model abstraction layer.
* Generate C headers for software.
* ... or be extended with your own plugin to generate other outputs

## References

- [SystemRDL Compiler]({{< ref "/items/systemrdl-compiler" >}} "SystemRDL Compiler")
- [PeakRDL-cheader](https://github.com/SystemRDL/PeakRDL-cheader)
- [PeakRDL-html](https://github.com/SystemRDL/PeakRDL-html)
- [PeakRDL-ipxact](https://github.com/SystemRDL/PeakRDL-ipxact)
- [PeakRDL-regblock](https://github.com/SystemRDL/PeakRDL-regblock)
- [PeakRDL-systemrdl](https://github.com/SystemRDL/PeakRDL-systemrdl)
- [PeakRDL-uvm](https://github.com/SystemRDL/PeakRDL-uvm)
