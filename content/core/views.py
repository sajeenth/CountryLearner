from django.http import HttpResponse
from django.shortcuts import render

def get_covid_cases(request):
     import requests
     country = request.GET.get('country')
     country = country.replace(" ", "-")
     USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
     LANGUAGE = "en-US,en;q=0.5"
     session = requests.Session()
     session.headers['User-Agent'] = USER_AGENT
     session.headers['Accept-Language'] = LANGUAGE
     session.headers['Content-Language'] = LANGUAGE
     html_content = session.get(f'https://tradingeconomics.com/{country}/coronavirus-cases').text
     return html_content


def get_covid_vaccines(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/coronavirus-vaccination-total').text
    return html_content


def get_hospitals(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/hospital').text
    return html_content


def get_doctors(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/medical-doctors').text
    return html_content


def get_nurses(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/nurses').text
    return html_content


def get_market_data(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/stock-market').text
    return html_content


def get_gdp_data(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/gdp').text
    return html_content


def get_gdp_growth_data(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/gdp-growth-annual').text
    return html_content


def get_employed_data(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/employed-persons').text
    return html_content

def get_wage(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/minimum-wages').text
    return html_content


def get_retire_men(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/retirement-age-men').text
    return html_content


def get_retire_women(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/retirement-age-women').text
    return html_content


def get_unemployed(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/unemployed-persons').text
    return html_content


def get_government_debt(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/government-debt').text
    return html_content


def get_government_spending(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "-")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://tradingeconomics.com/{country}/government-spending').text
    return html_content


def home(request):
    result = None
    if 'country' in request.GET:
        covid_cases = get_covid_cases(request)
        covid_vaccines = get_covid_vaccines(request)
        hospitals = get_hospitals(request)
        doctors = get_doctors(request)
        nurses = get_nurses(request)
        market = get_market_data(request)
        gdp = get_gdp_data(request)
        gdp_growth = get_gdp_growth_data(request)
        employees = get_employed_data(request)
        wage = get_wage(request)
        retired_men = get_retire_men(request)
        retired_women = get_retire_women(request)
        unemployed = get_unemployed(request)
        debt = get_government_debt(request)
        spending = get_government_spending(request)

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(covid_cases, 'html.parser')
        soup2 = BeautifulSoup(covid_vaccines, 'html.parser')
        soup3 = BeautifulSoup(hospitals, 'html.parser')
        soup4 = BeautifulSoup(doctors, 'html.parser')
        soup5 = BeautifulSoup(nurses, 'html.parser')
        soup6 = BeautifulSoup(market, 'html.parser')
        soup7 = BeautifulSoup(gdp, 'html.parser')
        soup8 = BeautifulSoup(gdp_growth, 'html.parser')
        soup9 = BeautifulSoup(employees, 'html.parser')
        soup10 = BeautifulSoup(wage, 'html.parser')
        soup11 = BeautifulSoup(retired_men, 'html.parser')
        soup12 = BeautifulSoup(retired_women, 'html.parser')
        soup13 = BeautifulSoup(unemployed, 'html.parser')
        soup14 = BeautifulSoup(debt, 'html.parser')
        soup15 = BeautifulSoup(spending, 'html.parser')

        result = dict()
        result['cases'] = soup.find("div", attrs={"class": "tab-pane active"}).text
        result['vaccinations'] = soup2.find("div", attrs={"class": "tab-content"}).text
        result['hospitals'] = soup3.find("div", attrs={"class": "tab-pane active"}).text
        result['doctors'] = soup4.find("div", attrs={"class": "tab-pane active"}).text
        result['nurses'] = soup5.find("div", attrs={"class": "tab-pane active"}).text
        result['market'] = soup6.find("div", attrs={"class": "tab-pane active"}).text
        result['gdp'] = soup7.find("div", attrs={"class": "tab-pane active"}).text
        result['gdp_growth'] = soup8.find("div", attrs={"class": "tab-pane active"}).text
        result['employees'] = soup9.find("div", attrs={"class": "tab-pane active"}).text
        result['wage'] = soup10.find("div", attrs={"class": "tab-pane active"}).text
        result['retired_men'] = soup11.find("div", attrs={"class": "tab-pane active"}).text
        result['retired_women'] = soup12.find("div", attrs={"class": "tab-pane active"}).text
        result['unemployed'] = soup13.find("div", attrs={"class": "tab-pane active"}).text
        result['debt'] = soup14.find("div", attrs={"class": "tab-pane active"}).text
        result['spending'] = soup15.find("div", attrs={"class": "tab-pane active"}).text

    return render(request, 'core/home.html', {'result': result})