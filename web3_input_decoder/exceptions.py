__all__ = ("InputDataError",)


class InputDataError(ValueError):
    pass


METHOD_NOT_FOUND = InputDataError("Specified method is not found in ABI")
CONSTRUCTOR_NOT_FOUND = InputDataError("Constructor is not found in ABI")
INVALID_INPUT = InputDataError("Invalid input")
UNABLE_TO_DETECT_CONSTRUCTOR_ARGUMENTS = InputDataError(
    "Unable to detect arguments including array. Please provide the bytecode."
)
