import calculateNumber from "./1-calcul.js";
import { strictEqual, throws } from 'assert';
console.log(calculateNumber("DIVIDE", 8.4, 0.4));


describe('calculateNumber', () => {
	describe('type "SUM"', () => {
		it('should return sum of integers', () => {
			strictEqual(calculateNumber('SUM', 1, 3), 4);
			strictEqual(calculateNumber('SUM', 1, -1), 0);
			strictEqual(calculateNumber('SUM', 1, -3), -2);
		});
		it('should round floats', () => {
			strictEqual(calculateNumber('SUM', 1, 3.7), 5);
			strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
			strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
			strictEqual(calculateNumber('SUM', 0.1, 0), 0);
			strictEqual(calculateNumber('SUM', 1.4, -4.5), -3);
		});

		it('should return the rounded number if only one is provided', () => {
			strictEqual(calculateNumber('SUM', 2), 2);
			strictEqual(calculateNumber('SUM', 2.7), 3);
		});
	});
	describe('type "SUBTRACT"', () => {
		it('should return difference of integers', () => {
			strictEqual(calculateNumber("SUBTRACT", 5, 1), 4);
			strictEqual(calculateNumber("SUBTRACT", 5, 5), 0);
			strictEqual(calculateNumber("SUBTRACT", 1, 5), -4);
		});

		it('should return difference of rounded floats', () => {
			strictEqual(calculateNumber("SUBTRACT", 8.6, 4.1), 5);
			strictEqual(calculateNumber("SUBTRACT", 10, 9.8), 0);
			strictEqual(calculateNumber("SUBTRACT", 8.2, 9.2), -1);

		});

		it('should return rounded number if only one is provided', () => {
			strictEqual(calculateNumber("SUBTRACT", 8.7), 9);
			strictEqual(calculateNumber("SUBTRACT", 0.3), 0);
			strictEqual(calculateNumber("SUBTRACT", -8.7), -9);
		});
	});
	describe('type "DIVIDE"', () => {
		it('should return quotient of integers', () => {
			strictEqual(calculateNumber("DIVIDE", 9, 4), 2.25);
			strictEqual(calculateNumber("DIVIDE", -9, 4), -2.25);
			strictEqual(calculateNumber("DIVIDE", 9, -4), -2.25);
			strictEqual(calculateNumber("DIVIDE", -9, -4), 2.25);
		});

		it('should return quotient of non-zero rounded floats', () => {
			strictEqual(calculateNumber("DIVIDE", 1.6, 5.2), 0.4);
			strictEqual(calculateNumber("DIVIDE", 1.6, 5), 0.4);
			strictEqual(calculateNumber("DIVIDE", -2, -5.2), 0.4);
		});

		it('should return 0 if "DIVIDE" rounds to 0', () => {
			strictEqual(calculateNumber("DIVIDE", 0.3, 3.6), 0);
			strictEqual(calculateNumber("DIVIDE", -0.3, 3.6), 0);
			strictEqual(calculateNumber("DIVIDE", 0, 3.6), 0);
		});

		it('should return "ERROR" if divisor rounds to 0', () => {
			strictEqual(calculateNumber("DIVIDE", 8.4, 0.4), 'ERROR');
			strictEqual(calculateNumber("DIVIDE", 8.4, -0.4), 'ERROR');
			strictEqual(calculateNumber("DIVIDE", 8.4, 0), 'ERROR');
		});
	});

	describe('invalid operation type', () => {
		it('should throw error if type is invalid', () => {
			throws(() => calculateNumber("INVALID", 5.7, 4.6), {
				message:
					'Opérateur inconnu ou non spécifié.'
			});
		});
	});

});
