import psycopg2

conn = psycopg2.connect("dbname=search_engine_project user=nadiamounzih host=/tmp/")

cur = conn.cursor()


def add_record(cur):
    name = input("What is the name of the country? ")
    capital = input("Enter capital: ")
    population = input("Enter population: ")
    aggregate = input("Enter Freedom House aggregate score: ")
    status = input("Enter Freedom House status: ")
    language = input("Enter official language: ")
    export = input("Enter top export: ")
    cur.execute("INSERT INTO country (name, capital, population, aggregate, status, language, export) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, capital, population, aggregate, status, language, export))
    print("Thank you. Our database has been updated.")


def search_record(cur):
    user_choice = int(input("\n\nSearch options: [1] country name or [2] Freedom House status or [3] highest/lowest aggregate scores? "))
    if user_choice == 1:
        search_name = input("\nPlease enter name of country: ")
        cur.execute("SELECT * from country WHERE name = %s", (search_name,))
        current = cur.fetchone()
        if current is not None:
            print("Country:", current[1])
            print("Capital:", current[2])
            print("Population (millions):", current[3])
            print("Aggregate Freedom Score:", current[4])
            print("Freedom Status:", current[5])
            print("Official Language:", current[6])
            print("Top Export:", current[7])
        else:
            print("\nSorry, that is not in our database.")
    elif user_choice == 2:
        search_status = input("Please enter Freedom House status (Free, Not Free, or Partly Free): ")
        cur.execute("SELECT * from country WHERE status = %s", (search_status,))
        current = cur.fetchall()
        if current is not None:
            for data_tupe in current:
                print("\n\n\nCountry:", data_tupe[1])
                print("Capital:", data_tupe[2])
                print("Population (millions):", data_tupe[3])
                print("Aggregate Freedom Score:", data_tupe[4])
                print("Freedom Status:", data_tupe[5])
                print("Official Language:", data_tupe[6])
                print("Top Export:", data_tupe[7])
    elif user_choice == 3:
        order_record(cur)


def update_record(cur):
    country_to_update = input("Which country would you like to update? ")
    field_to_update = input("Which field would you like to update? ")
    update_entry = input("Please enter the new entry: ")
    cur.execute("UPDATE country SET {} = %s WHERE name = %s".format(field_to_update), (update_entry, country_to_update))
    print("Your information has been saved.")


def delete_record(cur):
    country_to_delete = input("Which country do you want to delete? ")
    cur.execute("DELETE FROM country WHERE name = %s", (country_to_delete,))
    print("Your information has been saved.")


def order_record(cur):
    most_or_least = int(input("\n\nEnter [1] for 5 most free countries or [2] for 5 least free countries: "))
    if most_or_least == 1:
        cur.execute("SELECT name FROM country ORDER BY aggregate ASC LIMIT 5;")
        current = cur.fetchall()
        if current is not None:
            for data_tupe in current:
                for item in data_tupe:
                    print(item)
    elif most_or_least == 2:
        cur.execute("SELECT name from country ORDER BY aggregate DESC LIMIT 5;")
        current = cur.fetchall()
        if current is not None:
            for data_tupe in current:
                for item in data_tupe:
                    print(item)

def main():
    while True:
        first_options = input(("\n\tGlobal Stats Database. Options:\n\n\t\t[A]dd\n\t\t[S]earch\n\t\t[U]pdate\n\t\t[D]elete\n\n\t\t[Q]uit\n")).lower()
        if first_options == 'a' or first_options == 'add':
            add_record(cur)
        elif first_options == 's' or first_options == 'search':
            search_record(cur)
        elif first_options == 'u':
            update_record(cur)
        elif first_options == 'd':
            delete_record(cur)
        elif first_options == 'q' or first_options == 'quit':
            exit()
        else:
            print("That was not an option. Try again. ")


main()


cur.execute("SELECT * FROM country;")
cur.fetchone()

conn.commit()

cur.close()

conn.close()
