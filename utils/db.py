from config import user, password, database, host
import asyncpg
import time


async def start_db():
    conn = await asyncpg.connect(user=user, password=password,
                                 database=database, host=host)
    await conn.execute("""create table if not exists users
(
    user_id    bigint not null
        constraint user_id
            primary key,
    username   varchar(32),
    reg_time   integer,
    is_new     boolean,
    first_name varchar(30),
    full_name varchar(100)
);
""")
    await conn.close()


async def add_user(user_id, username, first_name, full_name):
    conn = await asyncpg.connect(user=user, password=password,
                                 database=database, host=host)
    reg_time = int(time.time())
    await conn.execute("INSERT INTO users VALUES ($1, $2, $3, true, $4, $5, false) ON CONFLICT DO NOTHING", user_id, username,
                       reg_time, first_name, full_name)


async def get_user(user_id):
    conn = await asyncpg.connect(user=user, password=password,
                                 database=database, host=host)
    row = await conn.fetchrow("SELECT user_id, full_name, username FROM users WHERE user_id = $1", user_id)
    await conn.close()
    return row


async def get_users():
    conn = await asyncpg.connect(user=user, password=password,
                                 database=database, host=host)
    row = await conn.fetch("SELECT user_id FROM users")
    await conn.close()
    return row


async def get_new_users():
    conn = await asyncpg.connect(user=user, password=password,
                                 database=database, host=host)
    rows = await conn.fetch("SELECT user_id, first_name FROM users WHERE is_new = true")
    await conn.execute("UPDATE users SET is_new = false")
    await conn.close()
    return rows


async def get_training(user_id):
    conn = await asyncpg.connect(user=user, password=password,
                                 database=database, host=host)
    row = await conn.fetch("SELECT is_training FROM users WHERE user_id = $1", user_id)
    await conn.execute("UPDATE users SET is_training = true WHERE user_id = $1", user_id)
    await conn.close()
    return row
