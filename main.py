

import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="username",
        password="parol123")

cursor = conn.cursor()

def insert_company():

    query = '''
        INSERT INTO companies(company_name, company_director, owner, nation, university, company_code) VALUES
    '''

    with open("./company.txt", "r", encoding = "utf-8") as f:

        companies = f.readlines()

        for company in companies:
            
            companyList = company.split(',')

            for index in range(0, len(companyList)):

                companyList[index] = companyList[index].replace("'", "")
                companyList[index] = companyList[index].replace('"', '')

            if len(companyList) == 7:
                query += "('%s', '%s', '%s', '%s', '%s', '%s'),\n" % (companyList[0], companyList[1], companyList[2], companyList[3], companyList[4]+companyList[5], companyList[6][:len(companyList[6]) - 1])
                continue
            query += "('%s', '%s', '%s', '%s', '%s', '%s'),\n" % (companyList[0], companyList[1], companyList[2], companyList[3], companyList[4], companyList[5][:len(companyList[5]) - 1])


    query = query[:len(query) - 2]


    cursor.execute(query)
    conn.commit()


def searchByNotion(search):

    query = "SELECT * FROM companies WHERE nation ILIKE '%s%%' OR company_code ILIKE '%s' " % (search, search)

    cursor.execute(query)

    return cursor.fetchall()

# insert_company()

search = input("Search by nation or company code:")
data = searchByNotion(search)

for val in data:
    print(*val)


conn.close()

