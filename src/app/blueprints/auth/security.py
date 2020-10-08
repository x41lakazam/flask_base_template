#!/usr/local/bin/python3
import flask, flask_login


def role_required(*roles, callback_f='auth.role_ban', callback_url=None):
    """
    A decorator that restrict a view to some roles
    This method implicitly requires that the user is logged in

    (Be careful to put it after the route decorator so it is registered by flask)

    :param *roles: (str) authorized roles
    :param callback_f: (str) name of the function that should be returned if the role doesn't match
    :param callback_url: (str) url to return if the role doesn't match, if this is provided,
    callback_f is ignored

    """
    def decorator(f):
        def new_f(*args, **kwargs):
            if flask_login.current_user.is_authenticated:
                for role in roles:
                    if flask_login.current_user.role == role:
                        return f(*args, **kwargs)

            if callback_url:
                return flask.redirect(callback_url)
            try:
                return flask.redirect(flask.url_for(callback_f))
            except:
                flask.abort(403)

        return new_f

    return decorator


