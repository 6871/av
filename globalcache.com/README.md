# Global Caché iTach Python Interface

Send and learn IR commands over IP using a Global Caché iTach device. 

* [How To Use The Python Interface](#how-to-use-the-python-interface)
* [Sending Learned IR Commands](#sending-learned-ir-commands)
* [Appendices](#appendices)
  * [Global Caché Documentation](#global-cach-documentation)
  * [Global Caché IR Database](#global-cach-ir-database)
  * [Alternate IR encoding mechanisms](#alternate-ir-encoding-mechanisms)
  * [Find IP2IR Device IP Address](#find-ip2ir-device-ip-address)

# How To Use The Python Interface

Use file [`./ip2ir.py`](ip2ir.py) to run commands; the following parameters
are accepted:

```bash
python3 ip2ir.py "${host}" "${port}" "${command}"
python3 ip2ir.py "${host}" "${port}" "${command}" "${response_timeout}"
```

Some examples:

```bash
# Print device's network configuration:
python3 ip2ir.py 192.168.84.42 4998 'get_NET,0:1'

# Capture remote control IR code (uses ip2ir device's internal IR receiver):
python3 ip2ir.py 192.168.84.42 4998 'get_IRL' 15

# Stop learning mode (also stops on receipt of non-learning command):
python3 ip2ir.py 192.168.84.42 4998 'stop_IRL'

# Send IR command (1:3 targets 3rd IR output socket; 0.1 second timeout):
python3 ip2ir.py 192.168.84.42 4998 'sendir,1:3,2,38226,1,1,98, ... ,4892' 0.1
```

Tested with device [`IP2IR-P`](https://www.globalcache.com/products/itach/ip2ir-pspecs/).

# Sending Learned IR Commands

The `get_IRL` command outputs a learned IR command in `sendir` format, but the
connector address will need to be changed to match the sending device's IR
output configuration before the command can be sent back to the device to
transmit the captured IR signal.

For example, a `get_IRL` capture may output the following `sendir` command
with an invalid output connector address of `2:1`:

```
sendir,2:1,2,38226,1,1, ... ,44,110,44,4892
       ^^^
```

If the device has an IR blaster plugged in to socket address `1:3`, simply
edit the IR command accordingly before sending it, i.e.:

```
sendir,1:3,2,38226,1,1, ... ,44,110,44,4892
       ^^^
```

Then use the edited `sendir` command to transmit the captured IR signal:

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

## Global Caché IR Database

* https://irdb.globalcache.com

## Alternate IR encoding mechanisms

* [ProntoEdit HEX Format (remotecentral.com)](http://www.remotecentral.com/features/irdisp2.htm)

## Find IP2IR Device IP Address

```bash
# Linux (Ubuntu)
nmap -sP 192.168.84.0/24 | grep -B 2 'Global Cache'
```
