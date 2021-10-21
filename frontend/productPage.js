// Accordion
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}

var courseID = 2
var classDetailsURL = `http://127.0.0.1:5002/class/${courseID}`
var courseDetailsURL = `http://127.0.0.1:5003/course/${courseID}`
    // # TODO: Add this function
var signUpCourseURL = ''
var studentID = 7

console.log(courseDetailsURL)
var app = new Vue({
    el: "#app",
    computed: {},
    data: {
        courseName: '',
        courseDetails: '',
        courseStartDate: '',
        courseEndDate: '',
        courseTrainers: '',
        courseSize: 0,
        coursePrerequisites: '',
        courseGradingBreakdown: 3,
        courseClasses: '',
        courseClassArray: [],
        courseChapters: 2,
        courseStudents: [],
        isEnrolled: false,
    },
    created: function() {
        this.getCourseDetails(),
            this.getClassDetails()
    },
    methods: {
        checkIsEnrolled: function() {
            console.log(this.courseStudents)
            if (this.courseStudents == 'No students') {
                this.isEnrolled = false
                console.log('student is not enrolled')
            } else {
                console.log(this.courseStudents)
                courseStudentsArray = this.courseStudents.split(',')
                this.isEnrolled = courseStudentsArray.includes(studentID.toString())
                console.log('student is already enrolled')
            }
        },
        signUpCourse: function(studentID, courseID) {
            console.log('Sign up has been clicked')
            let jsonData = JSON.stringify({
                studentID: studentID,
                courseID: courseID
            });
            fetch(`signUpCourseURL/{studentID}/{courseID}`, {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json"
                    },
                    body: jsonData
                })
                .then(response => response.json())
                .then(data => {
                    result = data.data;
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 200:
                            console.log('success')
                            break;
                        case 400:
                        case 500:
                            console.log('failure')
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })
        },
        getCourseDetails: function() {
            console.log('Getting course details')
            fetch(courseDetailsURL)
                .then(response => response.json())
                .then(data => {
                    result = data.data[0];
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 200:
                            console.log('success')
                            this.courseName = result.courseName
                            this.courseDetails = result.courseDetails
                            this.coursePrerequisites = result.prereqCourses
                            this.courseStudents = result.students

                            var classListNames = ""
                            var classArray = []
                            for (let i = 0; i < result.noOfClasses; i++) {
                                classArray.push(i + 1)
                                classListNames += "Class " + (i + 1) + ", "
                                console.log(classListNames)
                            }
                            classListNames = classListNames.slice(0, -2)
                            this.courseClasses = classListNames
                            this.courseClassArray = classArray

                            // Check if student is already enrolled 
                            this.checkIsEnrolled()
                            break;
                        case 400:
                        case 500:
                            console.log('failure')
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })
        },
        getClassDetails: function() {
            console.log('I am clicked toooo')
            fetch(classDetailsURL)
                .then(response => response.json())
                .then(data => {
                    result = data.data;
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 200:
                            console.log('success')
                            var trainersArray = []
                            var courseSize = 0
                            for (var eachClass of result) {
                                console.log(eachClass)
                                console.log(eachClass.trainerName)
                                if (!trainersArray.find(trainer => trainer == eachClass.trainerName))
                                    trainersArray.push(eachClass.trainerName)
                                courseSize += eachClass.classSize
                            }
                            this.courseStartDate = result[0].startDate
                            this.courseEndDate = result[0].endDate
                            this.courseTrainers = trainersArray.join(", ")
                            this.courseSize = courseSize
                            break;
                        case 400:
                        case 500:
                            console.log('failure')
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })
        }
    }
});