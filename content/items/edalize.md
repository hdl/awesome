---
title: edalize
description: An abstraction library for interfacing EDA tools
authors:
  - Olof Kindgren
links:
  gl: olofk/edalize
  docs: https://edalize.readthedocs.io/en/latest/
categories: [
  "Tools",
  "Tools:Managers"
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
  from: 2018
licenses: [
  "BSD-2-Clause"
]
talk: 63
---

Edalize is a Python Library for interacting with EDA tools. It can create project files for supported tools and run them in batch or GUI mode (where supported).

All EDA tools such as Icarus, Yosys, ModelSim, Vivado, Verilator, GHDL, Quartus etc get input HDL files (Verilog and VHDL) and some tool-specific files (constraint files, memory initialization files, IP description files etc). Together with the files, perhaps a couple of Verilog `defines, some top-level parameters/generics or some tool-specific options are set. Once the configuration is done, a simulation model, netlist or FPGA image is built, and in the case of simulations, the model is also executed, maybe with some extra run-time parameters.

The thing is, all these tools are doing this in completely different ways and there's generally no way to import configurations from one simulator to another.

Dread not! Edalize takes care of this for you. By telling Edalize what files you have, together with some info, what parametrization to use at compile- and run-time (e.g. plusargs, defines, generics, parameters), VPI library sources (when applicable) and any other tool-specific options not already mentioned, it will create the necessary project files and offer to build and run it for you.

References:

- edalize was part of [FuseSoC]({{< ref "/items/fusesoc" >}} "FuseSoC")
