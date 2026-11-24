# Maintaining the profile

GitHub displays the repository’s root README on the account profile. The portfolio contains the interactive architecture notes. Link to its stable [work section](https://junrillg.pages.dev/#work) when the case order changes. Keep client and product names out of case descriptions and illustrations.

## Profile banner

The banner shows a conceptual system diagram. Its background is charcoal (`#0a0a0a`), with warm white text (`#eeece8`), violet surfaces (`#5b5fe0`) and a lighter violet accent (`#a9abff`). GitHub serves the GIF by default. Readers who prefer reduced motion get the still image through the README’s `picture` element.

Generate both files from the repository root with Python 3 and Pillow installed:

```sh
python3 tools/render_architecture.py
```

The renderer writes to `assets/`. Its self-check verifies the 1200 × 440 frame, 80 frames, 70 ms frame timing, looping, and file size. Use `--help` for the optional font and output paths. When checking the published README, inspect the wide and narrow layouts, the reduced-motion source, and the destination of the linked banner.

## Repository sharing image

The editable [portrait card](../assets/social-preview.svg) and its [1280 × 640 PNG](../assets/social-preview.png) are the artwork for sharing a repository link. The PNG is ready for the repository’s social preview setting. GitHub documents the [upload step](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).
