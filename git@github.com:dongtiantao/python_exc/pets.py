'''例题'''
def describe_pet(animal_name,animal_type='dog'):
    ''' 显示动物的信息'''
    print("\nI have a "+ animal_type+ '.')
    print("My "+ animal_type + "'s name is "+ animal_name+".")

describe_pet('harry')
describe_pet('wille','hamster')

'''8-3'''
def make_shirt(size,text):
    '''显示Tshirt 详情'''
    print("\n 我的T恤大小是："+size+"，上面印有："+text)

make_shirt('12码','我爱python')
make_shirt(size='23码',text='北京欢迎你')
make_shirt(text='不到长城非好汉',size='43码')

'''8-4'''
def make_shirt(size='大号',text='I love Python'):
    '''显示Tshirt 详情'''
    print("\n 我的T恤大小是："+size+"，上面印有："+text)
make_shirt()
make_shirt('中号')
make_shirt(text='其他字体')

'''8-5'''

def describe_city(name,country='Iceland'):
    print("\n"+name +' is in '+country)

describe_city('Reykjavik')
describe_city('Beijing','China')
describe_city('New York','USA')



