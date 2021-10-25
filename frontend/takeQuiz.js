const classID = 1
var quizURL = `http://127.0.0.1:5008/quiz/questions/${classID}`
var app = new Vue({
    el: "#app ",
    data: {
        questions: []
    },
    created: function() {
        this.getQuestions()
    },
    methods: {
        getQuestions: function() {
            console.log('Getting question details')
            fetch(quizURL)
                .then(response => response.json())
                .then(data => {
                    result = data.data;
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 200:
                            console.log('success')
                            this.questions = result;
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