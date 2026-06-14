---
name: frontend-design
description: Designs and generates modern, production-ready UI for Spendly, a personal expense tracker built on Flask + Jinja2 + vanilla CSS. Produces clean fintech-style pages and components - cards, forms, tables, dashboards, modals - with consistent spacing, soft shadows, rounded corners, and Lucide icons. Use this skill whenever the user asks to design, build, create, redesign, improve, or style any Spendly page, screen, section, or component - including phrasings like "design the X page", "create UI for X", "build a component for X", "make the X look better", "redesign X", or any request about Spendly's frontend, layout, CSS, or visual polish - even when Spendly isn't named explicitly if the conversation context is clearly about it.
disable-model-invocation: true
---

# Spendly UI Designer

You are designing frontend UI for **Spendly**, a personal expense tracker. Spendly is a Flask app with server-rendered Jinja2 templates, vanilla CSS, and a sprinkle of vanilla JS. The goal of this skill is to help you generate UI that feels like it belongs in a polished, modern fintech product - not generic bootstrap-era output, and not React/Tailwind output that doesn't match the stack.

## What Spendly's stack looks like

- **Backend:** Flask (`app.py`), SQLite (`database/`)
- **Templates:** Jinja2 in `templates/` (e.g. `base.html`, `landing.html`, `login.html`, `register.html`)
- **Styles:** vanilla CSS in `static/css/style.css` - uses CSS custom properties (variables) extensively
- **Scripts:** small amounts of vanilla JS in `static/js/main.js` for interactions
- **Icons:** Can use Lucide via CDN, but current implementation uses text-based avatars

Generate output that fits this stack. Do not introduce React, Vue, Tailwind, shadcn, Bootstrap, or styled-components unless the user explicitly asks for a migration.

## Before you design: check what already exists

If the user's project files are available (e.g. they've shared the repo, uploaded files, or you're inside the codebase), open `base.html`, the main CSS file (`static/css/style.css`), and one or two existing templates before generating anything new. The goal is *consistency* - Spendly should feel like one coherent product, not a collage.

Specifically, look for and reuse:

- **Color tokens** (CSS custom properties from `:root` in `static/css/style.css`):
  - `--ink: #0f0f0f` (primary text)
  - `--ink-soft: #2d2d2d`
  - `--ink-muted: #6b6b6b`
  - `--ink-faint: #a0a0a0`
  - `--paper: #f7f6f3` (background)
  - `--paper-warm: #f0ede6`
  - `--paper-card: #ffffff` (card/panel background)
  - `--accent: #1a472a` (primary accent)
  - `--accent-light: #e8f0eb`
  - `--accent-2: #c17f24` (secondary accent)
  - `--accent-2-light: #fdf3e3`
  - `--danger: #c0392b` (error/danger)
  - `--danger-light: #fdecea`
  - `--border: #e4e1da` (border color)
  - `--border-soft: #eeebe4`
- **Typography variables**:
  - `--font-display: 'DM Serif Display', Georgia, serif` (for headings/titles)
  - `--font-body: 'DM Sans', system-ui, sans-serif` (for body text)
- **Layout variables**:
  - `--max-width: 1200px` (container maximum width)
  - `--auth-width: 440px` (authentication form width)
- **Border radius variables**:
  - `--radius-sm: 6px`
  - `--radius-md: 12px`
  - `--radius-lg: 20px`
- **Existing component classes** from the CSS (review `static/css/style.css` for patterns)
- **The base layout** - navbar with brand and links, main content area, footer

If you can't see the existing files and the request is non-trivial, ask the user to share a screenshot or paste a relevant template before you generate. One screenshot of the existing dashboard saves three rounds of revision.

## The Spendly design language

When you have no existing reference to follow, default to this. It's a clean, fintech-leaning aesthetic that matches the existing CSS variables and design patterns in the project.

**Palette (from existing CSS variables):**
- Background: `--paper: #f7f6f3` (very light neutral)
- Surface (cards): `--paper-card: #ffffff` (white) with border `--border: #e4e1da`
- Text: `--ink: #0f0f0f` (near-black for primary), `--ink-muted: #6b6b6b` (muted gray for secondary)
- Primary accent: `--accent: #1a472a` (a confident green color)
- Secondary accent: `--accent-2: #c17f24` (amber/orange for highlights)
- Semantic: `--danger: #c0392b` (red for expense/negative), use `--accent-2` for income/positive if needed
- Additional: `--paper-warm: #f0ede6`, `--accent-light: #e8f0eb`, `--accent-2-light: #fdf3e3`, `--danger-light: #fdecea`, `--border-soft: #eeebe4`

**Spacing:** Based on the radius variables and existing patterns. Use multiples that align with the `--radius-sm: 6px`, `--radius-md: 12px`, `--radius-lg: 20px` scale. Common spacing values: 4px, 6px, 8px, 12px, 16px, 20px, 24px.

**Radius:** Use the existing CSS variables:
- `--radius-sm: 6px` for inputs and small elements
- `--radius-md: 12px` for cards and modals
- `--radius-lg: 20px` for larger rounded elements

**Shadows:** subtle only, following the existing project patterns. Look at how shadows are used in the existing CSS (if any) and maintain consistency.

**Typography:** 
- Fonts: `--font-display: 'DM Serif Display', Georgia, serif` for headings/titles
- Fonts: `--font-body: 'DM Sans', system-ui, sans-serif` for body text
- Type scale: Use appropriate heading sizes (h1-h6) with consistent sizing
- Font weights: 400 for body, 500/600 for headings as needed
- Numbers (amounts): Consider using `font-variant-numeric: tabular-nums` for better alignment

**Layout patterns:**
- Card-based composition - group related info in surfaces, don't sprawl
- Generous whitespace - tight layouts read as cluttered in finance apps
- Left-aligned content with clear hierarchy; centered layouts only for empty states and auth states
- Tables: consider zebra stripes with `--border-soft`, always have row hover effects, right-align numeric columns
- Forms: label above input, helper text below, error state using `--danger` color with icon

## Icons: Lucide

The project can use Lucide icons. If implementing:

Load Lucide once in `base.html`:

```html
<script src="https://unpkg.com/lucide@latest"></script>
```

And call `lucide.createIcons()` after the DOM is ready (and after any dynamic DOM insert). In templates, use:

```html
<i data-lucide="wallet"></i>
<i data-lucide="trending-up"></i>
<i data-lucide="plus"></i>
```

Size icons via CSS with `width` and `height` on the `<svg>` (after Lucide replaces the `<i>`) or wrap in a span with the size you want. Prefer 16px for inline with text, 20px for buttons, 24px for section headers.

Pick icons that carry meaning. A few Spendly-appropriate defaults:
- Expense/spend: `arrow-down-right`, `shopping-bag`, `credit-card`
- Income: `arrow-up-right`, `wallet`, `trending-up`
- Budget: `target`, `pie-chart`
- Category: `tag`, `folder`
- Add/new: `plus`, `plus-circle`
- Settings: `settings`, `sliders-horizontal`
- Date/time: `calendar`, `clock`
- Search: `search`, Filter: `filter`

Don't sprinkle icons everywhere. One icon per button, one per section heading, one per table row action - that's usually the right density.

## Output structure

When fulfilling a design request, structure your response like this:

### 1. Short UI plan (2-5 bullets)
Name the key sections of the page/component and any notable UX decisions. Keep it tight - this is orientation, not a spec document. Example: "Dashboard has 4 summary cards on top (balance, income, expenses, savings), a 'recent transactions' table, and a category breakdown donut. Summary cards show trend vs last month as a small delta pill."

### 2. The code
- **Template file(s)** - full Jinja2 with `{% extends "base.html" %}` and a `{% block content %}` unless building `base.html` itself. Use Jinja control flow (`{% for %}`, `{% if %}`) with sensible placeholder variable names the user can wire to their Flask route.
- **CSS** - either a new file (e.g. `static/css/dashboard.css`) or additions to an existing stylesheet. Scope with a page/component class prefix (`.dashboard-...`, `.tx-table-...`) so styles don't leak.
- **JS** (only if needed) - vanilla, no frameworks. Small and readable.

Put each file in its own fenced code block with a clear header comment or path annotation like `{# templates/dashboard.html #}` or `/* static/css/dashboard.css */`.

### 3. Integration note (1-3 lines)
How to wire it up - which Flask route renders it, what variables the template expects, any new dependency (almost always none). If the user needs to add a link in the sidebar or a route in `app.py`, call that out.

## What to avoid

- **Generic/dated looks** - no `<h1>Welcome to My App</h1>` with default browser styles, no sharp-cornered bordered boxes, no 2012-era bootstrap cards.
- **Code dumps without structure** - always separate template, CSS, and JS into labeled blocks.
- **Over-styling** - if something can be solid color instead of a gradient, use solid. If it can be a border instead of a shadow, use border. Restraint reads as quality.
- **Inconsistent spacing** - if you used 16px for card padding in one place, use 16px in the next place too. No 14px here, 18px there.
- **Random color accents** - one primary accent, semantic colors for meaning, everything else neutral.
- **Clever-but-unclear UX** - a clearly-labeled button beats a mystery icon. In finance, trust matters more than cuteness.
- **Mobile afterthought** - use CSS that works at narrow widths. At minimum, stack cards vertically and make tables horizontally scrollable below ~768px.

## Handling ambiguity

If the user asks for something under-specified ("design the reports page"), make reasonable assumptions and *state them up front* in the UI plan - one line each, no long preamble. For example: "Assuming reports page shows: monthly spend trend, top categories, and a downloadable CSV. Let me know if you want different widgets."

Don't pepper the user with clarifying questions for things you can reasonably decide. Do ask when the answer genuinely changes the output - e.g. "Is this a standalone page or a modal on top of the dashboard?"

## A worked example of the right vibe

**Request:** "Design the add expense form"

**UI plan:**
- Modal dialog (not a full page) - users add expenses inline from the dashboard
- Fields: amount (large, prominent), category (pill selector), date (defaults to today), note (optional)
- Primary action "Add expense" anchors bottom-right; cancel is a subtle text button
- Amount field gets a currency symbol prefix and tabular-nums

**Template:** `templates/partials/add_expense_modal.html` - extends nothing, included via `{% include %}`. Uses a `.modal` overlay pattern already in `base.css` if present.

**CSS:** additions to `static/css/components.css` for the new pill selector; reuses existing `.input`, `.btn-primary`, `.modal` classes.

**JS:** small module-free script to open/close the modal and reset the form on close.

That's the shape - concrete, consistent with the stack, visually restrained, and immediately usable.




