from typing import Callable
from fastapi import FastAPI
from loguru import logger
from sqlalchemy.exc import OperationalError
from db import Base, engine

# Если MEMOIZATION_FLAG всё равно нужен в коде
from core.config import MEMOIZATION_FLAG

def preload_model():
    """
    Отключаем ML-загрузку для notifications-service.
    """
    pass  # ничего не делаем

def create_start_app_handler(app: FastAPI) -> Callable:
    def start_app() -> None:
        # ML отключен, MEMOIZATION_FLAG можно игнорировать
        try:
            Base.metadata.create_all(bind=engine)
        except OperationalError:
            logger.exception("failed to initialize database")

    return start_app
