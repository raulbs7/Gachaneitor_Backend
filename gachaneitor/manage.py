#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gachaneitor.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def compile_antlr():
    antlr4_jar = ["java", "-jar", "/usr/local/lib/antlr-4.9-complete.jar"]
    g4_path = "web/antlr/Gachaneitor.g4"
    antlr_compile = antlr4_jar + [ "-Dlanguage=Python3", "-encoding", "utf-8", g4_path ]
    subprocess.call(antlr_compile)

if __name__ == '__main__':
    compile_antlr()
    main()
