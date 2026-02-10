#!/usr/bin/env python
"""Bootstrap pip installation."""
import os
import shutil
import sys
import tempfile

def main():
    # Download and install pip
    tmpdir = tempfile.mkdtemp()
    try:
        import urllib.request
        url = "https://bootstrap.pypa.io/get-pip.py"
        print(f"Downloading pip from {url}")
        response = urllib.request.urlopen(url)
        data = response.read()
        
        pip_script = os.path.join(tmpdir, "get-pip.py")
        with open(pip_script, "wb") as f:
            f.write(data)
        
        print("Installing pip...")
        os.system(f'python "{pip_script}"')
    except Exception as e:
        print(f"Error: {e}")
        print("Please download get-pip.py manually from:")
        print("https://bootstrap.pypa.io/get-pip.py")
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

if __name__ == "__main__":
    main()