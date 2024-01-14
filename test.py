from manuf import manuf
import nmap

def get_device_info(mac_address):
    parser = manuf.MacParser()
    device_info = parser.get_manuf(mac_address)
    return device_info if device_info else "Unknown"

def get_mac_addresses():
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.0.1/24', arguments='-sn')  # Replace this with your network range
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            mac_address = nm[host]['addresses']['mac']
            device_info = get_device_info(mac_address)
            print(f"IP: {host}\tMAC Address: {mac_address}\tDevice Info: {device_info}")

if __name__ == "__main__":
    get_mac_addresses()
