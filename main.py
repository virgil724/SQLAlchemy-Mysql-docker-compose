from models.connection import engine

if __name__=="__main__":
    print(engine.connect())