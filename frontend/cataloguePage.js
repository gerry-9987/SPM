var get_course_url = "http://127.0.0.1:5003/course"
var get_classes_taken = "http://127.0.0.1:5007/take_class"
var studentID = 1

var app = new Vue({
    el: "#app ",
    created: function() {
        this.getAllCourse()
        this.getAllClassTaken()
    },
    data: {
        message: "",
        courses: [],
        classes_taken: [],
        courseCategories: ['IBM', 'HP', 'Xerox', 'Canon']
    },
    methods: {
        getAllCourse: function() {
            const response =
                fetch(get_course_url)
                .then(response => response.json())
                .then(data => {
                    if (data.code === 404) {
                        this.message = data.message;
                    } else {
                        this.courses = data.data.courses;
                        console.log(this.courses)
                    }
                })
                .catch(error => {
                    // Errors when calling the service; such as network error, 
                    // service offline, etc
                    console.log(this.message + error);
                });
        },
        getAllClassTaken: function() {
            const response =
                fetch(get_classes_taken)
                .then(response => response.json())
                .then(data => {
                    if (data.code === 404) {
                        this.message = data.message;
                    } else {
                        this.classes_taken = data.data.classes_taken;
                        console.log("=====Classes Taken=====")
                        console.log(this.classes_taken)
                    }
                })
                .catch(error => {
                    // Errors when calling the service; such as network error,
                    // service offline, etc
                    console.log(this.message + error);
                });
        },
        redirectProductPage: function(courseID) {
            window.location.href = `productPage?courseID=${courseID}`;
        },
        redirectTakeCoursePage: function(courseID, classID) {
            window.location.href = `takeCourse?courseID=${courseID}&classID=${classID}`;
        }
    }
});