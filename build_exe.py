"""
Build script to generate EXE file from Pulseforge Studio
Run: python build_exe.py
"""

import os
import subprocess
import shutil
import sys

def build_exe():
    """Build the EXE file using PyInstaller"""
    
    print("=" * 60)
    print("Pulseforge Studio - EXE Builder")
    print("=" * 60)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("✓ PyInstaller found")
    except ImportError:
        print("✗ PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyInstaller"])
    
    # Clean old build files
    print("\nCleaning old build files...")
    for folder in ['build', 'dist', '__pycache__']:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"  Removed {folder}/")
    
    for file in ['main.spec']:
        if os.path.exists(file):
            os.remove(file)
            print(f"  Removed {file}")
    
    # Build the EXE
    print("\nBuilding EXE file...")
    print("-" * 60)
    
    cmd = [
        'pyinstaller',
        '--onefile',                    # Single EXE file
        '--windowed',                   # No console window
        '--name=PulseforgeStudio',      # Application name
        '--icon=NONE',                  # No icon (you can add one later)
        '--add-data=.:.',               # Include data files
        'main.py'
    ]
    
    try:
        subprocess.check_call(cmd)
        print("-" * 60)
        print("\n✓ Build successful!")
        print("\nEXE file location:")
        exe_path = os.path.abspath(os.path.join('dist', 'PulseforgeStudio.exe'))
        print(f"  {exe_path}")
        print("\nYou can now:")
        print("  1. Run the EXE directly: dist/PulseforgeStudio.exe")
        print("  2. Share it with others to download and use")
        print("  3. Create a shortcut to launch the application")
        
    except subprocess.CalledProcessError as e:
        print("-" * 60)
        print(f"\n✗ Build failed with error: {e}")
        sys.exit(1)
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    build_exe()
