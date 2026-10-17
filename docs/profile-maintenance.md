# Profile design and maintenance

Updated 17 October 2026. Goal: a professional GitHub profile that matches [the portfolio](https://junrillg.pages.dev/), with the title **Senior Software Engineer** and focus **System Design & AI Integration**.

The profile uses the portfolio’s midnight `#090a1b`, lavender `#b9a3fb`, and light `#f6f5fd` palette. Its 3D architecture diagram is conceptual, not a product screenshot. Interactive Three.js stays on the portfolio because GitHub sanitizes scripts and styling in README content. The GIF supplies motion within those constraints; `<picture>` selects a still image for reduced-motion preferences.

Reference patterns reviewed: [Brittany Chiang](https://github.com/bchiang7), [Anurag Hazra](https://github.com/anuraghazra), and [Sindre Sorhus](https://github.com/sindresorhus). Adopt concise positioning, selected work evidence, a readable technology summary, and a clear portfolio link. Avoid badge walls, fragile external statistics, and unsupported project claims. Platform constraints: [GitHub’s rendering pipeline](https://github.com/github/markup), [profile README documentation](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme), and [GitHub Pages user sites](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

The role line uses the résumé’s Senior Software Engineer title; the separate focus line describes system design and AI integration. Career duration, cloud AI migration savings, deployment times, and platform scale come from the supplied résumé and published portfolio stories. The 25,000+ user figure is dated to 2020 and describes the platform. No former employer names, private contact details, original résumé, invented testimonials, or invented projects are published.

## Artwork

Requires Python 3 and Pillow. No network calls or Node tooling:

```sh
python3 tools/render_architecture.py --help
python3 tools/render_architecture.py
```

The default output is `assets/`; `--output DIRECTORY` changes it. `--font FILE` supplies a TrueType/OpenType font; otherwise the renderer checks installed Arial/DejaVu Sans and falls back to Pillow’s font. The script checks PNG dimensions, GIF dimensions, 80 frames, 70ms frame timing, infinite looping, periodic projection, and a 3 MiB GIF ceiling. Keep the PNG and GIF at 1200 × 440 and regenerate together.

Current correction verified locally on 17 October 2026: artwork reads “Senior Software Engineer” with “System Design · AI Integration.” `assets/senior-engineer-still.png`: 86,669 bytes; `assets/senior-engineer-motion.gif`: 907,436 bytes. Both remain 1200 × 440; all renderer self-checks pass (80 frames, 5.6-second loop). The still image was visually inspected for text fit and unchanged 3D composition. Live GitHub verification is pending publication.

The primary website remains `junrillg.pages.dev`. `junrillg.github.io` redirects to it, preventing duplicate portfolios. A personal custom domain can replace the primary address later; no domain purchase or DNS changes are required for this update.

## Publication history

Earlier publication on 17 October 2026: actual GitHub profile rendering verified on desktop (1440px) and mobile (390px). Artwork preserves its 1200:440 aspect ratio without a fixed HTML height. The reduced-motion preference selects the PNG; default motion selects the GIF. Earlier asset self-checks passed: 80 frames at 70ms, stable text, moving 3D scene. The portfolio link loaded the prior positioning, and the GitHub Pages entry point redirected there. This historical browser verification does not verify the current positioning correction.

The account sidebar bio remained unchanged because the available CLI token lacked `user` scope and the review browser was signed out. Current repository-description and live-publication verification are pending for the corrected positioning.
