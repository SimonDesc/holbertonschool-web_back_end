import HolbertonCourse from "./2-hbtn_course.js";

const c1 = new HolbertonCourse("ES6", 1, ["Bob", "Jane"])
console.log(c1.name);
c1.name = "Python 101";
console.log(c1);



try {
    const c3 = new HolbertonCourse("ES6", 1, [55, "Jane"]);
}
catch(err) {
    console.log(err);
}
