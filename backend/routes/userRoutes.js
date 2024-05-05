const express = require('express');
const userController = require('../controllers/userController');
const verifyToken = require('../middleware/authMiddleware');

const router = express.Router();

router.post('/get_inventory', verifyToken, userController.getInventory);
router.post('/get_vault', verifyToken, userController.getVault);
router.post('/drop', verifyToken, userController.drop);
router.post('/theft', verifyToken, userController.theft);

module.exports = router;