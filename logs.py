#!/usr/bin/env python3

import psycopg2
DBNAME = "news"


# Most sleek way to do it, insted of doing conn in every fun. as well as send
# querry and return result of each Q in the same def.
def run_query(query):
    # Connects to the database
    # Runs the querys
    # Returns the results
    db = psycopg2.connect('dbname=' + DBNAME)
    try:
        db = psycopg2.connect('dbname=' + DBNAME)
    except ImportError:
        print("Unable to connect to the database")
    c = db.cursor()
    c.execute(query)
    Answer = c.fetchall()
    db.close()
    return Answer


def TopThreeArticles():
    query = """
        SELECT articles.title, COUNT(*) as num
        FROM articles, log
        WHERE log.path = '/article/' || articles.slug
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;
    """
    # a lot of ways to do it, I copy this one cuz it's cute.
    Answer = run_query(query)
    print('\n Top three most viewd articles:')
    j = 1
    for i in Answer:
        print(i[0] + ': ' + str(i[1]) + " views")
        j += 1


def MostViewdAuthors():
    query = """
        SELECT authors.name, COUNT(*) as num
        FROM authors, articles, log
        WHERE authors.id = articles.author and log.path
        LIKE concat('/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 3;
    """
    Answer = run_query(query)

    print('\n Top three most viewd authors:')
    j = 1
    for i in Answer:
        print(i[0] + ': ' + str(i[1]) + " views")
        j += 1


def BadDay():
    query = """
        SELECT * FROM (
            SELECT date(time),round(100.0*sum(case log.status
                                               when '200 OK' then 0
                                               else 1
                                              end)
                                              /count(log.status),1) as "Error"
            FROM log group by date(time)
            ORDER BY "Error" desc) as subq
        where \"Error\" > 1
    """
    Answer = run_query(query)
    print('\n Days with more than 1% error:')
    for i in Answer:
        print(str(i[0]) + ': ' + str(i[1]) + '%')


if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported from another module'
print('\n Wait for it..~\n')
TopThreeArticles()
MostViewdAuthors()
BadDay()
