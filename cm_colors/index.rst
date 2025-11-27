CM-Colors
=========

**Automated Color Contrast Tuning for Accessibility**

CM-Colors is a library and CLI tool that automatically adjusts color pairs in your CSS to meet WCAG accessibility standards. It uses the OKLCH color space to preserve the visual intent of your design while ensuring readability.

.. grid:: 2

    .. grid-item-card:: Quickstart
        :link: quickstart
        :link-type: doc

        Get up and running with CM-Colors in 5 minutes. Learn how to install and tune your first CSS file.

    .. grid-item-card:: How-to Guides
        :link: guides
        :link-type: doc

        Step-by-step guides for integrating CM-Colors into your workflow, CI/CD pipelines, and more.

    .. grid-item-card:: Reference
        :link: cli
        :link-type: doc

        Detailed API and CLI documentation for developers and power users.

    .. grid-item-card:: Explanation
        :link: explanation
        :link-type: doc

        Deep dive into the concepts behind color spaces, accessibility standards (WCAG), and our tuning algorithms.

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents:
   
   quickstart
   guides
   explanation
   
.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Reference:

   cli
   api
   colorpair
   color
   technical

Choosing the Right API
----------------------

CM-Colors provides multiple ways to interact with its functionality. Choose the one that best fits your needs:

*   **Working with a Color Pair?** Use :doc:`colorpair`.
    Ideal for checking contrast, tuning colors, and validating accessibility for a specific foreground/background combination.

*   **Working with a Single Color?** Use :doc:`color`.
    Best for parsing, converting formats (Hex to RGB, etc.), and validating individual color values.

*   **Need a Standalone Utility?** Use :doc:`api` (CMColors).
    A functional interface for quick calculations or if you prefer not to instantiate objects.