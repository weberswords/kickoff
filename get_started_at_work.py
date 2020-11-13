#!/usr/bin/env python

import argparse
import subprocess
import webbrowser
from update import run_updates

parser = argparse.ArgumentParser(description='Launch apps and websites or update')
parser.add_argument('--apps', help='only open the apps', action='store_true')
parser.add_argument('--sites', help='only open the sites', action='store_true')
parser.add_argument('--update', help='do updates', action='store_true')

def launch_sites(sites):
	for key in sites:
		print("Opening %s..." % key)
		webbrowser.open_new_tab(sites[key])

def run(sites):
	# args = parser.parse_args()
	run_updates()
	launch_sites(sites)


sites = {
	"Mail" : "https://mail.google.com/",
	"Github": "https://github.com",
	"Calendar" : "https://calendar.google.com/",
	"Drive" : "https://drive.google.com/",
}

run(sites)



