import os
import secrets
from PIL import Image
from flask import url_for, current_app
import yagmail
from flaskblog.config import Config

app_passwd = Config.APP_PASSWORD
email = Config.MAIL_USERNAME

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pic', picture_fn)
    img = Image.open(form_picture)
    output_size = (125, 125)
    img.thumbnail(output_size)
    img.save(picture_path)
    
    
    return picture_fn



def send_reset_email(user):

    token = user.get_secret_token()
    msg = f''' 
           To reset your password visit the following link:
           {url_for('users.reset_token', token=token, _external = True )}            
            If you did not make this request then simply ignore this email) '''
    
    with yagmail.SMTP('shakurahack17@gmail.com', app_passwd) as yag:
        yag.send(to=user.email, subject ='Passowrd Reset Request', contents=msg)


#    msg.body = f''' 
#            To reset your password visit the following link:
#            {url_for('users.reset_token', token=token, _external = True )}
#            
#            If you did not make this request then simply ignore this email
#    '''
#    mail.send(msg)