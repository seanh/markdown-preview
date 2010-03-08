#!/usr/bin/env python 
"""markdown-preview.py: quick, temporary HTML preview of markdown text
in your browser.

Usage:

markdown-preview -- reads text from the primary X selection

markdown-preview filename -- reads text from a file

TODO:

*   Safer file and exception handling
*   Use the tempfile module for output files?
*   Report non-zero exit status and output of commands
*   Support a config file and/or environment variables for the options.
    Look for the $BROWSER environment variable?

"""
import sys,os,commands

# String replacement in these fields: %i = in_path, %o = out_path
MARKDOWN_COMMAND = 'markdown %i'
BROWSER_COMMAND = 'firefox %o'
OUT_DIR = '/tmp/'
TEMPLATE = '/home/seanh/.markdown-preview-template.html'

def replace(s,in_path,out_path):
    return s.replace("%i",in_path).replace("%o",out_path)

def do_file(in_path):
    out_path = os.path.join(OUT_DIR,os.path.split(in_path)[1]+".html")
    cmd = replace(MARKDOWN_COMMAND,in_path,out_path)
    html = commands.getoutput(cmd)
    html = file(TEMPLATE,'r').read().replace('%m',html)
    out_file = open(out_path,'w')
    out_file.write(html)
    out_file.close()    
    return out_path
    
def do_filename(filename):
    in_path = filename
    return in_path,do_file(in_path)
                        
def do_xclip():
    xclip_cmd = "xclip -o -selection primary"
    text = commands.getoutput(xclip_cmd)
    in_path = os.path.join(OUT_DIR,'markdown-preview.txt')
    in_file = open(in_path,'w')
    in_file.write(text)
    in_file.close()
    return in_path,do_file(in_path)
    
if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        in_path,out_path = do_filename(filename)
    except IndexError:
        in_path,out_path = do_xclip()
    cmd = replace(BROWSER_COMMAND,in_path,out_path)
    print commands.getoutput(cmd)
