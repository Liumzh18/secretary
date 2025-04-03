from utils.database import Database

def test_db():
    try:
        db = Database()
        print("✅ 数据库连接成功!")
        
        # 检查表结构
        tables = db.cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table'
        """).fetchall()
        
        print("\n现有数据表:", [table[0] for table in tables])
        
    except Exception as e:
        print(f"❌ 数据库连接失败: {str(e)}")

if __name__ == "__main__":
    test_db()