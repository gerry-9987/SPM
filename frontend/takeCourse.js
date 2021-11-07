// course and class IDs are hard coded here. Can be taken from nav bar later on
const learnerID = 1
    // var classID = 1
    // var courseID = 1
var detailsURL = `http://127.0.0.1:5011/all/${learnerID}`

// Extracting from URLSearchParams
// var courseID = 2
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const courseID = parseInt(urlParams.get('courseID'))
const classID = parseInt(urlParams.get('classID'))
console.log('Page details', courseID, classID)

var app = new Vue({
    el: "#app ",
    data: {
        courseID: 1,
        courseName: 'Placeholder',
        classID: 1,
        courseIndex: 0,
        courseDetails: "",
        progressPercentage: 5,
        chapters: [],
        chapterContent: [],
        selectedNum: 1,
        materialName: ["Census Income", "About google", "CSS Crash Course For Absolute Beginners"],
        materialType: ["document", "link", "video"],
        materials: ["https://cseweb.ucsd.edu/classes/sp15/cse190-c/reports/sp15/048.pdf", "https://www.google.com/", "https://www.youtube.com/embed/yfoY53QXEnI"],
        materialBody: ["Predicting if income exceeds $50,000 per year based on 1994 US Census Data with Simple Classification Techniques", "You can learn more about google", "We will be looking at styles, selectors, declarations, etc. We will build a CSS cheat sheet that you can keep as a resource and we will also create a basic website layout."],
        finish: [],
        quizIDs: []
    },
    created: function() {
        this.getQuizDetails()
        this.getDetails()
    },
    computed: {
        completedChapters() {
            return this.finish.length + 1;
        }
    },
    methods: {
        redirectQuizPage: function(quizID) {
            window.location.href = `takeQuiz?quizID=${quizID}`;
        },
        updateFinish: function() {
            console.log(this.finish.length)
            this.completedChapters = this.finish.length
        },
        getQuizDetails: function() {

            console.log('Finding Quizes')

            let jsonData = JSON.stringify({
                'courseID': this.courseID,
                'classID': this.classID
            });

            fetch(`http://127.0.0.1:5001/find_quizzes`, {
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
                            console.log('successfully gotten quizzes')
                            this.quizIDs = result
                            break;
                        case 300:
                            alert('Not enrolled lah')
                        case 500:
                            console.log('failure')
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })
        },
        getDetails: function() {
            console.log('Getting details 2.0')

            let jsonData = JSON.stringify({
                'courseID': courseID,
                'classID': classID
            });

            fetch(`http://127.0.0.1:5011/all`, {
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
                            console.log('successfully gotten details 2.0')
                            console.log(result)
                            this.courseName = result.courseName
                            this.courseDetails = result.courseDetails
                            this.chapters = result.chapters
                                // chapterContent: [],
                            for (var material of result.materials) {
                                this.materialName.push(material.materialName)
                                this.materialBody.push(material.materialLinkBody)
                                this.materialType.push(material.materialType)
                                this.materials.push(material.materialLink)

                            }
                            this.quizIDs = result.quizIDs
                            break;
                        case 500:
                            console.log('failure')
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })
        }
    },
});