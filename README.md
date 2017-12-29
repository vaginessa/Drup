## Drup - Default Routers,Modems and IP Cams Credentials

Find your device's default username, password, and ip address.

![screen](https://raw.githubusercontent.com/m4ll0k/Drup/master/screen.png)

### Installation

```
$ git clone https://github.com/m4ll0k/Drup.git drup
$ cd drup
$ python drup.py name_router 
```

### Usage

```
$ python drup.py cisco

#############################################
# Default Router,Modem,IP Cam Credentials
#     by Momo Outaadi (M4ll0k)
#############################################

[+] N. Brand: Cisco
[+] Username: user|admin|(none)|no default login|hsa|enable|Administrator|cusadmin|guest
[+] Password: cisco|admin|no default password|hsadb|tsunami|cable-docsis|default|system
[+] IP Addrs: 192.168.1.1|10.10.10.1|192.168.100.1

```

### Add Vendors

```
$ cd drup/db
$ vi name_router.json

{"info":{"name":"ADD NAME ROUTER...","user":"ADD USERS","pass":"ADD PASSWORDS","ip":"ADD IP"}}

$ exit vi with :wq!
```
