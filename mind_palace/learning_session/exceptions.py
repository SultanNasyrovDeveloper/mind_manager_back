from rest_framework import status
from rest_framework.exceptions import ValidationError


class ActiveSessionAlreadyExistsError(ValidationError):

    status_code = status.HTTP_400_BAD_REQUEST


class SessionExpiredError(ValidationError):

    statis_code = status
    default_detail = 'Session already expired. You can not perform this action.'
