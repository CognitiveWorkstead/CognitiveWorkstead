# Scope and completion

- Implement Greg's requested outcome and the supporting work necessary to make it complete. Propose unrelated features, new product behavior and optional improvements separately; wait for agreement before implementing them.
- Treat shared navigation and company-wide branding as site-wide work, including nested product, help, setup and terms pages. A homepage-only change is insufficient unless Greg explicitly limits the request to the homepage.
- Maintain one company menu from `_includes/company-navigation.html`, emitted into all content pages with `python3 scripts/sync-navigation.py`. Run `python3 scripts/sync-navigation.py --check` before release. Keep links available without JavaScript.
- Keep Cognitive Workstead home, RIG and COL-B reachable through the same company navigation on every content page. RIG's product navigation belongs beneath it. Preserve the retired `/ask-colb/` redirect.
- Verify desktop and mobile navigation, nested-page links, and the return path to company home. Review the changed-file list against the requested scope before declaring completion.
- Preserve page content, existing routes, accounts, application behavior, payments and checkout links when repairing navigation. Do not replace the live RIG application or COL-B delivery service as part of a company-site edit.
- Report exactly what was changed and verified, along with any unverified portion. Do not describe a single-page check as site-wide verification.
