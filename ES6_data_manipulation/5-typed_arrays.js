export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);
  view.setInt16(position - 1, value, false);
  return view;
}
