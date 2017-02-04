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
