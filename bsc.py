import re

script = input("Enter a script name: ")

def check_bash_script(script):
    dangerous_commands = [
        r'\brm\s+.*',
        r'\bcp\s+.*\s+.*',
        r'\bmv\s+.*\s+.*',
        r'\bchmod\s+.*', 
        r'\bchown\s+.*',
        r'\bkill\s+.*',
        r'\bshutdown\s+.*',
        r'\breboot\s+.*',
        r'\b(:|;|&&|\|\|)\s*$',
        'set -euo pipefail',
        'rm -rf /*',
        'sudo rm -rf /*',
        'sudo echo "triangle" > /dev/sda',
        'sudo dd if=/dev/random of=/dev/sda',
        ':(){ :|:& };:',
        'sudo dd if=/dev/urandom of=/dev/sda',
        'rm -rf --no-preserve-root /*',
        'rm -rf --no-preserve-root /',
        'rm -rf /',
        'rm -f',
    ]


    for command in dangerous_commands:
        if re.search(command, script):
            print(f"DANGEROUS COMMANDS FOUND!: {command}")
            return True

    print("Dangerous commands were not found in this script. The script is safe to run.")
    return False

check_bash_script(script)
