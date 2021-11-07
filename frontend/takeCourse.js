// course and class IDs are hard coded here. Can be taken from nav bar later on
const learnerID = 1
var classID = 1
var courseID = 1
var detailsURL = `http://127.0.0.1:5011/all/${learnerID}`

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
        this.getDetails()
        this.getQuizDetails()
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
        getDetails: function() {
            fetch(detailsURL)
                .then(response => response.json())
                .then(data => {
                    result = data.data;
                    console.log(result);
                    switch (data.code) {
                        case 200:
                            console.log(result)
                            for (var each in result) {
                                courseID = result[each].courseID
                                if (courseID == this.courseID) {
                                    this.courseIndex = each
                                    console.log(each)
                                }
                            }
                            console.log(result[this.courseIndex])
                            details = result[this.courseIndex]
                            chapters = details.chapters
                            this.courseDetails = details.courseDetails
                            console.log(details.courseName)
                            this.courseName = details.courseName
                            console.log(chapters)
                            for (var chapter in chapters) {
                                this.chapters.push(chapters[chapter].chapterID)
                                this.chapterContent.push(chapters[chapter].chapterDetails)
                            }

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
        getQuizDetails: function() {

            console.log('Finding Quizes')

            let jsonData = JSON.stringify({
                'courseID': this.courseID,
                'classID': this.classID
            });

            fetch(`http://127.0.0.1:5001/find_quizes`, {
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
                            console.log('successfully gotten quizes')
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
        }
    },
});