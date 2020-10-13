# # Routes - Basically the functions that help us navigate through the website from page to page
#
# import os
# import secrets
# from PIL import Image
# from flask import render_template, url_for, flash, redirect, request, abort
# from election import app, db, bcrypt
# from election.forms import (RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm)
# from election.models import User, Post
# from flask_login import login_user, current_user, logout_user, login_required
# from flask_mail import Message
# import flask_mail
#
#
#
#
#
#
#
#
#
#
#
#
#
# # For our Poll feature
# # import io
# # import random
# # from flask import Response
# # from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# # from matplotlib.figure import Figure
# #
#
# #
# #
# #
# #
# # @app.route('/plot.png')
# # def plot_png():
# #     fig = create_figure()
# #     output = io.BytesIO()
# #     FigureCanvas(fig).print_png(output)
# #     return Response(output.getvalue(), mimetype='image/png')
# #
# # def create_figure():
# #     fig = Figure()
# #     axis = fig.add_subplot(1, 1, 1)
# #     xs = range(100)
# #     ys = [random.randint(1, 50) for x in xs]
# #     axis.plot(xs, ys)
# #     return fig
