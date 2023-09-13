/* eslint-disable class-methods-use-this */
export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') throw TypeError('sqft must be a number');
    if (
      this.constructor !== Building
      && this.evacuationWarningMessage
        === Building.prototype.evacuationWarningMessage
    ) {
      throw new Error(
        'Class extending Building must override evacuationWarningMessage',
      );
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    throw new Error(
      'Class extending Building must override evacuationWarningMessage',
    );
  }
}
