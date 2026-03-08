from aiogram.fsm.state import StatesGroup,State

class Reg(StatesGroup):
    name = State() # не ставить запятую при объявлении состояний, иначе будет кортеж и не будет работать!!!(я сам так накосячил)
    phone = State()
