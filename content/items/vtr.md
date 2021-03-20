---
title: Verilog to Routing (VTR)
description: Open Source CAD Flow for FPGA Research
authors: []
links:
  web: https://verilogtorouting.org
  gh: verilog-to-routing/vtr-verilog-to-routing
categories: [
  "Frameworks",
  "Tools",
  "Tools:PnRs",
  "Tools:Synthesizers"
]
tags: [
  "synthesis",
  "packing",
  "placement",
  "routing",
  "sta",
  "verilog",
  "odin",
  "ABC",
  "VPR",
  "FASM",
]
active:
  from: 2011
licenses: [
  "MIT"
]
talk: 123
---

*"The Verilog-to-Routing (VTR) project is a world-wide collaborative effort to provide a open-source framework for conducting FPGA architecture and CAD research and development. The VTR design flow takes as input a Verilog description of a digital circuit, and a description of the target FPGA architecture."*

It performs:
* Elaboration & Synthesis (ODIN II)
* Logic Optimization & Technology Mapping (ABC)
* Packing, Placement, Routing & Timing Analysis (VPR)

*"to generate FPGA speed and area results. \[...\] VTR can also produce FASM to program some commercial FPGAs (via Symbiflow)."*

References:

- [Yosys]({{< ref "/items/yosys" >}} "Yosys")
- [Versatile Place and Route]({{< ref "/items/vpr" >}} "Versatile Place and Route")
- [SymbiFlow]({{< ref "/items/symbiflow" >}} "SymbiFlow")
- [FASM]({{< ref "/items/fasm" >}} "FASM")
