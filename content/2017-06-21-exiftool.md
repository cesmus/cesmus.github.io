---
title: ExifTool
slug: exiftool
date: 2017-06-21 10:38
category: exiftool
tags: exiftool, web, metadata
---

<div markdown="1" class="quote">
**Hack** meta information
</div>

> <http://owl.phy.queensu.ca/~phil/exiftool/>

## Overview

**ExifTool** is a powerful Perl library (`Image::ExifTool`) that comes with a command-line interface (`exiftool`) that reads, writes and edits meta information in image, audio, video, PDF and many others files. This makes **ExifTool** a valuable tool to use before exposing undesired information online.

Below you will find some common uses of ExifTool for reading and manipulating metadata in media files.
Be sure to visit [ExifTool's website](http://owl.phy.queensu.ca/~phil/exiftool/) to see more of what it does and [ExifTool's examples](http://owl.phy.queensu.ca/~phil/exiftool/examples.html) to see how to work with it.

More Internet resources about ExifTool: [Wikipedia](https://en.wikipedia.org/wiki/ExifTool) - [MIT](http://web.mit.edu/Graphics/src/Image-ExifTool-6.99/html/ExifTool.html) -

### Tags & Groups

Meta information is stored in tags and they are associated in groups. Here a list of some of the most common groups.

* File: system information
* EXIF: (Exchangeable image file format) [JEITA](http://www.jeita.or.jp/english/) standard
* MakerNotes: additional meta information from maker
* IPTC IIM: (IPTC Information Interchange Model) [International Press Telecommunications Council](https://iptc.org/)
* XMP: Adobe's XMP standard [Adobe's XMP](https://www.adobe.com/products/xmp.html)

### Quick Examples

Some common actions I usually perform with ExifTool:

Action                            | Command
--------------------------------- | -------
extract information | `exiftool file.jpg`
extract all meta information, including duplicates and unknown tags, sorted by group | `exiftool -a -u -g1 file.jpg`
extract common information | `exiftool -common file.jpg`
write information | `exiftool -createdate="2017:06:19 23:17:00" file.jpg`
write to multiple files | `exiftool -createdate="2017:06:19 23:17:00" file1.jpg file2.jpg file3.jpg`
write to all files in directory | `exiftool -createdate="2017:06:19 23:17:00" images/`
write multiple tags | `exiftool -createdate+=3 -modifydate+=3 file.jpg`
replaces existing comments | `exiftool -comment= file.jpg`
print specific tags | `exiftool -ImageSize -ExposureTime file.jpg`
output in tab columns | `exiftool -T -createdate -aperture -shutterspeed -iso file.jpg`
output in html | `exiftool -htmldump file.jpg`
output in json | `exiftool -json file.jpg`
remove all metadata | `exiftool -all= file.jpg`
delete all Photoshop metadata | `exiftool -Photoshop:All= file.jpg`
remove all gps tags | `exiftool -gps:all= file.jpg`

### Tips

> Do NOT delete meta information in RAW images, sometimes RAW formats contain information in the makernotes that is necessary for converting the image.

> Changes to PDF files by ExifTool are reversible (by deleting the update with "-PDF-update:all=") because the original information is never actually deleted from the file.  So ExifTool alone may not be used to securely edit metadata in PDF files
