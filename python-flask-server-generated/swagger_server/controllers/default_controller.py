import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.users_body import UsersBody  # noqa: E501
from swagger_server.models.users_id_body import UsersIdBody  # noqa: E501
from swagger_server import util


def users_get():  # noqa: E501
    """Get all users

    Returns a list of all users # noqa: E501


    :rtype: List[InlineResponse200]
    """
    return 'do some magic!'


def users_id_delete(id):  # noqa: E501
    """Delete a user by ID

    Deletes a user with the given ID # noqa: E501

    :param id: The ID of the user
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def users_id_get(id):  # noqa: E501
    """Get a user by ID

    Returns a user with the given ID # noqa: E501

    :param id: The ID of the user
    :type id: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def users_id_put(id, body=None):  # noqa: E501
    """Update a user by ID

    Updates a user with the given ID and name # noqa: E501

    :param id: The ID of the user
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = UsersIdBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_post(body=None):  # noqa: E501
    """Create a new user

    Creates a new user with the given name # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = UsersBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
