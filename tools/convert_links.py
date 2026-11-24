"""Converts Obsidian wikilinks to GitHub Pages & GitHub compatible standard Markdown links."""
import os
import glob
import re
import urllib.parse
from pathlib import Path

def convert_wikilinks(text: str) -> str:
    # Split text into mermaid blocks and non-mermaid blocks to handle them safely
    parts = re.split(r'(```mermaid[\s\S]*?```)', text)
    
    for i in range(len(parts)):
        if parts[i].startswith('```mermaid'):
            # Inside mermaid: strip [[ and ]] to keep node labels valid
            parts[i] = re.sub(
                r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]',
                lambda m: m.group(2) if m.group(2) else m.group(1),
                parts[i]
            )
        else:
            # Outside mermaid: convert [[target|alias]] or [[target]] to [alias](target.md)
            def replace_link(match):
                full_content = match.group(1).strip()
                if '|' in full_content:
                    target, alias = full_content.split('|', 1)
                    target = target.strip()
                    alias = alias.strip()
                else:
                    target = full_content
                    alias = full_content
                
                # Check for section anchor
                anchor = ''
                if '#' in target:
                    target, anchor = target.split('#', 1)
                    anchor = '#' + anchor.strip().lower().replace(' ', '-')
                
                if target.endswith('.md'):
                    url_target = target
                elif target:
                    url_target = target + '.md'
                else:
                    url_target = ''
                
                # URL-encode spaces in each path segment
                url_encoded = '/'.join(urllib.parse.quote(part) for part in url_target.split('/')) + anchor
                return f'[{alias}]({url_encoded})'
            
            parts[i] = re.sub(r'\[\[([^\]]+)\]\]', replace_link, parts[i])
            
    return ''.join(parts)

def process_vault_files():
    vault_dirs = glob.glob('vaults/*') + ['vp-vnp-vault']
    total_files = 0
    total_converted = 0

    for vdir in vault_dirs:
        for md_path in Path(vdir).rglob('*.md'):
            total_files += 1
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            converted = convert_wikilinks(content)
            if converted != content:
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(converted)
                total_converted += 1

    print(f"Scanned {total_files} vault notes. Converted wikilinks in {total_converted} files.")

if __name__ == '__main__':
    process_vault_files()
