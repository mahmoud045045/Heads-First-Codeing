def hook_fish():
    print('I got a fish!')

def wait():
    print('waiting...')
    
print('get worm')
print('put worm on hook')
print('throw in lure')

while True:
     response=input('is bobber underwater?')
     if response =='yes':
         is_moving=True
         print('i got a bite!')
         hook_fish()
     else:
         wait()