import scraper2
import datetime
from matplotlib import pyplot as plt


#tutaj mozna dac linki do swoich ulubionych spotow
Urls = ["https://www.windguru.cz/279709", "https://www.windguru.cz/500760"]

#day_info, wind_normal, wind_gust = scraper2.Data_clean_up(Url)

def test(*args):
    for arg in args:
        print("--------")
        print(arg)

def sorting_mid(wind_array, output_array, wind_or_gust):
    #normal = 0, gust = 1
    for index, wind_value in enumerate(wind_array):
        if wind_value >= (5 + wind_or_gust):
            output_array.append(index)
      


def sorting_wind_levels(wind_normal, wind_gust):
    wind_highs = []
    sorting_mid(wind_normal, wind_highs, wind_or_gust=0)
    sorting_mid(wind_gust, wind_highs, wind_or_gust=1)
    wind_highs_sorterd = sorted(list(set(wind_highs)))
    return wind_highs_sorterd

def good_windy_days(day_info, wind_highs, wind_normal, wind_gust, title):
    now = datetime.datetime.now()
    day = now.day
    month = now.month
    year = now.year
    print("-------------")
    print("W miejscowosci "+str(title))
    for wind_days in wind_highs:
        day_of_weak, day_of_mounth, hour = day_info[wind_days].split(".")
        month_ = month
        
        if int(day_of_mounth) < day:
            month_ += 1
            
        print(f"Bedzie wialo w {day_of_weak} dnia {day_of_mounth}.{month_} o godzinie {hour} bedzie wiala {wind_normal[wind_days]} a w szkwalach {wind_gust[wind_days]}.")
    print("-------------")
    

def graf_wind_single_location(day_info, wind_highs, wind_normal, wind_gust, title):
    plt.bar(range(len(day_info)), wind_normal, color='blue')
    plt.title('Wiatr w '+title)
    plt.ylabel("wiatr normalny")
    plt.show()

def scrapper_init_bruv(Url):
    day_info, wind_normal, wind_gust, title = scraper2.Data_clean_up(Url)
    wind_highs = sorting_wind_levels(wind_normal, wind_gust)
    good_windy_days(day_info, wind_highs, wind_normal, wind_gust, title)
    #graf_wind_single_location(day_info, wind_highs, wind_normal, wind_gust, title)

#test
def multi_web_test(Urls):
    for Url in Urls:
        scrapper_init_bruv(Url)

multi_web_test(Urls)
#scrapper_init_bruv(Url)
#test(day_info, wind_normal, wind_gust)




