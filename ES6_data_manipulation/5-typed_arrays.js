function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);

  try {
    view.setInt8(position, value);
  } catch (error) {
    throw new Error('Position outside range');
  }

  return view;
}

export default createInt8TypedArray;
