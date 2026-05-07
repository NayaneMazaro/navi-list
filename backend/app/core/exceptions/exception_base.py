class AppException(Exception):
    '''
    Classe base para exceções da aplicação.
    '''

    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

class NotFoundError(AppException):
    '''
    Exceção para recurso não encontrado.
    '''

    def __init__(self, message: str = 'Recurso não encontrado'):
        super().__init__(message, 404)

class ValidationError(AppException):
    '''
    Exceção para erros de validação.
    '''

    def __init__(self, message: str = 'Erro de validação'):
        super().__init__(message, 400)