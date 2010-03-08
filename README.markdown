`markdown-preview` reads text from the primary X selection,
`markdown-preview filename` reads text from a file.  The text is passed
through markdown, markdown's HTML output is written to a temporary file,
then the temporary file is opened in your browser.  Markdown's output is
wrapped in the HTML template at `~/.markdown-preview-template.html`,
`%m` in the template will will be replaced with markdown's output.

The markdown and web browser commands, the directory used for the output
files, and the HTML template can be configured by editing the constants
at the top of the python file.

Dependencies:

xclip -- for getting the primary X selection.
some version of markdown -- for doing the text-to-html conversion.

