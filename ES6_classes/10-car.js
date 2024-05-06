export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    // Utilisation de symboles pour cloner l'objet
    const clone = Object.create(Object.getPrototypeOf(this),
      Object.getOwnPropertyDescriptors(this));
    return clone;
  }
}
