const { getInventory, getVault, dropCard, theftCard } = require('../models/userModel');
const userIdToWsMap = require('../websocket/websocketManager');

exports.getInventory = async (req, res) => {
  try {
    const inventory = await getInventory(req.authData.user_id);
    res.json(inventory);
  } catch (error) {
    throw new Error(`Error converting inventory to JSON: ${error.message}`);
  }
};

exports.getVault = async (req, res) => {
  try {
    const vault = await getVault(req.authData.user_id);
    res.json(vault);
  } catch (error) {
    throw new Error(`Error converting inventory to JSON: ${error.message}`);
  }
};

exports.drop = async (req, res) => {
  const dropData = await dropCard(req.authData.user_id);
  if (!dropData) {
    return res.status(401).json({ status: 'Drop unauthorized now' });
  }
  res.json(dropData);
};

function sendMessageToUser(userId, jsonData) {
  try {
    const ws = userIdToWsMap[userId];
    if (ws) {
      const jsonString = JSON.stringify({
        card: jsonData.card,
        thief: jsonData.thief
      });
      ws.send(jsonString);
    }
  } catch (error) {
    console.log("couldnt send to victim");
  }
}

exports.theft = async (req, res) => {
  const theftData = await theftCard(req.authData.user_id);
  if (!theftData) {
    return res.status(401).json({ status: 'Theft unauthorized now' });
  }
  sendMessageToUser(theftData.victim_id, theftData);
  res.json({
    theft: theftData.card,
    next_theft: theftData.next_theft
  });
};