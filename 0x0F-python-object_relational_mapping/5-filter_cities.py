#!/usr/bin/python3
'''
Displays all cities of a given state from the
states table of the database hbtn_0e_4_usa.
Safe from SQL injections.
'''

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute('SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`')
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
