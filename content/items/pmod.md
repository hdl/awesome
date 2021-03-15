---
title: Digilent PMOD Interface Specification
description: Low frequency, low I/O pin count Peripheral Module interface specification
authors: []
links:
  doc: https://reference.digilentinc.com/reference/pmod/start
tags: []
talk: 178
---

PMOD is an interface specification for low frequency and low I/O pin count peripherals, based on standard 100 mil spaced, 25 mil square, pin-header style connectors. Connectors can have one or two rows, each of them with 6 pins, 2 of which correspond to Vcc and GND. Additionally, the Digilent Pmod Standard lays out guidelines for form factor and communication protocols.

{{< note >}}
Version 1.0.0 of the specification defined 2x4 connectors too, for I2C interfaces. However, those were removed in later versions. The latest version is [Digilent Pmod™ Interface Specification v1.3.0](https://reference.digilentinc.com/_media/reference/pmod/pmod-interface-specification-1_3_0.pdf).
{{< /note >}}

<!--more-->

Despite the main supplier of PMOD compliant peripherals being Digilent, several other vendors, makers and open source boards use it as well. Moreover, some of them provide peripherals which use two dual-row PMODs, for a total 24 pin count.

- [store.digilentinc.com/pmod-modules-connectors](https://store.digilentinc.com/pmod-modules-connectors/)
- [shop.trenz-electronic.de/en/Products/Digilent/Peripheral-Modules](https://shop.trenz-electronic.de/en/Products/Digilent/Peripheral-Modules/)
- [muselab-tech.aliexpress.com](https://muselab-tech.aliexpress.com/store/5940159)
- [icebreaker-fpga/icebreaker-pmod](https://github.com/icebreaker-fpga/icebreaker-pmod)
  - [docs.icebreaker-fpga.org/hardware/pmod](https://docs.icebreaker-fpga.org/hardware/pmod)

{{< note >}}
Most FPGA development [boards]({{< ref "/boards" >}} "boards") use PMOD connectors due to the otherwise widespread usage of 100 mil spaced pin-headers. For higher pin counts and/or higher frequencies, either [FMC](https://en.wikipedia.org/wiki/FPGA_Mezzanine_Card) or [SYZYGY](https://syzygyfpga.io) are used instead.
{{< /note >}}

It is also common to find baseboards or adapters for allowing connection of PMODs to development boards with other connectors:

- [TomKeddie/prj-pmod-feather](https://github.com/TomKeddie/prj-pmod-feather): a Feather plate/wing to allow PMOD usage.
- [MuseLab-Tech SODIMM baseboard](https://es.aliexpress.com/item/1005001686186007.html): provides 6 dual PMODs.
