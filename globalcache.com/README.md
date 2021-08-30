# Global Caché iTach Python Interface

How to send and learn IR commands over IP using a Global Caché iTach device. 

Tested with:

* [IP2IR-P](https://www.globalcache.com/products/itach/ip2ir-pspecs/)

## Usage

See: [`ip2ir.py`](ip2ir.py)

```bash
python3 ip2ir.py "${host}" "${port}" "${command}"
python3 ip2ir.py "${host}" "${port}" "${command}" "${response_timeout}"
```

## Examples

```bash
# Print device's network configuration:
python3 ip2ir.py 192.168.84.42 4998 'get_NET,0:1'

# Capture remote control button IR code (via ip2ir device's IR receiver):
python3 ip2ir.py 192.168.84.42 4998 'get_IRL' 15

# Stop learning mode (also stops on receipt of non-learning command):
python3 ip2ir.py 192.168.84.42 4998 'stop_IRL'

# Send an IR command; note '1:3' means send via device's 3rd output socket:
python3 ip2ir.py 192.168.84.42 4998 'sendir,1:3,2,38226,1,1,98, ... ,4892' 0.1
```

## Appendices

### Documentation

* iTach API Guide:
  * [Local Repository](API-iTach.pdf)
  * [Global Caché site](https://www.globalcache.com/files/docs/API-iTach.pdf)
    * Section 6: Error Codes 

### Find `ip2ir` device on network

#### Linux (Ubuntu)

```bash
nmap -sP 192.168.101.0/24 | grep -B 2 'Global Cache'
```
