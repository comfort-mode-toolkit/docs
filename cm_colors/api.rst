CM-Colors API Reference
=======================

This document provides a comprehensive reference for the `CMColors` class,
the primary interface for interacting with the CM-Colors library.
It details all public methods, their parameters, and what they return,
organized into logical categories for ease of navigation.

.. autoclass:: cm_colors.CMColors
    :members: __init__
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

    This class serves as the main entry point for all color accessibility and
    manipulation functionalities offered by the CM-Colors library.


Core Color Analysis & Compliance
---------------------------------

These methods provide tools for calculating contrast ratios, determining WCAG
compliance levels, and measuring perceptual color differences.

.. automethod:: cm_colors.CMColors.calculate_contrast

---

.. automethod:: cm_colors.CMColors.get_wcag_level

---

.. automethod:: cm_colors.CMColors.calculate_delta_e_2000

---

.. automethod:: cm_colors.CMColors.calculate_oklch_distance


Color Space Conversions
-----------------------

These methods facilitate conversions between different color spaces, which are
fundamental for accurate color manipulation and analysis within the library.

.. automethod:: cm_colors.CMColors.rgb_to_oklch

---

.. automethod:: cm_colors.CMColors.oklch_to_rgb

---

.. automethod:: cm_colors.CMColors.rgb_to_lab


Automated Accessibility Optimization
------------------------------------

These are the primary methods for intelligently adjusting colors to meet WCAG
accessibility standards while minimizing perceptual changes to preserve brand identity.

.. automethod:: cm_colors.CMColors.ensure_accessible_colors


Advanced/Internal Optimization Methods
--------------------------------------

For advanced users or those contributing to the library, these methods expose
the underlying optimization algorithms used internally.

.. automethod:: cm_colors.CMColors._binary_search_lightness

---

.. automethod:: cm_colors.CMColors._gradient_descent_oklch