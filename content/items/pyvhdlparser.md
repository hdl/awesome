---
title: pyVHDLParser
description: "A token-stream based parser for VHDL-2008 creating a document object model (DOM)."
authors:
  - Patrick Lehmann
links:
  gh: Paebbels/pyVHDLParser
date: "2019-12-28"
tags: [
  "streaming",
  "parser",
  "vhdl",
]
talk: 121
---

# Main Goals

* **Parsing**
  * Slice an input document into tokens and text blocks which are categorized in
    groups for fast indexing.
  * reserve case, whitespace and comments.
  * Recover on parsing errors
  * Good error reporting / throw exceptions
* **Fast Processing**
  * Multi-pass parsing and analysis
  * Delay analysis if not needed for current pass
  * Link tokens and blocks for fast-forward scanning (triple helix)
* **Generic VHDL Language Model**
  * Assemble a sourcecode document-object-model (Code-DOM)
  * Provide an API for code introspection
  * Provide an API for code modification / transformation


# Use Cases
* Generate documentation by using the fast-forward scanner
* Generate a document/language model by using the grouped text-block scanner
* Extract compile orders and other dependency graphs
* Generate highlighted syntax
