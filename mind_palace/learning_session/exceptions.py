from rest_framework import status
from rest_framework.exceptions import ValidationError


class ActiveSessionAlreadyExistsError(ValidationError):

    status_code = status.HTTP_409_CONFLICT
    default_detail = 'You can not create new learning session. First finish current session.'


class SessionExpiredError(ValidationError):

    default_detail = 'Session expired.'
