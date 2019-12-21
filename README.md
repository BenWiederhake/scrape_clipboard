# scrape_clipboard

> Scrapes your own clipboard.

Perfect for when you need to copy *lots* of stuff, and usually have to do this:

*select* *copy* *alt-tab* *paste* *alt-tab*  
*select* *copy* *alt-tab* *paste* *alt-tab*
*select* *copy* *alt-tab* *paste* *alt-tab*  
*select* *copy* *alt-tab* *paste* *alt-tab*  
*select* *copy* *alt-tab* *paste* *alt-tab*  
...

Because with this tool you instead do this:

*start*  
*select* *copy* *select* *copy* *select* *copy* *select* *copy* *select* *copy* ...

This is not designed to be a clipboard-logger,
although it can probably be repurposed into one.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [TODOs](#todos)
- [NOTDOs](#notdos)
- [Contribute](#contribute)

## Install

No.

## Usage

Just use it!  No python dependencies, and it's short enough.
You could probably write it yourself, but I thought
it'd be nice to share the few lines.

```
$ ./scrape_clipboard.py > seen_strings.txt
```

This calls `xclip`, which is pre-installed on most Linux systems,
and usually readily available in others.

## TODOs

* Implement
* Publish
* Stop yak-shaving

## NOTDOs

* Performance of any kind.
* Accessing the X clipboard directly, unless I have reason to believe that the intermediate python module will have more stable support than xclip.  And I don't think that's gonna happen.
* Support for any other display server (sorry, Windows users).

## Contribute

Feel free to dive in! [Open an issue](https://github.com/BenWiederhake/scrape_clipboard/issues/new) or submit PRs.
