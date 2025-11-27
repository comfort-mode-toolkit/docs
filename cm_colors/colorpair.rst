ColorPair Class
===============

The ColorPair class represents a foreground and background color pair, providing methods to check contrast, validate accessibility, and automatically tune colors to meet WCAG standards.

Overview
--------

The ColorPair class is the primary interface for checking and improving color accessibility. It accepts colors in any format, calculates contrast ratios, determines WCAG compliance levels, and can automatically adjust foreground colors to meet accessibility requirements.

.. code-block:: python

    from cm_colors import ColorPair

    # Create a color pair
    pair = ColorPair("#777777", "white")
    
    # Check accessibility
    print(pair.contrast_ratio)  # 4.47
    print(pair.wcag_level)      # FAIL
    
    # Tune to meet standards
    tuned_color, is_accessible = pair.tune_colors()
    print(tuned_color)          # rgb(117, 117, 117)
    print(is_accessible)        # True

Creating ColorPair Instances
-----------------------------

Basic Usage
~~~~~~~~~~~

.. code-block:: python

    from cm_colors import ColorPair

    # Both colors in hex
    pair = ColorPair("#646464", "#ffffff")
    
    # Mixed formats
    pair = ColorPair("rgb(100, 100, 100)", "white")
    
    # With named colors
    pair = ColorPair("rebeccapurple", "#f0f0f0")

Large Text Option
~~~~~~~~~~~~~~~~~

Text that is 18 points (24 pixels) or larger, or 14 points (18.5 pixels) or larger and bold, has different contrast requirements:

.. code-block:: python

    # Normal text (stricter requirements)
    pair_normal = ColorPair("#767676", "white")
    
    # Large text (more lenient requirements)
    pair_large = ColorPair("#767676", "white", large_text=True)
    
    print(pair_normal.wcag_level)  # FAIL
    print(pair_large.wcag_level)   # AA

Properties
----------

``contrast_ratio``
~~~~~~~~~~~~~~~~~~

**Type**: ``float``

The contrast ratio between the foreground and background colors, calculated according to WCAG guidelines. Higher values indicate better readability.

**Range**: 1.0 (no contrast) to 21.0 (maximum contrast)

.. code-block:: python

    pair = ColorPair("black", "white")
    print(pair.contrast_ratio)  # 21.0 (maximum contrast)
    
    pair = ColorPair("#777777", "white")
    print(pair.contrast_ratio)  # 4.47

``wcag_level``
~~~~~~~~~~~~~~

**Type**: ``str``

The WCAG conformance level based on the contrast ratio.

**Possible values**:

- ``"AAA"``: Exceeds enhanced conformance (7.0+ for normal text, 4.5+ for large text)
- ``"AA"``: Meets minimum conformance (4.5+ for normal text, 3.0+ for large text)
- ``"FAIL"``: Does not meet minimum contrast requirements

.. code-block:: python

    pair = ColorPair("black", "white")
    print(pair.wcag_level)  # AAA
    
    pair = ColorPair("#646464", "white")
    print(pair.wcag_level)  # AA
    
    pair = ColorPair("#cccccc", "white")
    print(pair.wcag_level)  # FAIL

``delta_e``
~~~~~~~~~~~

**Type**: ``float``

The perceptual color difference (Delta E 2000) between the foreground and background colors. This measures how different the colors appear to human vision, regardless of contrast.

**Range**: 0.0 (identical) to 100.0+ (very different)

**Guidelines**:

- 0.0-1.0: Differences not perceptible
- 1.0-2.3: Perceptible through close observation
- 2.3-10.0: Perceptible at a glance
- 10.0+: Colors are distinctly different

.. code-block:: python

    pair = ColorPair("#646464", "#666666")
    print(pair.delta_e)  # 0.45 (barely noticeable)

``is_valid``
~~~~~~~~~~~~

**Type**: ``bool``

Indicates whether both colors in the pair are valid and were successfully parsed.

.. code-block:: python

    valid_pair = ColorPair("red", "white")
    print(valid_pair.is_valid)  # True
    
    invalid_pair = ColorPair("not-a-color", "white")
    print(invalid_pair.is_valid)  # False

``errors``
~~~~~~~~~~

**Type**: ``list[str]``

A list of error messages if either color in the pair is invalid.

.. code-block:: python

    pair = ColorPair("invalid", "white")
    if not pair.is_valid:
        print(pair.errors)  # ["Could not parse color: invalid"]

Methods
-------

``tune_colors()``
~~~~~~~~~~~~~~~~~

**Signature**: ``tune_colors(details=False) -> tuple | dict``

Automatically adjusts the foreground color to meet WCAG AA standards while preserving visual similarity.

**Parameters**:

- ``details`` (bool, optional): If True, returns a detailed dictionary. If False (default), returns a simple tuple.

**Returns**:

When ``details=False`` (default):
    ``tuple[str, bool]``: (tuned_color_string, is_accessible)

When ``details=True``:
    ``dict``: Detailed result with the following keys:
    
    - ``tuned_text`` (str): The tuned foreground color
    - ``status`` (bool): True if accessible, False if tuning failed
    - ``wcag_level`` (str): The WCAG level after tuning
    - ``improvement_percentage`` (float): Percentage improvement in contrast
    - ``message`` (str): Human-readable status message

**Example (Simple)**:

.. code-block:: python

    pair = ColorPair("#777777", "white")
    tuned_color, is_accessible = pair.tune_colors()
    
    if is_accessible:
        print(f"Use this color: {tuned_color}")
    else:
        print("Could not tune - pick a different starting color")

**Example (Detailed)**:

.. code-block:: python

    pair = ColorPair("#777777", "white")
    result = pair.tune_colors(details=True)
    
    print(f"Tuned color: {result['tuned_text']}")
    print(f"WCAG level: {result['wcag_level']}")
    print(f"Improvement: {result['improvement_percentage']:.1f}%")
    print(f"Message: {result['message']}")

Understanding WCAG Levels
--------------------------

WCAG (Web Content Accessibility Guidelines) defines contrast requirements for text readability.

Contrast Requirements
~~~~~~~~~~~~~~~~~~~~~

**Normal Text** (less than 18pt or less than 14pt bold):

- AA level: Minimum 4.5:1 contrast ratio
- AAA level: Minimum 7.0:1 contrast ratio

**Large Text** (18pt+ or 14pt+ bold):

- AA level: Minimum 3.0:1 contrast ratio
- AAA level: Minimum 4.5:1 contrast ratio

When to Use Each Level
~~~~~~~~~~~~~~~~~~~~~~~

- **AA**: Minimum standard for most use cases. Required for legal compliance in many jurisdictions.
- **AAA**: Enhanced standard for better accessibility. Recommended for critical content, elderly users, or low-vision contexts.

Practical Examples
------------------

Example 1: Basic Accessibility Check
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from cm_colors import ColorPair

    # Check if colors are accessible
    pair = ColorPair("#646464", "white")
    
    if pair.wcag_level in ["AA", "AAA"]:
        print("Colors are accessible!")
    else:
        print(f"Contrast ratio: {pair.contrast_ratio:.2f}")
        print("Colors need improvement")

Example 2: Automatic Color Tuning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from cm_colors import ColorPair

    # Tune colors automatically
    pair = ColorPair("#777777", "#ffffff")
    
    print(f"Original: {pair.wcag_level} (contrast: {pair.contrast_ratio:.2f})")
    
    tuned_color, is_accessible = pair.tune_colors()
    
    if is_accessible:
        print(f"Tuned to: {tuned_color}")
        new_pair = ColorPair(tuned_color, "#ffffff")
        print(f"New level: {new_pair.wcag_level} (contrast: {new_pair.contrast_ratio:.2f})")

Example 3: Detailed Tuning Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from cm_colors import ColorPair

    pair = ColorPair("#888888", "#f0f0f0")
    result = pair.tune_colors(details=True)
    
    print(f"Status: {'Success' if result['status'] else 'Failed'}")
    print(f"Tuned color: {result['tuned_text']}")
    print(f"WCAG level: {result['wcag_level']}")
    print(f"Improvement: {result['improvement_percentage']:.1f}%")
    print(f"Message: {result['message']}")

Example 4: Working with Large Text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from cm_colors import ColorPair

    # Same color, different requirements
    text_color = "#767676"
    bg_color = "white"
    
    # Normal text
    normal = ColorPair(text_color, bg_color)
    print(f"Normal text: {normal.wcag_level}")  # FAIL
    
    # Large text (more lenient)
    large = ColorPair(text_color, bg_color, large_text=True)
    print(f"Large text: {large.wcag_level}")    # AA

Example 5: Batch Processing Colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from cm_colors import ColorPair

    colors_to_check = [
        ("#646464", "white"),
        ("#888888", "#f0f0f0"),
        ("#cccccc", "white"),
    ]
    
    results = []
    for text, bg in colors_to_check:
        pair = ColorPair(text, bg)
        if pair.wcag_level == "FAIL":
            tuned, success = pair.tune_colors()
            if success:
                results.append((text, tuned))
            else:
                print(f"Could not tune {text} on {bg}")

Example 6: Measuring Visual Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from cm_colors import ColorPair

    original = "#777777"
    background = "white"
    
    pair = ColorPair(original, background)
    tuned, success = pair.tune_colors()
    
    if success:
        # Measure how much the color changed
        change_pair = ColorPair(original, tuned)
        print(f"Delta E: {change_pair.delta_e:.2f}")
        
        if change_pair.delta_e < 2.3:
            print("Change is barely perceptible")
        else:
            print("Change is noticeable")

Best Practices
--------------

Check Validity First
~~~~~~~~~~~~~~~~~~~~

Always verify that the color pair is valid before using its properties:

.. code-block:: python

    pair = ColorPair(text_color, bg_color)
    
    if pair.is_valid:
        # Safe to use
        if pair.wcag_level == "FAIL":
            tuned, _ = pair.tune_colors()
    else:
        # Handle errors
        print(f"Invalid colors: {pair.errors}")

Target AA Level for Most Cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WCAG AA is the recommended standard for most applications:

.. code-block:: python

    pair = ColorPair(text, background)
    
    if pair.wcag_level in ["AA", "AAA"]:
        # Use colors as-is
        use_colors(text, background)
    else:
        # Tune to meet AA
        tuned, success = pair.tune_colors()
        if success:
            use_colors(tuned, background)

Handle Tuning Failures
~~~~~~~~~~~~~~~~~~~~~~~

Not all color pairs can be tuned while preserving visual similarity:

.. code-block:: python

    pair = ColorPair(text, background)
    tuned, is_accessible = pair.tune_colors()
    
    if is_accessible:
        # Success - use tuned color
        apply_color(tuned)
    else:
        # Failure - choose a different starting color
        print(f"Original contrast too low: {pair.contrast_ratio:.2f}")
        print("Please select a darker text or lighter background")

Use Large Text Flag Appropriately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only use ``large_text=True`` for text that actually qualifies:

.. code-block:: python

    # For headings (18pt+)
    heading_pair = ColorPair(heading_color, bg, large_text=True)
    
    # For body text
    body_pair = ColorPair(body_color, bg, large_text=False)

Limitations
-----------

Starting Color Must Be Reasonable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tuning algorithm preserves visual similarity by limiting color changes to a Delta E threshold. Extremely low-contrast pairs (e.g., light gray on white) cannot be fixed:

.. code-block:: python

    # This will likely fail to tune
    pair = ColorPair("#e0e0e0", "white")  # Contrast: 1.18
    tuned, success = pair.tune_colors()
    
    print(success)  # False - starting colors too similar

**Solution**: Choose a starting color that is closer to accessible contrast requirements.

Only Foreground Color Is Adjusted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``tune_colors`` method only adjusts the foreground (text) color. The background color remains unchanged:

.. code-block:: python

    pair = ColorPair(text, background)
    tuned, _ = pair.tune_colors()
    # tuned is the adjusted text color
    # background remains unchanged

Related Documentation
---------------------

- :doc:`color` - Color class for single colors
- :doc:`api` - CMColors class (alternative API)
- :doc:`cli` - Command-line tool for CSS files
