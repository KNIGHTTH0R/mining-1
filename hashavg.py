#!/usr/bin/env python
import traceback, sys, time, socket, json

def hashave(s):
    hashes = [int(line.split(' H/s')[0].split()[-1]) for line in s.split('\n') if ' H/s' in line]
    return sum(hashes)/len(hashes)/1000000. if len(hashes) else 0.

def counthashes(s):
    hashes = [int(line.split(' hashes')[0].split()[-1]) for line in s.split('\n') if ' H/s' in line]
    return sum(hashes)/1000000.

server = "10.0.0.1", 8888

def getinput(t=False, timestep=9.95):
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', server[1]))
try:
while 1:
start = time.time()
lines = []
while not t or time.time() - start < timestep:
newline = raw_input()
if not newline or newline == '\n':
break
lines.append(newline.strip())
if lines:
data = {'time':time.time(), 'typical':hashave('\n'.join(lines)), 'actual':counthashes('\n'.join(lines)) / (time.time()-start)}
else:
data = {'time':time.time(), 'typical':0.0, 'actual':0.0}
print "Time:%(time)10.2f\tTypical: %(typical)4.2f MH/s\tActual: %(actual)4.2f MH/s" % data
s.sendto(json.dumps(data), server)
except EOFError:
if 'lines' in locals() and lines:
print "Result: %4.2f MH/s" % hashave('\n'.join(lines))
s.close()
except KeyboardInterrupt:
s.close()
return
except:
print "Unexpected exception raised:"
traceback.print_exc()
print "To exit, press ctrl-D to generate an EOF character."
s.close()
return getinput()

if __name__ == "__main__":
getinput('-t' in sys.argv)
