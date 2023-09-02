__all__ = (
    "InputDataError",
    "METHOD_NOT_FOUND",
    "CONSTRUCTOR_NOT_FOUND",
    "INVALID_INPUT",
    "UNABLE_TO_DETECT_CONSTRUCTOR_ARGUMENTS",
)


class InputDataError(ValueError):
    pass


METHOD_NOT_FOUND = InputDataError("Specified method is not found in ABI")
CONSTRUCTOR_NOT_FOUND = InputDataError("Constructor is not found in ABI")
INVALID_INPUT = InputDataError("Invalid input")
UNABLE_TO_DETECT_CONSTRUCTOR_ARGUMENTS = InputDataError(
    "Unable to detect arguments including array. Please provide the bytecode."
)
