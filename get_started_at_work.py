#!/usr/bin/env python

import argparse
import psutil
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

def get_processes():
	ids = psutil.pids()
	process_names = []
	for id in ids:
		# print("Adding %s" % psutil.Process(id).name())
		process_names.append(psutil.Process(id).name())
	return process_names

def launch_apps(apps):
	process_names = get_processes()
	for app in apps:
		if app not in process_names:
			print("%s not open..." % app)
			print("Opening %s..." % app)
			app_name = app + ".app"
			psutil.Popen(['open', '-ga', app_name])
		else:
			print("%s is already open!" % app)

def run(sites, apps):
	args = parser.parse_args()
	if args.update:
		run_updates()
	if args.apps:
	    launch_apps(apps)
	if args.sites:
	    launch_sites(sites)
	if not args.apps and not args.sites:
		launch_apps(apps)
		launch_sites(sites)


apps = ['Slack', '1Password 7', 'Spectacle', 'Amphetamine', 'Docker', 'Todoist']
sites = {
"Mail" : "https://mail.google.com/",
"Github": "https://github.com",
"Calendar" : "https://calendar.google.com/",
"Drive" : "https://drive.google.com/",
}

run(sites, apps)



