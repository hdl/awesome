**Tools:**

- [LibreCores CI](#LibreCores-CI)
- [AAPG (Automated Assembly Program Generator)](#AAPG)
- [riscv-dv](#riscv-dv)
- [covered](#covered)
- [svlint](#svlint)
- [sv-parser](#sv-parser)
- [rggen](#rggen) (Code generation tool for configuration and status registers)
- [EBMC / CBMC](#ebmc--cbmc) (Model checker for C/C++ and hardware designs)

**Frameworks:**

- [riscv-formal](#riscv-formal)
- [V3](#V3)

**Components / VIPs**

- [uvm_axi](#uvm_axi)
- [AXI Bus Formal VIP](#axi-bus-formal-vip)
- [AXI Bus Functional Model tvip-axi](#AXI-Bus-Functional-Model---tvip-axi)
- [APB Bus Functional Model tvip-apb](#APB-Bus-Functional-Model---tvip-apb)

**Guides:**

- [Dan Gisselquist Formal Verification Blogs](#Dan-Gisselquist-Formal-Verification-Blogs)

## Tools:

## AAPG

*"Automated Assembly Program Generator (aapg) is a tool that is intended to generate random RISC-V programs to test RISC-V cores."*

From the [Shakti](https://gitlab.com/shaktiproject) RISC-V core project.
Acts as a way to generate random stimulus for a RISC-V core.
Output of the programs can then be checked between DUT and a GRM.

- Link: https://gitlab.com/shaktiproject/tools/aapg
- License: BSD 3-clause
- Written In: Python

## riscv-dv

Similar to [AAPG](#AAPG), but this time from Google.
Generates randomised RISC-V programs which can
then be run by the DUT and A GRM and checked for equivilence.
It has knowledge of interesting features like page tables, CSR access and
trap/interrupt handling.
Can generate randomised instruction streams with features like loops
and function calls etc.

This project cannot be used with current free open source HDL simulators
since it relies on the object orientated parts of UVM. It is still a
useful piece of Verification IP though, and serves as a guide for other
similar projects.

- Link: https://github.com/google/riscv-dv
- License: Apache-2.0
- Written In: SystemVerilog + UVM

### covered

*"Covered is a Verilog code coverage analysis tool that can be useful for determining how well a diagnostic test suite is covering the design under test."* ... *"Covered reads in the Verilog design files and a VCD, LXT or FST formatted dumpfile from a diagnostic run and generates a database file called a Coverage Description Database (CDD) file"* ... "*Once a CDD file is created, the user can use Covered to generate various human-readable coverage reports in an ASCII format or use Covered's GUI to interactively look at coverage results*".

- Link: https://github.com/anders-code/verilog-covered
- License: GPL-2.0
- Written In: C

### svlint

An open source, MIT licensed SystemVerilog linting tool. Built on top of an open source [SystemVerilog parser](#sv-parser).

- Link: https://github.com/dalance/svlint
- License: MIT
- Written In: Rust

### sv-parser

An open source, MIT/Apache licensed SystemVerilog parser/ Useful for quickly building custom tools / checkers.

- Link: https://github.com/dalance/sv-parser
- License: MIT / Apache
- Written In: Rust

### RgGen

"*RgGen is a code generation tool for ASIC/IP/FPGA/RTL engineers. It will
automatically generate soruce code related to configuration and status
registers (CSR), e.g. SytemVerilog RTL, UVM RAL model, Wiki documents, from
human readable register map specifications.*"

- Link: https://github.com/rggen/rggen
- License: MIT
- Written in: Ruby


### EBMC / CBMC

**EBMC:**

"*EBMC is a Model Checker for hardware designs. It includes both bounded and
unbounded analysis, i.e., it can both discover bugs and is also able to prove
the absence of bugs. It can read Netlists (ISCAS89 format), Verilog, System
Verilog and SMV files. Properties can be given in LTL or a fragment of System
Verilog Assertions.*"

- Link: http://www.cprover.org/ebmc/
- Licence: http://www.cprover.org/ebmc/download/license.txt
- Written in: _Unknown_.

Note: Only the binaries for EBMC can be downloaded, no source-code is
available.  It's included on this list because it is a powerful tool which
would otherwise not be available to the open hardware community.
For a completely free and open tool with similar capabilities,
look at [SymbiYosys](#Symbiyosys).

**CBMC:**

"*CBMC is a Bounded Model Checker for C and C++ programs.*"

"*Furthermore, it can check C and C++ for consistency with other languages,
such as Verilog. The verification is performed by unwinding the loops in the
program and passing the resulting equation to a decision procedure.*"

- Link: http://www.cprover.org/cbmc/
  - Source: https://github.com/diffblue/cbmc
- Licence: https://github.com/diffblue/cbmc/blob/develop/LICENSE
- Written in: C++.


## Frameworks:

### riscv-formal

A re-usable formal verification framework for RISC-V CPU designs.
Uses the [Yosys/SymbiYosys](#SymbiYosys) tools.

- License: [ISC](https://github.com/SymbioticEDA/riscv-formal/blob/master/COPYING)
- Written In: Verilog
- Link: https://github.com/SymbioticEDA/riscv-formal

### V3

*"V3 is a new and extensible framework for hardware verification and debugging researches on both Boolean-level and word-level designs. It is a powerful tool for users and an elaborate framework for developers as well."*

Academic project, looks unmaintained since 2014.

- Written In: C++
- Write Testbenches In: Unclear?
- License: [Non-commercial](https://github.com/chengyinwu/V3/blob/master/COPYING)
- Supports: formal methods based approaches using AGIER / SAT Solving over verilog input files. Not entirely clear how one specifies correctness properties.
- Link: https://github.com/chengyinwu/V3

## Components / VIPs

### uvm_axi

A bus functional model for ARM's AXI bus protocol. Looks like it has been written as a standard UVM Verification Package.
Being written in SystemVerilog (using all of its object orientated, behavioural modelling features) makes it hard
to re-use with the current set of FOSS simulators. It is still a good example of re-usable verification IP.

Last commit in 2013, so likely un-maintained.

- Link: https://github.com/funningboy/uvm_axi
- Written in: System Verilog
- Write Testbenches In: System Verilog
- License: GNU Lesser General Public License

### AXI Bus Formal VIP

A set of formal properties for checking for correct protocol behaviour in an AXI bus.
Used as part of a Wishbone-AXI bus bridge, but usable with any AXI bus.
There is a great blog post on it's use [here](https://zipcpu.com/formal/2018/12/28/axilite.html) from ZipCPU.
It works with SymbiYosys.

- Link: https://github.com/ZipCPU/wb2axip/blob/master/bench/formal/faxil_slave.v
- Written in: Verilog
- Write Testbenches In: Verilog
- License: None specified

### AXI Bus Functional Model - tvip-axi

Bus function model for AMBA AXI protocol.
Supports master and slave agents, AXI4 and AXI4-Lite protocols.
Configurable address/data/id widths.
Supports in/out-of-order responses, delayed responses and read interleaving.

- Link: https://github.com/taichi-ishitani/tvip-axi
- Written in: SystemVerilog and UVM
- License: Apache-2.0

### APB Bus Functional Model - tvip-apb

Bus function model for AMBA APB protocol

- Link: https://github.com/taichi-ishitani/tvip-apb
- Written in: SystemVerilog and UVM
- License: Apache-2.0

## Guides:

### Dan Gisselquist Formal Verification Blogs

A set of posts on experiences using [Symbiyosys/Yosys](#Symbiyosys) for formally verifying a CPU design.
Includes lots of useful insights and guides for specific and general use cases.

- Link: https://zipcpu.com/formal/formal.html
