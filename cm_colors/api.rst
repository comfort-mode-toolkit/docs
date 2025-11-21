API Reference
===============

*Everything you can do with CM-Colors (the non-scary version)*

This is your complete guide to all the functions in CM-Colors. Don't worry - 
you probably only need the first one, but the rest are here if you get curious!

.. note::

    **New in v0.3.0**: The :doc:`colorpair` and :doc:`color` classes provide a more intuitive API for working with colors. This CMColors class remains fully supported for backward compatibility.

.. autoclass:: cm_colors.CMColors
    :members: __init__
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

    The main CM-Colors class. Create one of these, then use it to tune your colors!

The One You Actually Need
-------------------------

*Start here. This is probably all you'll ever use.*

.. automethod:: cm_colors.CMColors.tune_colors

    **What it does:** Takes your pretty colors and makes tiny adjustments so everyone can read them.
    
    **When to use it:** Always! This is the magic function that fixes accessibility problems.
    
    **What you get back:** 
    
    * **Simple mode** (default): Just the tuned color and whether it's accessible
    * **Details mode** (``details=True``): Full report with improvement stats and messages
    
    **Examples:**
    
    .. code-block:: python
    
        # Simple - just get the fixed color
        text = "rgb(100, 100, 100)"  # Gray text
        background = "rgb(255, 255, 255)"  # White background

        tuned_text, is_accessible = cm.tune_colors(text, background)
        print(f"Tuned color: {tuned_text}") #"rgb(98, 98, 98)"
        print(f"Is accessible: {is_accessible}") #True
        
    .. code-block:: python
    
        # Detailed - get the full report
        result = cm.tune_colors(text, background, details=True)
        print(f"Tuned color: {result['tuned_text']}")
        print(f"WCAG level: {result['wcag_level']}")
        print(f"Message: {result['message']}")
        print(f"Improvement: {result['improvement_percentage']:.1f}%")
        
    .. code-block:: python
    
        # Large text has different requirements
        large_tuned_text, large_accessible = cm.tune_colors(text, background, large_text=True)

Color Checking Functions
------------------------

*For when you want to test your colors before tuning them*

.. automethod:: cm_colors.CMColors.contrast_ratio

    **What it does:** Gives you a number that tells you how readable your text is.
    
    **The magic numbers:**
    
    * Under 4.5 = Hard to read (needs tuning)
    * 4.5-7.0 = Pretty readable (AA level)  
    * Over 7.0 = Super readable (AAA level)
    
    **Example:**
    
    .. code-block:: python
    
        score = cm.contrast_ratio((80, 80, 80), (255, 255, 255))
        print(f"Readability score: {score:.1f}")
        # Higher numbers = easier to read

---

.. automethod:: cm_colors.CMColors.wcag_level

    **What it does:** Tells you if your colors pass the readability test.
    
    **What the results mean:**
    
    * "FAIL" = People can't read this 😞
    * "AA" = Most people can read this fine ✅ *(This is what you want)*
    * "AAA" = Everyone can read this easily ⭐
    
    **Examples:**
    
    .. code-block:: python
    
        # Normal text
        result = cm.wcag_level((100, 100, 100), (255, 255, 255))
        print(f"Your colors: {result}")  # "AA", "AAA", or "FAIL"
        
        # Large text (18pt+ or 14pt+ bold) has different requirements
        large_result = cm.wcag_level((100, 100, 100), (255, 255, 255), large_text=True)
        print(f"Large text level: {large_result}")

Color Difference Functions
--------------------------

*For perfectionists who want to know exactly how much colors changed*

.. automethod:: cm_colors.CMColors.delta_e

    **What it does:** Measures how different two colors look to human eyes.
    
    **The magic numbers:**
    
    * Under 1.0 = You literally can't tell the difference
    * 1.0-2.3 = Barely noticeable difference  
    * 2.3+ = You can clearly see the difference
    
    **Example:**
    
    .. code-block:: python
    
        original = (100, 100, 100)
        adjusted = (85, 85, 85)
        
        difference = cm.delta_e(original, adjusted)
        print(f"Visual difference: {difference:.2f}")
        # Lower = more similar looking

Color Format Functions
----------------------

*For working with different color formats*

.. automethod:: cm_colors.CMColors.parse_to_rgb

    **What it does:** Converts hex codes, rgb strings, or other formats to RGB tuples.
    
    **When to use it:** When you have colors in different formats and need them as RGB tuples.
    
    **Example:**
    
    .. code-block:: python
    
        # Convert hex to RGB
        rgb = cm.parse_to_rgb("#7B2DC8")
        print(f"RGB: {rgb}")  # (123, 45, 200)
        
        # You can also pass different formats directly to tune_colors
        tuned_text, accessible = cm.tune_colors("#7B2DC8", "#FFFFFF")

Color Conversion Functions
--------------------------

*For when you need to work with different color systems*

.. automethod:: cm_colors.CMColors.rgb_to_oklch

    **What it does:** Converts regular RGB colors to OKLCH (a fancy color system that matches human vision).
    
    **Why you might need this:** OKLCH is better for making color adjustments that look natural.
    
    **What you get:** Three numbers - Lightness (0-1), Chroma (0-~0.4), and Hue angle (0-360°).
    
    **Example:**
    
    .. code-block:: python
    
        rgb = (255, 128, 64)  # Orange color
        l, c, h = cm.rgb_to_oklch(rgb)
        print(f"Lightness: {l:.2f}, Chroma: {c:.2f}, Hue: {h:.0f}°")

---

.. automethod:: cm_colors.CMColors.oklch_to_rgb

    **What it does:** Converts OKLCH colors back to regular RGB.
    
    **When to use it:** After you've adjusted colors in OKLCH space and need them for CSS.
    
    **Example:**
    
    .. code-block:: python
    
        # Convert back to RGB for use in your website
        oklch_color = (0.7, 0.15, 45.0)
        rgb = cm.oklch_to_rgb(oklch_color)
        print(f"RGB: {rgb}")  # Ready for CSS!

---

.. automethod:: cm_colors.CMColors.rgb_to_lab

    **What it does:** Converts RGB to LAB color space (used in professional color work).
    
    **When you need it:** Mostly for advanced color calculations or if you're doing print design.
    
    **Example:**
    
    .. code-block:: python
    
        rgb = (255, 128, 64)
        l_star, a_star, b_star = cm.rgb_to_lab(rgb)
        print(f"LAB: L*={l_star:.1f}, a*={a_star:.1f}, b*={b_star:.1f}")

Quick Reference Card
--------------------

**Just want readable colors?**

.. code-block:: python

    # Simple way
    tuned_text, is_accessible = cm.tune_colors(your_text, your_background)

    # With details
    result = cm.tune_colors(your_text, your_background, details=True)

**Want to check colors first?**

.. code-block:: python

    level = cm.wcag_level(your_text, your_background)
    if level == "FAIL":
        tuned_text, _ = cm.tune_colors(your_text, your_background)

**Want to see how much changed?**

.. code-block:: python

    original = (100, 100, 100)
    t, _ = cm.tune_colors(original, background)
    difference = cm.delta_e(original, tuned_text)
    # Under 2.3 = barely noticeable

**Working with different color formats?**

.. code-block:: python

    # Parse any format
    rgb = cm.parse_to_rgb("#FF8040")
    
    # Or use directly
    tuned_text, _ = cm.tune_colors("#FF8040", "#FFFFFF")

**Large text (18pt+ or 14pt+ bold)?**

.. code-block:: python

    # Large text has relaxed contrast requirements
    tuned_text, accessible = cm.tune_colors(text, bg, large_text=True)
    level = cm.wcag_level(text, bg, large_text=True)

Function Return Values Quick Guide
----------------------------------

**tune_colors() returns:**

* **details=False (default):** ``(tuned_color_string, is_accessible_boolean)``
* **details=True:** Dictionary with keys:

  * ``'tuned_text'`` - The tuned color
  * ``'status'`` - True if accessible, False if failed
  * ``'wcag_level'`` - "AA", "AAA", or "FAIL"
  * ``'improvement_percentage'`` - How much contrast improved
  * ``'message'`` - Human-readable status message

**Other functions return:**

* ``contrast_ratio()`` - Float (higher = more readable)
* ``wcag_level()`` - String ("AA", "AAA", or "FAIL")  
* ``delta_e()`` - Float (lower = more similar)
* ``parse_to_rgb()`` - RGB tuple (r, g, b)
* Color conversions - Tuples in respective color spaces