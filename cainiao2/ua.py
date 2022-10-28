import random


def get_ua():
    '''
    两种方式
    1. 此方法为第一种
    2. 用第三方包: 
    from fake_useragent import UserAgent
    ua = UserAgent()
    //ua = ua.chrome
    ua = ua.random
    '''
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)',
        '(X11; Linux x86_64)', '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    first = random.randint(55, 62)
    third = random.randint(0, 3200)
    fourth = random.randint(0, 140)
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first, third, fourth)
    return ' '.join([
        'Mozilla/5.0',
        random.choice(os_type), 'AppleWebKit/537.36', '(KHTML, like Gecko)',
        chrome_version, 'Safari/537.36'
    ])


print(get_ua())
