---
title: Silice
description: Silice is an open source language that simplifies writing algorithms fully exploiting FPGA architectures
authors:
  - Sylvain Lefebvre
links:
  gh: sylefeb/Silice
categories: [
  "Languages",
  "Frameworks"
]
tags: [
  "HDL",
  "RTL",
  "verilog"
]
active:
  from: 2019
licenses: [
  "AGPL-3.0"
]
talk: 93
---

*"Silice makes it possible to write algorithms for FPGAs in the same way we write them for processors: defining sequences of operations, subroutines that can be called, and using control flow statements such as while and break. At the same time, Silice lets you fully exploit the parallelism and niceties of FPGA architectures, describing operations and algorithms that run in parallel and are always active, as well as pipelines. Silice remains close to the hardware: nothing gets obfuscated away. When writing an algorithm you are in control of what happens at which clock cycle, with predictable rules for flow control. Clock domains are exposed. In fact, Silice compiles to and inter-operates with Verilog: you can directly instantiate and bind with existing modules."*
