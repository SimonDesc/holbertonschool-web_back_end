export default function getStudentIdsSum(listStudents) {
  const studentsById = listStudents.reduce((total, obj) => total + obj.id, 0);
  return studentsById;
}
