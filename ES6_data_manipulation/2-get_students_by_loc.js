export default function getStudentsByLocation(listStudents, City) {
  const arraySpecificCity = listStudents.filter((students) => students.location === City);
  return arraySpecificCity;
}
