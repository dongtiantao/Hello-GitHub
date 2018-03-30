def get_formmated_name(first_name,last_name):
    '''返回整洁的姓名'''
    full_name = first_name+' ' + last_name
    return full_name

while True:
    print('\nPlease tell me your name:')
    f_name = input('first_name:')
    l_name = input('last_name:')

    formatted_name = get_formmated_name(f_name,l_name)
    print("\nHello,"+formatted_name +'!')