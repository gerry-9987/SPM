const now = Date.now()
const start = new Date(now)
console.log(now)
console.log(start)
const classID = 1
const quizID = 1
var quizURL = `http://127.0.0.1:5008/quiz/${quizID}`
var questionsURL = `http://127.0.0.1:5008/quiz/${quizID}/questions`
var allquizURL = `http://127.0.0.1:5008/quiz`
var learnerquizURL = `http://127.0.0.1:5010/learnerquiz`;
var app = new Vue({
    el: "#app ",
    data: {
        classID: 1,
        staffID: 1,
        duration: 0,
        questions: [],
        allquizzes: [],
        response:[],
        learnerAnswer: [],
        questions_answers: [],
        answers: [],
        score: 0,
        alertMessage: "",
        postSuccessful: false
    },
    created: function() {
        this.getQuestions(),
        this.getDuration(),
        this.timeAlert(),
        this.getLearnerAnswers(),
        this.getQuiz()
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
        getDuration: function() {
            fetch(quizURL)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.duration = data.data.duration
                })
                console.log(typeof(now))
            console.log(now + 60*(this.duration))
            this.endDate = new Date(now + 60*this.duration)
            // var endDate = new Date(now + 60*this.duration)
            console.log('END DATE')
            console.log(this.endDate)
        },

        timeAlert: function() {
            
            if (now == this.endDate){
                console.log('Times up!')
                console.log(now)
                alert("Your Time Is Up! Submit your quiz NOW!")
            }
        },
        
        getLearnerAnswers: function() {
            let inputs = document.getElementsByClassName('answer')
            for (var an_input of inputs) {
                console.log('in getLearnerAnswers - an input')
                console.log(an_input.checked)
                if (an_input.checked) {
                    console.log(an_input)
                    console.log(an_input.value)
                    this.learnerAnswer.push(an_input.value)
                }
            }
            console.log('Learner Answer')
            console.log(this.learnerAnswer)
        },

        getQuiz: function() {
            // TODO: i think no need this function because can call the answer API endpoint in checkAnswers() function
            console.log('Getting all quizes details')
            fetch(allquizURL)
                .then(response => response.json())
                .then(data => {
                    result = data.data.quiz;
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 200:
                            console.log('success');
                            this.allquizzes = result;
                            for (var quiz of this.allquizzes) {
                                if (quiz.quizID == this.classID) {
                                    this.questions_answers.push([quiz.question, quiz.answer])
                                    this.answers.push(quiz.answer)
                                }
                            }

                            console.log('Q&A!')
                            console.log(this.questions_answers)
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

        checkAnswers: function(){
            // TODO: you can retrieve the /quiz/<quizID>/answers API endpoint to check against this.learnerAnswer
            // we managed to retrieve the list of answers that the learner entered

            for(var i=0; i<this.answers.length+1; i++){
                if (this.learnerAnswer[i]==this.answer){
                    this.score++
                }
            }
        },

        // postAnswers: function(){
            
        //     if(this.learnerAnswer.length == this.questions.length){
                
        //         let jsonData = JSON.stringify(
        //             {
        //                 "quizID" : this.quizID,
        //                 "staffID" : this.staffID,
        //                 "quizScore" : this.score,
        //             });

        //         console.log(jsonData);

        //         fetch(learnerquizURL, {
        //                 method: "POST",
        //                 mode: "cors",
        //                 headers: {
        //                     "Content-type": "application/json",
        //                     'Accept': 'application/json'
        //                 },

        //                 body: jsonData
        //             })
        //             .then(response => response.json())
        //             .then(data => {
        //                 console.log(data);
        //                 result = data.data;
        //                 console.log(result);
        //                 // 3 cases
        //                 switch (data.code) {
        //                     case 201:
        //                         // 201
        //                         this.postSuccessfull = true;
        //                         console.log('201 - Posted quiz score successfully!');
        //                         break;

        //                     case 400:
        //                         // 400
        //                         this.postSuccessfull = false;
        //                         break;
        //                     case 500:
        //                         // 500
        //                         console.log(data.message);
        //                         break;
        //                     default:
        //                         throw `${data.code}: ${data.message}`;

        //                 } // switch
        //                 this.postSuccessful = true;
        //             })
        //             .catch(error => {
        //                 console.log("Problem in posting quiz Score " + error);
        //             })
        //     }
        //     else{
        //         this.alertMessage='You cannot submit this quiz before you have finished all the questions!';
        //     }
        // }
    }
});