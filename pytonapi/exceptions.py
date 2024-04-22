from typing import Optional


class TONAPIError(Exception):
    """Base class for all exceptions."""


class TONAPIClientError(TONAPIError):
    """Base class for client-side errors (HTTP 4xx)."""


class TONAPIServerError(TONAPIError):
    """Base class for server-side errors (HTTP 5xx)."""


class TONAPIBadRequestError(TONAPIClientError):
    """Raised when the client sends a bad request (HTTP 400)."""


class TONAPIUnauthorizedError(TONAPIClientError):
    """Raised when the client is not authorized to access a resource (HTTP 401)."""

    def __init__(self, text: Optional[str] = None):
        if text and "limit of streaming" in text:
            raise TONAPISSELimitReachedError(text)
        super().__init__(
            "API key is missing or invalid. "
            "You can get an access token here https://tonconsole.com/"
        )


class TONAPISSEError(TONAPIServerError):
    """Raised when the server encounters an error (HTTP 4xx)."""


class TONAPISSELimitReachedError(TONAPISSEError):
    """Raises when the limit of streaming connections is reached (HTTP 401)."""


class TONAPINotFoundError(TONAPIClientError):
    """Raised when the requested resource is not found (HTTP 404)."""


class TONAPITooManyRequestsError(TONAPIClientError):
    """Raised when the rate limit is exceeded (HTTP 429)."""

    def __init__(self, text: Optional[str] = None):
        super().__init__(
            text or "Too many requests per second. Upgrade your plan "
                    "on https://tonconsole.com/tonapi/pricing."
        )


class TONAPIInternalServerError(TONAPIServerError):
    """Raised when the server encounters an internal error (HTTP 500)."""

    def __init__(self, text: Optional[str] = None):
        if "mempool is not enabled" in text:
            raise TONAPIMempoolNotEnabledError(
                "Mempool functionality is not enabled on your plan. "
                "Upgrade your plan on https://tonconsole.com."
            )
        super().__init__(text)


class TONAPIMempoolNotEnabledError(TONAPIClientError):
    """Raised when mempool functionality is not enabled for the selected plan (HTTP 500)."""


class TONAPINotImplementedError(TONAPIServerError):
    """Raised when the requested method is not implemented (HTTP 501)."""
