def longest(st):
    st = st.strip()
    while '  ' in st:
        st = st.replace('  ',' ')
    s_max = ''
    index = 1
    while index>0:
        index = st.find(' ')
        if index>0:
            s = st[:index+1]
            st = st[index+1:]
            if len(s_max)< len(s):
                s_max = s
    if s_max =='':
        s_max = st
    return s_max


def solution():
    fi = open('input.txt','r')
    fo = open('output.txt','w')
    for i in sorted(fi,key = lambda st: len(longest(st))):
        fo.write(longest(i)+'\n')
    fo.close()
    fi.close()

solution()
print('finished')
