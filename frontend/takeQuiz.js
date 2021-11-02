const classID = 1
var questionsURL = `http://127.0.0.1:5008/quiz/questions/${classID}`
var allquizURL = `http://127.0.0.1:5008/quiz`
var learnerquizURL = ``;
var app = new Vue({
    el: "#app ",
    data: {
        classID: 1,
        questions: [],
        allquizzes: [],
        options:["True", "False"],
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
        this.getQuiz(),
        this.getAnswers(),
        this.postAnswers()
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

        getQuiz: function() {
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
            for(var i=0; i<this.answers.length+1; i++){
                if (this.learnerAnswer[i]==this.answer){
                    this.score++
                }
            }
        },

        postAnswers: function(){
            
            if(this.learnerAnswer.length == this.questions.length){
                
                let jsonData = JSON.stringify(
                    {
                        "quizID" : this.quizID,
                        "staffID" : this.staffID,
                        "quizScore" : this.Score,
                    });

                console.log(typeof(jsonData));

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
                        result = data.data;
                        console.log(result);
                        // 3 cases
                        switch (data.code) {
                            case 201:
                                // 201
                                this.postSuccessfull = true;
                                console.log('201 - Posted quiz score successfully!');
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
            }
            else{
                this.alertMessage='You cannot submit this quiz before you have finished all the questions!';
            }
        }
    }
});