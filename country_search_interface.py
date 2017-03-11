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
    user_choice = int(input("\n\nSearch options: [1] country name or [2] Freedom House status? "))
    if user_choice == 1:
        search_name = input("\nPlease enter name of country: ")
        cur.execute("SELECT * from country WHERE name = %s", (search_name,))
        current = cur.fetchone()
        if current != None:
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
        if current != None:
            for data_tupe in current:
                print("\n\n\nCountry:", data_tupe[1])
                print("Capital:", data_tupe[2])
                print("Population (millions):", data_tupe[3])
                print("Aggregate Freedom Score:", data_tupe[4])
                print("Freedom Status:", data_tupe[5])
                print("Official Language:", data_tupe[6])
                print("Top Export:", data_tupe[7])


def main():
    while True:
        first_options = input(("\nGlobal Stats Database. Options:\n\n\t\t[A]dd\n\t\t[S]earch\n\t\t[Q]uit\n")).lower()
        if first_options == 'a' or first_options == 'add':
            add_record(cur)
        elif first_options == 's' or first_options == 'search':
            search_record(cur)
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
