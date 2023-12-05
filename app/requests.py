from sqlalchemy import select, ScalarResult
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from app.models import User, Base

engine: AsyncEngine = create_async_engine('sqlite+aiosqlite:///db.sqlite3', echo=True)
async_session = async_sessionmaker(bind=engine)


async def async_insert_user(tg_id: int) -> None:
    session = async_session()
    session.add(User(tg_id=tg_id))
    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()


async def async_select_users() -> ScalarResult:
    async with async_session() as session:
        return await session.scalars(select(User))


async def async_db_main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
