---
title: "Axion-HDL"
description: "AXI4-Lite register interface generator from HDL annotations or structured data files"
authors:
  - Bugra Tufan
links:
  gh: "bugratufan/axion-hdl"
  web: "https://axion-hdl.com"
  docs: "https://axion-hdl.readthedocs.io/en/stable/"
tags:
  - code-generator
  - axi4-lite
  - csr
  - configuration-register
  - vhdl
  - systemverilog
  - yaml
  - toml
  - c-header
  - documentation
  - cdc
  - RTL
  - Python
categories:
  - "Tools:CSR Automation"
licenses:
  - MIT
active:
  from: 2024
---

Axion-HDL generates AXI4-Lite register interfaces from inline HDL annotations or standalone data files (YAML, TOML, XML, JSON). Registers are described directly inside VHDL or SystemVerilog source files using `@axion` comments, removing the need for a separate register description language.

Axion-HDL can:

* Read register definitions from inline `@axion` comments in VHDL or SystemVerilog source files
* Read standalone register map files in YAML, TOML, XML, or JSON format
* Generate synthesizable VHDL and SystemVerilog AXI4-Lite register block modules
* Generate C headers with access macros for software integration
* Generate HTML register map documentation
* Export register maps back to YAML, TOML, XML, or JSON
* Insert built-in clock domain crossing (CDC) synchronizers, configurable per module
* Pack multiple fields into a single address (subregisters) and auto-split wide signals across addresses
