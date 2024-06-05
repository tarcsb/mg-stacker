const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const winston = require('winston');
const morgan = require('morgan');
const tracer = require('jaeger-client').initTracer;
const promClient = require('prom-client');
const AWS = require('aws-sdk');
const { AzureKeyVaultSecret } = require('azure-sdk');

const app = express();
app.use(cors());
app.use(express.json());
app.use(morgan('combined'));

mongoose.connect('mongodb://localhost:27017/yourdbname', { useNewUrlParser: true, useUnifiedTopology: true });

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
