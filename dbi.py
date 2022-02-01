import mariadb as db
import dbcreds


class DbInteraction:

    def make_post(self, username, post_input):
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO blog_post(username, content) VALUES ('{username}', '{post_input}')")
        conn.commit()

        cursor.close()
        conn.close()

    def print_posts(self):
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute(f"select * from blog_post bp")
        posts = cursor.fetchall()
        print("Total rows are: ", len(posts))
        for post in posts:
            print("Username: ", post[0])
            print("Post content: ", post[1])
            print("Post id: ", post[2])

        cursor.close()
        conn.close()
