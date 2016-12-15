from movie_client import MovieClient
import requests.exceptions


def main():
    print_header()
    search_event_loop()
    

def print_header():
    print('------------------------------')
    print('    Movie Search App')
    print('------------------------------')


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input('Title to search ("x" to exit): ')
            if search != 'x':
                client = MovieClient(search)
                results = client.perform_search()
                print("Found {} results".format(len(results)))
                for r in results:
                    print('{} -- {}'.format(r.Year, r.Title))
        except requests.exceptions.ConnectionError as ce:
            print('ERROR: Can\'t reach the network')
            print(ce)
        except ValueError as ve:
            print('ERROR: Your search string is invalid: {}'.format(ve))
        except Exception as x:
            print('ERROR: {}'.format(x))

    print('exiting . . . ')

if __name__ == '__main__':
    main()
