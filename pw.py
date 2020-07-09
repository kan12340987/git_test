#! python3
#pw.py - An insecure password locker program

password = PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}

import sys,pyperclip
if len(sys.argv)<2:
    print('Usage: python pw.py [account]-copy account password')
    sys.exit()

account=sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print('Password for' + account + 'copied to clipboard.')
else:
    print('the account does not exist'+ account)
