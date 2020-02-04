# Contributing

Contributions are welcome!

## Adding a resource

Most awesome lists are written in a single long Markdown file (see [awesome-list](https://github.com/topics/awesome-list)). However, in this repository each resource is described in a separate Markdown file (see [content/items](../content/items)). The frontmatter is used to provide data about the resource, while the body can contain a long description. The prototype of the frontmatter is the following:

```yml
---
title: "name of the tool"
description: "description"
author: ["first author", "second author"]
links:
  gh: "https://github.com/user/repo"
  gl: "https://gitlab.com/user/repo"
  web: "https://example.com"
  docs: "https://doc.example.com"
tags: [
  "a_tag",
  "another_tag"
]
categories: [
  "a_category"
]
---

Long description of the resource
```

> NOTE: links are optional, and non-exclusive.

Further guidelines:

* Add one resource/file per pull request and explain why it is awesome.
* Keep descriptions in the frontmatter concise.
* See list of defined categories in [config.yml](../config.yml).
  * Add a new category if needed. If done, a description of the category must be included.
* Regular chores:
  * Search previous suggestions before making a new one.
  * Check spelling and grammar.
  * Remove any trailing whitespace.

## Modifying the site/theme

The website is built with [Hugo](https://github.com/gohugoio/hugo), using a theme based on [Bare Hugo](https://github.com/orf/bare-hugo-theme). The theme is a submodule of the `master` branch. However, at the same time, the customized version is hosted in branch `theme` of this same repo. Hence, users willing to contribute to the theme need to:

- Clone this repo recursively, or `git submodule init` and `git submodule update`.
- Change directory to `themes/bare-hugo-theme`.
- Make changes, commit them and push a feature branch.
- Open a pull request againt branch `theme`, NOT `master`.