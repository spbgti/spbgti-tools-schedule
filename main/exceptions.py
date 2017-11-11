class BaseError(Exception):
    pass


class GroupAlreadyExistsError(BaseError):
    pass


class GroupDoesNotExistError(BaseError):
    pass


class PairAlreadyExistsError(BaseError):
    pass