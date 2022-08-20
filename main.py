

import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="user2",
        password="123456")

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
def updateCompanyName(id,name):
    query = "UPDATE companies SET company_name = '%s' WHERE id = %d" % (name,id)
    cursor.execute(query)
    conn.commit()

def getCompanies(offset,limit):
    query = "SELECT * FROM companies ORDER BY id OFFSET %d LIMIT %d" % ((offset - 1) * 10,limit)

    cursor.execute(query)

    return cursor.fetchall()


'''
search = input("Search by nation or company code:")
data = searchByNotion(search)

for val in data:
    print(*val)
'''


offset = int(input("varog'ini kiriting:"))
limit = int(input("limit kiriting:"))

data = getCompanies(offset, limit)
for val in data:
    print(*val)

id = int (input("Id ni kiriting"))
nname = input("yangi nomni kirit")

updateCompanyName(id,nname)
conn.close()

