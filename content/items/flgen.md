---
title: FLGen
description: Filelist generator
authors:
  - PEZY Computing K.K.
links:
  gh: pezy-computing/flgen
categories:
  - Tools
  - Tools:Managers
tags:
  - EDA
  - filelist
licenses:
  - Apache-2.0
---

FLGen provides a DSL to describe your filelists and a generator tool to generate a filelist (*.f file) which are given to EDA tools.

Creating a filelist on shell script/makefile is very bother work; add/remove option switches, resolve source file path, etc.
FLGen is a tool to resolve such problems.

You can find an exmpale from [here](https://github.com/pezy-computing/flgen/tree/master/sample).

[sample/foo.list.rb](https://github.com/pezy-computing/flgen/blob/master/sample/foo.list.rb)

```ruby
compile_argument '-foo_0'
runtime_argument '-foo_1'
include_directory 'bar'
source_file 'foo.sv'
file_list   'sample/bar/bar.list.rb'
```

You can generate a filelist below from the above FLGen filelist.

```
$ flgen --output=filelist.f sample/foo.list.rb
$ cat filelist.f
//  flgen version 0.14.0
//  applied arguments
//    --output=filelist.f
//    sample/foo.list.rb
+define+BAR_0
+define+BAR_1=1
+incdir+/home/taichi/workspace/pezy/flgen/sample/bar
+incdir+/home/taichi/workspace/pezy/flgen/sample/bar/baz
-foo_0
/home/taichi/workspace/pezy/flgen/sample/foo.sv
/home/taichi/workspace/pezy/flgen/sample/bar/bar.sv
/home/taichi/workspace/pezy/flgen/sample/bar/baz/baz.sv
```
