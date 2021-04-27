---
title: "Synthesijer"
description: "A compiler from Java to VHDL/Verilog-HDL."
authors:
  - Takefumi Miyoshi
links:
  gh: "synthesijer/synthesijer"
  docs: "https://synthesijer.github.io/web/"
tags:
  - code-generator
  - verilog
  - vhdl
  - high-level-synthesis
  - java
  - scala
categories:
  - Tools
licenses:
  - Apache-2.0
active:
  from: 2014
talks:
---

Synthesijer is a high-level synthesis tool, which generates VHDL and Verilog HDL code from Java code. Synthesijer also provides a backend to generate VHDL/Verilog HDL, which helps to develop high-level synthesis tools and DSLs.

For example, prepare the following Java program,

```
/* Test.java */
public class Test{
    public boolean flag;
    private int count = 0;

    public void run(){
        while(true){
            count++;
            if(count == 5000000){
                count = 0;
                flag = !flag;
            }
        }
    }
}
```

and compile it with Synthesijer.

```
synthesijer --vhdl --verilog Test.java
```

You can get Test.vhd and Test.v from the given Test.java.
