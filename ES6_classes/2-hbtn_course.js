export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName === 'string') {
      this._name = newName;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  get length() {
    return this._length;
  }

  set length(newlength) {
    if (typeof newlength === 'number') {
      this._length = newlength;
    } else {
      throw new TypeError('Length must be a string');
    }
  }

  get students() {
    return this._students;
  }

  set students(newStudent) {
    if (
      Array.isArray(newStudent)
      && newStudent.every((student) => typeof student === 'string')
    ) {
      this._students = newStudent; // Initialisez l'attribut underscore _students
    } else {
      throw new TypeError('Students must be an array of strings');
    }
  }
}
