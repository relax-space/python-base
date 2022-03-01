import re

def test_split():
    data1 = 'you     are \
        the best'
    res_list=re.split(r'\s+',data1)
    assert ['you','are','the','best']==res_list,'re split error'
    

def test_sub():
    data1 ='my mobile is 15811112222'
    num = re.sub(r'^.*is ','',data1)
    assert '15811112222'==num,'re sub error'
    
    num = re.sub(r'\D+','',data1)
    assert '15811112222'==num,'re sub error'

def test_sub2():
    data1 = 'a:1,b:2,c:3'
    def multi(matched):
        v = int(matched.group())
        return str(v*2)
    
    res=re.sub(r'\d+',multi,data1)
    assert 'a:2,b:4,c:6'==res,'re sub2 error'
    