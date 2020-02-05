# Doc

* Verilog [IEEE Std 1364-2001](https://inst.eecs.berkeley.edu/~cs150/fa06/Labs/verilog-ieee.pdf), [Quick Ref Guide](http://sutherland-hdl.com/pdfs/verilog_2001_ref_guide.pdf), [SystemVerilog 3.1a](http://www.ece.uah.edu/~gaede/cpe526/SystemVerilog_3.1a.pdf), [Synthesizing SystemVerilog Busting the Myth that SystemVerilog is only for Verification](http://sutherland-hdl.com/papers/2013-SNUG-SV_Synthesizable-SystemVerilog_paper.pdf)
* VHDL standards [IEEE Std 1076-2000](http://edg.uchicago.edu/~tang/VHDLref.pdf)
* SystemC standards [IEEE Std 1666-2011](http://paginas.fe.up.pt/~ee07166/lib/exe/fetch.php?media=1666-2011.pdf)
* [SystemVerilog Assertions Handbook](https://verificationacademy.com/forums/systemverilog/new-book-systemverilog-assertions-handbook-4th-edition) - Assertion Guide for static and dynamic verification.
* [Writing Testbenches using SystemVerilog](http://www.springer.com/us/book/9780387292212) - Writing Testbenches Using SystemVerilog offers a clear blueprint of a verification process that aims for first-time success using the SystemVerilog language. From simulators to source.
* [Asynchronous & Synchronous Reset Design Techniques](http://www.sunburst-design.com/papers/CummingsSNUG2003Boston_Resets.pdf)
* [Clock Domain Crossing (CDC) Design & Verification Techniques Using SystemVerilog](http://www.sunburst-design.com/papers/CummingsSNUG2008Boston_CDC.pdf)

# Simulators and compilers

* [Lola-2](https://inf.ethz.ch/personal/wirth/Lola/Lola2.pdf)
  - [Oberon-2013](https://inf.ethz.ch/personal/wirth/Lola/) - Project Oberon, 2013 Edition, written in [Oberon-07](http://www-oldurls.inf.ethz.ch/personal/wirth/Oberon/) [License](https://inf.ethz.ch/personal/wirth/ProjectOberon/license.txt)

# Meta HDL and Transpilers

* C++
   - [SystemC](https://www.doulos.com/knowhow/systemc/) - an IEEE standard meta-HDL
   - [VisualHDL](http://sysprogs.com/legacy/visualhdl/) - an integrated development environment (IDE) rapid design for FPGAs
* Haskell
   - [concat](https://github.com/conal/concat) Haskell to hardware, 2016+
   - https://github.com/conal/talk-2015-haskell-to-hardware
   - [CλaSH](https://github.com/clash-lang/clash-compiler) - A functional hardware description language
   - [pipelineDSL](https://github.com/p12nGH/pipelineDSL) - A Haskell DSL for describing hardware pipelines
* Java
   - [jhdl](http://www.jhdl.org/) ..2006
   - [PSHDL](http://pshdl.org/)
* JavaScript
   - [reqack](https://github.com/drom/reqack) -  elastic circuit toolchain
   - [hdl-js](https://github.com/DmitrySoshnikov/hdl-js) - Hardware description language (HDL) parser, and Hardware simulator.
   - [shdl](https://github.com/jcbuisson/shdl) - Simple Hardware Description Language
* Julia
   - [Julia-Verilog](https://github.com/interplanetary-robot/Verilog.jl) - a Verilog-generation DSL for Julia., 2017
* Python
  - [HWT](https://github.com/Nic30/hwt) Meta HDL, verification env. IP-core generator, analysis tools, HDL glue
  - [garnet](https://github.com/StanfordAHA/garnet) Coarse-Grained Reconfigurable Architecture generator based on magma, 2018+
  - [magma](https://github.com/phanrahan/magma/) - Meta HDL, 2017+
  - [migen](https://github.com/m-labs/migen) - Meta HDL, 2011+
  - [MyHDL](https://github.com/myhdl/myhdl) - Process based HDL, verification framework included, 2004+
  - [Pyrope](https://masc.soe.ucsc.edu/pyrope.html) - Python-like language supporting "fluid pipelines" and "live flow", 2017+
  - [PyRTL](https://github.com/UCSBarchlab/PyRTL) - Meta HDL, simulator suitable for research.
  - [PyMTL](https://github.com/cornell-brg/pymtl) - Process based HDL, verification framework included, 2014+
  - [veriloggen](https://github.com/PyHDI/veriloggen) - Python, Verilog centric meta HDL with HLS like features, 2015-?
* Ruby
   - [RHDL](https://github.com/philtomson/RHDL)
* Rust
   - [hoodlum](https://github.com/tcr/hoodlum) - Meta HDL, 2016+
   - [kaze](https://github.com/yupferris/kaze) - Meta HDL, 2019+
* Scala
   - [chisel](https://github.com/freechipsproject/chisel3) - Meta HDL, 2012+
   - [SpinalHDL](https://github.com/SpinalHDL/SpinalHDL) - Meta HDL 2012+

# HLS

* [hlslibs](https://github.com/hlslibs) - ac_math, ac_dsp, ac_types
* [legup](http://legup.eecg.utoronto.ca/) - 2011-2015, LLVM based c->verilog
* [bambu](http://panda.dei.polimi.it/?page_id=31) - 2003-?, GCC based c->verilog
* [augh](http://tima.imag.fr/sls/research-projects/augh/) - c->verilog, DSP support
* https://github.com/utwente-fmt - abstract hls, verification libraries
* [Shang](https://github.com/etherzhhb/Shang) - 2012-2014, LLVM based, c->verilog
* [xronos](https://github.com/endrix/xronos) - 2012, java, simple HLS
* [Potholes](https://github.com/SamuelBayliss/Potholes) - 2012-2014 - polyhedral model preprocessor, Uses Vivado HLS, PET
* [hls_recurse](https://github.com/m8pple/hls_recurse) - 2015-2016 - conversion of recursive fn. for stackless architectures
* [hg_lvl_syn](https://github.com/funningboy/hg_lvl_syn) - 2010, ILP, Force Directed scheduler
* [abc](https://people.eecs.berkeley.edu/~alanmi/abc/) <2008-?, A System for Sequential Synthesis and Verification
* [polyphony](https://github.com/ktok07b6/polyphony) - 2015-2017, simple python to hdl
* [DelayGraph](https://github.com/ni/DelayGraph) - 2016, C#, register assignment algorithms
* [ahaHLS](https://github.com/dillonhuff/ahaHLS) - 2019, An open source high level synthesis (HLS) tool using LLVM
* [combinatorylogic/soc](https://github.com/combinatorylogic/soc) - 2019, An experimental System-on-Chip with a custom compiler toolchain.

# Other HDL languages

* [act](https://github.com/asyncvlsi/act) - asynchronous circuit/compiler tools
* [autopiper](https://github.com/google/autopiper)
* [TL-Verilog](https://makerchip.com) - 2015+, Supports "timing-abstract" and "transaction-level design" methodologies; supported by proprietary and open-source tools

# Hardware Intermediate Representations

* [coreir](https://github.com/rdaly525/coreir) - 2016-?, LLVM HW compiler## License
* [lgraph](https://github.com/masc-ucsc/lgraph) - 2017-?, A Multi-Language Synthesis and Simulation IR for Hardware Design
* [firrtl](https://github.com/freechipsproject/firrtl) - 2016-?, Flexible Intermediate Representation for RTL

# Libraries with information about boards/chips

* [loam](https://github.com/phanrahan/loam) - Buildsystem for magma
* [litex](https://github.com/enjoy-digital/litex) - Buildsystem for migen

# Visualization and Documentation generators

* [bitfield](https://github.com/drom/bitfield) - Javascript bit field diagram renderer
* [d3-wave](https://github.com/Nic30/d3-wave) - Javascript wave graph visualizer for RTL simulations
* [d3-hwschematic](https://github.com/Nic30/d3-hwschematic) - Javascript hierarchycal schematic visualizer for HDLs
* [sphinx-hwt](https://github.com/Nic30/sphinx-hwt) - Plugin for sphinx documentation generator which adds shematic into html documentaion.

# Parsers

* [sv-parser](https://github.com/dalance/sv-parser) -  IEEE 1800-2017 System Verilog Parser written in Rust

# Other Simulation tools

* [midas](https://github.com/ucb-bar/midas) - FPGA-Accelerated Simulation Framework Automatically Transforming Arbitrary RTL

# Open Hardware

* [opencores.org](https://opencores.org/) - webpage which hosts many openhardware projects
* [ohwr](https://ohwr.org/welcome) - Open Hardware Repository, Cern open hardware community.
* [enjoy-digital repositories](https://github.com/enjoy-digital?tab=repositories) - Migen, SoC level modules
* [ZipCPU repositories](https://github.com/ZipCPU?tab=repositories) - Verilog, mostly peripherals, DSP
* [rhea](https://github.com/cfelton/rhea) - MyHDL, SoC level modules
* [FPGAwars FPGA-peripherals](https://github.com/FPGAwars/FPGA-peripherals) - Verilog, simple peripherals
* [PoC](https://github.com/VLSI-EDA/PoC) - VHDL, utils
* [picorv32](https://github.com/cliffordwolf/picorv32) - Verilog, A Size-Optimized RISC-V SoC
* [openrisc](https://github.com/openrisc) - OpenRISC, FuseSoC, peripherals and cpu parts
* [NyuziProcessor](https://github.com/jbush001/NyuziProcessor) - GPGPU
* [Miaow](http://miaowgpu.org/) - Miaow, Southern Island compatible ISA compute only GPGPU
* [VexRiscv](https://github.com/SpinalHDL/VexRiscv) - RISC-V written in SpinalHDL
* [Open-Source-FPGA-Bitcoin-Miner](https://github.com/progranism/Open-Source-FPGA-Bitcoin-Miner) - A completely open source implementation of a Bitcoin Miner for Altera and Xilinx FPGAs.
* [space-invaders-vhdl](https://github.com/fabioperez/space-invaders-vhdl) - Space Invaders game implemented with VHDL.
* [miaow](https://github.com/VerticalResearchGroup/miaow) - An open source GPU based off of the AMD Southern Islands ISA.
* [amiga2000-gfxcard](https://github.com/mntmn/amiga2000-gfxcard) - MNT VA2000, an Amiga 2000 Graphics Card (Zorro II), written in Verilog.
* [gplgpu](https://github.com/asicguy/gplgpu) - GPL v3 2D/3D graphics engine in verilog.
* [oh](https://github.com/parallella/oh) - Silicon validated Open Verilog library for IC and FPGA designers.
* [FPGA-Litecoin-Miner](https://github.com/kramble/FPGA-Litecoin-Miner) - Litecoin script miner implemented with FPGA on-chip memory.
* [verilog-ethernet](https://github.com/alexforencich/verilog-ethernet) - Collection of Ethernet-related components for both gigabit and 10G packet processing (8 bit and 64 bit datapaths).

# Verilog-Toolkit

- [verilog-mode](https://github.com/veripool/verilog-mode) - Verilog-Mode for Emacs with Indentation, Hightlighting and AUTOs.
- [Pyverilog](https://github.com/PyHDI/Pyverilog) - Python-based Hardware Design Processing Toolkit for Verilog HDL.
- [PyCoRAM](https://github.com/PyHDI/PyCoRAM) - Python-based Portable IP-core Synthesis Framework for FPGA-based Computing.
- [Pyverilog-toolbox](https://github.com/fukatani/Pyverilog_toolbox) - Pyverilog-based verification/design tool including code clone finder, metrics calculator and so on.

# VHDL-Toolkit

- [sublime-vhdl](https://github.com/yangsu/sublime-vhdl) - VHDL Package for Sublime Text 2/3.

# Tutorial

- [IntroToSpartanFPGABook](https://github.com/hamsternz/IntroToSpartanFPGABook) - A book on using the Spartan 3E FPGA with VHDL, using the Papilio One or Digilent Basys2 boards.
- [EDA playground](https://www.edaplayground.com/) - Edit, save, simulate, synthesize SystemVerilog, Verilog, VHDL and other HDLs from your web browser.
