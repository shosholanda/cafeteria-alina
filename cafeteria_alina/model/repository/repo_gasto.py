# Import the entity to read as Entity object
import datetime
from sqlalchemy import func
from cafeteria_alina.model.gasto import Gasto
from cafeteria_alina.model.tipo_gasto import TipoGasto

# Import the database
from cafeteria_alina import db

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
    today = datetime.date.today()
    last_day = today.weekday()
    init = today.replace(day=today.day - last_day)
    today = last_second(today)
    return get_all_gastos_by_date(init, today)

def get_all_gastos_by_date(init, finish):
    return get_all_avaliable_gastos()\
            .filter(Gasto.fecha.between(init, finish))\
            .order_by(-Gasto.id)

def get_all_weekly_total_gastos():
    '''Obtiene la fecha semanalmente, empezando siempre en lunes
    Y terminando en el día que se esté'''
    today = datetime.date.today()
    last_day = today.weekday()
    init = today.replace(day=today.day - last_day)
    today = last_second(today)
    return get_total_gastos_by_date(init, today)

def get_daily_total_gastos():
    '''Obtiene el total de gastos hechas en un día'''
    today = datetime.date.today()
    tomorrow = today.replace(day=today.day+1)
    return get_total_gastos_by_date(today, tomorrow)

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


def last_second(date):
    return date.strftime('%Y-%m-%d 23:59:59')