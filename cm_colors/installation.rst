Getting Started with CM-Colors
==============================

*Making your beautiful colors readable for everyone (without ruining your vibe)*

Install It
----------

.. code-block:: bash

    pip install cm-colors

That's it. Seriously.

The One Function You Actually Need
----------------------------------

*Skip to this if you just want your colors to work for everyone*

.. code-block:: python

    from cm_colors import CMColors

    cm = CMColors()

    # Your original colors (these might be hard to read)
    text_color = (100, 100, 100)  # Some gray text
    background = (255, 255, 255)  # White background

    # ✨ The magic happens here ✨
    fixed_text, is_accessible = cm.tune_colors(text_color, background)

    print(f"Your original text color: {text_color}")
    print(f"New readable text color: {fixed_text}")
    print(f"Is it accessible now? {is_accessible}")

**Want more details?**

.. code-block:: python

    # Get the full report
    result = cm.tune_colors(text_color, background, details=True)
    
    print(f"Fixed color: {result['tuned_text']}")
    print(f"WCAG level: {result['wcag_level']}")
    print(f"Status: {result['message']}")
    print(f"Improvement: {result['improvement_percentage']:.1f}%")

**What just happened?**

- We took your gray text on white background
- Made the tiniest possible adjustment so people can actually read it
- You probably can't even tell the difference visually
- But now it passes accessibility standards

**That's literally it.** Use ``fixed_text`` in your CSS and you're done.

"But Wait, What's This Accessibility Thing?"
--------------------------------------------

*Quick explainer for the curious*

**The Problem:** Some color combinations are gorgeous but impossible to read for people with visual differences, older screens, or even just bright sunlight.

**The Solution:** There are official rules (called WCAG) that say "your text needs THIS much contrast against the background so humans can read it."

**The Levels:**

- **FAIL** = People literally can't read your text 😢
- **AA** = Most people can read it comfortably ✅ *(This is what you want)*
- **AAA** = Everyone can read it easily, even in tough conditions ⭐

Our library gets you to AA (or better) with the smallest possible color change.

Other Handy Functions
---------------------

*For when you want to dig deeper*

"Are My Colors Already Good?"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Check if your colors pass the readability test
    text = (80, 80, 80)
    background = (255, 255, 255)

    # Get a simple pass/fail
    level = cm.wcag_level(text, background)
    print(f"Your colors are: {level}")  # "AA", "AAA", or "FAIL"

    # Get the actual contrast number (higher = more readable)
    contrast = cm.contrast_ratio(text, background)
    print(f"Contrast score: {contrast:.1f}")
    # 4.5+ = Good, 7+ = Excellent, under 4.5 = Needs fixing

"How Different Do These Colors Look?"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*For the perfectionists who want to know exactly how much we changed*

.. code-block:: python

    original = (100, 100, 100)
    adjusted = (85, 85, 85)

    # This measures how different colors look to human eyes
    # Under 2.0 = You probably can't tell the difference
    difference = cm.delta_e(original, adjusted)
    print(f"Visual difference: {difference:.1f}")

"Working with Different Color Formats"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Because not everyone uses RGB tuples*

.. code-block:: python

    # Parse different color formats
    hex_color = "#7B2DC8"  # Purple in hex
    rgb_tuple = cm.parse_to_rgb(hex_color)
    print(f"Hex {hex_color} as RGB: {rgb_tuple}")

    # You can also pass hex or rgb strings directly to tune_colors
    fixed, accessible = cm.tune_colors("#7B2DC8", "#FFFFFF")
    print(f"Fixed hex color: {fixed}")

"Large Text Gets Special Treatment"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*18pt+ text or 14pt+ bold text has relaxed requirements*

.. code-block:: python

    # Normal text needs higher contrast
    normal_fixed, _ = cm.tune_colors((150, 150, 150), (255, 255, 255))
    
    # Large text can get away with less contrast
    large_fixed, _ = cm.tune_colors((150, 150, 150), (255, 255, 255), large_text=True)
    
    print(f"Normal text needs: {normal_fixed}")
    print(f"Large text needs: {large_fixed}")

Color Science Stuff
^^^^^^^^^^^^^^^^^^^

*Advanced features for color nerds*

.. code-block:: python

    # Convert between different color systems
    rgb_color = (255, 128, 64)  # Orange-ish

    # Convert to OKLCH (a fancy color system that matches human vision better)
    l, c, h = cm.rgb_to_oklch(rgb_color)
    print(f"In human-vision color space: Lightness={l:.2f}, Colorfulness={c:.2f}, Hue={h:.0f}°")

    # Convert back to RGB
    back_to_rgb = cm.oklch_to_rgb((l, c, h))
    print(f"Back to RGB: {back_to_rgb}")

    # Or convert to LAB color space (used in professional color matching)
    l_star, a_star, b_star = cm.rgb_to_lab(rgb_color)
    print(f"In LAB space: L*={l_star:.1f}, a*={a_star:.1f}, b*={b_star:.1f}")

Real-World Examples
-------------------

"I'm Building a Website"
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    def fix_my_website_colors(text_color, bg_color):
        """
        Takes your website colors and makes them readable.
        Returns CSS-ready colors.
        """
        cm = CMColors()
        
        # Get detailed info about the fix
        result = cm.tune_colors(text_color, bg_color, details=True)
        
        # Convert to CSS format if needed
        fixed_text = result['tuned_text']
        if isinstance(fixed_text, tuple):
            css_text = f"rgb({fixed_text[0]}, {fixed_text[1]}, {fixed_text[2]})"
        else:
            css_text = fixed_text  # Already a string
        
        return {
            'text_color': css_text,
            'background_color': bg_color,
            'wcag_level': result['wcag_level'],
            'is_accessible': result['status'],
            'improvement': f"{result['improvement_percentage']:.1f}%"
        }

    # Use it
    colors = fix_my_website_colors((120, 80, 200), (255, 255, 255))
    print(f"CSS: color: {colors['text_color']};")
    print(f"Accessibility: {colors['wcag_level']} ({colors['improvement']} better)")

"I Need to Check a Bunch of Colors"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Your brand color palette
    brand_colors = [
        ("Purple text", (120, 80, 200)),
        ("Gray text", (100, 100, 100)),
        ("Dark blue", (30, 50, 100))
    ]

    white_bg = (255, 255, 255)

    print("Color Accessibility Report:")
    print("-" * 40)

    for name, color in brand_colors:
        level = cm.wcag_level(color, white_bg)
        contrast = cm.contrast_ratio(color, white_bg)
        
        status = "✅ Good" if level in ["AA", "AAA"] else "❌ Needs fixing"
        print(f"{name}: {status} (Level: {level}, Contrast: {contrast:.1f})")
        
        if level == "FAIL":
            fixed, _ = cm.tune_colors(color, white_bg)
            print(f"  → Suggested fix: {fixed}")

"Batch Processing Colors"
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Process multiple color pairs at once
    color_pairs = [
        ((120, 80, 200), (255, 255, 255)),  # Purple on white
        ((100, 100, 100), (240, 240, 240)), # Gray on light gray
        ((200, 50, 50), (255, 255, 255))    # Red on white
    ]

    print("Batch processing results:")
    for i, (text, bg) in enumerate(color_pairs, 1):
        fixed, accessible = cm.tune_colors(text, bg)
        print(f"Pair {i}: {text} → {fixed} (accessible: {accessible})")

Why This Matters
----------------

- **Legal stuff:** Many places require accessible websites by law
- **Human stuff:** 1 in 12 people have vision differences that make bad contrast painful
- **Practical stuff:** Your content is useless if people can't read it
- **Professional stuff:** Shows you actually know what you're doing

Questions?
----------

**Q: Will this ruin my carefully chosen colors?**

A: Nope! We make the tiniest possible changes. The math ensures you won't notice, but screen readers will.

**Q: What if my colors are already perfect?**

A: We'll tell you they're great and leave them alone.

**Q: I picked terrible colors, can you help?**

A: We'll try our best! But if you chose neon yellow on white... pick better starting colors first 😅

**Q: Do I need to understand color science?**

A: Not at all! That's exactly why this library exists.

**Q: What's the difference between details=True and details=False?**

A: `details=False` (default) gives you just the fixed color and a yes/no on accessibility. `details=True` gives you the full report with WCAG levels, improvement percentages, and helpful messages.

----

*Making the web readable for everyone, one tiny color tweak at a time* 🌈✨