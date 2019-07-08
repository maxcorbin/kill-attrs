# What this does

This takes a directory full of HTML files (the current directory) and strips out all of the attributes for each tag, excluding `src` and `href` attributes. These are presumed to be of some utility to `img` and `a` tags, respectively.

# Why would you do this

Sometimes web frameworks and WYSIWYG tools add extra attributes to HTML tags to store application-specific information. Often times this builds up as users copy and paste the output of these tools into new tools, so cruft builds up. Additionally, sometimes tools store data in these attributes in the form of base64 encoded JSON or images, which balloons the size of these files and makes the less readable to a later editor.

This script takes the 'nuke it from high orbit' approach to this problem by removing any styling, class, id, or data attributes, leaving a readable and pretty-printed HTML document.

# How do you do this

1. Download the `kill-attrs.py` script however you want.
2. Place the script into the directory containing your HTML files you want to sanitize.
3. Install dependencies from `requirements.txt`, preferably into a virtual environment.
4. Run the script using `python kill-attrs.py`.

# Requirements

`bs4`, beautiful soup
`python3`, python 3, not 2
some HTML files you hate

# Recommendations

Make sure you back up your HTML files before you do this in case something goes wrong.

# TODOs

[ ] Directory recursion (affects files within sub folders)
[ ] Ability to target the script to just a few specific files or folders
