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
var studentID = 001

console.log(courseDetailsURL)
var app = new Vue({
    el: "#section-wrapper",
    computed: {},
    data: {
        courseID: "",
        courseTrainers: "",
        courseSize: 100,
        coursePrerequisites: [],
        courseGradingBreakdown: 3,
        courseClasses: [],
        courseChapters: 0
    },
    mounted: function() {
        this.getCourseDetails(),
        this.getClassDetails()
    },
    methods: {
        signUpCourse: function(studentID, courseID) {
            console.log('Sign up has been clicked')
            let jsonData = JSON.stringify({
                studentID: studentID,
                courseID: courseID
            });
            fetch(`signUpCourseURL/{studentID}/{courseID}`,{
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
            console.log('I am clicked')
            fetch(courseDetailsURL)
                .then(response => response.json())
                .then(data => {
                    result = data.data;
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 200:
                            console.log('success')
                            var classList = ""
                            for (let i=0; i < result.noOfClasses; i++) {

                                classList += "Class " + (i+1) + ", "
                                console.log(classList)
                            }
                            classList = classList.slice(0, -2)
                            console.log(classList)
                            this.courseClasses = classList
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
                            console.log(trainersArray)
                            console.log(courseSize)
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