---
title: "TVIP-AXI"
description: "UVM based AMBA AXI VIP"
authors:
  - Taichi Ishitani
links:
  gh: "taichi-ishitani/tvip-axi"
tags:
  - vip
  - amba
  - axi
  - uvm
  - systemverilog
categories:
  - Verification
licenses:
  - Apache License 2.0
active:
  from: 2018
talk: 211
---

TVIP-AXI is an UVM based AMBA AXI4 VIP.

* Support master and slave agent
* Highly configurable
    * address width
    * data width
    * ID width
* Response ordering
    * in-order response
    * out-of-order response
* Support response interleaving
* Include UVM reg adapter and predictor
