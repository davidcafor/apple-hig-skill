#!/usr/bin/env python3
"""Validate package links, source provenance, and evaluation-case integrity."""
import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def validate(root):
    errors = []
    skill = root / 'apple-hig-skill'
    required = ['SKILL.md', 'LICENSE', 'NOTICE.md', 'agents/openai.yaml', 'references/sources.json']
    for name in required:
        if not (skill / name).is_file():
            errors.append(f'Missing package file: {name}')
    if errors:
        return errors
    registry = json.loads((skill / 'references/sources.json').read_text())
    source_urls = set()
    source_ids = set()
    for item in registry:
        if item['id'] in source_ids:
            errors.append(f"Duplicate source ID: {item['id']}")
        source_ids.add(item['id'])
        url = item['url'].rstrip('/')
        source_urls.add(url)
        if urlsplit(url).netloc != 'developer.apple.com':
            errors.append(f'Non-Apple source: {url}')
        if date.fromisoformat(item['reviewed']) > date.today():
            errors.append(f'Future review date: {url}')
        if not item['review_scope'].strip():
            errors.append(f'Missing review scope: {url}')
    for file in root.rglob('*.md'):
        content = re.sub(r'```.*?```', '', file.read_text(), flags=re.S)
        for link in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', content):
            url = urlsplit(link)
            if url.scheme:
                if file.is_relative_to(skill / 'references') and '/design/human-interface-guidelines/' in link:
                    if link.split('#')[0].rstrip('/') not in source_urls:
                        errors.append(f'{file.relative_to(root)}: unregistered HIG source {link}')
                continue
            target = (file.parent / unquote(url.path)).resolve() if url.path else file
            if not target.exists():
                errors.append(f'{file.relative_to(root)}: broken link {link}')
            elif url.fragment and target.suffix == '.md':
                headings = re.findall(r'^#{1,6}\s+(.+)$', target.read_text(), flags=re.M)
                slugs = {re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-') for heading in headings}
                if unquote(url.fragment) not in slugs:
                    errors.append(f'{file.relative_to(root)}: unknown heading {link}')
    cases = json.loads((root / 'evals/cases.json').read_text())
    ids = set()
    for case in cases:
        if case['id'] in ids:
            errors.append(f"Duplicate evaluation ID: {case['id']}")
        ids.add(case['id'])
        for field in ['platform', 'prompt', 'expected', 'forbidden']:
            if not case.get(field):
                errors.append(f"Case {case['id']} has no {field}")
    return errors

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        errors = validate(args.root.resolve())
    except (ValueError, KeyError, OSError) as exc:
        errors = [str(exc)]
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        sys.exit(1)
    print('PASS: package files, Markdown links/headings, HIG source registry, and evaluation schema.')
    print('Structural validation only; not behavioral or device validation.')
