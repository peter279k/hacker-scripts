# hacker-scripts

- All bash scripts can be run on Kali Linux successfully.

## Bash Script Lists

- [Welcome Script](first_bash_script.sh)
- [Port Scanner script](port_scanner.sh)
- [Advanced Port Scanner Script](advanced_port_scanner.sh)

## Initial PostgreSQL DB for MetaSploit

- msfconsole
- `msf5> ` msfdb init
- `msf5> ` su postgres
- `postgres@kali:~$ ` createuser msf_user -P
- `postgres@kali:~$ ` createdb --owner=msf_user hackers_arise_db
- `postgres@kali:~$ ` exit
- `msf5> ` db_connect msf_user:password@127.0.0.1/hackers_arise_db
- `msf5> ` db_status
