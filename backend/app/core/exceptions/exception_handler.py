from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from backend.app.core.exceptions.exception_base import AppException


def register_exception_handlers(app: FastAPI):
    """
    Registra os handlers globais de exceções.
    """

    @app.exception_handler(AppException)
    async def app_exception_handler(
        request: Request,
        exc: AppException
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": exc.__class__.__name__,
                "message": exc.message,
                "status_code": exc.status_code
            }
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(
        request: Request,
        exc: Exception
    ):
        return JSONResponse(
            status_code=500,
            content={
                "error": "InternalServerError",
                "message": "Erro interno do servidor",
                "status_code": 500
            }
        )