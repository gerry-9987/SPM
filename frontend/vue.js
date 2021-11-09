// Define a new component called button-counter
Vue.component('nav-bar', {
    data: function() {
        return {
            count: 0
        }
    },
    template: '<div></div>'
})


var vm = new Vue({
    el: '#nav-bar'
});

// Define a new component called button-counter
Vue.component('admin-toolbar', {
    data: function() {
        return {
            count: 0
        }
    },
    template: `<div class="container">
                    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">

                        <ul class="nav nav-pills">
                            <li class="nav-item"><a href="index.html" class="nav-link">Home</a></li>
                            <li class="nav-item"><a href="createCourse.html" class="nav-link">Course</a></li>
                            <li class="nav-item"><a href="createQuiz.html" class="nav-link">Quiz</a></li>
                            <li class="nav-item"><a href="assignLearners.html" class="nav-link">Assign</a></li>
                        </ul>
                    </header>
                </div>`
})


var vm = new Vue({
    el: '#admin-toolbar'
});

// User tool bar
Vue.component('learner-toolbar', {
    data: function() {
        return {
            count: 0
        }
    },
    template: `<div class="container">
                    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
                        

                        <ul class="nav nav-pills">
                            <li class="nav-item"><a href="index.html" class="nav-link">Home</a></li>
                            <li class="nav-item"><a href="cataloguePage.html" class="nav-link">Courses</a></li>
                        </ul>
                    </header>
                </div>`
})


var vm = new Vue({
    el: '#learner-toolbar'
});