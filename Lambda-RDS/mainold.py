# A lambda function to interact with AWS RDS MySQL

import pymysql
import sys
import json

rds_host  = "database-prueba.cmk4tzokwqsd.us-west-2.rds.amazonaws.com"
name = "admin"
password = "MinsaitKof19"
db_name = "kof"

def save_events(event):
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("insert into Clientes (nombreCliente, nombreTienda, cordX, cordY) values( '%s', '%s', %s, %s)" % (event['nombreCliente'], event['nombreTienda'], event['cordX'], event['cordY']))
        cur.execute("select * from Clientes")
        conn.commit()
        cur.close()
    print cur.lastrowid
    return cur.lastrowid

def main(event, context):
    id = save_events(event)
    response = {
        "id": id
    }
        
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

# event = {
#   "id": 777,
#   "name": "appychip"
# }
# context = ""
# main(event, context)
#nombreCliente=Kevin&nombreTienda=Kevin&cordX=11.123456&cordY=-15.123456