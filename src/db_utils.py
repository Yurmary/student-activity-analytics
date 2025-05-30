import psycopg2
from psycopg2.extras import execute_values

def create_tables():
    conn = psycopg2.connect(
        database="nordwind",
        user="student",
        password="qweasd963",
        host="95.163.241.236",
        port="5432"
    )
    cursor = conn.cursor()

    create_temp_table_query = """
    CREATE TEMP TABLE statistics_data (
        user_id TEXT,
        oauth_consumer_key TEXT,
        lis_result_sourcedid TEXT,
        lis_outcome_service_url TEXT,
        is_correct TEXT,
        attempt_type TEXT,
        created_at TIMESTAMP
    );
    """
    cursor.execute(create_temp_table_query)
    conn.commit()

    cursor.close()
    conn.close()

def insert_data(data):
    conn = psycopg2.connect(
        database="nordwind",
        user="student",
        password="qweasd963",
        host="95.163.241.236",
        port="5432"
    )
    cursor = conn.cursor()

    records = [
        (
            rec["user_id"],
            rec["oauth_consumer_key"],
            rec["lis_result_sourcedid"],
            rec["lis_outcome_service_url"],
            rec["is_correct"],
            rec["attempt_type"],
            rec["created_at"]
        )
        for rec in data
    ]

    insert_query = """
    INSERT INTO statistics_data
    (user_id, oauth_consumer_key, lis_result_sourcedid, lis_outcome_service_url, is_correct, attempt_type, created_at)
    VALUES %s;
    """
    execute_values(cursor, insert_query, records)
    conn.commit()

    cursor.close()
    conn.close()
