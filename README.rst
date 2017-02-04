numerus
=======

numerus is a pure-python mathematical utilities package with no C dependencies.

Current functionality consists of trigonometric functions and numerical checks.

Installing
----------

pip
~~~

numerus can be installed using pip:

``$ pip install numerus``

numerus is written for Python 3. If the above installation fails, it may be
that your system uses ``pip`` for the Python 2 version - if so, try:

``$ pip3 install numerus``

Requirements
~~~~~~~~~~~~

numerus currently has no dependencies - neither Python nor compiled ones.

Overview
--------

Geometry
~~~~~~~~

The sine law and cosine law are both trigonometric equations that allow you to
determine some missing component of a triangle given a specific set of known
components.

The sine law, for example, allows you to determine a side if you know the
opposite angle, and another side-angle pair - or, alternatively, it can tell
you an angle if you know the opposing side and another side-angle pair.

    >>> import numerus
    >>> numerus.sine_law(side1=7, angle1=35, angle2=105)
    11.788282006559363
    >>> numerus.sine_law(side1=7, angle1=35, side2=11.8)
    75.21404844616559
    >>> numerus.sine_law(side1=7, angle1=35, side2=11.8, obtuse=True)
    104.78595155383441

The cosine law can be used to find any interior angle of a triangle if you know
all three sides, or a side if the opposing angle is known as well as the other
two sides. In each case, you need to know two sides, and these are the first
two arguments:

    >>> numerus.cosine_law(5, 9, side3=8)
    62.181860715346076
    >>> numerus.cosine_law(5, 9, angle=62.2)
    8.001574993050417

Changelog
---------

Release 0.1.0
~~~~~~~~~~~~~

`4 February 2017`

* Added basic trigonometry functions.
* Added check for non-boolean numbers.
