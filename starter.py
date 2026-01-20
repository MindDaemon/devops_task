def login() -> bool:
    username : str = input('Benutzer:')
    return 'passwort' == input('Passwort:')

def main() -> None:
    try:
        print('Hallo Welt! Kannst du mich hören? Du darfst mich nicht beim Chatten stören. Mein Tagesablauf ist sehr klein, denn ich bin, bin, bi-bi-bin durchgehend online.')
        if login() :
            print('Erfolgreich angemeldet.')
        else :
            print('Nicht erfolgreich angemeldet.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    main()