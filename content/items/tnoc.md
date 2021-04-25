---
title: "TNoC"
description: "NoC router implementation written in SystemVerilog"
authors:
  - Taichi Ishitani
links:
  gh: "taichi-ishitani/tnoc"
tags:
  - network-on-chip
  - ip-core
  - systemverilog
  - rtl
  - uvm
  - axi
categories:
  - Cores
licenses:
  - Apache-2.0 License
active:
  from: 2017
---

TNoC is a network on chip router implementation written in SystemVerilog.
TNoC has following features:

* 2-D mesh network
* Dimension order routing (X-Y routing)
* Flow control
    * Wormhole (FLIT based) flow control
    * Virtual channel flow control
    * On/Off Flow control
* Configurable design
    * Packet format
    * Mesh size
    * FIFO size
    * etc.
* Support standard bus protocol
    * AMBA AXI4

In addition, UVM based test environments are included.
