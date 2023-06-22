const express = require('express');
const kue = require('kue');
const redis = require('redis');
const { promisify } = require('util');

const client = redis.createClient();
const app = express();
const clientGet = promisify(client.get).bind(client);
const clientSet = promisify(client.set).bind(client);
const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
]

function getItemById(id) {
  return listProducts.filter((item) => item.itemId === id)[0];
}
function reserveStockById(itemId, stock) {
  clientSet(itemId, stock);
}
async function getCurrentReservedStockById(itemId) {
  const reservedStock = await clientGet(itemId);
  return reservedStock;
}
app.get('/list_products', (req, res) => res.send(JSON.stringify(listProducts)));
app.get('/list_products/:itemId', async (req, res) => {
  const IId = Number(req.params.itemId);
  const getItem = getItemById(IId);
  const cReservedStock = await getCurrentReservedStockById(IId);
  if (getItem) {
    getItem.cuurentQuantity = stock;
    res.json(getItem);
    return;
  }
  res.status(404).json({'status': 'Product not found'});
})
app.get('/reserve_product/:itemId', async (req, res) => {
  const IId = Number(req.params.itemId);
  const getItem = getItemById(IId);
  const cReservedStock = await getCurrentReservedStockById(IId);
  if (getItem.length < 1) {
    res.status(404).json({'status': 'Product not found'});
    return;
  }
  const stock = await getCurrentReservedStockById(IId);
  if (stock < 1) {
    res.status(403).json({'status': 'Not enough stock available', IId});
    return;
  }
  reserveStockById(IId, stock);
  res.json({'status': 'Reservation confirmed', IId});
})
app.listen(1245);
