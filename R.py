import os


banner = '''

\033[38;5;46msss sssss   sSSSs   d       b d sss  d d     S 
\033[38;5;46m    S      S     S  S       S S      S S    P  
\033[38;5;46m    S     S       S S       S S      S Ssss'   
\033[38;5;46m    S     S       S S       S S sSSs S S   s   
\033[38;5;46m    S     S       S S       S S      S S    b  
\033[38;5;46m    S      S     S   S     S  S      S S     b 
\033[38;5;46m    P       "sss"     "sss"   P      P P     P 
  << Coded By PICCI-TOUFIK >>
    << The Multi Encryption >>
          << Marshal >>'''

try:
    import marshal
    os.system('clear')
    print(banner)
    __F = input('\n [•] Input script path: ')
    O__ = input('\n [•] Out putt path: ')
    try:
        __R = open(__F,'r').read()
    except:
        exit('\n script not found ')
    os.system(f'cp {__F} {O__}')
    for _ in range(20):
        cc = open(O__,'r').read()
        data = marshal.dumps(cc)
        _nop_ = open(O__,'w')
        _nop_.write('#Enc > SEX:) BRAND\n')
        _nop_.write('import marshal\n')
        _nop_.write(f'exec(marshal.loads({repr(data)}))')
        _nop_.close()
    print(f'\n [•] file saved in: {O__}')
    exit()
except Exception as e:
    exit(e)