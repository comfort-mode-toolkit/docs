Explanation
===========

Understanding the concepts behind CM-Colors.

Why Accessibility Matters
-------------------------

Web accessibility ensures that people with diverse abilities can perceive, understand, navigate, and interact with the web. Color contrast is a critical aspect of visual accessibility.

Low contrast text can be difficult or impossible to read for users with:
*   Low vision
*   Color blindness
*   Aging eyes
*   Situational impairments (e.g., reading on a phone in bright sunlight)

By tuning your colors, you make your content readable for everyone.

Understanding WCAG
------------------

The Web Content Accessibility Guidelines (WCAG) are the international standard for web accessibility. CM-Colors focuses on **Success Criterion 1.4.3 (Contrast Minimum)**.

*   **AA Level**: Requires a contrast ratio of at least **4.5:1** for normal text and **3.0:1** for large text.
*   **AAA Level**: Requires a contrast ratio of at least **7.0:1** for normal text and **4.5:1** for large text.

CM-Colors automatically calculates these ratios and adjusts colors to meet the target level (defaulting to AA).

Color Spaces: RGB vs OKLCH
--------------------------

Most web colors are defined in **RGB** (Red, Green, Blue). While convenient for screens, RGB is not "perceptually uniform"—mathematical changes in RGB don't always correspond to the visual changes we perceive.

CM-Colors uses the **OKLCH** color space for its tuning algorithms.
*   **L (Lightness)**: Perceived brightness.
*   **C (Chroma)**: Color intensity/saturation.
*   **H (Hue)**: The color itself (red, blue, etc.).

By working in OKLCH, we can adjust the **Lightness** to improve contrast while keeping the **Hue** and **Chroma** as close as possible to your original design intent. This ensures your brand colors remain recognizable, just more accessible.

How Tuning Works
----------------

When you provide a text and background color pair:
1.  CM-Colors calculates the current contrast ratio.
2.  If it fails WCAG standards, it converts the text color to OKLCH.
3.  It iteratively adjusts the Lightness (and sometimes Chroma) until the target contrast ratio is met.
4.  It converts the result back to RGB/Hex for use in your CSS.
