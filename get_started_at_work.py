#!/usr/bin/env python

import psutil
import subprocess
import webbrowser
from update import run_updates

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
	launch_sites(sites)
	launch_apps(apps)


apps = ['Slack', 'Spectacle', 'Postman', 'Amphetamine', 'Docker', 'IntelliJ']
sites = {"Toggl" : "https://toggl.com/app/timer",
"Inbox" : "https://inbox.google.com/u/0/",
"Github": "https://github.com",
"Calendar" : "https://calendar.google.com/calendar/r?pli=1",
"Trello" : "https://www.trello.com"}

run_updates()
run(sites, apps)



