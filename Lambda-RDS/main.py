import sys
import logging
import pymysql
#rds settings
rds_host  = "database-prueba.cmk4tzokwqsd.us-west-2.rds.amazonaws.com"
name = "admin"
password = "MinsaitKof19"
db_name = "kof"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
        cur.execute("insert into Clientes (nombreCliente, nombreTienda, cordX, cordY) values( '%s', '%s', %s, %s)"% (event['nombreCliente'], event['nombreTienda'], event['cordX'], event['cordY']))
        conn.commit()
        cur.execute("select * from Clientes")
        for row in cur:
            item_count += 1
            logger.info(row)
            #print(row)

        noCliente = cur.lastrowid
    conn.commit()

    return noCliente