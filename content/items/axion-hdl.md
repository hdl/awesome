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
  - Tools
licenses:
  - MIT
active:
  from: 2024
---

Axion-HDL generates AXI4-Lite register interfaces from inline HDL annotations or standalone data files (YAML, TOML, XML, JSON). Registers are described directly inside VHDL or SystemVerilog source files using `@axion` comments, removing the need for a separate register description language.

Key features:

* **Annotation-based input:** describe registers with inline comments in existing VHDL/SystemVerilog source files; no separate RDL or XML file required
* **Multi-format input:** also accepts YAML, TOML, XML, and JSON as standalone register map descriptions
* **Multi-HDL output:** generates both VHDL and SystemVerilog register block modules from the same source
* **C header generation:** produces C headers with access macros for software integration
* **HTML documentation:** generates human-readable register map documentation
* **CDC support:** built-in clock domain crossing synchronizers, configurable per module
* **Subregisters and wide signals:** supports packing multiple fields into one address and auto-splitting 64-bit+ signals across addresses
* **Export:** round-trips back to YAML/TOML/XML/JSON for interoperability
* **Verified:** 300+ tests including GHDL RTL simulation via cocotb
