import dtlpy as dl

def dl_login(ec2_login_method):
    if dl.token_expired():
        if ec2_login_method:
            dl.login_m2m(email= 'bot.722580db-11f0-4069-89e1-bc69e9e5fb1f@bot.dataloop.ai', password='b!eLQN7^&3N391n10')
        else:
            dl.login()
    
    return



