module.exports = function calculateNumber(type, a, b = 0) {
	const aNum = Number(a);
	const bNum = Number(b);

	if (Number.isNaN(aNum) || Number.isNaN(bNum))
		throw TypeError('Parameters must be numbers');

	// On vérifie si type fait partie des options dispo
	const type_operator_dictionnary = { 'SUM': '+', 'SUBTRACT': '-', 'DIVIDE': '/' };
	const type_operator = type_operator_dictionnary[type] || null

	switch (type_operator) {
		case '+':
			return Math.round(aNum) + Math.round(bNum);
		case '-':
			return Math.round(aNum) - Math.round(bNum);
		case '/':
			if (Math.round(bNum) === 0) {
				return ('ERROR')
			}
			result = Math.round(aNum) / Math.round(bNum);
			if (result === 0 && 1 / result === -Infinity)
				return 0;
			return result;
		default:
			throw new Error('Opérateur inconnu ou non spécifié.');
	}

};
