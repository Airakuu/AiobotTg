from aiogram.fsm.state import StatesGroup,State # импорт для создания состояний, StatesGroup для создания группы состояний, State для создания состояния

class Reg(StatesGroup):
    name = State() # не ставить запятую при объявлении состояний, иначе будет кортеж и не будет работать!!!(я сам так накосячил)
    phone = State()
