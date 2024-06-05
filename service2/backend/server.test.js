const request = require('supertest');
const app = require('./server'); // Assuming your Express app is exported from server.js

describe('GET /', () => {
  it('should return Hello World', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toEqual(200);
    expect(res.text).toBe('Hello World!');
  });
});
