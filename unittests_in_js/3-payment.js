import Utils from './utils.js';


export default function sendPaymentRequestToApi(totalAmount, totalShipping) {
	const calculated_SUM = Utils.calculateNumber('SUM', totalAmount, totalShipping);
	console.log('The total is: ' + calculated_SUM);
}
