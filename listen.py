import struct, traceback, select, sys
from pprint import pprint
from message import *
from event_handler import *

def listener(host):
    while True:
        ready_to_read, ready_to_write, in_error = select.select([host.conn], [], [])
        conn_state = True
        try:
            itype = host.conn.recv(4) # TODO have to determine the size of header
            # print(itype)
        except ConnectionError:
            conn_state = False
        if len(itype) < 4:
            conn_state = False
        if not conn_state:
            host.conn.close()
        else:
            itype = struct.unpack('!I', itype)[0]
            print('type: ', itype)
            header = convert(itype, host)
        try:
            handler(host, itype, header)
        except:
            pprint(sys.exc_info())
            traceback.print_exc(file=sys.stdout)
            pass
            