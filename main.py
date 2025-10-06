from func_wake import *
from mysql.connector import connect, Error

try:
    with connect(
        host="5.tcp.eu.ngrok.io",
        port="19530",
        user="uuser",
        password="Andreikin_192192",
        database="wake_up_data",
        auth_plugin='mysql_native_password'
    ) as connection:

        def registration():                                                 # регистрация
            email = input("Электронная почта: ")
            password1, password2 = "0", "1" 
            while password1 != password2 and password1 != "":
                password1 = input("Пароль: ")
                password = input("Повторите пароль: ")

            insert_user_data = f"""
            INSERT INTO users (email, password)
            VALUES
                ({"{email}","{password}"});
            """
            with connection.cursor() as cursor:
                cursor.execute(insert_user_data)
                connection.commit()

        def log_in():                                                       # вход
            
            
            email = input("Электронная почта: ")
            password = input("Пароль: ")

            

    registration()


except Error as e:
    print(e)