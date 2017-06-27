---
title: Markdown notes
slug: markdown-notes
date: 2017-06-19 23:58
category: markdown
tags: markdown, markup, web, html
---

# Markdown

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

1. a plain text formatting syntax.
2. a software converter that converts the plain text to valid HTML.

Markdown specifically is a family of syntaxes that are based on the original work of John Gruber with substantial contributions from Aaron Swartz. Since its release, a number of web or web-facing applications have incorporated Markdown into their text-entry systems, frequently with custom extensions.

Due to the complexity and security pitfalls of formal markup languages (e.g., HTML5) and proprietary binary formats (e.g., word-processing software), yet unwilling to be confined to the restrictions of plain text, many users have turned to Markdown for document processing.  Whole toolchains now exist to support Markdown for online and offline projects.

The original implementation of Markdown is written in a Perl script called `Markdown.pl`.

Despite Markdown being the **most commonly used lightweight markup language on the internet**, it does not have a specification, lacks common features found in other markup languages and does not have a clear translation for most HTML tags, and adding HTML code in a Markdown document conflicts with the basic purpose of the language. That being said, Markdown simplicity rocks.

## Lack of standard

There is no defined Markdown standard, John Gruber’s canonical description of Markdown’s syntax does not specify the syntax unambiguously. This has led to fragmentation as different vendors wrote their own variants of the language.

As Markdown became more popular, more and more sites started to implement their own Markdown. This has make it hard to port Markdown between sites and versions.

In the last few years, **CommonMark** was developed as a standardized effort on Markdown and there are plans to announce a finalized 1.0 spec in 2017.

## Lack of extensibility

The lack of some features and bugs found in the original Markdown code saw the birth of more _Markdown extensions_ variants such as **Markdown Extra** (PHP, Python, Ruby), **MultiMarkdown** (Perl) and **Pandoc Markdown** (Haskell).

## CommonMark
[Website](http://commonmark.org)

CommonMark propose a **standard, unambiguous syntax specification for Markdown**, along with a **suite of comprehensive tests** to validate Markdown implementations against the specification.

For further information about CommonMark, read more

## Quick Examples

#### `md_syntax.md`
```markdown
# h1
## h2
###### h6

Paragraphs are separated
by a blank line.

Two spaces at the end of a line leave a  
line break.

Text attributes _italic_, *italic*, __bold__, **bold**, `monospace`.

Horizontal rule:
---

Bullet list:
  - apples
  - oranges
  - pears

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
- [Medium.com: README.md History and Components](https://medium.com/@NSomar/readme-md-history-and-components-a365aff07f10)
- [repat README-templates](https://github.com/repat/README-template)
- [Wikipedia's README article](https://en.wikipedia.org/wiki/README)

#### `content/my_first_blog.md`
```markdown
---
Title: Blog Title
Slug: blog-title
Date: 2017-06-22 18:05
Category: blog
Tags: blog, foo, bar
Authors: Foo Bar
Summary: A test blog entry
---

blog entry.
```

#### `about.md`
```markdown
---
Title: About
---

about page
```

## Dingus

Try your Markdown online, they come with a quick Markdown cheatsheet

- [Daring Fireball: Markdown dingus](https://daringfireball.net/projects/markdown/dingus)
- [PHP Markdown dingus](https://michelf.ca/projects/php-markdown/dingus/)
- [Fountain.io](https://fountain.io/dingus)
- [CommonMark](http://spec.commonmark.org/dingus/)
- [Symfony Project](http://www.symfony-project.org/plugins/markdown_dingus)


## Markdown Extra

Markdown Extra is an extension with some features currently not available with the plain Markdown syntax, and was initially implemented in PHP Markdown.

[Website](https://michelf.ca/projects/php-markdown/extra/)

#### PHP Markdown (PHP)
PHP Markdown implements plain Markdown syntax and PHP Markdown Extra implements Markdown Extra.

[Website](https://michelf.ca/projects/php-markdown/) | [GiHub](https://github.com/michelf/php-markdown)

#### Python Markdown
Python implementation of Markdown, contains:

- Python Markdown (original Markdown syntax)
- Python Markdown extensions (Markdown Extra + more extensions (official and third party) + Extensions API)
- markdown_py (command-line interface)

[Website](https://pythonhosted.org/Markdown/)

#### MultiMarkdown
MultiMarkdown (MMD) is a superset of the original. It adds multiple syntax features (tables, footnotes, citations, etc.) and can output to various formats.

[Website](http://fletcherpenney.net/multimarkdown/)

## Markdown Flavors
* [List of Markdown Flavors](https://github.com/jgm/CommonMark/wiki/Markdown-Flavors)
* [List of Markdown Implementations](https://github.com/markdown/markdown.github.com/wiki/Implementations)
* [List of CommonMark implementations](https://github.com/jgm/CommonMark/wiki/List-of-CommonMark-Implementations)

Below some of the most popular implementations of Markdown:

#### Pandoc (Haskell)
Pandoc is an open source software document converter. It can convert files from one markup to another. It is the Swiss Army knife for document conversion.

[Website](http://pandoc.org/)

#### GitHub Flavored Markdown
GitHub Flavored Markdown (GFM) is the dialect of Markdown currently supported for user content at GitHub. GFM is a strict superset of CommonMark, all features not specified in the original CommonMark Spec are known as **extensions**.

[Website](https://github.github.com/gfm/)

#### Fountain.io
Fountain is a simple markup syntax for writing, editing, and sharing screenplays in plain, human-readable text.

[Website](https://fountain.io)

#### kramdown (Ruby)
kramdown is a Ruby superset implementation of Markdown written by Thomas Leitner.

[Website](https://kramdown.gettalong.org/)

#### Discount (C)
Pure C implementation

[Website](http://www.pell.portland.or.us/%7Eorc/Code/discount/)

#### marked (JavaScript)
A full-featured markdown parser and compiler, written in JavaScript. Built for speed.

[Website](https://github.com/chjj/marked)

## Markdown Alternatives

#### reStructuredText
reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system. It is useful for in-line program documentation (such as Python docstrings), for quickly creating simple web pages, and for standalone documents.

[Website](http://docutils.sourceforge.net/rst.html)

#### Textile
Textile is a simple text format that can be converted to HTML, eliminating the need to use HTML directly to create documents, blogs, or web pages. Textile gives you readable text while you’re writing and beautiful text for your readers.

[Website](https://www.promptworks.com/textile) | [GitHub](https://github.com/textile)

#### AsciiDoc
**AsciiDoc** is a text document format for writing notes, documentation, articles, books, ebooks, slideshows, web pages, man pages and blogs. AsciiDoc files can be translated to many formats including HTML, PDF, EPUB, man page.

[Website](http://asciidoc.org/)

#### Creole
Creole is a lightweight markup language, aimed at being a common markup language for wikis, enabling and simplifying the transfer of content between different wiki engines.

[Website](http://wikicreole.org/)

These wiki engines have implemented full or partial support for Creole such as [OddMuse](http://www.oddmuse.org/), [MoinMoin](http://moinmo.in/), [DokuWiki](https://www.dokuwiki.org), among others. [MediaWiki](https://mediawiki.org/) does not support Creole.  

## Further reading

For further information about Markdown syntax, check the [Daring Fireball: Markdown syntax](https://daringfireball.net/projects/markdown/syntax), [PHP Markdown Concepts page](https://michelf.ca/projects/php-markdown/concepts/), [Markdown-here Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

For further information about Markdown, read [Wikipedia](https://en.wikipedia.org/wiki/Markdown).
