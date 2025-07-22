from abc import ABC, abstractmethod

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker

import logging
log = logging.getLogger("awer")

class AbstractRepository(ABC):
    @abstractmethod
    async def add():
        raise NotImplementedError
    
    @abstractmethod
    async def get_by_id():
        raise NotImplementedError
    
    @abstractmethod
    async def delete():
        raise NotImplementedError
    

class GeneralRepository(AbstractRepository):
    def __init__(self, session: async_sessionmaker):
        self.session = session
    
    model = None

    async def add(self, **kwargs):
        object = self.model(**kwargs)
        self.session.add(object)
        await self.session.commit()
        return object

    
    async def get_by_id(self, id: int):
        result = await self.session.execute(select(self.model).where(self.model.id == id))
        return result.scalars().first()

    async def delete():
        pass

