# Global Caché iTach Python Interface

Send and learn IR commands over IP using a Global Caché iTach device. 

Use file [`./ip2ir.py`](ip2ir.py) to run commands. Tested with device
[`IP2IR-P`](https://www.globalcache.com/products/itach/ip2ir-pspecs/).

To run [`./ip2ir.py`](ip2ir.py):

```bash
python3 ip2ir.py "${host}" "${port}" "${command}"
python3 ip2ir.py "${host}" "${port}" "${command}" "${response_timeout}"
```

Examples:

```bash
# Print device's network configuration:
python3 ip2ir.py 192.168.84.42 4998 'get_NET,0:1'

# Capture remote control button IR code (via ip2ir device's IR receiver):
python3 ip2ir.py 192.168.84.42 4998 'get_IRL' 15

# Stop learning mode (also stops on receipt of non-learning command):
python3 ip2ir.py 192.168.84.42 4998 'stop_IRL'

# Send IR command (1:3 targets 3rd IR output socket; 0.1 sec timeout):
python3 ip2ir.py 192.168.84.42 4998 'sendir,1:3,2,38226,1,1,98, ... ,4892' 0.1
```

# Sending Learned IR Commands

The `get_IRL` command outputs an IR command in `sendir` command format, but
the connector address will need to be changed to match the sending device's
IR output configuration.

For example, a `get_IRL` capture may output the following `sendir` command
with an invalid output connector address of `2:1`:

```
sendir,2:1,2,38226,1,1, ... ,44,110,44,4892
       ^^^
```

If the device has an IR blaster plugged in to the socket with address `1:3`,
simply edit the IR command accordingly before sending it, i.e.:

```
sendir,1:3,2,38226,1,1, ... ,44,110,44,4892
       ^^^
```

```bash
host=192.168.84.42
port=4998
command='sendir,1:3,2,38226,1,1, ... ,44,110,44,4892'
timeout=0.1

python3 ip2ir.py "${host}" "${port}" "${command}" "${timeout}"
```

# Appendices

## Global Caché Documentation

* iTach API Guide:
  * [PDF (Local Repository)](API-iTach.pdf)
  * [PDF (Global Caché site)](https://www.globalcache.com/files/docs/API-iTach.pdf)
  * Useful sections:
    * Section 5: Command Set
    * Section 6: Error Codes

## Alternate IR encoding mechanisms

* [ProntoEdit HEX Format (remotecentral.com)](http://www.remotecentral.com/features/irdisp2.htm)

## Find IP2IR Device IP Address

```bash
# Linux (Ubuntu)
nmap -sP 192.168.84.0/24 | grep -B 2 'Global Cache'
```
