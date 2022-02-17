#!/usr/bin/python3
import pwn

p = pwn.ssh(host='pwnable.kr', port=2222, user='memcpy', password='guest')
p.interactive()
