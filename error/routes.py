from app.error import err
from flask import render_template


@err.app_errorhandler(404)
def erro_404(err):
    return render_template('err_handle/err_404.html'), 404

@err.app_errorhandler(403)
def erro_403(err):
    return render_template('err_handle/err_403.html'), 403

@err.app_errorhandler(500)
def erro_500(err):
    return render_template('err_handle/err_500.html'), 500

@err.app_errorhandler(405)
def erro_405(err):
    return render_template('err_handle/err_405.html'), 405
