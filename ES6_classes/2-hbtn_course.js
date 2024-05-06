export default class HolbertonCourse {
  constructor(name, length, students) {
    // Vérification des types
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    if (!Array.isArray(students) || students.some((student) => typeof student !== 'string')) {
      throw new TypeError('Students must be an array of strings');
    }

    // Initialisation des attributs privés
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Getters et setters
  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = value;
  }

  get students() {
    return this._students;
  }

  set students(value) {
    if (!Array.isArray(value) || value.some((student) => typeof student !== 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = value;
  }
}
