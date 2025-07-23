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
    fixed_text, _, level, old_contrast, new_contrast = cm.ensure_accessible_colors(text_color, background)

    print(f"Your original text color: {text_color}")
    print(f"New readable text color: {fixed_text}")
    print(f"Readability level achieved: {level}")
    print(f"Contrast improved from {old_contrast:.1f} to {new_contrast:.1f}")

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
    level = cm.get_wcag_level(text, background)
    print(f"Your colors are: {level}")  # "AA", "AAA", or "FAIL"

    # Get the actual contrast number (higher = more readable)
    contrast = cm.calculate_contrast(text, background)
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
    difference = cm.calculate_delta_e_2000(original, adjusted)
    print(f"Visual difference: {difference:.1f}")

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

    def fix_my_website_colors(text_rgb, bg_rgb):
        """
        Takes your website colors and makes them readable.
        Returns CSS-ready colors.
        """
        cm = CMColors()
        
        fixed_text, fixed_bg, level, _, _ = cm.ensure_accessible_colors(text_rgb, bg_rgb)
        
        # Convert to CSS format
        css_text = f"rgb({fixed_text[0]}, {fixed_text[1]}, {fixed_text[2]})"
        css_bg = f"rgb({fixed_bg[0]}, {fixed_bg[1]}, {fixed_bg[2]})"
        
        return {
            'text': css_text,
            'background': css_bg,
            'passes': level,
            'ready_for_css': True
        }

    # Use it
    colors = fix_my_website_colors((120, 80, 200), (255, 255, 255))
    print(f"CSS: color: {colors['text']}; background: {colors['background']};")

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
        level = cm.get_wcag_level(color, white_bg)
        contrast = cm.calculate_contrast(color, white_bg)
        
        status = "✅ Good" if level in ["AA", "AAA"] else "❌ Needs fixing"
        print(f"{name}: {status} (Level: {level}, Contrast: {contrast:.1f})")

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

----

*Making the web readable for everyone, one tiny color tweak at a time* 🌈✨
