---
title: "Synth Explorer"
description: "Browser-based Compiler Explorer for RTL: synthesize with Yosys and GHDL in WebAssembly and inspect the netlist client-side"
authors: []
links:
  web: https://www.synthexplorer.dev
  gh: cachanova/synth-explorer
categories: [
  "Tools",
  "Tools:Synthesizers",
]
tags: [
  "synthesis",
  "verilog",
  "vhdl",
  "netlist",
]
licenses: [
  "Apache-2.0",
]
talk: 249
---

A browser-based "Compiler Explorer" for RTL. Yosys and GHDL are compiled to WebAssembly and run entirely client-side, so Verilog, SystemVerilog and VHDL-2008 sources are synthesized locally and never leave the browser.
<!--more-->
The synthesized netlist can be explored interactively by path, endpoint, fanin, fanout, or source location, making it useful for teaching synthesis, debugging elaboration, and quickly inspecting how HDL maps to gates.
