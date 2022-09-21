from fastapi import status


class ZooException(Exception):
    def __init__(self, message, code=status.HTTP_500_INTERNAL_SERVER_ERROR):
        self.code = code
        self.message = message
        super().__init__(self, message)


class EntityNotFoundException(ZooException):
    def __init__(self, message):
        super().__init__(message=message, code=status.HTTP_404_NOT_FOUND)
