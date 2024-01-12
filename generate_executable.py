import os
import subprocess

def generate_executable():
    version = "1.0"
    executable_name = f"qr_generator_{version}"

    subprocess.run(["pyinstaller", "--onefile", "--name", executable_name, "gui.py"], check=True)

if __name__ == "__main__":
    generate_executable()
