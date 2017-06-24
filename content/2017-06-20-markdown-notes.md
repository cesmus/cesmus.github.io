title: Markdown notes
slug: markdown-notes
date: 2017-06-19 23:58
category: markdown
tags: markdown, markup, web

## Markdown

<table class="infobox u-full-width">
  <tbody>
    <tr>
      <th>Filename extensions</th><td>.md .markdown .mdown .mkdn</td>
    </tr>
    <tr>
      <th>MIME type</th><td>text/markdown</td>
    </tr>
    <tr>
      <th>Developed by</th><td>John Gruber</td>
    </tr>
    <tr>
      <th>Year launched</th><td>2004</td>
    </tr>
    <tr>
      <th>RFCs</th><td><a href="https://tools.ietf.org/html/rfc7763">RFC 7763</a> <a href="https://tools.ietf.org/html/rfc7764">RFC 7764</a></td>
    </tr>
    <tr>
      <th>Website</th><td>http://daringfireball.net/projects/markdown</td>
    </tr>
  </tbody>
</table>

<div class="quote">
  text-to-HTML conversion tool for web writers
</div>

Markdown is two things:

1. a plain text formatting syntax
2. a software converter that converts the plain text to valid HTML

The original implementation of Markdown is written in a Perl script `Markdown.pl`.

Markdown is the most commonly used lightweight markup language on the internet.

### Lack of standard

There is no clearly defined Markdown standard, John Gruber’s canonical description of Markdown’s syntax does not specify the syntax unambiguously. This has led to fragmentation as different vendors wrote their own variants of the language.

As Markdown became more popular, more and more sites started to implement their own Markdown. This has make it hard to port Markdown between sites and versions.

In the last few years, **CommonMark** was developed as a standardized Markdown but adoption has been slow but there are plans to announce a finalized 1.0 spec in 2017.

### Lack of extensibility

The lack of some features in the original Markdown saw the birth of more _Markdown extensions_ variants such as **Markdown Extra** (PHP, Python, Ruby), **MultiMarkdown** (Perl) and **Pandoc Markdown** (Haskell).

### CommonMark
[Website](http://commonmark.org)

CommonMark propose a **standard, unambiguous syntax specification for Markdown**, along with a **suite of comprehensive tests** to validate Markdown implementations against the specification.

### Quick Examples

#### `md_syntax.md`
```markdown
# Heading

## Sub-heading

### Another deeper heading

Paragraphs are separated
by a blank line.

Two spaces at the end of a line leave a  
line break.

Text attributes _italic_, *italic*, __bold__, **bold**, `monospace`.

Horizontal rule:

---

Bullet list:

  * apples
  * oranges
  * pears

Numbered list:

  1. apples
  2. oranges
  3. pears

A [link](http://example.com).
```

#### `README.md`
```markdown
## Synopsis

At the top of the file there should be a short introduction and/ or overview that explains **what** the project is. This description should match descriptions added for package managers (Gemspec, package.json, etc.)

## Code Example

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Motivation

A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Installation

Provide code examples and explanations of how to get the project.

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

Describe and show how to run the tests with code examples.

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

A short snippet describing the license (MIT, Apache, etc.)
```

Some good readings about READMEs:
* [Medium.com: README.md History and Components](https://medium.com/@NSomar/readme-md-history-and-components-a365aff07f10)
* [repat README-templates](https://github.com/repat/README-template)
* [Wikipedia's README article](https://en.wikipedia.org/wiki/README)

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


### Markdown Flavors
* [List of Markdown Flavors](https://github.com/jgm/CommonMark/wiki/Markdown-Flavors)
* [List of Markdown Implementations](https://github.com/markdown/markdown.github.com/wiki/Implementations)
* [List of CommonMark implementations](https://github.com/jgm/CommonMark/wiki/List-of-CommonMark-Implementations)

There are several variations of the original Markdown. Below some of the most popular variations:

#### PHP Markdown (PHP)
[Website](https://michelf.ca/projects/php-markdown/)

PHP variation of Markdown Extra.

#### Python Markdown (Python)
[Website](https://pythonhosted.org/Markdown/)

Python variation of Markdown Extra.

#### MultiMarkdown
[Website](http://fletcherpenney.net/multimarkdown/)

MultiMarkdown (MMD) is a superset of the original. It adds multiple syntax features (tables, footnotes, citations, etc.) and can output to various formats.

#### Pandoc (Haskell)
[Website](http://pandoc.org/)

Pandoc is an open source software document converter. It can convert files from one markup to another. It is a swiss-army knife for document conversion.

#### GitHub Flavored Markdown
[Website](https://github.github.com/gfm/)

GitHub Flavored Markdown (GFM) is the dialect of Markdown currently supported for user content at GitHub. GFM is a strict superset of CommonMark, all new features not specified in the original CommonMark Spec are hence known as **extensions**.

#### Fountain.io
[Website](https://fountain.io)

Fountain is a simple markup syntax for writing, editing, and sharing screenplays in plain, human-readable text.

#### kramdown (Ruby)
[Website](https://kramdown.gettalong.org/)

kramdown is a Ruby superset implementation of Markdown written by Thomas Leitner.

#### Discount (C)
[Website](http://www.pell.portland.or.us/%7Eorc/Code/discount/)

Pure C implementation

#### marked (JavaScript)
[Website](https://github.com/chjj/marked)

A full-featured markdown parser and compiler, written in JavaScript. Built for speed.


### Alternatives

#### reStructuredText
[Website](http://docutils.sourceforge.net/rst.html)

reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system. It is useful for in-line program documentation (such as Python docstrings), for quickly creating simple web pages, and for standalone documents.reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system. It is useful for in-line program documentation (such as Python docstrings), for quickly creating simple web pages, and for standalone documents.

#### Textile
[Website](https://www.promptworks.com/textile) [GitHub](https://github.com/textile)

Textile is a simple text format that can be converted to HTML, eliminating the need to use HTML directly to create documents, blogs, or web pages. Textile gives you readable text while you’re writing and beautiful text for your readers.

#### AsciiDoc
[Website](http://asciidoc.org/)

**AsciiDoc** is a text document format for writing notes, documentation, articles, books, ebooks, slideshows, web pages, man pages and blogs. AsciiDoc files can be translated to many formats including HTML, PDF, EPUB, man page.

#### Creole
[Website](http://wikicreole.org/)

> common wiki markup language

Creole is a lightweight markup language, aimed at being a common markup language for wikis, enabling and simplifying the transfer of content between different wiki engines.

These wiki engines have implemented full or partial support for Creole such as [OddMuse](http://www.oddmuse.org/), [MoinMoin](http://moinmo.in/), [DokuWiki](https://www.dokuwiki.org), among others. [MediaWiki](https://mediawiki.org/) does not support Creole.  

### More resources
* <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>
