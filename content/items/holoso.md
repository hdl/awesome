---
title: Holoso
description: High-level synthesis of idiomatic Python into synthesizable and verifiable Verilog
authors:
  - Pavel Kirienko <pavel.kirienko@zubax.com>
links:
  gh: Zubax/holoso
  web: http://holoso.digital/
tags:
  - high-level-synthesis
  - Python
  - Verilog
  - RTL
  - DSP
categories:
  - "Tools:Synthesizers"
licenses:
  - Apache-2.0
active:
  from: 2026
---

Holoso turns numerical, control, and DSP kernels written in an ordinary Python into portable Verilog, and emits a Cocotb testbench for co-simulation.

Holoso doesn't require rewriting the kernel source for synthesis, unlike all existing (as of 2026) Python-source HLS. The core idea is that whatever code was written in regular Python to simulate and analyze the system (using NumPy with linear algebra etc) can be fed directly into the synthesizer as-is. This can dramatically simplify the simulation and verification and speed up design iteration.

Holoso doesn't generate II≈1 pipelines; instead, it builds a custom VLIW-like CPU core with statically scheduled microcode and the minimal required set of operators. This approach enables very fabric-efficient and low-latency modules that beat softcores by orders of magnitude while using less fabric area than conventional pipelines. The downside is that the initiation interval is ultimately data-dependent.

An interactive browser playground is available at <http://holoso.digital>.
