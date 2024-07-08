# Import the entity to read as Entity object
import datetime
from sqlalchemy import func
from src.model.gasto import Gasto
from src.model.tipo_gasto import TipoGasto

# Import the database
from src import db

def get_all_avaliable_gastos():
    return Gasto.query.filter(Gasto.status == 1)

def get_gasto_by_id(id):
    '''Regresa todos los tipos de gasto disponibles por gasto'''
    return Gasto.query.get(id)

def get_gasto_by_name(nombre):
    '''Regresa todos los tipos de gasto disponibles por gasto'''
    return Gasto.query.filter(Gasto.id == nombre).first()

def add_gasto(tipo_gasto):
    db.session.add(tipo_gasto)
    db.session.commit()

def get_all_weekly_gastos():
    '''Obtiene la fecha semanalmente, empezando siempre en lunes
    Y terminando en el día que se esté'''
    today = datetime.datetime.now()
    last_day = today.weekday()
    init = today.replace(day=today.day - last_day)
    return get_all_gastos_by_date(init, today)

def get_all_gastos_by_date(init, finish):
    return get_all_avaliable_gastos()\
            .filter(Gasto.fecha.between(init, finish))\
            .order_by(-Gasto.id)

def get_all_weekly_total_gastos():
    '''Obtiene la fecha semanalmente, empezando siempre en lunes
    Y terminando en el día que se esté'''
    today = datetime.datetime.now()
    last_day = today.weekday()
    init = today.replace(day=today.day - last_day)
    return get_total_gastos_by_date(init, today)

def get_daily_total_gastos():
    '''Obtiene el total de gastos hechas en un día'''
    today = datetime.datetime.now()
    today_noon = today.replace(hour=0, minute=0, second=0)
    return get_total_gastos_by_date(today, today_noon)

def get_total_gastos_by_date(init, finish):
    '''Obtienew el total de las gastos hechas en el rango de fecha
    db = query
    SELECT SUM(total) FROM QUERY
        WHERE fecha < finish ;'''
    return db.session.query(func.sum(Gasto.cantidad))\
            .filter(Gasto.fecha.between(init, finish), Gasto.status == 1).scalar()

def hide_gasto(gasto):
    gasto.status = 0
    add_gasto(gasto)

