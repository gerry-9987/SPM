// Extracting from URLSearchParams
// var courseID = 2
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const courseID = urlParams.get('courseID')
console.log(courseID)

// API end points
var classDetailsURL = `http://127.0.0.1:5002/classes/${courseID}`
var courseDetailsURL = `http://127.0.0.1:5003/course/${courseID}`
var courseURL = 'http://127.0.0.1:5003'
var chapterDetailsURL = `http://127.0.0.1:5000/chapter/course/${courseID}`
var studentID = 13

// VUE JS
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
        courseChapters: 0,
        courseChaptersArray: [],
        courseStudents: [],
        isEnrolled: false,
    },
    created: function() {
        this.getCourseDetails(),
            this.getClassDetails(),
            this.getChapterDetails()
    },
    methods: {
        checkIsEnrolled: function() {
            console.log(this.courseStudents)
            if (this.courseStudents == 'No students') {
                this.isEnrolled = false
                console.log('student is not enrolled')
                return false
            } else {
                console.log(this.courseStudents)
                courseStudentsArray = this.courseStudents.split(',')
                this.isEnrolled = courseStudentsArray.includes(studentID.toString())
                console.log('student is already enrolled')
                return true
            }
        },
        signUpCourse: function() {
            console.log('Sign up has been clicked')

            // Check if already enrolled
            if (this.isEnrolled == true) {
                alert('Already enrolled')
                return
            }

            let jsonData = JSON.stringify({
                'studentID': studentID,
                'courseID': courseID
            });
            fetch(`${courseURL}/signup`, {
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
                            this.isEnrolled = true
                            alert("Scuessfully Enrolled!");
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
                    console.log(data);
                    result = data.data;
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
            console.log('Getting class details...')
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
        },
        getChapterDetails: function() {
            fetch(chapterDetailsURL)
                .then(response => response.json())
                .then(data => {
                    result = data.data;
                    console.log(result);
                    switch (data.code) {
                        case 200:
                            this.courseChapters = result.length
                            this.courseChaptersArray = result
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