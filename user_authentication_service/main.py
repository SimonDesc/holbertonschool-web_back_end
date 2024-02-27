#!/usr/bin/env python3
"""
Main file
"""
import requests


EMAIL = "SimonDescombes@holberton.io"
PASSWD = "iHateUnitTest"
NEW_PASSWD = "itsBoringHelp"
BASE_URL = "http://0.0.0.0:5000"
session = requests.Session()


def register_user(email: str, password: str) -> None:
    """
    Test the user registration:
    [POST] /user
    """
    response = requests.post(
        f'{BASE_URL}/users',
        data={
            "email": email,
            "password": password
        }
    )
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Test the login with a wrong password:
    [POST] /sessions
    """
    response = requests.post(
        f'{BASE_URL}/sessions',
        data={
            "email": email,
            "password": password
        }
    )
    assert response.status_code == 401


def profile_unlogged() -> None:
    """
    Test check with a invalid session ID:
    [GET] /profile
    """
    response = requests.get(f'{BASE_URL}/profile')

    assert response.status_code == 403


def log_in(email: str, password: str) -> str:
    """
    Test login with a password:
    [POST] /sessions
    """
    response = session.post(
        f'{BASE_URL}/sessions',
        data={
            "email": email,
            "password": password
        }
    )
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}


def profile_logged(session_id: str) -> None:
    """
    Check the user profile with a valid session ID:
    [GET] /profile
    """
    response = session.get(f'{BASE_URL}/profile')

    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """
    Check delete session with a valid session ID:
    [DELETE] /sessions
    """
    response = session.delete(f'{BASE_URL}/sessions')
    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """
    Check reset password and generate reset token:
    [POST] /reset_password
    """
    response = session.post(
        f'{BASE_URL}/reset_password',
        data={
            "email": email,
        }
    )
    assert response.status_code == 200
    json_response = response.json()
    assert json_response.get('email') == email

    return json_response.get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Check update password:
    [PUT] /reset_password
    """
    response = session.put(
        f'{BASE_URL}/reset_password',
        data={
            "email": email,
            "reset_token": reset_token,
            "new_password": new_password
        }
    )
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
