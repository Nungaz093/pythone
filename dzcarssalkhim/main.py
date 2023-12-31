import os
from dzcarssalkhim.carss.database import DATABASE_NAME
import crea_database as db_crater

if __name__ == '__main__':
    db_is_crea = os.path.exists(DATABASE_NAME)
    if not db_is_crea:
        db_crater.crate_database()
