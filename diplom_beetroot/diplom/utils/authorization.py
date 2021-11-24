
def authorization(login, password, user_list):
    for user in user_list:
        if user.user_hash == hash((login, password)):
            return True
    return False