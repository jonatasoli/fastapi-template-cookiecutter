

def get_engine():
    ...

def get_session():
    ...
    _engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
    try:
        yield db
    finally:
        db.close()


class Base:
    ...
