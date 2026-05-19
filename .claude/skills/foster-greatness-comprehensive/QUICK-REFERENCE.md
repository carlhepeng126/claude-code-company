# Foster Greatness Brand Quick Reference

## Colors (CSS Variables)

```css
:root {
    /* Primary */
    --fg-navy: #1a2949;
    --fg-teal: #0067a2;

    /* Accents */
    --fg-orange: #fa8526;
    --fg-yellow: #faca2c;
    --fg-teal-accent: #00c8b7;
    --fg-blue-accent: #7abad8;
    --fg-light-blue: #ddf3ff;

    /* Gradients */
    --fg-gradient-primary: linear-gradient(135deg, #0067a2 0%, #1a2949 100%);
    --fg-gradient-business: linear-gradient(135deg, #1a2949 0%, #000000 100%);
    --fg-gradient-energy: linear-gradient(135deg, #fa8526 0%, #faca2c 100%);
    --fg-gradient-community: linear-gradient(135deg, #ddf3ff 0%, #00c8b7 100%);
}
```

## Typography

**Font Family:**
```css
font-family: 'Century Gothic', 'Futura', 'AppleGothic', sans-serif;
```

**Sizes:**
- H1: 48-64px (Bold)
- H2: 36-42px (Bold)
- H3: 28-32px (Semibold)
- Body: 16-18px (Regular)
- CTA: 20-24px (Bold)

## Social Media Sizes

- Instagram Post: 1080x1080px
- Instagram Story: 1080x1920px
- Facebook Post: 1200x630px
- Email Header: 600x200px
- Landing Hero: 1440x600px

## Language Guidelines

### ✅ Always Use
- Community member
- Support you deserve
- Resources, opportunities
- Former foster youth
- Youth with lived experience
- Empower, connect, thrive

### ❌ Never Use
- Beneficiary, client
- At-risk, vulnerable
- Charity, handout
- Aged out
- Fix, save, rescue
- Help the less fortunate

## Power Words
Belonging • Community • Transform • Navigate • Thrive • Connect • Empower • Celebrate • Deserve • Lifelong • Platform • Peer

## DGW Canva Commands

```bash
# Render graphic
pnpm render --html ./design.html --format both

# With upload
pnpm render --html ./design.html --upload --campaign "name"

# List formats
pnpm formats
```

## HTML Template Starter

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="brand" content="foster-greatness">
    <meta name="format" content="instagram-post">
    <title>Foster Greatness - [Title]</title>
    <style>
        :root {
            --fg-navy: #1a2949;
            --fg-teal: #0067a2;
            --fg-gradient-primary: linear-gradient(135deg, #0067a2 0%, #1a2949 100%);
        }
        body {
            font-family: 'Century Gothic', sans-serif;
            color: var(--fg-navy);
            margin: 0;
            padding: 0;
        }
    </style>
</head>
<body>
    <!-- Your content here -->
</body>
</html>
```

## Common Components

### CTA Button
```html
<a href="#" style="
    display: inline-block;
    background: #0067a2;
    color: white;
    padding: 16px 32px;
    border-radius: 8px;
    font-size: 20px;
    font-weight: bold;
    text-decoration: none;
">Join Our Community</a>
```

### Stat Card
```html
<div style="text-align: center; padding: 32px;">
    <div style="font-size: 64px; font-weight: bold; color: #fa8526;">1,100+</div>
    <div style="font-size: 24px; color: #1a2949;">Community Members</div>
</div>
```

### Quote Block
```html
<blockquote style="
    font-size: 24px;
    font-style: italic;
    color: #1a2949;
    border-left: 4px solid #0067a2;
    padding-left: 24px;
    margin: 32px 0;
">"This community gave me something I never had before—a place to belong."
<footer style="font-size: 16px; font-style: normal; margin-top: 16px;">
    — Jordan, Foster Greatness Member
</footer>
</blockquote>
```

## Accessibility Checklist

- [ ] Text contrast ≥ 4.5:1
- [ ] Font size ≥ 16px for body
- [ ] Touch targets ≥ 44x44px
- [ ] Alt text on images
- [ ] No essential info in color only

## Quality Checklist

- [ ] Uses Century Gothic
- [ ] Brand colors from palette
- [ ] No charity/deficit language
- [ ] Empowering imagery
- [ ] Clear CTA
- [ ] Mobile-friendly sizes
- [ ] File size < 500KB

---

## Component Library

**Need ready-to-use components?** See `COMPONENTS.md` for:
- 10+ pre-built components (Buttons, Cards, Badges, Alerts, etc.)
- Complete HTML/CSS code snippets
- Modern UI-inspired designs
- Foster Greatness branded
- Copy-paste ready for DGW Canva

**Example graphics:** Check `/examples/component-library/` for:
- `stat-card-instagram.html` - Impact statistic graphic
- `event-card-instagram.html` - Event announcement
- `quote-instagram-story.html` - Member testimonial

---

**Need the full brand system?** See SKILL.md in this folder.
