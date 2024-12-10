from sqlalchemy import create_engine
import os

DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_USER=os.getenv("DB_USER")
DB_PASS=os.getenv("DB_PASS")


engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{os.getenv('DB_HOST')}:{DB_PORT}"
)
