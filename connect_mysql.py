from sqlalchemy import create_engine
import pymysql 
import pandas as pd
import datetime

# 連結資料庫,將指定的資料庫內及讀取指定的資料表資料,存成df 
def opensql_read_sheet_todf(db,sheet):
    # now = datetime.now()
    # sheet = now.strftime('%Y-%m-%d')
    #連結資料庫,並存到資料庫指定資料表內
    sqlEngine = create_engine(f'mysql+pymysql://root:123456@127.0.0.1/{db}',pool_recycle=3600) 
    #連接資料庫
    dbConnection=sqlEngine.connect()
    #建立資料表,已當天為單位,建立資料表
    create_table_query = f'''
        CREATE TABLE IF NOT EXISTS table_{sheet} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        class VARCHAR(255),
        上課時間 DATETIME(5),
        下課時間 DATETIME(5)
        
    )
    '''
    dbConnection.execute(create_table_query)

    # 讀取簽到資料表,並轉 dataframe
    sql_to_df = pd.read_sql((f"select * from table_{sheet}"),con=dbConnection)
    # 關閉連接
    dbConnection.close()
    return sql_to_df
    

# df 寫入 mysql 函數, 輸入( df name , 資料庫名稱 db, 資料表 sheet 名稱)
def df_to_sql(df_name,db,sheet):
    sqlEngine = create_engine(f'mysql+pymysql://root:123456@127.0.0.1/{db}',pool_recycle=3600)
    dbConnection = sqlEngine.connect()
    print("資料庫連結 OK")
    df_name.to_sql(f'table_{sheet}',dbConnection,if_exists='append',index=False) # 將單筆資料寫入資料表內 
    print("資料寫入完成,簽到成功!")
    dbConnection.close()