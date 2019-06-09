def user_prompt():
    ans = input('Enter a number: ')
    try:
        float(ans)
    except:
        import sys
        sys.exit('NaN')
    return 'Your number is {}'.format(ans)