'use strict';
const request = require('request');
const chai = require('chai');

describe('basic integration testing', () => {
  describe('GET /', () => {
    it('endpoint GET /', (done) => {
      const call = {
        url: 'http://localhost:7865',
        method: 'GET',
      };
      request(call, (error, response, body) => {
        chai.expect(response.statusCode).to.equal(200);
        chai.expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });
});




describe('regex integration testing', () => {
	describe('GET /cart/:id', () => {
		it('endpoint: GET /cart/:id', (done) => {
			const call = {
				url: 'http://localhost:7865/cart/12',
				method: 'GET',
			};
			request(call, (error, response, body) => {
				chai.expect(response.statusCode).to.equal(200);
				chai.expect(body).to.equal('Payment methods for cart 12');
				done();
			});
		});
	});
	describe('GET /cart/:isNaN', () => {
		it('endpoint: GET /cart/:isNaN', (done) => {
			const call = {
				url: 'http://localhost:7865/cart/toto',
				method: 'GET',
			};
			request(call, (error, response, body) => {
				chai.expect(response.statusCode).to.equal(404);
				done();
			});
		});
	});
});


describe('login integration testing', () => {
	describe('POST /login with username', () => {
		it('endpoint: POST /login', (done) => {
			const call = {
				url: 'http://localhost:7865/login',
				method: 'POST',
				json: {
					userName: 'Betty',
				},
			};
			request(call, (error, response, body) => {
				chai.expect(response.statusCode).to.equal(200);
				chai.expect(body).to.equal('Welcome Betty');
				done();
			});
		});
	});
	describe('POST /login without username', () => {
		it('endpoint: POST /login', (done) => {
			const call = {
				url: 'http://localhost:7865/login',
				method: 'POST',
				json: {
					userName: '',
				},
			};
			request(call, (error, response, body) => {
				chai.expect(response.statusCode).to.equal(200);
				chai.expect(body).to.equal('Welcome ');
				done();
			});
		});
	});
});


describe('GET /available_payments', () => {
	it('endpoint: GET /available_payments', (done) => {
		const call = {
			url: 'http://localhost:7865/available_payments',
			method: 'GET',
		};
		request(call, (error, response, body) => {
			chai.expect(response.statusCode).to.equal(200);
			chai.expect(body).to.deep.equal({
				payment_methods: {
					credit_cards: true,
					paypal: false,
				},
			});
			done();
		});
	});
});


