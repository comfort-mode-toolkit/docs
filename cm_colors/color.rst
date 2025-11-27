Color Class
===========

The Color class represents a single color and provides validation, parsing, and conversion functionality for multiple color formats.

Overview
--------

The Color class simplifies working with colors in different formats. It handles parsing, validation, and conversion between formats, making it easy to work with colors from various sources (CSS, design tools, user input).

.. code-block:: python

    from cm_colors import Color

    # Create a color from any format
    color = Color("#ff5733")
    
    # Check if valid
    if color.is_valid:
        print(color.to_hex())        # #ff5733
        print(color.to_rgb_string()) # rgb(255, 87, 51)

Supported Formats
-----------------

The Color class accepts colors in the following formats:

Hexadecimal
~~~~~~~~~~~

.. code-block:: python

    Color("#ff5733")    # Standard 6-digit hex
    Color("#f57")       # Shorthand 3-digit hex
    Color("ff5733")     # Without hash symbol

RGB and RGBA
~~~~~~~~~~~~

.. code-block:: python

    # Tuple format
    Color((255, 87, 51))
    
    # String format
    Color("rgb(255, 87, 51)")
    Color("rgba(255, 87, 51, 0.8)")

For RGBA colors with alpha transparency, the color is automatically composited over a white background for accurate contrast calculations.

HSL and HSLA
~~~~~~~~~~~~

.. code-block:: python

    Color("hsl(9, 100%, 60%)")
    Color("hsla(9, 100%, 60%, 0.9)")

HSL (Hue, Saturation, Lightness) is converted to RGB internally. HSLA colors are composited over white.

Named Colors
~~~~~~~~~~~~

.. code-block:: python

    Color("red")
    Color("cornflowerblue")
    Color("rebeccapurple")

All standard CSS named colors are supported.

Creating Color Instances
-------------------------

Basic Usage
~~~~~~~~~~~

.. code-block:: python

    from cm_colors import Color

    # From hex
    red = Color("#ff0000")
    
    # From RGB tuple
    blue = Color((0, 0, 255))
    
    # From CSS string
    green = Color("rgb(0, 255, 0)")
    
    # From named color
    purple = Color("rebeccapurple")

Validation
~~~~~~~~~~

Always check if a color is valid before using it:

.. code-block:: python

    color = Color("#gggggg")  # Invalid hex
    
    if color.is_valid:
        # Use the color
        print(color.to_hex())
    else:
        # Handle the error
        print(f"Invalid color: {color.errors}")

Properties
----------

``is_valid``
~~~~~~~~~~~~

**Type**: ``bool``

Indicates whether the color was successfully parsed and is valid.

.. code-block:: python

    color = Color("#ff5733")
    print(color.is_valid)  # True

    invalid = Color("not-a-color")
    print(invalid.is_valid)  # False

``_rgb``
~~~~~~~~

**Type**: ``tuple[int, int, int]`` or ``None``

The internal RGB representation of the color. This property is ``None`` if the color is invalid.

.. code-block:: python

    color = Color("#ff5733")
    print(color._rgb)  # (255, 87, 51)

``errors``
~~~~~~~~~~

**Type**: ``list[str]``

A list of error messages if the color is invalid.

.. code-block:: python

    color = Color("invalid")
    if not color.is_valid:
        print(color.errors)  # ["Could not parse color: invalid"]

Methods
-------

``to_hex()``
~~~~~~~~~~~~

**Returns**: ``str``

Converts the color to hexadecimal format with a leading hash symbol.

.. code-block:: python

    color = Color("rgb(255, 87, 51)")
    print(color.to_hex())  # #ff5733

``to_rgb_string()``
~~~~~~~~~~~~~~~~~~~

**Returns**: ``str``

Converts the color to CSS RGB string format.

.. code-block:: python

    color = Color("#ff5733")
    print(color.to_rgb_string())  # rgb(255, 87, 51)

Practical Examples
------------------

Example 1: Format Conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from cm_colors import Color

    # Start with a hex color
    color = Color("#3498db")
    
    # Convert to different formats
    rgb_string = color.to_rgb_string()  # rgb(52, 152, 219)
    hex_string = color.to_hex()         # #3498db
    rgb_tuple = color._rgb              # (52, 152, 219)

Example 2: Validating User Input
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from cm_colors import Color

    def get_valid_color(user_input):
        color = Color(user_input)
        
        if color.is_valid:
            return color
        else:
            raise ValueError(f"Invalid color: {', '.join(color.errors)}")

    # Usage
    try:
        user_color = get_valid_color("#3498db")
        print(f"Valid color: {user_color.to_hex()}")
    except ValueError as e:
        print(e)

Example 3: Working with Transparency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from cm_colors import Color

    # Semi-transparent blue
    color = Color("rgba(52, 152, 219, 0.7)")
    
    if color.is_valid:
        # Automatically composited over white
        print(color._rgb)  # Result after compositing
        print(color.to_hex())

Example 4: Batch Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from cm_colors import Color

    colors = ["#ff0000", "rgb(0, 255, 0)", "blue", "invalid"]
    
    valid_colors = []
    invalid_colors = []
    
    for c in colors:
        color = Color(c)
        if color.is_valid:
            valid_colors.append(color)
        else:
            invalid_colors.append((c, color.errors))
    
    print(f"Valid: {len(valid_colors)}")
    print(f"Invalid: {len(invalid_colors)}")

Validation and Error Handling
------------------------------

Understanding Errors
~~~~~~~~~~~~~~~~~~~~

The Color class provides detailed error messages for invalid inputs:

.. code-block:: python

    color = Color("rgb(300, 100, 100)")  # Red channel out of range
    
    if not color.is_valid:
        print(color.errors)
        # ["Invalid RGB value: values must be 0-255"]

Common Validation Issues
~~~~~~~~~~~~~~~~~~~~~~~~

1. **Invalid hex format**: Incorrect number of characters or invalid characters
2. **RGB values out of range**: Values must be 0-255
3. **Malformed strings**: Missing parentheses, commas, or percentages
4. **Unknown named color**: Not in the CSS color list

Best Practices
--------------

Always Validate
~~~~~~~~~~~~~~~

Check ``is_valid`` before accessing color properties:

.. code-block:: python

    color = Color(user_input)
    
    if color.is_valid:
        # Safe to use
        rgb = color._rgb
    else:
        # Handle error
        return None

Use Appropriate Formats
~~~~~~~~~~~~~~~~~~~~~~~~

Choose the format that matches your data source:

- API responses: Usually hex or RGB tuples
- User input: Often hex strings
- CSS files: Any format
- Design tools: Usually hex or RGB

Handle Transparency
~~~~~~~~~~~~~~~~~~~

Remember that RGBA and HSLA colors are composited automatically:

.. code-block:: python

    # This is composited over white
    semi_transparent = Color("rgba(255, 0, 0, 0.5)")
    
    # For custom compositing, work with tuples directly
    # or use the ColorPair class which handles backgrounds

Related Documentation
---------------------

- :doc:`colorpair` - Working with color pairs and contrast
- :doc:`api` - CMColors class API
- :doc:`cli` - Command-line tool
