import calculateNumber from './0-calcul.js';
import { strictEqual, throws } from 'assert';


describe('calculateNumber', () => {
	it('should return sum of integers', () => {
		strictEqual(calculateNumber(1, 3), 4);
		strictEqual(calculateNumber(1, -1), 0);
		strictEqual(calculateNumber(1, -3), -2);
	});
	it('should round floats', () => {
		strictEqual(calculateNumber(1, 3.7), 5);
		strictEqual(calculateNumber(1.2, 3.7), 5);
		strictEqual(calculateNumber(1.5, 3.7), 6);
		strictEqual(calculateNumber(0.1, 0), 0);
		strictEqual(calculateNumber(1.4, -4.5), -3);
	});

	it('should return the rounded number if only one is provided', () => {
		strictEqual(calculateNumber(2), 2);
		strictEqual(calculateNumber(2.7), 3);
	});

	it('should cast non-numbers into numbers', () => {
		strictEqual(calculateNumber(true, '3'), 4);
		strictEqual(calculateNumber(1, '3.7'), 5);
		strictEqual(calculateNumber('1.2', 3.7), 5);
	});

	it('should throw TypeError if either param cannot be coerced to a number', () => {
		throws(() => calculateNumber('toto'), {
			name: 'TypeError',
			message: 'Parameters must be numbers',
		});
		throws(() => calculateNumber(1.2, 'Simon'), {
			name: 'TypeError',
			message: 'Parameters must be numbers',
		});
	});
});
