CLI Tool
========

The CM-Colors command-line interface automatically tunes color contrast in CSS files to meet accessibility standards.

Overview
--------

The CLI tool scans CSS files for color pairs (foreground and background colors), checks their contrast against WCAG standards, and automatically adjusts colors that fail to meet accessibility requirements. Modified CSS files are saved with a ``_cm`` suffix, and a visual HTML report is generated for successfully tuned pairs.

Installation
------------

Install CM-Colors with pip:

.. code-block:: bash

    pip install cm-colors

The CLI tool is automatically available after installation.

Basic Usage
-----------

Process a single CSS file:

.. code-block:: bash

    cm-colors style.css

Process all CSS files in a directory:

.. code-block:: bash

    cm-colors ./styles/

Process files in the current directory:

.. code-block:: bash

    cm-colors .

Command-Line Options
--------------------

``--default-bg``
~~~~~~~~~~~~~~~~

Specifies the default background color for rules that do not explicitly define a background color.

**Default**: ``white``

**Example**:

.. code-block:: bash

    cm-colors style.css --default-bg "#f0f0f0"

This is useful when your CSS relies on a body-level background color that is not repeated in every rule.

Features
--------

CSS Variable Support
~~~~~~~~~~~~~~~~~~~~

The CLI supports tuning colors defined as CSS variables (custom properties).

*   **Scope**: Variables must be defined in ``:root`` or ``html`` blocks within the same file.
*   **Behavior**: When a variable is used in a color pair that requires tuning, the CLI updates the **variable definition** itself. This ensures that all other usages of that variable also benefit from the improved contrast.

**Example Input**:

.. code-block:: css

    :root {
        --text-primary: #ccc; /* Too light */
    }
    body {
        color: var(--text-primary);
        background: white;
    }

**Example Output** (``_cm.css``):

.. code-block:: css

    :root {
        --text-primary: #767676; /* Tuned */
    }
    body {
        color: var(--text-primary);
        background: white;
    }

Understanding the Output
------------------------

Summary Statistics
~~~~~~~~~~~~~~~~~~

The CLI displays a color-coded summary at the top of the output:

.. code-block:: text

    2 pairs already accessible (Great job on these)
    3 pairs tuned
    5 failed tuning (Please pick better starter colors for these)

- **Already accessible** (cyan): Color pairs that already meet WCAG AA standards
- **Tuned** (green): Color pairs that were successfully adjusted to meet standards
- **Failed tuning** (red): Color pairs that could not be tuned within acceptable limits

Detailed Failure Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For pairs that could not be tuned, the CLI provides detailed information:

.. code-block:: text

    Could not tune 2 pairs:
      style.css -> .header
        #cccccc on #ffffff (Contrast: 1.61)
        Reason: Could not tune without too much changes

Each failure shows:

- The file and CSS selector
- The original color pair (highlighted in red)
- The current contrast ratio
- The reason for failure

Output Files
~~~~~~~~~~~~

Modified CSS Files
^^^^^^^^^^^^^^^^^^

For each processed CSS file, a modified version is created with the suffix ``_cm``:

- Input: ``style.css``
- Output: ``style_cm.css``

The modified file contains the same CSS structure with tuned colors where necessary.

HTML Report
^^^^^^^^^^^

When colors are successfully tuned, an HTML report is generated at ``cm_colors_report.html``. This report provides a visual comparison of the before and after states for each tuned color pair.

Practical Examples
------------------

Example 1: Single File Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cm-colors navigation.css

**Output**:

.. code-block:: text

    Processing 1 files...

    1 pairs already accessible (Great job on these)
    2 pairs tuned

    Report generated: /path/to/cm_colors_report.html
    Have a chocolate

Example 2: Directory Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cm-colors ./css/

**Output**:

.. code-block:: text

    Processing 5 files...

    8 pairs already accessible (Great job on these)
    4 pairs tuned
    1 failed tuning (Please pick better starter colors for these)

    Could not tune 1 pairs:
      main.css -> .warning
        #fff200 on #ffffff (Contrast: 1.13)
        Reason: Could not tune without too much changes

    Report generated: /path/to/cm_colors_report.html
    Have a chocolate

Troubleshooting
---------------

Command Not Found
~~~~~~~~~~~~~~~~~

If the ``cm-colors`` command is not found after installation:

1. Verify installation: ``pip show cm-colors``
2. Check that the installation location is in your PATH
3. Try using the module directly: ``python -m cm_colors.cli.main``

No CSS Files Found
~~~~~~~~~~~~~~~~~~

If you see "No CSS files found":

- Verify the path is correct
- Check that CSS files exist in the specified directory
- Ensure files have the ``.css`` extension
- Note that ``*_cm.css`` files are automatically excluded

Many Failures
~~~~~~~~~~~~~

If many color pairs fail to tune:

- Review your color palette for sufficient contrast
- Consider using darker text colors or lighter backgrounds
- Consult the WCAG contrast calculator for guidance: https://webaim.org/resources/contrastchecker/

Related Documentation
---------------------

- :doc:`color` - Color class API
- :doc:`colorpair` - ColorPair class API  
- :doc:`api` - CMColors class API
