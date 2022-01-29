import mariadb as db
import dbcreds


class DbInteraction:
    def make_post(self, username, post_input):
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO blog_post(username, content) VALUES({username}, {post_input})")
        conn.commit()

        cursor.close()
        conn.close()

   # def print_posts(self):
