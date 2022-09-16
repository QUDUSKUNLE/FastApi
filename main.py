from enum import Enum
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Query
from models.item import Item

class className(str, Enum):
  nursery = 'nursery'
  kindergatern = 'kindergatern'
  primary = 'primary'
  secondary = 'secondary'


app = FastAPI()

fake_users_db = [
  { 'user_id': '1' },
  { 'user_id': '2' },
  { 'user_id': '3' },
  { 'user_id': '4' }
]

@app.get('/')
async def root():
  return { 'message': 'Hello world' }

@app.get('/class/{class_name}')
async def read_class(class_name: className):
  return { 'class_name': f'{class_name}'.title(), 'message': f'{class_name} class.'.title() }

@app.get('/items/')
async def read_items(query: Union[str, None] = Query(default=None, max_length=50, regex='^fixedquery$')):
  results = { 'users': fake_users_db }
  if query:
    results.update({ 'query': query })
  return results

@app.post('/items')
async def create_item(item: Item):
  item_dict = item.dict()
  if item.tax:
    price_with_tax = item.price + item.tax
    item_dict.update({ 'price_with_tax': price_with_tax })
  return item_dict

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item, query: Union[str, None] = None):
  result = { 'item_id': item_id, **item.dict() }
  if query:
    result.update({ 'query': query })
  return result

@app.get('/users/me')
async def read_user_me():
  return { 'user_id': 'The current user' }

@app.get('/users/{user_id}/items/{item_id}')
async def read_user(user_id: str, item_id: str, query: Union[str, None] = None, short: bool = False):
  user = { 'user_id': user_id, 'item_id': item_id }
  if query:
    item.update({ 'query': query })
  if not uni:
    item.update({
      'description': 'This is an amazing user that has a long description.'
    })
  return user

@app.get('/users')
async def read_users():
  return ['Abdul-Quddus', 'Muhsinah', 'Mar`yam']
