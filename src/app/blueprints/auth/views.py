from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_user, logout_user, login_required

from .models import User
from .forms import LoginForm, RegistrationForm
from . import blueprint, db


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data, role=form.role.data)
        user.save()
        login_user(user)
        flash('Enregistrement réussi. Le compte doit être approuvé.')
        return redirect(url_for("main.index"))
    elif form.is_submitted():
        print(form.errors)
        flash('La donnée fournie est invalide.', 'danger')
    return render_template('auth/register.jin', form=form)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.authenticate(form.user_id.data, form.password.data)
        if not user.approved:
            flash('Utilisateur non approuvé.', 'danger')
            return render_template('auth/login.jin', form=form)
        if user is not None:
            login_user(user)
            flash('Login réussi.', 'success')
            return redirect(url_for('main.index'))
        flash('Erreur login ou mot de passe.', 'danger')
    return render_template('auth/login.jin', form=form)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Vous êtes déconnecté.', 'info')
    return redirect(url_for('main.index'))

@blueprint.route('/unauthorized-page')
def role_ban():

    return render_template('auth/unauthorized_page.jin')
