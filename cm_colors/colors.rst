Color Engine (Internal)
=======================
Everything you can do with CM-Colors’ internal color classes  

This module provides CM-Colors' internal color engine, including
the Color and ColorPair classes.

Color
=====
Represents a single color in any supported format.

.. autoclass:: cm_colors.color.Color
    :members: __init__, is_valid, rgb, error, to_hex, to_rgb_string, to_oklch
    :show-inheritance:

What it does
------------
* Parses color input: hex, rgb(), rgba(), HSL, tuples, lists…
* Converts everything into a clean RGB tuple
* Handles RGBA compositing if you pass a background
* Provides helpers (hex, CSS rgb string, OKLCH conversion)

Examples
--------

Simple parsing:

.. code-block:: python
  
    from cm_colors.color import Color

    c = Color("#7B2DC8")
    print(c.rgb)         # (123, 45, 200)
    print(c.to_hex())    # "#7b2dc8"
    print(c.to_rgb_string())  # "rgb(123, 45, 200)"

RGBA with background:

.. code-block:: python
  
    c = Color("rgba(100, 150, 200, 0.5)", background_context=Color("#000"))
    print(c.rgb)  # composited RGB


Property Reference
------------------

**is_valid**  
    ``True`` if parsing succeeded.

**rgb**  
    Returns ``(r, g, b)`` or ``None``.

**error**  
    Returns an error message if invalid.

**to_hex()**  
    Returns lowercase ``"#rrggbb"``.

**to_rgb_string()**  
    CSS-style ``"rgb(r, g, b)"``.

**to_oklch()**  
    Converts to OKLCH color space.


ColorPair
=========
Holds a text color and a background color, and evaluates readability.

.. autoclass:: cm_colors.color.ColorPair
    :members: __init__, is_valid, errors, contrast_ratio, wcag_level, delta_e, tune_colors
    :show-inheritance:

What it does
------------
* Parses both text and background colors
* Computes readability metrics:
  - WCAG contrast ratio
  - WCAG level (AA, AAA, FAIL)
  - Delta E (visual difference)
* Fixes colors automatically using ``tune_colors()``

Examples
--------

Check readability:

.. code-block:: python

    pair = ColorPair("#777", "#fff")
    print(pair.contrast_ratio)
    print(pair.wcag_level)

Tune colors automatically:

.. code-block:: python

    pair = ColorPair("rgba(100, 100, 100, 0.5)", "white")
    tuned, is_ok = pair.tune_colors()
    print(tuned, is_ok)


Property Reference
------------------

**is_valid**  
    True if both text/background colors are valid.

**errors**  
    List of error messages.

**contrast_ratio**  
    Float value — higher = more readable.

**wcag_level**  
    "FAIL", "AA", "AAA", or "AA Large".

**delta_e**  
    CIEDE2000 difference between text + background.

**tune_colors(details=False)**  
    Automatically fixes colors.

    Returns:

    *Simple mode*::

        (tuned_rgb_tuple, success_boolean)

    *Details mode*::

        {
            "status": True/False,
            "tuned_text": (r, g, b),
            "wcag_level": "AA" | "AAA" | "FAIL",
            "message": "...",
        }


Quick Reference Card
====================

Parse any color:

.. code-block:: python

    c = Color("#fa0")

Check if valid:

.. code-block:: python

    if not c.is_valid:
        print(c.error)

Get color formats:

.. code-block:: python

    c.rgb
    c.to_hex()
    c.to_rgb_string()

Check color contrast:

.. code-block:: python

    pair = ColorPair("#777", "#fff")
    pair.contrast_ratio
    pair.wcag_level

Fix colors:

.. code-block:: python

    tuned, ok = pair.tune_colors()

Calculate perceptual difference:

.. code-block:: python

    pair.delta_e

Convert to OKLCH:

.. code-block:: python

    Color("#ff8040").to_oklch()

