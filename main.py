from tools import tools
from tools import proxy
from termcolor import colored
import requests


tools.clear()
tools.ICC()
tools.clear()

while True:
	tools.clear()
	tools.banner()
	tools.banner_tools()

	try:
		tool = input(colored("\n~# ", "red"))
	except KeyboardInterrupt:
		continue
	if tool == "1":
		numb, ct, pr = tools.start_input()
		if numb != 0:
			tools.start(numb, ct, proxy_=pr)
	elif tool == "0":
		tools.clear()
		break
	elif tool == "99":
		tools.banner_info()
	elif tool == "2":
		tools.donate()
	#elif tool == "3":
		#tools.inst_logs()
	elif tool.lower() == "3":
		tools.app()
	elif tool.lower() == "clear logs":
		tools.clear_logs()
	elif tool.lower() == "update":
		tools.force_update()
	else:
		pass