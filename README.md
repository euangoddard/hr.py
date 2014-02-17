hr.py
=====

Horizontal rule for your terminal - in python!

Tired of not finding things in your terminal because there's a lot of logs and
garbage? Tired of destroying the Enter key by creating a "void zone" in your
terminal so that you can see the error that you're trying to debug?

Use the old `<hr />` tag, but in your terminal.

## Inspiration

The original version of the hr script was implement in bash (https://github.com/LuRsT/hr), and I thought, "why not have a python version?". So here we are!

## Setup

    $ pip install git+git://github.com/euangoddard/hr.py.git

*NB* PyPI release coming soon!

## How to use it?

    $ hr
    ################################## # Till the end of your terminal window
    $

    $ hr '*'
    ********************************** # Till the end of your terminal window
    $

You can also make "beautiful" ASCII patterns

    $ hr - '#' -
    ----------------------------------
    ##################################
    ----------------------------------
    $ hr '-#-' '-' '-#-'
    -#--#--#--#--#--#--#--#--#--#--#--
    ----------------------------------
    -#--#--#--#--#--#--#--#--#--#--#--


The only requirement is python (tested in python 2.7)
