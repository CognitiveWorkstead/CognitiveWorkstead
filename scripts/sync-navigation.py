"""Maintain static, JS-independent company navigation on every public content page."""
from pathlib import Path
import argparse
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- CW navigation:'
BLOCK = re.compile(r'<!-- CW navigation:[\s\S]*?<!-- /CW navigation -->\s*')
ASSET = re.compile(r'\n?<(?:link|script)\b[^>]*(?:href|src)="/assets/company-navigation\.(?:css|js)[^"]*"[^>]*>(?:</script>)?\n?')

def content_pages():
    for page in sorted(ROOT.rglob('*.html')):
        if any(part.startswith(('.', '_')) for part in page.relative_to(ROOT).parts):
            continue
        text = page.read_text(encoding='utf-8')
        if not re.search(r'<meta\b[^>]*http-equiv=[\"\']refresh[\"\']', text, re.I):
            yield page, text

def page_url(page):
    path = '/' + page.relative_to(ROOT).as_posix()
    return path[:-10] if path.endswith('index.html') else path

def expected(page, text):
    text = BLOCK.sub('', text)
    text = ASSET.sub('', text)
    old = re.search(r'<header\b[\s\S]*?</header>', text)
    product = ''
    if old:
        if 'id="product-nav"' in old.group():
            product = re.sub(r'<div class="company-bar">[\s\S]*?</div></div>', '', old.group(), count=1)
            product = product.replace('>Menu <span aria-hidden="true">☰</span>', '>RIG menu <span aria-hidden="true">☰</span>')
        text = text[:old.start()] + text[old.end():]
    template = (ROOT/'_includes/company-navigation.html').read_text(encoding='utf-8')
    url = page_url(page)
    section = '/' + url.strip('/').split('/')[0] + '/' if url != '/' else '/'
    if section not in ('/', '/rig/', '/col-b/', '/services/', '/solutions/', '/colby-systems/', '/applied-work/', '/assessment/', '/workshops/', '/contact/'):
        raise ValueError(f'Unmapped section: {page}')
    current = 'page' if section == url else 'location'
    template = template.replace(f'href="{section}"', f'href="{section}" aria-current="{current}"')
    # Home appears twice (brand and menu): keep aria-current on the menu only.
    template = re.sub(r'(<a class="cw-brand" href="/") aria-current="[^"]+"', r'\1', template)
    text = re.sub(r'(<body\b[^>]*>)\s*', lambda m: m.group(1)+'\n'+template+product+'\n', text, count=1)
    css_hash = hashlib.sha256((ROOT/'assets/company-navigation.css').read_bytes()).hexdigest()[:10]
    js_hash = hashlib.sha256((ROOT/'assets/company-navigation.js').read_bytes()).hexdigest()[:10]
    assets = f'\n<link rel="stylesheet" href="/assets/company-navigation.css?v={css_hash}">\n<script src="/assets/company-navigation.js?v={js_hash}" defer></script>\n'
    return text.replace('</head>', assets+'</head>', 1)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    template = (ROOT/'_includes/company-navigation.html').read_text(encoding='utf-8')
    nav = re.search(r'<nav\b[\s\S]*?</nav>', template).group()
    targets = re.findall(r'<a href="([^"]+)"', nav)
    if not {'/', '/rig/', '/col-b/'} <= set(targets) or len(targets) != len(set(targets)):
        raise SystemExit('Company navigation must include unique links to Home, RIG and COL-B.')
    for target in targets:
        if not target.startswith('/') or not (ROOT/target.lstrip('/')/'index.html').is_file():
            raise SystemExit(f'Company navigation destination does not exist: {target}')
    count = 0
    stale = []
    for page, text in content_pages():
        result = expected(page, text)
        if result.count('data-cw-navigation') != 1 or result.count('id="cw-primary-nav"') != 1:
            raise SystemExit(f'Company navigation missing or repeated: {page}')
        count += 1
        if result != text:
            stale.append(page.relative_to(ROOT).as_posix())
            if not args.check:
                page.write_text(result, encoding='utf-8', newline='\n')
    if args.check and stale:
        raise SystemExit('Navigation differs from its shared template: '+', '.join(stale))
    print(f'{count} content pages: shared navigation '+('verified' if args.check else 'synchronized'))

if __name__ == '__main__':
    main()
