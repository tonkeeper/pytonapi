class TONAPIError(Exception):
    """Base class for all exceptions."""


class TONAPIClientError(TONAPIError):
    """Base class for client-side errors."""


class TONAPIServerError(TONAPIError):
    """Base class for server-side errors."""


class TONAPIBadRequestError(TONAPIClientError):
    """Raised when the client sends a bad request (HTTP 400)."""


class TONAPIUnauthorizedError(TONAPIClientError):
    """Raised when the client is not authorized to access a resource (HTTP 401)."""

    def __init__(self):
        super().__init__(
            "Access token is missing or invalid. "
            "You can get an access token here https://tonconsole.com/"
        )


class TONAPINotFoundError(TONAPIClientError):
    """Raised when the requested resource is not found (HTTP 404)."""

    def __init__(self):
        super().__init__(
            "Error 404: Method does not exist."
        )


class TONAPIInternalServerError(TONAPIServerError):
    """Raised when the server encounters an internal error (HTTP 500)."""
