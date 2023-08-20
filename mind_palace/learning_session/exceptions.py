from rest_framework import status
from rest_framework.exceptions import ValidationError


class ActiveSessionAlreadyExistsError(ValidationError):

    status_code = status.HTTP_409_CONFLICT
    default_detail = 'You can not create new learning learning_session. First finish current learning_session.'


class SessionExpiredError(ValidationError):

    statis_code = status
    default_detail = 'Session already expired. You can not perform this action.'
