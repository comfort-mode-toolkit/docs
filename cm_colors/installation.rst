Installation & Quick Start
==========================

This section guides you through setting up the CM-Colors library and demonstrates
its core functionalities for color accessibility and manipulation.

Installation
------------

Install the CM-Colors library using pip:

.. code-block:: bash

    pip install cm-colors

Basic Usage
-----------

To begin, import the `CMColors` class from the `cm_colors` package and initialize an instance:

.. code-block:: python

    from cm_colors import CMColors
    
    # Initialize the library
    cm = CMColors()

Core Functionalities
--------------------

CM-Colors provides a suite of tools categorized by their primary purpose.

Contrast Analysis & WCAG Compliance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These functions help you assess and ensure your color combinations meet WCAG standards.

.. code-block:: python

    # Define example colors
    text_color = (100, 100, 100) # A medium gray
    bg_color = (255, 255, 255)   # White

    # Calculate the WCAG contrast ratio between text and background colors
    contrast_ratio = cm.calculate_contrast(text_color, bg_color)
    print(f"Contrast ratio: {contrast_ratio:.2f}")
    # Expected Output: Contrast ratio: 5.92 (or similar, depends on exact math)

    # Check WCAG compliance level for normal text (default)
    normal_level = cm.get_wcag_level(text_color, bg_color)
    print(f"WCAG Level (Normal Text): {normal_level}")
    # Expected Output: WCAG Level (Normal Text): AA (if ratio is >= 4.5 and < 7.0)

    # Check WCAG compliance level for large text
    large_level = cm.get_wcag_level(text_color, bg_color, large_text=True)
    print(f"WCAG Level (Large Text): {large_level}")
    # Expected Output: WCAG Level (Large Text): AAA (if ratio is >= 4.5)

Automated Accessibility Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Leverage CM-Colors to automatically adjust colors for WCAG compliance while
preserving visual integrity.

.. code-block:: python

    # Define original colors for optimization
    original_text = (100, 100, 100) # A gray that might not be compliant
    background = (255, 255, 255)   # White

    # Automatically adjust the text color to meet WCAG AAA (or AA for large text)
    # Returns: (adjusted_text_rgb, original_bg_rgb, final_wcag_level, initial_contrast, new_contrast)
    adjusted_text, _, final_level, old_contrast, new_contrast =
        cm.ensure_accessible_colors(original_text, background)
    
    print(f"Original Text: {original_text} -> Adjusted Text: {adjusted_text}")
    print(f"Contrast improved from {old_contrast:.2f} to {new_contrast:.2f}, achieving {final_level} level.")
    # Expected Output: e.g., Original Text: (100, 100, 100) -> Adjusted Text: (74, 74, 74)
    # Contrast improved from 5.92 to 7.01, achieving AAA level.


Color Space Conversions
^^^^^^^^^^^^^^^^^^^^^^^

Convert colors between different color spaces for advanced manipulation or analysis.

.. code-block:: python

    # RGB to OKLCH conversion
    rgb_color = (255, 128, 64) # An orange-red
    oklch_values = cm.rgb_to_oklch(rgb_color)
    print(f"RGB {rgb_color} in OKLCH: L={oklch_values[0]:.3f}, C={oklch_values[1]:.3f}, H={oklch_values[2]:.1f}")
    # Expected Output: e.g., RGB (255, 128, 64) in OKLCH: L=0.741, C=0.170, H=60.0

    # OKLCH to RGB conversion
    oklch_input = (0.7, 0.15, 45.0) # A specific OKLCH color
    rgb_values = cm.oklch_to_rgb(oklch_input)
    print(f"OKLCH {oklch_input} in RGB: {rgb_values}")
    # Expected Output: e.g., OKLCH (0.7, 0.15, 45.0) in RGB: (255, 184, 107)

    # RGB to CIELAB conversion
    lab_values = cm.rgb_to_lab((255, 0, 0)) # Red
    print(f"RGB (255, 0, 0) in LAB: L={lab_values[0]:.2f}, a={lab_values[1]:.2f}, b={lab_values[2]:.2f}")
    # Expected Output: e.g., RGB (255, 0, 0) in LAB: L=53.24, a=80.11, b=67.22

Perceptual Color Difference
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Measure how different two colors *appear* to the human eye using advanced metrics.

.. code-block:: python

    # Calculate Delta E 2000 (most perceptually accurate color difference)
    color_a = (255, 0, 0)   # Red
    color_b = (250, 5, 5)   # Slightly different red
    delta_e = cm.calculate_delta_e_2000(color_a, color_b)
    print(f"Delta E 2000 between {color_a} and {color_b}: {delta_e:.2f}")
    # Expected Output: e.g., Delta E 2000 between (255, 0, 0) and (250, 5, 5): 1.15

    # Calculate OKLCH distance (perceptual distance in OKLab space)
    # First, convert RGB to OKLCH for the distance calculation
    oklch1 = cm.rgb_to_oklch((255, 0, 0))
    oklch2 = cm.rgb_to_oklch((0, 255, 0))
    distance = cm.calculate_oklch_distance(oklch1, oklch2)
    print(f"OKLCH distance between Red and Green: {distance:.2f}")
    # Expected Output: e.g., OKLCH distance between Red and Green: 0.65 (a large distance)

---

Common Use Cases
----------------

* **Accessibility Compliance**: Use :meth:`~cm_colors.CMColors.ensure_accessible_colors` to automatically fix color combinations to meet WCAG standards while preserving visual integrity.
* **Manual Contrast Checking**: Utilize :meth:`~cm_colors.CMColors.calculate_contrast` and :meth:`~cm_colors.CMColors.get_wcag_level` for direct assessment of color pairs.
* **Color Similarity Analysis**: Employ :meth:`~cm_colors.CMColors.calculate_delta_e_2000` and :meth:`~cm_colors.CMColors.calculate_oklch_distance` for precise perceptual difference measurements.
* **Advanced Color Manipulation**: Leverage color space conversion methods like :meth:`~cm_colors.CMColors.rgb_to_oklch` and :meth:`~cm_colors.CMColors.oklch_to_rgb` for fine-grained color adjustments.

For detailed API documentation, including all parameters and return types, see the :doc:`api` reference.