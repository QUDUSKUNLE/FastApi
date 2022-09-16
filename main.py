from enum import Enum
from typing import Union
from fastapi import FastAPI

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


@app.get('/items')
async def read_item(skip: int = 0, limit: int = 10):
  return fake_users_db[skip:skip + limit]

@app.get('/users/me')
async def read_user_me():
  return { 'user_id': 'The current user' }

@app.get('/users/{user_id}/items/{item_id}')
async def read_user(user_id: str, item_id: str, uni: Union[str, None] = None, short: bool = False):
  user = { 'user_id': user_id, 'item_id': item_id }
  if uni:
    item.update({ 'union': uni })
  if not uni:
    item.update({
      'description': 'This is an amazing user that has a long description.'
    })
  return user

@app.get('/users')
async def read_users():
  return ['Abdul-Quddus', 'Muhsinah', 'Mar`yam']
