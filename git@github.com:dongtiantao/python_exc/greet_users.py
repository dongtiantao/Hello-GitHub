def greet_users(names):
    '''向列表中每个用户发出问候'''
    for name in names:
        msg = '\nHello '+name.title()+'!'
        print(msg)

names =['tom','jake','lily']
greet_users(names)