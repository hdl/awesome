---
title: pyFPGA
description: A Python package to use FPGA development tools programmatically
authors:
  - Rodrigo Alejandro Melo
links:
  gl: rodrigomelo9/pyfpga
  docs: https://rodrigomelo9.gitlab.io/pyfpga
categories: [
  "Tools",
  "Tools:Managers"
]
tags: [
  "vivado",
  "ise",
  "quartus",
  "libero",
  "ghdl",
  "yosys",
  "nextpnr",
  "icestorm",
  "trellis",
  "vhdl",
  "verilog",
  "python",
  "tcl"
]
active:
  from: 2019
licenses: [
  "GPL-3.0-or-later"
]
talk: 58
---

PyFPGA is a Python Class for vendor-independent FPGA development.
It allows using a single project file and programmatically executing synthesis, implementation, generation of bitstream and/or transference to supported boards.

* The workflow is command-line centric.
* It's friendly with Version Control Systems and Continuous Integration (CI).
* Allows reproducibility and repeatability.
* Consumes fewer system resources than GUI based workflows.

Also, some command-line helpers are provided, for quick tests or small projects.
