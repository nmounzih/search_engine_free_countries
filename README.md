# search_engine_free_countries

#Background information:

This is a database containing 17 countries and information about those countries. The fields in the table are name of country, capital, population in millions, aggregate score from Freedom House rankings, Freedom House status, official language, and top export. Freedom House is an organization that ranks states based on a series of questions about political rights and civil liberties. The status of "free","partly free" or "not free" is based on an aggregate score out of 100 points. 100 means a country is most free, 0 means a country is least free. (You will find Syria actually has a -1 right now.) For more information on Freedom House, visit their website at www.freedomhouse.org.

To find a nation's top export, I looked on the OEC's (or Observatory of Economic Complexity) website.

atlas.media.mit.edu/en/resources/about/

#How to make the program work:

The country_search.py file will create a table of 17 countries from teh country_data.csv file. It contains the 5 most free countries, the 5 least free, 5 partly free countries, and the USA and Russia. USA is on the list for comparison and Russia is on the list due to current relevance. The country_search_interface.py file will run a program that will prompt you to add, search, update, or delete from the table. Follow the instructions on the command line.
