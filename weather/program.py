import requests
import bs4
import collections

WeatherRpt = collections.namedtuple('WeatherRpt',
                                    'conditions, temperature, scale, location')

def main():
    print_header()
    zipcode = input('What zipcode? ')
    html = get_html_from_web(zipcode)
    report = get_weather_from_html(html)
    # print('------------------------------')
    # print(report)
    # print('------------------------------')

    #display the weather
    print ('The temp in {} is {}{} and {}'.format(
        report.location,
        report.temperature,
        report.scale,
        report.conditions
    ))


def print_header():
    print('--------------------------------------')
    print('           Weather or Not')
    print('--------------------------------------')
    print('')


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/cgi-bin/findweather/getForecast?query={}'.format(zipcode)
    response = requests.get(url)
    return response.text



def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    cond = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # print(l, condition, temp, scale)

    # return l, condition, temp, scale
    rpt = WeatherRpt(location=loc, conditions=cond, temperature=temp, scale=scale)
    # print(rpt)
    return rpt


def cleanup_text(text):
    if not text:
        return text
    text = text.strip()
    return text


def find_city_and_state_from_location(text):
    parts = text.split('\n')
    return parts[0].strip()


if __name__ == '__main__':
    main()

