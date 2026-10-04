from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#"postgresql://username:password@localhost:5432/my_database"
SQLALCHEMY_DATABASE_URL = "postgresql://:1234@localhost:5432/gngn_learn"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 



with SessionLocal() as session:
    # Use text() to safely format your raw SQL query
    query = text("SELECT uid, name FROM users")
    
    # Execute and pass parameters as a dictionary
    result = session.execute(query, {"role_name": "admin"})
    
    # Fetch data (returns Row objects)
    for row in result:
        print(f"ID: {row.uid}, Name: {row.name}")
