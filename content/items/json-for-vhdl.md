---
title: JSON-for-VHDL
description: A JSON library implemented in VHDL
authors:
  - Patrick Lehmann
links:
  gh: Paebbels/JSON-for-VHDL
categories: [
  "Cores",
  "Tools",
  "Verification"
]
tags: [
  "VHDL",
  "JSON",
  "encode",
  "parameters",
  "generics",
]
active:
  from: 2015
licenses: [
  "Apache-2.0"
]
talk: 104
---

JSON-for-VHDL is a library to parse and query JSON data structures in VHDL. The complete functionality is included in a single synthesizable VHDL package, without special dependencies.

It allows reading JSON from files and/or from (optionally encoded) stringified JSON generics. It is included in [VUnit]({{< ref "/items/vunit" >}} "VUnit"), for passing generics for arbitrary complexity from Python to the testbeches.
