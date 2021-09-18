import os
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
os.system('banner Network')
console = Console()

def yprint(string):
	console.print(Text(string,style="bold yellow"))

def rprint(string): 
	console.print(Text(string,style="bold red"))
	
def gprint(string): 
	console.print(Text(string,style="bold green"))

def interface_list():
	interfaces = os.popen('ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read().split('\n')
	interfaces.pop(4)
	interfaces_list = interfaces[0::2]
	interface_ch = Prompt.ask("\tEnter Interface", choices=interfaces_list, default="ens33")
	return interface_ch

def arp_list():
	arp_cache = os.popen('ip n show | cut -d " " -f5').read()
	arp_cache_ch_list = arp_cache.split('\n')
	arp_cache_ch = Prompt.ask("\tEnter Interface", choices=arp_cache_ch_list)	
	return arp_cache_ch
	
def assign_ip():
	ip_address = Prompt.ask("\tEnter the ip address")
	interface_ch = interface_list()
	os.popen(f'ip address add {ip_address} dev {interface_ch}').read()
	yprint("\tAdded")
		
def delete_ip():	
	ip_address =Prompt.ask("\tEnter the ip address to be delete")
	interface_ch = interface_list()
	os.popen(f'sudo ip address del {ip_address} dev {interface_ch}').read()
	yprint("\tDeleted")
	
def display_ip():
	gprint("--------------------------------------------------------------------------")
	yprint(os.popen('ip a').read())
	gprint("--------------------------------------------------------------------------")
	
def display_interface():
	gprint("--------------------------------------------------------------------------")
	yprint(os.popen('ip l').read())
	gprint("--------------------------------------------------------------------------")
	
def configure_route():
	while True:
		menu_route()
		ch = Prompt.ask("Enter your option : ", choices=["1", "2", "3", "4"])
		if ch == "1":
			gateway_addr = Prompt.ask("\t\tEnter the gateway address")
			ip_addr = Prompt.ask("\t\tEnter the IP address")
			os.popen(f'sudo ip r add {ip_addr} via {gateway_addr}').read()
			yprint("\t\tRouter Added")
		elif ch == "2":
			ip_addr = Prompt.ask("\t\tEnter the IP address")
			os.popen(f'sudo ip route del {ip_addr}').read()
			yprint("\t\tRouter Deleted")
		elif ch == "3":
			yprint(os.popen('ip route').read())
		elif ch == "4":
			break
	
def off_on_interface():
	while True:
		menu_turn()
		ch = Prompt.ask("Enter your option : ", choices=["1", "2", "3"])
		if ch == "1":
			interface_ch = interface_list()
			os.popen(f'sudo ip link set dev {interface_ch} up').read()
			yprint(f"\t\tTurned On the interface {interface_ch}")
		elif ch == "2":
			interface_ch = interface_list()
			os.popen(f'sudo ip link set dev {interface_ch} down').read()
			yprint(f"\t\tTurned Off the interface {interface_ch}")
		elif ch == "3":
			break

def add_arp():
	ip_address = Prompt.ask("\tEnter the ip address to be add")
	interface_ch= interface_list()
	arp_cache_ch = arp_list()
	os.popen(f'sudo ip n add {ip_address} lladdr {arp_cache_ch} dev {interface_ch}').read()
	yprint("\tAdded")
	
def delete_arp():
	ip_address = Prompt.ask("\tEnter the ip address")
	interface_ch= interface_list()
	os.popen('sudo ip n del {ip_address} dev {interface_ch}').read()
	yprint("\tDeleted")
	
def restart_network():
	os.popen('sudo systemctl restart networking').read()
	yprint("\tNetwork restarted")
	
def change_host():
	new_name =Prompt.ask("\tEnter new hostname")
	os.popen(f'hostname {new_name}').read()
	yprint("\tHostname Changed")

def add_dns_entry():
	os.popen('sudo cat >>/etc/resolv.conf').read()
	yprint("\t Added")

def menu_route():
	gprint("\t1. Add new route")
	gprint("\t2. Delete route")
	gprint("\t3. Display route list")
	gprint("\t4. Exit")
	
def menu_turn():
	gprint("\t1. Turn on Interface")
	gprint("\t2. Turn off Interface")
	gprint("\t3. Exit")	
def menu():
	gprint("1. Assign IP address")
	gprint("2. Delete IP address")
	gprint("3. Display IP address")
	gprint("4. Display all interfaces")
	gprint("5. Configure routing")
	gprint("6. Turn On/Off interface")
	gprint("7. Add ARP entry")
	gprint("8. Delete ARP entry")
	gprint("9. Restart Network")
	gprint("10. Change hostname")
	gprint("11. Add DNS server entry")
	gprint("12. Exit")
	
while True:
	menu()
	ch = Prompt.ask("Enter your option ", choices=["1", "2", "3","4","5","6","7","8","9","10","11","12"])
	if ch == "1":
		assign_ip()
	elif ch == "2":
		delete_ip()
	elif ch == "3":
		display_ip()
	elif ch == "4":
		display_interface()
	elif ch == "5":
		configure_route()
	elif ch == "6":
		off_on_interface()
	elif ch == "7":
		add_arp()
	elif ch == "8":
		delete_arp()
	elif ch == "9":
		restart_network()
	elif ch == "10":
		change_host()
	elif ch == "11":
		add_dns_entry()
	elif ch == "12":
		break

	
