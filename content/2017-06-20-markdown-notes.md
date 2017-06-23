title: markdown notes
slug: markdown-notes
date: 2017-06-19 23:58
category: markdown
tags: markdown, web

## Markdown

<http://daringfireball.net/projects/markdown>

> the overriding design goal for Markdown’s formatting syntax is to make it as readable as possible. The idea is that a Markdown-formatted document should be publishable as-is, as plain text, without looking like it’s been marked up with tags or formatting instructions.

* text-to-HTML conversion tool for the web
* easy-to-read, easy-to-write plain text format for structured documents
* developed by John Gruber

Markdown is two things:

1. a plain text formatting syntax
2. a software converter, written in Perl, that converts the plain text to valid HTML

---

### Syntax

##### headers

    :::markdown
    # h1
    ## h2
    ### h3
    #### h4
    ##### h5
    ###### h6

# h1
## h2
### h3
#### h4
##### h5
###### h6

##### emphasis

    :::markdown
    italics: *asterisks* - _underscores_
    bold: **asterisks** - __underscores__
    strikethrough: ~~scratch~~

italics: *asterisks* - _underscores_

bold: **asterisks** - __underscores__

strikethrough: ~~scratch~~

##### code and syntax highlightning

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```

```
No language indicated, so no syntax highlighting.
But let's throw in a <b>tag</b>.
```

##### tables

```markdown
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
```

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

***

### Examples

#### `content/my_first_blog.md`
```markdown
Title: Blog Title
slug: blog-title
Date: 2017-06-22 18:05
Category: blog
Tags: blog, foo, bar
Authors: Foo Bar
Summary: A test blog entry

Very first blog entry.
```

#### `about.md`
```markdown
---
Title: About
---

about page
```

## Markdown Extensions

There are several implementations of the original Markdown written in Perl in 2004.
Most programming languages have a few different implementation. Below some of them:

### Markdown Extra



### MultiMarkdown

> <fletcherpenney.net/multimarkdown/>

MultiMarkdown (MMD) is a superset of the original. It adds multiple syntax features (tables, footnotes, citations, etc.) and is intended to output to various formats.

### Pandoc (Haskell)

> <http://pandoc.org/>



### GitHub Flavored Markdown

> <https://github.github.com/gfm/>

GitHub Flavored Markdown (GFM) is the dialect of Markdown currently supported for user content at GitHub. GFM is a strict superset of CommonMark, all new features not specified in the original CommonMark Spec are hence known as **extensions**.

### Fountain.io

> <https://fountain.io>

Fountain is a simple markup syntax for writing, editing, and sharing screenplays in plain, human-readable text.

### CommonMark

> <http://commonmark.org>

CommonMark is a standard, unambiguous syntax specification for Markdown, along with a suite of comprehensive tests to validate Markdown implementations against the specification.


### kramdown (Ruby)

> <https://kramdown.gettalong.org/>

kramdown is a markdown parser by Thomas Leitner.

### Python Markdown (Python)

> <https://pythonhosted.org/Markdown/>

### PHP Markdown Extra (PHP)

> <https://michelf.ca/projects/php-markdown/>

Markdown Extra is an extension to PHP Markdown implementing some features currently not available with plain Markdown syntax.

### marked (JavaScript)

> <https://github.com/chjj/marked>

A full-featured markdown parser and compiler, written in JavaScript. Built for speed.

## Alternatives

### reStructuredText

* ReStructuredText (ReST)
* text markup developed by the Python community
* replaced an earlier language called StructuredText
* Python community replaced LaTeX with ReST for their documentation
* rigid syntax

### Creole

<http://wikicreole.org/>

> <Python community replaced LaTeX with ReST for their documentation>

Creole is a lightweight markup language, aimed at being a common markup language for wikis, enabling and simplifying the transfer of content between different wiki engines.

## More resources
* [IETF Guidance on Markdown](https://tools.ietf.org/html/rfc7764)
* <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>
