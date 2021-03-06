const base_url = "http://ec2-54-205-2-225.compute-1.amazonaws.com"
var quizURL = `${base_url}:5008/quiz/create`
var quizURLAll = `${base_url}:5008/quiz`
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
        passingScore: 0,
        lastQuizNum:0,
    },
    // created: function() {
    //     this.getLastQuizID()
    // },
    methods: {
        addQuestion: function() {
            console.log("addQuestion")
            this.numQuestions += 1
            window.scrollTo(0, document.body.scrollHeight);
        },
        createQuiz: function() {
                var tempStartDate = Date(this.quizStart).toString()
                var tempDateArray = tempStartDate.split(" ")
                var startDate = tempDateArray[2] + " " + tempDateArray[1] + " " + tempDateArray[3]
                var tempEndDate = Date(this.quizEnd).toString()
                var tempEDateArray = tempEndDate.split(" ")
                var endDate = tempEDateArray[2] + " " + tempEDateArray[1] + " " + tempEDateArray[3]
    
                let jsonData = JSON.stringify({
                    'startDate': startDate,
                    'endDate': endDate,
                    'questions': this.quizQuestions.join(", "),
                    'answers': this.quizAnswers.join(", "),
                    'duration': this.quizDuration,
                    'passingScore': this.passingScore
                });

                console.log(jsonData)

                fetch(quizURL, {
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
                            alert('Successfully added quiz!')
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
        }
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