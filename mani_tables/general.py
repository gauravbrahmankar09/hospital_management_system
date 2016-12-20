#----------------------general----------------------------------------
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [ [ row for row in cursor.fetchall() ]  , columns ]

