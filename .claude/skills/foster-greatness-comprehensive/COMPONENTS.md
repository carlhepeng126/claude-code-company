# Foster Greatness Component Library
## HTML/CSS Components for DGW Canva

Modern UI-inspired components with Foster Greatness branding for static HTML graphics.

---

## Setup

### CSS Variables (Add to `<style>` tag)

```css
:root {
    /* Primary Colors */
    --fg-navy: #1a2949;
    --fg-teal: #0067a2;

    /* Accent Colors */
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

    /* Typography */
    --font-family: 'Century Gothic', 'Futura', 'AppleGothic', sans-serif;

    /* Spacing */
    --spacing-xs: 8px;
    --spacing-sm: 16px;
    --spacing-md: 24px;
    --spacing-lg: 32px;
    --spacing-xl: 48px;

    /* Border Radius */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 12px;
    --radius-xl: 16px;

    /* Shadows */
    --shadow-sm: 0 1px 2px rgba(26, 41, 73, 0.1);
    --shadow-md: 0 4px 8px rgba(26, 41, 73, 0.12);
    --shadow-lg: 0 8px 16px rgba(26, 41, 73, 0.15);
    --shadow-xl: 0 16px 32px rgba(26, 41, 73, 0.2);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: var(--font-family);
    color: var(--fg-navy);
}
```

---

## Components

### 1. Buttons

#### Primary Button
```html
<button class="btn btn-primary">
    Join Our Community
</button>

<style>
.btn {
    font-family: var(--font-family);
    font-weight: bold;
    padding: 16px 32px;
    border: none;
    border-radius: var(--radius-md);
    font-size: 18px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
    text-align: center;
}

.btn-primary {
    background: var(--fg-teal);
    color: white;
}

.btn-primary:hover {
    background: var(--fg-navy);
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}
</style>
```

#### Secondary Button
```html
<button class="btn btn-secondary">
    Learn More
</button>

<style>
.btn-secondary {
    background: transparent;
    color: var(--fg-teal);
    border: 2px solid var(--fg-teal);
}

.btn-secondary:hover {
    background: var(--fg-teal);
    color: white;
}
</style>
```

#### Gradient Button (Energy)
```html
<button class="btn btn-gradient">
    Get Started Now
</button>

<style>
.btn-gradient {
    background: var(--fg-gradient-energy);
    color: white;
    border: none;
}

.btn-gradient:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-xl);
}
</style>
```

---

### 2. Cards

#### Default Card
```html
<div class="card">
    <div class="card-header">
        <h3 class="card-title">Community Platform</h3>
        <p class="card-description">Your community in your pocket</p>
    </div>
    <div class="card-content">
        <p>Join 1,100+ foster youth and alumni in a community where you're seen, celebrated, and supported—24/7.</p>
    </div>
    <div class="card-footer">
        <button class="btn btn-primary">Connect Now</button>
    </div>
</div>

<style>
.card {
    background: white;
    border-radius: var(--radius-lg);
    padding: var(--spacing-lg);
    box-shadow: var(--shadow-md);
    transition: all 0.3s ease;
}

.card:hover {
    box-shadow: var(--shadow-xl);
    transform: translateY(-4px);
}

.card-header {
    margin-bottom: var(--spacing-md);
}

.card-title {
    font-size: 24px;
    font-weight: bold;
    color: var(--fg-navy);
    margin-bottom: var(--spacing-xs);
}

.card-description {
    font-size: 16px;
    color: var(--fg-teal);
    margin-bottom: 0;
}

.card-content {
    font-size: 16px;
    line-height: 1.6;
    color: var(--fg-navy);
    margin-bottom: var(--spacing-md);
}

.card-footer {
    display: flex;
    gap: var(--spacing-sm);
    align-items: center;
}
</style>
```

#### Gradient Card
```html
<div class="card card-gradient">
    <div class="card-header">
        <h3 class="card-title" style="color: white;">Transform Your Impact</h3>
        <p class="card-description" style="color: rgba(255,255,255,0.9);">Business-powered sustainability</p>
    </div>
    <div class="card-content" style="color: white;">
        <p>Every promotional product order directly funds scholarships, crisis support, and career development.</p>
    </div>
</div>

<style>
.card-gradient {
    background: var(--fg-gradient-primary);
    color: white;
}
</style>
```

#### Stat Card
```html
<div class="card card-stat">
    <div class="stat-number">1,100+</div>
    <div class="stat-label">Community Members</div>
    <div class="stat-description">Finding lifelong belonging</div>
</div>

<style>
.card-stat {
    text-align: center;
    padding: var(--spacing-xl);
}

.stat-number {
    font-size: 64px;
    font-weight: bold;
    color: var(--fg-orange);
    line-height: 1;
    margin-bottom: var(--spacing-sm);
}

.stat-label {
    font-size: 24px;
    font-weight: bold;
    color: var(--fg-navy);
    margin-bottom: var(--spacing-xs);
}

.stat-description {
    font-size: 18px;
    color: var(--fg-teal);
}
</style>
```

---

### 3. Badges

```html
<span class="badge badge-primary">New</span>
<span class="badge badge-success">Active</span>
<span class="badge badge-warning">Urgent</span>

<style>
.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: var(--radius-sm);
    font-size: 14px;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.badge-primary {
    background: var(--fg-teal);
    color: white;
}

.badge-success {
    background: var(--fg-teal-accent);
    color: white;
}

.badge-warning {
    background: var(--fg-orange);
    color: white;
}
</style>
```

---

### 4. Alert / Banner

```html
<div class="alert alert-info">
    <div class="alert-icon">ℹ️</div>
    <div class="alert-content">
        <h4 class="alert-title">Event Reminder</h4>
        <p class="alert-description">Join us this Saturday at 3:00 PM PT for our community gathering!</p>
    </div>
</div>

<style>
.alert {
    display: flex;
    gap: var(--spacing-sm);
    padding: var(--spacing-md);
    border-radius: var(--radius-md);
    border-left: 4px solid;
}

.alert-info {
    background: var(--fg-light-blue);
    border-color: var(--fg-teal);
}

.alert-icon {
    font-size: 24px;
    flex-shrink: 0;
}

.alert-content {
    flex: 1;
}

.alert-title {
    font-size: 18px;
    font-weight: bold;
    color: var(--fg-navy);
    margin-bottom: var(--spacing-xs);
}

.alert-description {
    font-size: 16px;
    color: var(--fg-navy);
    margin: 0;
}
</style>
```

---

### 5. Quote / Testimonial

```html
<div class="quote-card">
    <div class="quote-mark">"</div>
    <blockquote class="quote-text">
        This community gave me something I never had before—a place to belong.
    </blockquote>
    <div class="quote-author">
        <div class="author-name">Jordan</div>
        <div class="author-role">Foster Greatness Member</div>
    </div>
</div>

<style>
.quote-card {
    background: white;
    padding: var(--spacing-xl);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    position: relative;
}

.quote-mark {
    font-size: 120px;
    color: var(--fg-light-blue);
    position: absolute;
    top: -20px;
    left: 20px;
    line-height: 1;
    font-family: Georgia, serif;
}

.quote-text {
    font-size: 24px;
    font-style: italic;
    color: var(--fg-navy);
    line-height: 1.5;
    margin: 40px 0 var(--spacing-lg) 0;
    position: relative;
    z-index: 1;
}

.quote-author {
    padding-left: var(--spacing-md);
    border-left: 3px solid var(--fg-teal);
}

.author-name {
    font-size: 18px;
    font-weight: bold;
    color: var(--fg-navy);
}

.author-role {
    font-size: 14px;
    color: var(--fg-teal);
}
</style>
```

---

### 6. Hero Section

```html
<div class="hero">
    <div class="hero-content">
        <h1 class="hero-title">Age Into But Never Age Out</h1>
        <p class="hero-subtitle">Lifelong community for current and former foster youth nationwide</p>
        <div class="hero-actions">
            <button class="btn btn-primary btn-lg">Join Our Community</button>
            <button class="btn btn-secondary btn-lg">Learn More</button>
        </div>
    </div>
</div>

<style>
.hero {
    background: var(--fg-gradient-primary);
    padding: 80px 40px;
    text-align: center;
    border-radius: var(--radius-xl);
}

.hero-content {
    max-width: 800px;
    margin: 0 auto;
}

.hero-title {
    font-size: 56px;
    font-weight: bold;
    color: white;
    line-height: 1.2;
    margin-bottom: var(--spacing-md);
}

.hero-subtitle {
    font-size: 24px;
    color: rgba(255, 255, 255, 0.9);
    line-height: 1.5;
    margin-bottom: var(--spacing-xl);
}

.hero-actions {
    display: flex;
    gap: var(--spacing-md);
    justify-content: center;
    flex-wrap: wrap;
}

.btn-lg {
    padding: 20px 40px;
    font-size: 20px;
}
</style>
```

---

### 7. Impact Stats Grid

```html
<div class="stats-grid">
    <div class="stat-item">
        <div class="stat-number">1,100+</div>
        <div class="stat-label">Members</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">220</div>
        <div class="stat-label">Resources Delivered</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">$39K+</div>
        <div class="stat-label">Tax Credits Returned</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">77</div>
        <div class="stat-label">Wishes Granted</div>
    </div>
</div>

<style>
.stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: var(--spacing-lg);
    padding: var(--spacing-xl);
}

.stat-item {
    text-align: center;
    padding: var(--spacing-lg);
    background: white;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-sm);
    transition: all 0.3s ease;
}

.stat-item:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
}

.stat-item .stat-number {
    font-size: 48px;
    font-weight: bold;
    color: var(--fg-teal);
    line-height: 1;
    margin-bottom: var(--spacing-sm);
}

.stat-item .stat-label {
    font-size: 16px;
    color: var(--fg-navy);
    font-weight: 600;
}
</style>
```

---

### 8. Feature List

```html
<div class="feature-list">
    <div class="feature-item">
        <div class="feature-icon">🏠</div>
        <div class="feature-content">
            <h4 class="feature-title">Resource Navigation</h4>
            <p class="feature-description">Access 600,000+ scholarships, housing options, and support programs</p>
        </div>
    </div>
    <div class="feature-item">
        <div class="feature-icon">💼</div>
        <div class="feature-content">
            <h4 class="feature-title">Career Development</h4>
            <p class="feature-description">Direct pathway to meaningful employment with ongoing support</p>
        </div>
    </div>
    <div class="feature-item">
        <div class="feature-icon">🤝</div>
        <div class="feature-content">
            <h4 class="feature-title">Community Events</h4>
            <p class="feature-description">Workshops, gatherings, and spaces where you're celebrated</p>
        </div>
    </div>
</div>

<style>
.feature-list {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-md);
}

.feature-item {
    display: flex;
    gap: var(--spacing-md);
    padding: var(--spacing-md);
    background: white;
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-sm);
    transition: all 0.3s ease;
}

.feature-item:hover {
    box-shadow: var(--shadow-md);
    transform: translateX(8px);
}

.feature-icon {
    font-size: 48px;
    flex-shrink: 0;
    width: 64px;
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--fg-light-blue);
    border-radius: var(--radius-md);
}

.feature-content {
    flex: 1;
}

.feature-title {
    font-size: 20px;
    font-weight: bold;
    color: var(--fg-navy);
    margin-bottom: var(--spacing-xs);
}

.feature-description {
    font-size: 16px;
    color: var(--fg-navy);
    line-height: 1.5;
    margin: 0;
}
</style>
```

---

### 9. Call-to-Action Banner

```html
<div class="cta-banner">
    <div class="cta-content">
        <h2 class="cta-title">Ready to Find Your Community?</h2>
        <p class="cta-text">Join 1,100+ members in a space where you truly belong</p>
    </div>
    <div class="cta-action">
        <button class="btn btn-primary btn-lg">Sign Up Free</button>
    </div>
</div>

<style>
.cta-banner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: var(--spacing-lg);
    padding: var(--spacing-xl);
    background: var(--fg-gradient-primary);
    border-radius: var(--radius-xl);
}

.cta-content {
    flex: 1;
}

.cta-title {
    font-size: 32px;
    font-weight: bold;
    color: white;
    margin-bottom: var(--spacing-sm);
}

.cta-text {
    font-size: 18px;
    color: rgba(255, 255, 255, 0.9);
    margin: 0;
}

.cta-action {
    flex-shrink: 0;
}
</style>
```

---

### 10. Tag Group

```html
<div class="tag-group">
    <span class="tag">Community</span>
    <span class="tag">Belonging</span>
    <span class="tag">Empowerment</span>
    <span class="tag">Support</span>
    <span class="tag">Lifelong</span>
</div>

<style>
.tag-group {
    display: flex;
    gap: var(--spacing-xs);
    flex-wrap: wrap;
}

.tag {
    display: inline-block;
    padding: 8px 16px;
    background: var(--fg-light-blue);
    color: var(--fg-teal);
    border-radius: var(--radius-lg);
    font-size: 14px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.tag:hover {
    background: var(--fg-teal);
    color: white;
    transform: scale(1.05);
}
</style>
```

---

## Usage Example

### Complete Instagram Post Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="brand" content="foster-greatness">
    <meta name="format" content="instagram-post">
    <title>Foster Greatness - Community Impact</title>
    <style>
        :root {
            --fg-navy: #1a2949;
            --fg-teal: #0067a2;
            --fg-orange: #fa8526;
            --fg-light-blue: #ddf3ff;
            --fg-gradient-primary: linear-gradient(135deg, #0067a2 0%, #1a2949 100%);
            --font-family: 'Century Gothic', 'Futura', 'AppleGothic', sans-serif;
            --spacing-md: 24px;
            --spacing-lg: 32px;
            --radius-lg: 12px;
            --shadow-md: 0 4px 8px rgba(26, 41, 73, 0.12);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: var(--font-family);
            width: 1080px;
            height: 1080px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--fg-gradient-primary);
        }

        .container {
            width: 960px;
            padding: 60px;
            text-align: center;
        }

        .stat-number {
            font-size: 120px;
            font-weight: bold;
            color: white;
            line-height: 1;
            margin-bottom: 20px;
        }

        .stat-label {
            font-size: 48px;
            font-weight: bold;
            color: white;
            margin-bottom: 30px;
        }

        .stat-description {
            font-size: 32px;
            color: rgba(255, 255, 255, 0.9);
            line-height: 1.4;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="stat-number">1,100+</div>
        <div class="stat-label">Community Members</div>
        <div class="stat-description">Finding lifelong belonging across the nation</div>
    </div>
</body>
</html>
```

---

## Tips for DGW Canva

1. **Copy components** from this file into your HTML designs
2. **Adjust sizing** for your format (Instagram, Facebook, etc.)
3. **Use CSS variables** for consistent branding
4. **Test render** with `pnpm render --html ./design.html --format both`
5. **Mix and match** components to create unique layouts

---

**Component Library Version:** 1.0
**Last Updated:** October 2024
**For:** Foster Greatness + DGW Canva
