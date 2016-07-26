FlexGet extras
==============

This contains collection of plugins that are not considered widely used enough to be included in standard 
distribution package or are not actively maintained and supported by `FlexGet`_ development team. 

This repository also serves example how to do separate distribution package for plugins.

You will need to have `FlexGet`_ virtualenv active when executing any of these commands or directly use it's
`bin/` or `scripts`. Using `virtualenvwrapper`_ recommended.

Install
-------

TBD, this will likely work after FlexGet 2.2 is released::

    pip install https://github.com/Flexget/extras/archive/master.zip


Development
-----------

Clone and at the checkout directory run::

    python setup.py develop

Tests
-----

In the checkout directory run::

    py.test


.. _FlexGet: http://flexget.com
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/install.html