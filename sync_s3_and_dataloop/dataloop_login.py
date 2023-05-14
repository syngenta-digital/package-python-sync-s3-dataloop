import dtlpy as dl

def dl_login(ec2_login_method, dl_email, dl_password):
    if dl.token_expired():
        if ec2_login_method:
            dl.login_m2m(email= dl_email, password=dl_password)
        else:
            dl.login()
    
    return



