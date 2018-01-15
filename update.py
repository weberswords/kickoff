import subprocess

def run_updates():
	subprocess.call(["pip3", "install", "--upgrade", "pip", "setuptools", "wheel"])
	subprocess.call(["brew", "update"])
	subprocess.call(["brew", "upgrade"])
	subprocess.call(["brew", "cleanup", "-s"])
	subprocess.call(["brew", "cask", "cleanup"])
	subprocess.call(["npm", "update", "-g"])

run_updates()