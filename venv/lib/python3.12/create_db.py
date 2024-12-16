from dataBase import engine
import models

models.Base.metadata.create_all(bind=engine)
print("Database and tables created!")
