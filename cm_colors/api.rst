CMColors Utility Class
======================

The ``CMColors`` class provides a high-level utility interface for color contrast tuning and analysis.

.. note::
    **Recommendation**: For object-oriented color manipulation, consider using the :doc:`colorpair` and :doc:`color` classes. The ``CMColors`` class is maintained for backward compatibility and for users who prefer a functional utility approach.

.. autoclass:: cm_colors.CMColors
    :members: __init__
    :undoc-members:
    :show-inheritance:

    The main utility class for CM-Colors operations.

Color Tuning
------------

.. automethod:: cm_colors.CMColors.tune_colors

    Adjusts a foreground color to meet WCAG contrast requirements against a background color.

    **Examples:**

    .. code-block:: python

        cm = CMColors()

        # Simple tuning
        tuned_text, is_accessible = cm.tune_colors("gray", "white")
        print(f"Tuned: {tuned_text}")

        # Detailed report
        result = cm.tune_colors("gray", "white", details=True)
        print(f"WCAG Level: {result['wcag_level']}")

Contrast Analysis
-----------------

.. automethod:: cm_colors.CMColors.contrast_ratio

    Calculates the contrast ratio between two colors.

    **Returns:**
        float: The contrast ratio (1.0 to 21.0).

    **Example:**

    .. code-block:: python

        ratio = cm.contrast_ratio("#000000", "#FFFFFF")
        # Returns 21.0

.. automethod:: cm_colors.CMColors.wcag_level

    Determines the WCAG compliance level for a color pair.

    **Returns:**
        str: "AAA", "AA", or "FAIL".

    **Example:**

    .. code-block:: python

        level = cm.wcag_level("#767676", "#FFFFFF")
        # Returns "AA"

.. automethod:: cm_colors.CMColors.delta_e

    Calculates the Delta E (CIE 2000) distance between two colors.

    **Returns:**
        float: The perceptual difference between the colors.

Color Conversion
----------------

.. automethod:: cm_colors.CMColors.parse_to_rgb

    Parses a color string into an RGB tuple.

.. automethod:: cm_colors.CMColors.rgb_to_oklch

    Converts an RGB tuple to OKLCH color space.

.. automethod:: cm_colors.CMColors.oklch_to_rgb

    Converts an OKLCH tuple to RGB color space.

.. automethod:: cm_colors.CMColors.rgb_to_lab

    Converts an RGB tuple to LAB color space.