How-to Guides
=============

Practical guides for integrating CM-Colors into your workflow.

Integrate with CI/CD
--------------------

You can run CM-Colors in your Continuous Integration (CI) pipeline to ensure no accessibility regressions are introduced.

**GitHub Actions Example:**

.. code-block:: yaml

    name: Accessibility Check
    on: [push, pull_request]
    
    jobs:
      check-colors:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v3
          - name: Set up Python
            uses: actions/setup-python@v4
            with:
              python-version: '3.9'
          - name: Install CM-Colors
            run: pip install cm-colors
          - name: Run Check
            # Run in check-only mode (if supported) or just run and check for changes
            run: cm-colors . 

Use with Pre-commit
-------------------

To catch accessibility issues before you commit, add CM-Colors to your `.pre-commit-config.yaml`:

.. code-block:: yaml

    repos:
      - repo: local
        hooks:
          - id: cm-colors
            name: CM-Colors
            entry: cm-colors
            language: python
            types: [css]
            additional_dependencies: ['cm-colors']

Customize Contrast Thresholds
-----------------------------

By default, CM-Colors aims for WCAG AA (4.5:1 for normal text). You can adjust this behavior using flags (if supported by CLI) or by using the Python API.

**Python API:**

.. code-block:: python

    from cm_colors import CMColors
    
    cm = CMColors()
    
    # Tune for Large Text (requires 3.0:1)
    tuned, accessible = cm.tune_colors(text, bg, large_text=True)

Working with CSS Variables
--------------------------

CM-Colors supports CSS variables defined in `:root` or `html` blocks within the same file.

**Example:**

.. code-block:: css

    :root {
        --text-color: #ccc; /* Will be tuned here */
    }
    body {
        color: var(--text-color);
    }

When you run `cm-colors .`, the definition of `--text-color` will be updated to a compliant color, ensuring all usages are fixed.
