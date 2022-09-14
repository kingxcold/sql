import time
import sqlalchemy
import random
engine = sqlalchemy.create_engine(
    'mysql://root:password/@localhost/test')
conn = engine.connect()

all_data = conn.execute("SELECT * FROM test.my_data").fetchall()


def update_row_by_row(data):
    for i in range(len(data)):
        random_data = generate_random_data()
        conn.execute(
            "UPDATE my_data SET `r1` = {},`r2` ={},`r3` ={},`r4` ={},`r5` ={},`r6`={},`r7`={},`r8`={},`r9`={},`r10`={},`c1`={},`c2`={},`c3`={},`c4`={},`c5`={},`c6`={},`c7`={},`c8`={},`c9`={},`c10`={} WHERE id={};".format(random_data[0], random_data[1], random_data[2], random_data[3], random_data[4], random_data[5], random_data[6], random_data[7], random_data[8], random_data[9], random_data[10], random_data[11], random_data[12], random_data[13], random_data[14], random_data[15], random_data[16], random_data[17], random_data[18], random_data[19], data[i]["id"]))


def update_CASE(data):
    query = construct_CASE_query(data, ["r1", "r2", "r3", "r4", "r5", "r6", "r7",
                                 "r8", "r9", "r10", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"])
    # print(query)
    conn.execute(query)


# def update_IF(data):
# #     UPDATE students SET
# #     JavaScore = IF(ID=1,76,IF(ID=2,81,IF(ID=3,87,IF(ID=4,56,NULL)))),
# #     PythonScore = IF(ID=1,71,IF(ID=2,86,IF(ID=3,95,IF(ID=4,76,NULL))))
# # WHERE ID IN (1,2,3,4);
#     query = """UPDATE my_data SET
#         r1 = IF()
#     """


def update_ON_DUPLICATE(data):
    query = """ 
    INSERT INTO my_data 
    (id,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10)
        VALUES

    """
    for i in range(len(data)):
        query = query + "({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(data[i]["id"], random_val(), random_val(), random_val(), random_val(), random_val(), random_val(
        ), random_val(), random_val(), random_val(), random_val(), random_val(), random_val(), random_val(), random_val(), random_val(), random_val(), random_val(), random_val(), random_val(), random_val())
        if i != (len(data)-1):
            query = query + ","
        query = query + "\n"

    query = query + "ON DUPLICATE KEY UPDATE" + """ 
    r1 = VALUES(r1),
    r2 = VALUES(r2),
    r3 = VALUES(r3),
    r4 = VALUES(r4),
    r5 = VALUES(r5),
    r6 = VALUES(r6),
    r7 = VALUES(r7),
    r8 = VALUES(r8),
    r9 = VALUES(r9),
    r10 = VALUES(r10),
    c1 = VALUES(c1),
    c2 = VALUES(c2),
    c3 = VALUES(c3),
    c4 = VALUES(c4),
    c5 = VALUES(c5),
    c6 = VALUES(c6),
    c7 = VALUES(c7),
    c8 = VALUES(c8),
    c9 = VALUES(c9),
    c10 = VALUES(c10);
    """
    conn.execute(query)


# def insert_random_data():
#     for i in range(400):
#         random_data = generate_random_data()
#         conn.execute(
#             "INSERT INTO my_data (`r1`,`r2`,r3,r4,r5,r6,r7,r8,r9,r10,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", random_data)


def generate_random_data():
    random_data = []
    for i in range(20):
        random_data.append(random.randint(9865, 12597))
    return random_data


def random_val():
    return random.randint(9865, 12597)


# def generate_random_data_CASE():
#     random_data = []
#     for i in range(400):
#         random_data.append(random.randint(9865, 12597))
#     return random_data


def construct_CASE_query(data, colsToBeUpdated):
    query = "UPDATE my_data SET "
    for i in range(len(colsToBeUpdated)):
        col = """
        {}=(
            CASE id
        """.format(colsToBeUpdated[i])
        for j in range(400):
            random_data = random.randint(9865, 12597)
            col = col + \
                "WHEN {} THEN {}".format(data[j]["id"], random_data) + "\n"

        query = query + col + "END" + "\n)"
        if i != len(colsToBeUpdated)-1:
            query = query + ","
    return query


avg = 0.0
for i in range(100):
    start_time = time.time()
    update_row_by_row(all_data)
    avg = avg + (time.time() - start_time)
print(f"Average row by row : {avg/100}")

avg = 0.0
for i in range(100):
    start_time = time.time()
    update_CASE(all_data)
    avg = avg + (time.time() - start_time)
print(f"Average CASE : {avg/100}")

avg = 0.0
for i in range(100):
    start_time = time.time()
    update_ON_DUPLICATE(all_data)
    avg = avg + (time.time() - start_time)
print(f"Average duplicate : {avg/100}")
