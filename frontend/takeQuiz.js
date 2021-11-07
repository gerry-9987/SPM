const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const quizID = urlParams.get('quizID')
console.log('QuizID!')
console.log(quizID)

const now = Date.now()
const start = new Date(now)
console.log(now)
console.log(start)
const classID = 1
const quizID = 1
var quizURL = `http://127.0.0.1:5008/quiz/${quizID}`
var questionsURL = `http://127.0.0.1:5008/quiz/${quizID}/questions`
var answersURL = `http://127.0.0.1:5008/quiz/${quizID}/answers`
var allquizURL = `http://127.0.0.1:5008/quiz`
var learnerquizURL = `http://127.0.0.1:5010/learnerquiz`;
var app = new Vue({
    el: "#app ",
    data: {
        classID: 1,
        // DO NOT USE 1 and 2 for StaffID, learers are staffID 1,2,6,7,8,9
        staffID: 6,
        duration: 0,
        questions: [],
        answers: [],
        tookQuiz: [],
        response: [],
        learnerAnswer: [],
        endDate: 1,
        // questions_answers: [],       
        score: 0,
        alertMessage: "",
        postSuccessful: ""
    },
    created: function() {
        this.getQuestions(),
            this.getAnswers(),
            this.takenQuiz(),
            this.getDuration(),
            // this.timer(),
            // this.timeAlert(),
            this.getLearnerAnswers()
            // this.getQuiz()
            // this.getQuiz(),
            // this.getAnswers(),
            // this.postAnswers()
    },

    methods: {
        getQuestions: function() {
            console.log('Getting question details')
            fetch(questionsURL)
                .then(response => response.json())
                .then(data => {
                    result = data.data;
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 200:
                            console.log('success')
                            this.questions = result;
                            console.log('Questions!')
                            console.log(this.questions)
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

        getAnswers: function() {
            console.log('Getting answer details')
            fetch(answersURL)
                .then(response => response.json())
                .then(data => {
                    result = data.data;
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 200:
                            console.log('success')
                            this.answers = result;
                            console.log('Answers!')
                            console.log(this.answers)
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


        takenQuiz: function() {
            console.log('Getting learners who have taken this quiz')
            fetch(learnerquizURL)
                .then(response => response.json())
                .then(data => {
                    result = data.data.quiz;
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 200:
                            console.log('success')
                            for (var quiz of result) {
                                // console.log(quiz.quizID)
                                if (quiz.quizID == quizID) {
                                    this.tookQuiz.push(quiz.staffID)
                                }
                            }
                            console.log('taken quiz')
                            console.log(this.tookQuiz)
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

        getDuration: function() {
            fetch(quizURL)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.duration = data.data.duration
                    console.log(this.duration)
                    console.log(typeof(now))
                    console.log(now)
                    var oldDateObj = now;
                    var endTime = new Date();
                    endTime.setTime(oldDateObj + (this.duration * 60 * 1000));
                    console.log(this.duration)
                    console.log(this.duration * 60 * 1000)
                    this.endDate = endTime;
                    // var endDate = new Date(now + 60*this.duration)
                    console.log('END DATE')
                    console.log(this.endDate)

                    this.timer()
                })
        },

        timer: function() {
            // Set the date we're counting down to
            console.log('in timer!')
            console.log(this.endDate)
            var countDownDate = new Date(this.endDate).getTime();

            // Update the count down every 1 second
            var x = setInterval(function() {

                // Get today's date and time
                var now = new Date().getTime();

                // Find the distance between now and the count down date
                var distance = countDownDate - now;

                // Time calculations for days, hours, minutes and seconds
                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // Output the result in an element with id="demo"
                document.getElementById("timer").innerHTML = days + "d " + hours + "h " +
                    minutes + "m " + seconds + "s ";

                // If the count down is over, write some text 
                if (distance < 0) {
                    clearInterval(x);
                    document.getElementById("timer").innerHTML = "Time's Up!";
                    alert("Your Time Is Up! Submit your quiz NOW!")
                }
            }, 1000);
        },

        getLearnerAnswers: function() {
            let inputs = document.getElementsByClassName('answer')
            for (var an_input of inputs) {
                // console.log('in getLearnerAnswers - an input')
                // console.log(an_input.checked)
                if (an_input.checked) {
                    // console.log(an_input)
                    // console.log(an_input.value)
                    this.learnerAnswer.push(an_input.value)
                }
            }
            console.log('Learner Answer')
            console.log(this.learnerAnswer)
        },


        checkAnswers: function() {
            // TODO: you can retrieve the /quiz/<quizID>/answers API endpoint to check against this.learnerAnswer
            // we managed to retrieve the list of answers that the learner entered

            if (!(this.learnerAnswer.length == this.questions.length)) {
                alert('You cannot submit the quiz until you have completed all the questions.')
            } else {
                console.log('Check answers!')
                console.log(this.answers)
                console.log(this.learnerAnswer)
                    // console.log(this.answers[0])
                    // console.log(this.answers[0])
                for (var i = 0; i < this.answers.length; i++) {
                    // console.log(i)
                    if (this.learnerAnswer[i] == this.answers[i]) {
                        this.score++
                    }
                }

                // this.score = this.score-1;
                console.log('Score is here!');

                console.log(this.score);
                // this.checkedAnswers = true;
                if (!this.tookQuiz.includes(this.staffID)) {
                    console.log('Post Answers')
                    this.postAnswers();
                } else {
                    console.log('Retake Quiz')
                    this.retakeQuiz()
                }
            }

        },

        postAnswers: function() {

            if ((this.learnerAnswer.length == this.questions.length)) {

                console.log('Conditions satisfied, post answers!')

                let jsonData = JSON.stringify({
                    "quizID": quizID,
                    "staffID": this.staffID,
                    "quizScore": this.score,
                });

                console.log(jsonData);

                fetch(learnerquizURL, {
                        method: "POST",
                        mode: "cors",
                        headers: {
                            "Content-type": "application/json",
                            'Accept': 'application/json'
                        },

                        body: jsonData
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                        result = data.code;
                        console.log(result);
                        // 3 cases
                        switch (result) {
                            case 200:
                                // 201
                                this.postSuccessfull = true;
                                console.log('200 - Posted quiz score successfully!');
                                alert('Quiz submitted successfully!');
                                break;

                            case 400:
                                // 400
                                this.postSuccessfull = false;
                                break;
                            case 500:
                                // 500
                                console.log(data.message);
                                break;
                            default:
                                throw `${data.code}: ${data.message}`;

                        } // switch
                        this.postSuccessful = true;
                    })
                    .catch(error => {
                        console.log("Problem in posting quiz Score " + error);
                    })
            } else {
                this.alertMessage = 'You cannot submit this quiz before you have finished all the questions!';
            }
        },


        retakeQuiz: function() {

            if ((this.learnerAnswer.length == this.questions.length)) {

                console.log('Conditions satisfied, post answers for retake quiz!')

                let jsonData = JSON.stringify({
                    "quizID": this.classID,
                    "staffID": this.staffID,
                    "quizScore": this.score,
                });

                console.log(jsonData);

                fetch(learnerquizURL, {
                        method: "PUT",
                        mode: "cors",
                        headers: {
                            "Content-type": "application/json",
                            'Accept': 'application/json'
                        },

                        body: jsonData
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                        result = data.code;
                        console.log(result);
                        // 3 cases
                        switch (result) {
                            case 200:
                                // 201
                                this.postSuccessfull = true;
                                console.log('200 - Posted quiz score successfully!');
                                alert('Quiz retaken successfully!');
                                break;

                            case 400:
                                // 400
                                this.postSuccessfull = false;
                                break;
                            case 500:
                                // 500
                                console.log(data.message);
                                break;
                            default:
                                throw `${data.code}: ${data.message}`;

                        } // switch
                        this.postSuccessful = true;
                    })
                    .catch(error => {
                        console.log("Problem in posting quiz Score " + error);
                    })
            } else {
                this.alertMessage = 'You cannot submit this quiz before you have finished all the questions!';
            }
        }
    }
});