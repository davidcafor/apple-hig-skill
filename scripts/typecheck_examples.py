#!/usr/bin/env python3
"""Typecheck original snippets with installed Apple SDKs; never launch devices."""
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / 'apple-hig-skill/examples'
COMMON = ['AccessibleAction.swift', 'AdaptiveActions.swift', 'ReducedMotionFeedback.swift']
TARGETS = [
    ('macosx', 'arm64-apple-macos13.0', COMMON + ['DraftEditor.swift', 'MacSettings.swift']),
    ('iphonesimulator', 'arm64-apple-ios16.0-simulator', COMMON + ['DraftEditor.swift']),
    ('watchsimulator', 'arm64-apple-watchos9.0-simulator', COMMON + ['WatchQuickAction.swift']),
    ('appletvsimulator', 'arm64-apple-tvos16.0-simulator', COMMON + ['TelevisionFocus.swift']),
    ('xrsimulator', 'arm64-apple-xros1.0-simulator', COMMON + ['DraftEditor.swift']),
]

def main():
    # Caller can select Xcode using DEVELOPER_DIR. Do not alter global selection.
    subprocess.run(['xcrun', 'swiftc', '--version'], check=True)
    with tempfile.TemporaryDirectory(prefix='hig-module-cache-') as cache:
        for sdk, target, files in TARGETS:
            path = subprocess.check_output(['xcrun', '--sdk', sdk, '--show-sdk-path'], text=True).strip()
            command = ['xcrun', '--sdk', sdk, 'swiftc', '-typecheck', '-warnings-as-errors',
                       '-sdk', path, '-target', target, '-module-cache-path', cache]
            subprocess.run(command + [str(EXAMPLES / name) for name in files], check=True)
            print(f'PASS {target}: {len(files)} examples', flush=True)
    print('Typechecking only; no runtime or device validation. iOS and iPadOS share the iOS SDK.')

if __name__ == '__main__':
    main()
