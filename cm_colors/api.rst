CM-Colors API Reference
=======================

*Everything you can do with CM-Colors (the non-scary version)*

This is your complete guide to all the functions in CM-Colors. Don't worry - 
you probably only need the first one, but the rest are here if you get curious!

.. autoclass:: cm_colors.CMColors
    :members: __init__
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

    The main CM-Colors class. Create one of these, then use it to fix your colors!

The One You Actually Need
-------------------------

*Start here. This is probably all you'll ever use.*

.. automethod:: cm_colors.CMColors.ensure_accessible_colors

    **What it does:** Takes your pretty colors and makes tiny adjustments so everyone can read them.
    
    **When to use it:** Always! This is the magic function that fixes accessibility problems.
    
    **What you get back:** Your adjusted colors, plus info about how much better they got.
    
    **Example:**
    
    .. code-block:: python
    
        # Your colors might be hard to read
        text = (100, 100, 100)  # Gray text
        background = (255, 255, 255)  # White background
        
        # Fix them automatically
        better_text, _, level, old_score, new_score = cm.ensure_accessible_colors(text, background)
        
        print(f"Old color: {text} -> New color: {better_text}")
        print(f"Readability improved from {old_score:.1f} to {new_score:.1f}")
        print(f"Now passes {level} level!")

Color Checking Functions
------------------------

*For when you want to test your colors before fixing them*

.. automethod:: cm_colors.CMColors.calculate_contrast

    **What it does:** Gives you a number that tells you how readable your text is.
    
    **The magic numbers:**
    
    * Under 4.5 = Hard to read (needs fixing)
    * 4.5-7.0 = Pretty readable (AA level)  
    * Over 7.0 = Super readable (AAA level)
    
    **Example:**
    
    .. code-block:: python
    
        score = cm.calculate_contrast((80, 80, 80), (255, 255, 255))
        print(f"Readability score: {score:.1f}")
        # Higher numbers = easier to read

---

.. automethod:: cm_colors.CMColors.get_wcag_level

    **What it does:** Tells you if your colors pass the readability test.
    
    **What the results mean:**
    
    * "FAIL" = People can't read this 😞
    * "AA" = Most people can read this fine ✅ *(This is what you want)*
    * "AAA" = Everyone can read this easily ⭐
    
    **Example:**
    
    .. code-block:: python
    
        result = cm.get_wcag_level((100, 100, 100), (255, 255, 255))
        print(f"Your colors: {result}")  # "AA", "AAA", or "FAIL"

Color Difference Functions
--------------------------

*For perfectionists who want to know exactly how much colors changed*

.. automethod:: cm_colors.CMColors.calculate_delta_e_2000

    **What it does:** Measures how different two colors look to human eyes.
    
    **The magic numbers:**
    
    * Under 1.0 = You literally can't tell the difference
    * 1.0-2.0 = Barely noticeable difference  
    * 2.0+ = You can see the difference
    
    **Example:**
    
    .. code-block:: python
    
        original = (100, 100, 100)
        adjusted = (85, 85, 85)
        
        difference = cm.calculate_delta_e_2000(original, adjusted)
        print(f"Visual difference: {difference:.2f}")
        # Lower = more similar looking

---

.. automethod:: cm_colors.CMColors.calculate_oklch_distance

    **What it does:** Another way to measure color differences (for color science nerds).
    
    **When to use it:** When Delta E 2000 isn't fancy enough for you.

Color Conversion Functions
--------------------------

*For when you need to work with different color systems*

.. automethod:: cm_colors.CMColors.rgb_to_oklch

    **What it does:** Converts regular RGB colors to OKLCH (a fancy color system that matches human vision).
    
    **Why you might need this:** OKLCH is better for making color adjustments that look natural.
    
    **What you get:** Three numbers - Lightness, Colorfulness, and Hue angle.
    
    **Example:**
    
    .. code-block:: python
    
        rgb = (255, 128, 64)  # Orange color
        l, c, h = cm.rgb_to_oklch(rgb)
        print(f"Lightness: {l:.2f}, Colorfulness: {c:.2f}, Hue: {h:.0f}°")

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

Advanced Stuff (For Library Contributors)
------------------------------------------

*These are the guts of how the magic works. You probably don't need these unless you're contributing to the library or just really curious about the math.*

.. automethod:: cm_colors.CMColors._binary_search_lightness

    **What it does:** Uses binary search to find the exact lightness needed for accessibility.
    
    **For who:** People contributing code or wanting to understand the algorithms.

---

.. automethod:: cm_colors.CMColors._gradient_descent_oklch

    **What it does:** Uses gradient descent optimization to find minimal color changes.
    
    **For who:** Math nerds and contributors who want to improve the algorithms.

Quick Reference Card
--------------------

**Just want readable colors?**

.. code-block:: python

    fixed_color, _, level, _, _ = cm.ensure_accessible_colors(your_text, your_background)

**Want to check colors first?**

.. code-block:: python

    level = cm.get_wcag_level(your_text, your_background)
    if level == "FAIL":
        # Fix them with ensure_accessible_colors()

**Want to see how much changed?**

.. code-block:: python

    difference = cm.calculate_delta_e_2000(original_color, fixed_color)
    # Under 2.0 = barely noticeable
