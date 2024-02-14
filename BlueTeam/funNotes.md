## CCDC Notes

# Use Network Miner to watch for new IP connections
- Network Miner is a passive network sniffer
- It can be used to watch for new IP connections

What is the best way to use network miner to watch for new IP connections?
- Use the "Live Sniffer" tab to watch for new IP connections

# NMAP NSE scripts
- NMAP NSE scripts can be used to automate the process of finding vulnerabilities
- Thoe following NSE scripts can be used to find vulnerabilities:
  - vuln
  - vulscan
  - vulners

- Use vuln.nse to find vulnerabilities
Run the following command to use vuln.nse:
```bash
nmap -sV --script=vuln.nse <target>
```

- Use vulscan.nse to find vulnerabilities
Run the following command to use vulscan.nse:
```bash
nmap -sV --script=vulscan.nse <target>
```

- Use vulners.nse to find vulnerabilities
Run the following command to use vulners.nse:
```bash
nmap -sV --script=vulners.nse <target>
```

# Nikto Web Scanner
- Nikto is a web scanner that can be used to find vulnerabilities in web servers
- Use the following command to use Nikto:
```bash
nikto -h <target>
```

