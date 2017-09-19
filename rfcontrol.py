#!/usr/bin/python

import sys
import os

t433="-t27"
t315="-t18"
EXE = "_433D"

class Device:
  def __init__(self, freq, cmdon, cmdoff):
    self.freq = freq
    self.cmd = {'on': cmdon, 'off': cmdoff}

sockets433 = [['5583299', '5583296'],
	      ['5620172', '5620160'],
	      ['5574128', '5574080'],
	      ['1388995', '1388992'],
	      ['1425868', '1425856'],
	      ['1379824', '1379776']]

devices = {}
i = 1
for s in sockets433:
  devices['s%d' % i] = Device(433, s[0], s[1])
  i = i + 1

devices['light'] = Device(315, '5592512', '5592368')
 
aliases = {
  'pot': 's1',
  'printer': 's4',
  'pianolight': 's5',
  'childroomlight': 's3'
}
freqs = {
  315: t315,
  433: t433
}

if len(sys.argv) != 3 or sys.argv[2]!='on' and sys.argv[2]!='off':
  print("usage: %s [device] [on|off]" % sys.argv[0])
  exit()

# start pigpiod if not running
pid=os.popen("ps -e|grep pigpiod").read()
if len(pid) == 0:
  os.system("sudo pigpiod")

device = sys.argv[1]
if device in aliases:
  device = aliases[device]

command = sys.argv[2]

if device in devices:
  dev = devices[device]
  os.system("%s %s %s" % (EXE, freqs[dev.freq], dev.cmd[command]))
else:
  print('Device "%s" is not defined.' % device) 
