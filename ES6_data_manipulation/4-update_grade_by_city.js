export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  const arraySpecificCity = getListStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const matchingGrade = newGrades.find((s) => s.studentId === student.id);
      if (matchingGrade) {
        return { ...student, grade: matchingGrade.grade };
      }
      return { ...student, grade: 'N/A' };
    });
  return arraySpecificCity;
}
