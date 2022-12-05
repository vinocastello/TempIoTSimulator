from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    UpdateRowsEvent,
    WriteRowsEvent,
)

mysql_settings = {'host': 'localhost', 'port': 3306, 'user': 'root', 'passwd': 'cs198eth2'}

stream = BinLogStreamReader(connection_settings = mysql_settings, server_id=100)

for binlogevent in stream:
    if isinstance(binlogevent,WriteRowsEvent) or isinstance(binlogevent,UpdateRowsEvent):
        binlogevent.dump()

stream.close()