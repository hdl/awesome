# Bare

[![Netlify Status](https://api.netlify.com/api/v1/badges/e25dc0cd-2a9e-4c4e-bf39-c5e558d967e7/deploy-status)](https://app.netlify.com/sites/hugo-bare-theme/deploys)

Preview: https://hugo-bare-theme.netlify.com/

A speed-focused, minimalist Hugo blog theme based on [Bulma.io](https://bulma.io/). Looks 
great on mobile and loads in a flash.

Homepage   |  Post | Mobile
:---------------------------:|:-------------------------:|:------:|
![](https://raw.githubusercontent.com/orf/bare-hugo-theme/master/images/screenshot.png) |  ![](https://raw.githubusercontent.com/orf/bare-hugo-theme/master/images/post.png) |  ![](https://raw.githubusercontent.com/orf/bare-hugo-theme/master/images/mobile.png)

## How to use:

Install the theme:

```
git submodule add https://github.com/orf/bare-hugo-theme.git themes/bare
# This is required:
git submodule update --init --recursive
```

## Configuring the theme

Example configuration:

```toml
[params]
mainSections = ["posts"]
author = "Tom Forbes"
email = "tom@tomforb.es"
description = 'Python developer living and working in Lisbon'
postcss = true
# Include the author name in the <title> of articles
includeAuthorInTitle = true
```


The theme will pull posts from the content sections you define in `mainSections`. In the example above 
all posts from `content/posts` will be included in the homepage.

### PostCSS

You can use `postcss` to strip out all the unused Bulma CSS rules. This brings the CSS bundle down 
from 180kb to 10kb. 

To enable this set `params.postcss` to `true` in your `config.toml`. Then, copy the `package.json` and the 
`postcss.config.js` into your repository and run `npm install`.

### Social buttons

Social buttons can be configured by adding a `params.social` array. Icons come from 
https://materialdesignicons.com/:

```toml
[[params.social]]
icon = "github-circle"
url = "https://github.com/my-github-user/"

[[params.social]]
icon = "linkedin"
url = "https://linkedin.com/in/my-username"
```

### Hiding the theme link

I get it, you might not want to have a link to this repo on the footer of your blog. Add `disableAttribution` to your 
site parameters and it will be hidden. 
