# game.spec
from PyInstaller.utils.hooks import collect_submodules
from pathlib import Path

block_cipher = None

# --- Safe data collection ---
datas = []
for folder in ['data', 'graphics']:
    for path in Path(folder).rglob('*'):
        if path.is_file():
            # ('data/some/file.png', 'data')
            datas.append((str(path), str(path.parent)))



# --- Optional: collect all py_tmx modules ---
hiddenimports = collect_submodules('py_tmx') + collect_submodules('pygame')

a = Analysis(
    ['code/main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PlatformerWorld',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # False if it's a GUI app and you don't want a terminal window
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='platformer_bundle',
    strip=False,
    upx=True,
    upx_exclude=[],
)

