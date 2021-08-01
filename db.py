from gino import Gino


db = Gino()


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.BigInteger, primary_key=True)
    guild_id = db.Column(db.BigInteger)


async def setup_db(bind):
    await db.set_bind(bind)
    await db.gino.create_all()


async def get_all():
    return await Role.query.gino.all()


async def get_all_from_guild_id(guild_id):
    return await Role.query.where(
        Role.guild_id == guild_id
    ).gino.all()


async def get(role_id):
    return await Role.query.where(
        Role.id == role_id
    ).gino.first()


async def is_exist(role_id):
    if await get(role_id) is None:
        return False
    return True


async def add(role_id, guild_id):
    int_role_id = role_id
    if await is_exist(int_role_id):
        return

    await Role.create(
        id=int_role_id,
        guild_id=guild_id
    )
