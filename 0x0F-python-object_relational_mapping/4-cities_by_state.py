#!/usr/bin/python3
'''
Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
'''

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute('SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`')
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    conn.close()
