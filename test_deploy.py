#!/usr/bin/env python3
"""
Test script for pyinfra deployment without actual pyinfra execution
Validates syntax and import structure
"""

import sys
import ast
from pathlib import Path

def validate_python_file(file_path):
    """Validate Python file syntax"""
    try:
        with open(file_path) as f:
            content = f.read()
        ast.parse(content, filename=str(file_path))
        print(f"✓ {file_path} - Syntax valid")
        return True
    except SyntaxError as e:
        print(f"✗ {file_path} - Syntax error: {e}")
        return False
    except Exception as e:
        print(f"✗ {file_path} - Error: {e}")
        return False

def check_file_structure():
    """Check if all required files exist"""
    required_files = [
        "inventory.py",
        "deploy.py", 
        "config.py",
        ".env.sample",
        "tasks/__init__.py",
        "tasks/base.py",
        "tasks/fail2ban.py",
        "tasks/logwatch.py",
        "tasks/postfix.py",
        "tasks/cronapt.py",
        "tasks/docker.py",
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
        else:
            print(f"✓ {file_path} - Found")
    
    if missing_files:
        print(f"✗ Missing files: {missing_files}")
        return False
    return True

def check_template_files():
    """Check if template files exist"""
    template_files = [
        "tasks/tmpl/etc/fail2ban/jail.local",
        "tasks/tmpl/etc/logwatch/modify-logwatch.rb",
        "tasks/tmpl/etc/postfix/sasl_passwd.j2",
        "tasks/tmpl/etc/postfix/modify-maincf.rb",
        "tasks/tmpl/etc/cron-apt/modify-cronapt.rb",
        "tasks/tmpl/tmp/debconf-set-selections.tmp",
    ]
    
    missing_templates = []
    for file_path in template_files:
        if not Path(file_path).exists():
            missing_templates.append(file_path)
        else:
            print(f"✓ {file_path} - Found")
    
    if missing_templates:
        print(f"⚠ Missing template files: {missing_templates}")
        return False
    return True

def main():
    """Run all validation tests"""
    print("=== VPS Provisioning Deployment Test ===\n")
    
    print("1. Checking file structure...")
    structure_ok = check_file_structure()
    
    print("\n2. Checking template files...")
    templates_ok = check_template_files()
    
    print("\n3. Validating Python syntax...")
    python_files = [
        "inventory.py",
        "deploy.py",
        "config.py",
        "tasks/base.py",
        "tasks/fail2ban.py", 
        "tasks/logwatch.py",
        "tasks/postfix.py",
        "tasks/cronapt.py",
        "tasks/docker.py",
    ]
    
    syntax_ok = all(validate_python_file(f) for f in python_files)
    
    print("\n=== Test Results ===")
    print(f"File structure: {'✓ PASS' if structure_ok else '✗ FAIL'}")
    print(f"Template files: {'✓ PASS' if templates_ok else '⚠ MISSING'}")
    print(f"Python syntax:  {'✓ PASS' if syntax_ok else '✗ FAIL'}")
    
    if structure_ok and syntax_ok:
        print("\n🎉 Deployment files are ready!")
        print("\nNext steps:")
        print("1. Install pyinfra: pip install pyinfra")
        print("2. Copy .env.sample to .env and configure")
        print("3. Run: pyinfra inventory.py deploy.py --dry")
        return 0
    else:
        print("\n❌ Fix the issues above before deployment")
        return 1

if __name__ == "__main__":
    sys.exit(main())