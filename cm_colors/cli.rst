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
      style.css -> .button
        #3498db on #ffffff (Contrast: 3.15)
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

The report includes:

- The CSS selector and file name
- Visual color swatches showing the original and tuned colors
- Sample text demonstrating the readability difference
- WCAG level badges (FAIL to AA, FAIL to AAA, etc.)

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
    Have a chocolate 🍫

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
    Have a chocolate 🍫

Example 3: Custom Background Color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your site uses a light gray background:

.. code-block:: bash

    cm-colors style.css --default-bg "#f5f5f5"

This ensures accurate contrast calculations for rules that do not specify a background color.

Common Scenarios
----------------

Scenario 1: All Colors Are Accessible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your colors already meet accessibility standards:

.. code-block:: text

    Processing 1 files...

    5 pairs already accessible (Great job on these)

    No changes needed. ✨

No ``_cm`` files or HTML report are generated since no changes were made.

Scenario 2: Some Colors Cannot Be Tuned
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When starting colors are too far from accessible:

.. code-block:: text

    Could not tune 1 pairs:
      style.css -> .accent
        #e0e0e0 on #ffffff (Contrast: 1.18)
        Reason: Could not tune without too much changes

**Solution**: Choose a darker starting color for the text or a different background color. The library preserves visual similarity, so extremely low-contrast pairs cannot be fixed without significant color changes.

Scenario 3: Nested CSS Rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CLI correctly handles nested rules such as media queries:

.. code-block:: css

    @media (min-width: 768px) {
        .responsive-text {
            color: #777777;
            background-color: white;
        }
    }

Colors within ``@media`` and ``@supports`` rules are processed and tuned as needed.

Workflow Integration
--------------------

Pre-Commit Hook
~~~~~~~~~~~~~~~

Add CM-Colors to your pre-commit workflow:

.. code-block:: yaml

    # .pre-commit-config.yaml
    repos:
      - repo: local
        hooks:
          - id: cm-colors
            name: Check CSS color contrast
            entry: cm-colors
            language: system
            files: \.css$
            pass_filenames: true

Continuous Integration
~~~~~~~~~~~~~~~~~~~~~~

Run CM-Colors in your CI pipeline:

.. code-block:: bash

    # In your CI script
    cm-colors ./css/
    if [ $? -ne 0 ]; then
        echo "Color contrast check failed"
        exit 1
    fi

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
