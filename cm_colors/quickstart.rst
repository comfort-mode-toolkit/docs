Quickstart
==========

Get started with CM-Colors in 5 minutes! This guide will show you how to install the tool and tune your first CSS file for accessibility.

Installation
------------

CM-Colors requires Python 3.9 or higher. Install it using pip:

.. code-block:: bash

    pip install cm-colors

CLI: Tuning a CSS File
----------------------

The most common way to use CM-Colors is through the Command Line Interface (CLI). It scans your CSS files for color contrast issues and automatically fixes them.

1.  **Create a sample CSS file** (or use an existing one):

    .. code-block:: css
       :caption: styles.css

       body {
           background-color: white;
           color: #ccc; /* This is too light for white background! */
       }

2.  **Run the CLI**:

    .. code-block:: bash

        cm-colors .

    This command scans the current directory (`.`) for CSS files.

3.  **Check the output**:

    You will see a report in your terminal showing which colors were tuned. A new file `styles_cm.css` will be created with the accessible colors:

    .. code-block:: css
       :caption: styles_cm.css

       body {
           background-color: white;
           color: #767676; /* Tuned to meet WCAG AA */
       }

Python: Checking a Color Pair
-----------------------------

You can also use CM-Colors as a library in your Python scripts.

.. code-block:: python

    from cm_colors import CMColors

    cm = CMColors()

    # Check contrast
    text = "#cccccc"
    bg = "white"
    
    contrast = cm.contrast_ratio(text, bg)
    print(f"Contrast Ratio: {contrast:.2f}")  # Output: ~1.60 (Fail)

    # Tune colors
    tuned_text, is_accessible = cm.tune_colors(text, bg)
    print(f"Tuned Text: {tuned_text}")        # Output: #767676
    
Next Steps
----------

*   Explore :doc:`guides` for more advanced usage.
*   Check the :doc:`cli` for full CLI details.

