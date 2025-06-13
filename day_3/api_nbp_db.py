from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Float
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
import requests
from pydantic import BaseModel

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json"

response = requests.get(url)
print(response)  # <Response [200]>
# 200 ok
# 3xx
# 4xx
# 5xx
print(response.text)
# {"table":"A","currency":"euro","code":"EUR","rates":[{"no":"114/A/NBP/2025","effectiveDate":"2025-06-13","mid":4.2720}]}
data = response.json()
print(data)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '114/A/NBP/2025', 'effectiveDate': '2025-06-13', 'mid': 4.272}]}
print(type(data))
print(data['rates'][0]['mid'])  # 4.272


class Rates(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class Currency(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rates]


currency_data = Currency(**data)
print(currency_data)
# table='A' currency='euro' code='EUR' rates=[Rates(no='114/A/NBP/2025', effectiveDate='2025-06-13', mid=4.272)]
print(currency_data.rates[0].mid)  # 4.272

engine = create_engine('sqlite:///currencies.db', echo=True)
Base = declarative_base()


class RatesDB(Base):
    __tablename__ = 'rates'
    id = Column(Integer, primary_key=True)
    no = Column(String)
    effectiveDate = Column(String)
    mid = Column(Float)
    currency_id = Column(ForeignKey('currency.id'))
    currencies = relationship("CurrencyDB", back_populates="rates")


class CurrencyDB(Base):
    __tablename__ = "currency"
    id = Column(Integer, primary_key=True)
    table = Column(String)
    currency = Column(String)
    code = Column(String)
    rates = relationship("RatesDB", back_populates="currencies", cascade='all')


Base.metadata.create_all(engine)

Sesion = sessionmaker(bind=engine)
session = Sesion()

rates_list = []
for i in currency_data.rates:
    rates_list.append(
        RatesDB(
            no=i.no,
            effectiveDate=i.effectiveDate,
            mid=i.mid
        )
    )

eur = CurrencyDB(
    table=currency_data.table,
    currency=currency_data.currency,
    code=currency_data.code,
    rates=rates_list
)

eur.rates = rates_list
session.add(eur)
session.commit()
