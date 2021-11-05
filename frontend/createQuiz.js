// Varoables quizID = courseID + classID + chapterID
var quizID = 118
var quizURL = `http://127.0.0.1:5008`
// var gradedQuizURL = `http://127.0.0.1:5009`

var app = new Vue({
    el: "#app ",
    computed: {},
    data: {
        quizStart: "",
        quizEnd: "",
        quizIsGraded: "ungraded",
        quizQuestions: [],
        quizAnswers: [],
        numQuestions: 1,
        quizDuration: 1,
        passingScore: 0
    },
    methods: {
        addQuestion: function() {
            console.log("addQuestion")
            this.numQuestions += 1
            window.scrollTo(0, document.body.scrollHeight);
        },
        createQuiz: function() {

            console.log("Adding quiz...")

            var tempStartDate = Date(this.quizStart).toString()
            var tempDateArray = tempStartDate.split(" ")
            var startDate = tempDateArray[2] + " " + tempDateArray[1] + " " + tempDateArray[3]
            var tempEndDate = Date(this.quizEnd).toString()
            var tempEDateArray = tempEndDate.split(" ")
            var endDate = tempEDateArray[2] + " " + tempEDateArray[1] + " " + tempEDateArray[3]


            let jsonData = JSON.stringify({
                'quizID': quizID,
                'startDate': startDate,
                'endDate': endDate,
                'questions': this.quizQuestions.join(", "),
                'answers': this.quizAnswers.join(", "),
                'duration': this.quizDuration,
                'passingScore': this.passingScore
            });

            console.log(jsonData)

            fetch(`${quizURL}/quiz/create`, {
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
            //                 if (this.quizIsGraded == 'graded') {
            //                     this.addGradedQuiz()
            //                 } else {
            //                     alert("Scuessfully added quiz!");
            //                 }
                            break;
                        case 500:
                            alert("Failed to add quiz!");
                            console.log('failure')
                            break;
                        default:
                            alert("Failed to add quiz :(");
                            throw `${data.code}: ${data.message}`;
                    }
                })
        },
        // addGradedQuiz: function() {

        //     let jsonData = JSON.stringify({
        //         'quizID': quizID,
        //         'passingScore': this.passingScore
        //     });
        //     console.log(jsonData)
        //     console.log(`${gradedQuizURL}/gradedquiz`)

        //     fetch(`${gradedQuizURL}/gradedquiz`, {
        //             method: "POST",
        //             headers: {
        //                 "Content-type": "application/json"
        //             },
        //             body: jsonData
        //         })
        //         .then(response => response.json())
        //         .then(data => {
        //             result = data.data;
        //             console.log(result);
        //             // 3 cases
        //             switch (data.code) {
        //                 case 200:
        //                     console.log('success')
        //                     alert("Scuessfully Added graded quiz!");
        //                     break;
        //                 case 500:
        //                     console.log('failure')
        //                     break;
        //                 default:
        //                     throw `${data.code}: ${data.message}`;
        //             }
        //         })

        // }
    }
});

$(document).ready(function() {
    var date_input = $('input[name="date1"]'); //our date input has the name "date"
    var container = $('.bootstrap-iso form').length > 0 ? $('.bootstrap-iso form').parent() : "body";
    var options = {
        format: 'mm/dd/yyyy',
        container: container,
        todayHighlight: true,
        autoclose: true,
    };
    date_input.datepicker(options);
})