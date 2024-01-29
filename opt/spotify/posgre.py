import os
import psycopg2

# DATABASE_URL='postgresql://postgre:postgre@localhost:5432/postgres'
DB_URL="dbname=test_db user=user password=postgres host=postgres_pta port=5432"
def main():
    #DBに接続
    conn = psycopg2.connect(DB_URL)
    cursor=conn.cursor()

    #SQLコマンドを実行
    #テーブルを表示
    cursor.execute("SELECT * FROM teset_tbl")
    print(cursor.fetchall())

    #閉じる
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
