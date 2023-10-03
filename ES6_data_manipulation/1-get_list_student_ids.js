export default function getListStudentIds(ListStudents) {
  if (typeof (ListStudents) === 'object') {
    return ListStudents.map((student) => student.id);
  }

  return [];
}
