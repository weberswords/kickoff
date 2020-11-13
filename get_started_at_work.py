#!/usr/bin/env python

import argparse
import subprocess
import webbrowser
from update import run_updates

parser = argparse.ArgumentParser(description='Launch apps and websites or update\n--apps\n--sites\n--update\n--work')
parser.add_argument('--apps', help='only open the apps', action='store_true')
parser.add_argument('--sites', help='only open the sites', action='store_true')
parser.add_argument('--update', help='do updates', action='store_true')
parser.add_argument('--work', help='also open work-related things', action='store_true')

def launch_sites(sites):
	for key in sites:
		print("Opening %s..." % key)
		webbrowser.open_new_tab(sites[key])

def open_apps(apps):
	for app in apps:
		subprocess.call(['open', app])

def run():
	args = parser.parse_args()
	if args.update:
		run_updates()
	if args.apps:
	    open_apps(apps)
	if args.sites:
	    launch_sites(sites)
	if args.work:
		launch_sites(work_sites)
		open_apps(work_apps)
	if not args.apps and not args.sites:
		open_apps(apps)
		launch_sites(sites)


sites = {
	"Mail" : "https://mail.google.com/",
	"Calendar" : "https://calendar.google.com/",
	"Drive" : "https://drive.google.com/",
}

work_sites = {
}

apps = [
	'/Applications/Amphetamine.app',
	'/Applications/Todoist.app',
	'/Applications/iTerm.app'
]

work_apps = [
	'/Applications/Slack.app'
]

run()



