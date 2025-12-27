#!/usr/bin/env python3
"""Generate cover images for the article across LinkedIn, Substack, and Twitter."""

from PIL import Image, ImageDraw, ImageFont
import os

# Output directory
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Colors
BG_DARK = "#1e293b"       # Slate 800
PRIMARY = "#3b82f6"       # Blue 500
ACCENT = "#10b981"        # Emerald 500
TEXT_WHITE = "#f8fafc"    # Slate 50
TEXT_LIGHT = "#94a3b8"    # Slate 400

# Platform dimensions
PLATFORMS = {
    "linkedin": (1200, 628),
    "substack": (1100, 220),
    "twitter": (1200, 675),
}

def get_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Load system font with fallback."""
    font_paths = [
        "/System/Library/Fonts/SFNSMono.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Monaco.ttf",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    if bold:
        font_paths.insert(0, "/System/Library/Fonts/Supplemental/Arial Bold.ttf")

    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                continue
    return ImageFont.load_default()

def draw_code_snippet(draw: ImageDraw.Draw, x: int, y: int, width: int, height: int):
    """Draw a stylized code snippet box."""
    # Code box background
    draw.rounded_rectangle(
        [x, y, x + width, y + height],
        radius=8,
        fill="#0f172a"
    )

    # Window dots
    dot_y = y + 12
    colors = ["#ef4444", "#eab308", "#22c55e"]
    for i, color in enumerate(colors):
        draw.ellipse([x + 12 + i * 18, dot_y - 4, x + 20 + i * 18, dot_y + 4], fill=color)

    # Code lines (simplified)
    line_y = y + 35
    code_font = get_font(14)
    code_lines = [
        ("import ", PRIMARY),
        ("learning_pillars", TEXT_LIGHT),
        ("\n", None),
        ("skills", ACCENT),
        (" = extract(", TEXT_LIGHT),
        ("pdf", PRIMARY),
        (")", TEXT_LIGHT),
    ]

    current_x = x + 15
    for text, color in code_lines:
        if text == "\n":
            line_y += 20
            current_x = x + 15
            continue
        if color:
            draw.text((current_x, line_y), text, fill=color, font=code_font)
            bbox = draw.textbbox((current_x, line_y), text, font=code_font)
            current_x = bbox[2]

def draw_pillar_blocks(draw: ImageDraw.Draw, x: int, y: int, scale: float = 1.0):
    """Draw 4 pillar indicator blocks."""
    colors = [PRIMARY, ACCENT, "#8b5cf6", "#f59e0b"]  # Blue, Green, Purple, Amber
    labels = ["Structure", "Content", "Practice", "UX"]

    block_w = int(80 * scale)
    block_h = int(40 * scale)
    gap = int(10 * scale)
    font = get_font(int(11 * scale))

    for i, (color, label) in enumerate(zip(colors, labels)):
        bx = x + i * (block_w + gap)
        draw.rounded_rectangle(
            [bx, y, bx + block_w, y + block_h],
            radius=4,
            fill=color
        )
        # Center text
        bbox = draw.textbbox((0, 0), label, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text(
            (bx + (block_w - tw) // 2, y + (block_h - th) // 2 - 2),
            label,
            fill=TEXT_WHITE,
            font=font
        )

def draw_arrow(draw: ImageDraw.Draw, x1: int, y1: int, x2: int, y2: int, color: str):
    """Draw an arrow from (x1,y1) to (x2,y2)."""
    draw.line([(x1, y1), (x2, y2)], fill=color, width=3)
    # Arrow head
    arrow_size = 8
    draw.polygon([
        (x2, y2),
        (x2 - arrow_size, y2 - arrow_size // 2),
        (x2 - arrow_size, y2 + arrow_size // 2),
    ], fill=color)

def create_linkedin_cover():
    """Create LinkedIn cover image (1200x628)."""
    w, h = PLATFORMS["linkedin"]
    img = Image.new("RGB", (w, h), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Title
    title_font = get_font(42, bold=True)
    title = "Building Shareable Learning Design Skills"
    draw.text((60, 50), title, fill=TEXT_WHITE, font=title_font)

    subtitle_font = get_font(28)
    subtitle = "with Canvas MCP Integration"
    draw.text((60, 105), subtitle, fill=PRIMARY, font=subtitle_font)

    # Tagline
    tagline_font = get_font(20)
    tagline = "PDF  →  Extraction  →  Skills  →  GitHub  →  Community"
    draw.text((60, 160), tagline, fill=TEXT_LIGHT, font=tagline_font)

    # Draw 4 pillar blocks
    draw_pillar_blocks(draw, 60, 220, scale=1.2)

    # Code snippet on right
    draw_code_snippet(draw, 700, 200, 440, 120)

    # Compounding loop visualization
    loop_y = 380
    labels = ["skill-creator", "validates", "new skills", "integrate with", "canvas-mcp"]
    positions = [80, 250, 420, 600, 800]
    small_font = get_font(16)

    for i, (label, px) in enumerate(zip(labels, positions)):
        color = ACCENT if i % 2 == 0 else TEXT_LIGHT
        draw.text((px, loop_y), label, fill=color, font=small_font)
        if i < len(labels) - 1:
            next_px = positions[i + 1]
            bbox = draw.textbbox((px, loop_y), label, font=small_font)
            draw_arrow(draw, bbox[2] + 10, loop_y + 10, next_px - 10, loop_y + 10, TEXT_LIGHT)

    # Skills count badge
    draw.rounded_rectangle([60, 450, 200, 510], radius=8, fill=PRIMARY)
    badge_font = get_font(24, bold=True)
    draw.text((85, 465), "5 Skills", fill=TEXT_WHITE, font=badge_font)

    # GitHub badge
    draw.rounded_rectangle([220, 450, 420, 510], radius=8, fill=ACCENT)
    draw.text((245, 465), "Open Source", fill=TEXT_WHITE, font=badge_font)

    # Footer branding
    footer_font = get_font(16)
    draw.text((60, 580), "The Hybrid Builder  |  chatwithgpt.substack.com", fill=TEXT_LIGHT, font=footer_font)

    # Decorative elements
    draw.rectangle([0, 0, w, 5], fill=PRIMARY)  # Top accent bar

    return img

def create_substack_cover():
    """Create Substack banner (1100x220) - extreme horizontal format."""
    w, h = PLATFORMS["substack"]
    img = Image.new("RGB", (w, h), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Left side: Title
    title_font = get_font(28, bold=True)
    draw.text((30, 40), "Building Shareable", fill=TEXT_WHITE, font=title_font)
    draw.text((30, 75), "Learning Design Skills", fill=PRIMARY, font=title_font)

    # Center: Flow diagram
    flow_y = 90
    items = ["PDF", "→", "Skills", "→", "GitHub"]
    flow_font = get_font(18)
    start_x = 420

    for i, item in enumerate(items):
        color = TEXT_LIGHT if item == "→" else (ACCENT if i == 2 else TEXT_WHITE)
        draw.text((start_x + i * 70, flow_y), item, fill=color, font=flow_font)

    # Right side: Pillar blocks (compact)
    draw_pillar_blocks(draw, 780, 80, scale=0.7)

    # Bottom: Branding
    footer_font = get_font(14)
    draw.text((30, 180), "The Hybrid Builder", fill=TEXT_LIGHT, font=footer_font)

    # Accent bars
    draw.rectangle([0, 0, w, 3], fill=PRIMARY)
    draw.rectangle([0, h - 3, w, h], fill=ACCENT)

    return img

def create_twitter_cover():
    """Create Twitter card (1200x675)."""
    w, h = PLATFORMS["twitter"]
    img = Image.new("RGB", (w, h), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Title (larger, centered)
    title_font = get_font(48, bold=True)
    title1 = "Building Shareable"
    title2 = "Learning Design Skills"

    bbox1 = draw.textbbox((0, 0), title1, font=title_font)
    bbox2 = draw.textbbox((0, 0), title2, font=title_font)

    draw.text(((w - (bbox1[2] - bbox1[0])) // 2, 80), title1, fill=TEXT_WHITE, font=title_font)
    draw.text(((w - (bbox2[2] - bbox2[0])) // 2, 140), title2, fill=PRIMARY, font=title_font)

    # Subtitle
    subtitle_font = get_font(24)
    subtitle = "Canvas MCP Integration + Evidence-Based Principles"
    bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    draw.text(((w - (bbox[2] - bbox[0])) // 2, 210), subtitle, fill=TEXT_LIGHT, font=subtitle_font)

    # Pillar blocks (centered)
    draw_pillar_blocks(draw, 280, 280, scale=1.3)

    # Flow diagram
    flow_y = 400
    flow_font = get_font(22)
    items = ["PDF", "→", "Extract", "→", "Skills", "→", "Validate", "→", "Share"]

    # Calculate total width
    total_w = sum(draw.textbbox((0,0), item, font=flow_font)[2] for item in items) + len(items) * 15
    start_x = (w - total_w) // 2

    current_x = start_x
    for item in items:
        color = TEXT_LIGHT if item == "→" else ACCENT
        draw.text((current_x, flow_y), item, fill=color, font=flow_font)
        bbox = draw.textbbox((current_x, flow_y), item, font=flow_font)
        current_x = bbox[2] + 15

    # Stats badges
    badge_y = 500
    badge_font = get_font(20, bold=True)

    badges = [("5 Skills", PRIMARY), ("46 Principles", ACCENT), ("Open Source", "#8b5cf6")]
    badge_w = 180
    gap = 30
    total_badges_w = len(badges) * badge_w + (len(badges) - 1) * gap
    badge_start = (w - total_badges_w) // 2

    for i, (text, color) in enumerate(badges):
        bx = badge_start + i * (badge_w + gap)
        draw.rounded_rectangle([bx, badge_y, bx + badge_w, badge_y + 50], radius=8, fill=color)
        bbox = draw.textbbox((0, 0), text, font=badge_font)
        tw = bbox[2] - bbox[0]
        draw.text((bx + (badge_w - tw) // 2, badge_y + 12), text, fill=TEXT_WHITE, font=badge_font)

    # Footer
    footer_font = get_font(16)
    footer = "The Hybrid Builder  |  github.com/vishalsachdev/learning-design-pillars"
    bbox = draw.textbbox((0, 0), footer, font=footer_font)
    draw.text(((w - (bbox[2] - bbox[0])) // 2, 620), footer, fill=TEXT_LIGHT, font=footer_font)

    # Accent bars
    draw.rectangle([0, 0, w, 5], fill=PRIMARY)
    draw.rectangle([0, h - 5, w, h], fill=ACCENT)

    return img

def main():
    print("Generating cover images...")

    # LinkedIn
    linkedin_img = create_linkedin_cover()
    linkedin_path = os.path.join(OUTPUT_DIR, "2024-12-27-cover-image.png")
    linkedin_img.save(linkedin_path, "PNG")
    print(f"  LinkedIn: {linkedin_path}")

    # Substack
    substack_img = create_substack_cover()
    substack_path = os.path.join(OUTPUT_DIR, "2024-12-27-substack-banner.png")
    substack_img.save(substack_path, "PNG")
    print(f"  Substack: {substack_path}")

    # Twitter
    twitter_img = create_twitter_cover()
    twitter_path = os.path.join(OUTPUT_DIR, "2024-12-27-twitter-card.png")
    twitter_img.save(twitter_path, "PNG")
    print(f"  Twitter: {twitter_path}")

    print("\nDone! All cover images generated.")

if __name__ == "__main__":
    main()
